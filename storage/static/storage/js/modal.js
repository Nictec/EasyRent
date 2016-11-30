// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
 
var modal = document.getElementById('myModal'); 

var equipment
function openModal(eq){ 
    ajax('GET', '/eqadd/', {'eq':eq}, {200:ok, 404:function not_found(){console.error('view not found')}}) 
    window.equipment = eq
} 

function ok(response){ 
    var modal = document.getElementById('myModal');
    var content = document.getElementById('modalContent'); modal.style.display = "block"; 
    content.innerHTML = response.responseText; 
    return console.log('modal opened')
}


function ajaxSubmit(){ 
    var token = document.getElementById("qform").csrfmiddlewaretoken.value;
    var quantity = document.getElementById("id_quantity"); 
    
    ajax("POST", "/eqadd/", {quantity:quantity, csrfmiddlewaretoken:token,}, {200:closeModal, 404:function not_found(){console.error('view not found')}});  
    
    function closeModal(response){ 
       modal.style.display = "none"; 
       console.info("Data successfully posted"); 
        
    } 
    
}