var conf = confirm("Fullscreen mode?");
var docelem = document.documentElement; 
var interact = document.getElementById('toggle');

if (conf == true) {
    if (docelem.requestFullscreen) {
        docelem.requestFullscreen();
    }
    else if (docelem.mozRequestFullScreen) {
        docelem.mozRequestFullScreen();
    }
    else if (docelem.webkitRequestFullscreen) {
        docelem.webkitRequestFullscreen();
    }
    else if (docelem.msRequestFullscreen) {
        docelem.msRequestFullscreen();
    }
} 

interact.onclick = function (argument) {
    var conf = confirm("Fullscreen mode?");
    var docelem = document.documentElement;

    if (conf == true) {
        if (docelem.requestFullscreen) {
            docelem.requestFullscreen();
        }
        else if (docelem.mozRequestFullScreen) {
            docelem.mozRequestFullScreen();
        }
        else if (docelem.webkitRequestFullScreen) {
            docelem.webkitRequestFullScreen();
        }
        else if (docelem.msRequestFullscreen) {
            docelem.msRequestFullscreen();
        }
    }
}