var elm = document.getElementById("app") 

ajax("GET", "/dashboard", { 
200: load(), 
404: error()
})

function load(response){ 
 elm.innerHTML = response.responseText
} 

function error(){ 
    console.error("resource not found")
}