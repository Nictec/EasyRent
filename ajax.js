function ajax(method, url, form_obj, cb_obj) {
    var key, req_data;
    form_obj = form_obj || {};
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function() {
        if(ajax.readyState == 4){
            if(cb_obj[ajax.status]) { cb_obj[ajax.status](ajax); }
            else if(cb_obj.fallback) { cb_obj.fallback(ajax); }
            else { console.log('error: neither status nor default callback specified for ajax: ', ajax); }
        }
        //maybe a progress cb?
    };
    if(method == 'POST') {
        req_data = new FormData();
        for(key in form_obj){ req_data.append(key, form_obj[key]); }
        ajax.open(method,url,true);
        ajax.send(req_data);
    } else if(method == 'GET') {
        url += '?';
        for(key in form_obj){ url += key + '=' + form_obj[key] + '&'; }
        ajax.open(method,url.slice(0, -1),true);
        ajax.send();
    } else {
        console.log('invalid method: ' + method);
    }
}

/* * usage:
 * ajax("GET",
 *      "server.x/your/doc",
 *      { "param1": "val1", "param2":"val2" },
 *      {   200: function success(){ ... },
 *          404: function not_found(){ ...},
 *          fallback: function unhandled_status(){ ... }});
 */
