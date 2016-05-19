
//Jquery 1.8.3
//var $elems = $("html, body");
var $elems = $("body");
var delta = 0;

$(document).ready(function(){
	enterFullscreen();
	console.log("Prompter");
});

$(document).on("mousemove", function(e) {
    var h = $(window).height();
    var y = e.clientY - h / 2;
    delta = y * 0.07;

    //cursor
    $mouseY = e.clientY;
});

$(window).on("blur mouseleave", function() {
    delta = 0;
});


/*
(function f() {
    if(delta) {
		$("#cursor").css({top:$mouseY +'px'});

        $elems.scrollTop(function(i, v) {
        	$("#foo").text(v+delta);
            return v + delta;
        });

    }

    //cursor
    //$yp += (($mouseY - $yp)/12);
    //
    //webkitRequestAnimationFrame(f);
    requestAnimationFrame(f);
})();*/

function f() {
    if(delta) {
		$("#cursor").css({top:$mouseY +'px'});

        $elems.scrollTop(function(i, v) {
        	$("#foo").text(v+delta);
            return v + delta;
        });

    }

    //cursor
    //$yp += (($mouseY - $yp)/12);
    //
    //webkitRequestAnimationFrame(f);
    requestAnimationFrame(f);
}

var fps = 30;
(function draw() {
	setTimeout(function() {
		requestAnimationFrame(draw);
		// Drawing code goes here
		if(delta) {
			$("#cursor").css({top:$mouseY +'px'});

			$elems.scrollTop(function(i, v) {
				$("#foo").text(v+delta+"  --  "+delta);
				return v + delta;
			});

		}

	}, 1000 / fps);
})();


