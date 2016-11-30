function ajaxLogin() {
    var token = document.getElementById("login-form").csrfmiddlewaretoken.value;
    var user = document.getElementById("username").value;
    var pw = document.getElementById("password").value;

    ajax("POST", "/login/", {
        username: user,
        password: pw,
        csrfmiddlewaretoken: token
    }, {
        200: success,
        400: fail, 
        
    });




    function success(response) {
        var redirectUrl = getQueryVariable("next");

        function getQueryVariable(variable) {
            var query = window.location.search.substring(1);
            var vars = query.split("&");
            for (var i = 0; i < vars.length; i++) {
                var pair = vars[i].split("=");
                if (pair[0] == variable) {
                    return pair[1];
                }
            }
            
        }
        console.log("Success");
        window.location = redirectUrl || '/dashboard/';
    }

    function fail(response) {
        console.error("wrong credentials");
        document.querySelector(".alert").classList.remove("hidden");
    }
}