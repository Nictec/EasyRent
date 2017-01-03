# -*- coding: utf-8 -*
from django.shortcuts import render, redirect, HttpResponse
import datetime 
from .forms import neweqForm, neweventForm, FilterForm, quantityForm, login_form, UserForm 
from .models import Equipment, Order, client, Assignment
from django.contrib import messages 
from django.views.generic import ListView, DetailView 
from django.views.generic import UpdateView 
from django.views.generic import DeleteView  
from django.views.generic.edit import FormMixin 
from custom_responses import AjaxTemplateMixin
from django.core.urlresolvers import reverse 
from django.db.models import Count 
from django.contrib.auth import authenticate, login, logout
import json 
from django.core import serializers
from django.contrib.auth.decorators import login_required 
from django.template import RequestContext 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpResponseForbidden 
from django.views.decorators.http import require_http_methods
from ember import *
from django.views.generic.base import View 
from django.contrib.auth.models import User
# Create your views here. 

def index(request): 
    return render(request, 'main/login_ajax.html')


def loginsys(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user) 
            #return redirect('/dashboard') 
            return HttpResponse('success') 
        else: 
            return HttpResponse(status=400)
            
    else: 
        #messages.error(request, "Username oder Passwort falsch")
        return HttpResponseForbidden() 
    
        
    
def logout_view(request): 
    logout(request) 
    return redirect('/')
    
#@login_required(login_url='/')    
def dashboard(request):  
    now = str(datetime.date.today().strftime("%A %d.%m.%Y")) 
    today = datetime.date.today() 
    events = Order.objects.filter(date=today).values('date')  
    num = events.aggregate(data=Count('date')) 
    return render(request,'main/index.html', {'date':now, 'number':num, 'filter':today})


class jlist(View): 
    def serialize(self, obj):
        return model_to_dict(obj,  
        fields = ['id', 'name', 'fabricator', 'storeplace', 'labor']) 
    def get(self, request): 
        data = ["equipment", map(self.serialize, Equipment.objects.all())] 
        return render_to_ember(data)

class storage(LoginRequiredMixin, ListView): 
    login_url='/'
    model = Equipment 
    template_name= 'main/storage.html' 
    
    
class storageupdate(LoginRequiredMixin, UpdateView): 
    login_url='/'
    model = Equipment 
    template_name= 'main/storageupdate.html' 
    ajax_template_name = 'main/storageupdate_inner.html'
    fields = ['name', 'fabricator', 'storeplace'] 
     
    

    
class storagedelete(LoginRequiredMixin, AjaxTemplateMixin, DeleteView): 
      login_url='/'
      model = Equipment
      template_name = 'main/storagedelete.html' 
      ajax_template_name= 'main/storagedelete_inner.html'
      def get_success_url(self): 
            return reverse('storage')
        
    
    
    
@login_required(login_url='/')    
def clients(request): 
     return render(request, 'main/clients.html') 
    
    
class Order_view(LoginRequiredMixin, ListView): 
    login_url='/'
    model = Order 
    template_name = 'main/Order.html' 
    

        
        
@login_required(login_url='/')   
def new_Order(request): 
             # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = neweventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            event = form.save(commit=False) 
            event.save() 
            messages.success(request, "Erfolgreich gespeichert") 
            request.session['event_name'] = event.id
            # redirect to a new URL:
            return redirect('/chose') 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = neweventForm()

    return render(request, 'main/newevent.html', {'form': form}) 

    
@login_required(login_url='/')   
def bills(request): 
     return render(request, 'main/bills.html')  
@login_required(login_url='/')    
def reservations(request): 
    return render(request, 'main/reservations.html') 
@login_required(login_url='/')
def neweq(request): 
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = neweqForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            equip = form.save(commit=False) 
            equip.save() 
            messages.success(request, "Erfolgreich gespeichert")
            
            # redirect to a new URL:
            return redirect('/equipment')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = neweqForm()

    return render(request, 'main/neweq.html', {'form': form}) 


@login_required(login_url='/')
def eqadd(request): 
    eventid = request.session['event_name'] 
    order = Order.objects.get(pk=eventid)
    eqid = request.GET.get('eq', '') 
    equipment = Equipment.objects.get(pk=eqid) 
    if request.method == 'POST': 
        form = quantityForm(request.POST) 
        if form.is_valid():  
            quantity_input = form.cleaned_data['quantity'] 
            Assignment.objects.create(Equipment=equipment, Order=order, quantity=quantity_input) 
            return redirect("/chose/") 
    else: 
        form = quantityForm(request.POST) 
        return render(request, 'main/eqadd.html', {'form':form})
         
             
    
    
    
#    if equipment.quantity > 0: 
#        equipment.event.add(eventname) 
#        Equipment.objects.filter(pk=eqid).update(quantity=-1)
#        return redirect("/lager/dashboard")
#    else: 
#        return redirect("/lager/chose")
#    
    
    


class eqlist(LoginRequiredMixin, ListView): 
    login_url='/'
    model=Equipment 
    template_name='main/eqlist.html' 
    
    def get_queryset(self):
        queryset = Equipment.objects.all()

        if self.request.GET.get('filter'): 
            queryset = queryset.filter(labor=self.request.GET.get('filter')) 
        return queryset 
@login_required(login_url='/')   
def details(request, pk): 
    order = Order.objects.get(pk=pk) 
    equipment_in = Equipment.objects.filter(event__id=pk) 
    assignment = Assignment.objects.filter(Order=pk) 
    equipment = zip(equipment_in, assignment)
    payload={'order':order, 'equipment':equipment, 'pk':pk}
    return render(request, 'main/details.html', payload) 

#@login_required(login_url='/')
def picklist(request, pk): 
    order = Order.objects.get(pk=pk)
    equipment_internal = Equipment.objects.filter(event__id=pk)  
    assignment = Assignment.objects.filter(Order=pk)
    equipment = zip(equipment_internal) 
    payload = {'equipment':equipment, 'order':order} 
    return render(request, 'main/picklist.html', payload) 
#    data = serializers.serialize('json', self.get_queryset())
#    return HttpResponse(data, mimetype="application/json")
    
    
@login_required(login_url='/')        
def SetOrder(request): 
    oid = request.GET.get('o', '') 
    Order.objects.filter(id = oid).update(status = 'bereit') 
    return redirect("/events")
    
    
  
   
        
        
       
    
    
    
class ass_detail(LoginRequiredMixin, DetailView):
    login_url='/'
    model = Order
    template_name='main/ass_detail.html' 
    queryset = Order.objects.select_related() 
    
def admin(request): 
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
#            login(new_user)
            # redirect, or however you want to get to the main view
            return redirect("/config/")
    else:
      form = UserForm() 
      users = User.objects.all()
    return render(request, 'main/admin.html', {'form': form, 'users':users}) 

    

 

    
    
    
    
def del_session(request): 
    del request.session['event_name'] 
    return redirect('/lager/chose')
    
     
        
        
        
class userlist(LoginRequiredMixin, ListView): 
    login_url='/'
    model=client 
    template_name='main/clients.html' 
    
#def picklist(request): 
#    eqid = request.GET.get('eq', '') 
    
#    equipment_py = Equipment.objects.filter(event = eqid)
#    return render(request, 'main/picklist.html', {'equipment': equipment_py}) 

def debug(request): 
    return render(request, 'main/spa.html')
        

    


    

    
    
