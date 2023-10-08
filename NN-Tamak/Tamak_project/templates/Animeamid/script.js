let stpbl1 = document.getElementById("stepbl1");
let stpbrdr1 = document.getElementById("stepbrdr1");

let stpbl2 = document.getElementById("stepbl2");
let stpbrdr2 = document.getElementById("stepbrdr2");

let stpbl3 = document.getElementById("stepbl3");
let stpbrdr3 = document.getElementById("stepbrdr3");

stpbl1.onmouseover = function() {
    stpbrdr1.style.borderBottom = "3px solid white";
}
stpbl1.onmouseout = function() {
    stpbrdr1.style.borderBottom = "3px solid black";
}

stpbl2.onmouseover = function() {
    stpbrdr2.style.borderBottom = "3px solid white";
}
stpbl2.onmouseout = function() {
    stpbrdr2.style.borderBottom = "3px solid black";
}

stpbl3.onmouseover = function() {
    stpbrdr3.style.borderBottom = "3px solid white";
}
stpbl3.onmouseout = function() {
    stpbrdr3.style.borderBottom = "3px solid black";
}






var guy = $('.guy'),
        posMove = 'guy rhythm',
        posArms = 'guy rhythm move-arms',
        posLeft = 'guy rhythm look-left',
        posRight = 'guy rhythm look-right';

    $(document).keydown(function(e) {
        console.log(e.which);
        switch (e.which) {
            case 37: // left
                guy.attr('class', posLeft);
                break;

            case 38: // up
                guy.attr('class', posArms);
                break;

            case 39: // right
                guy.attr('class', posRight);
                break;

            case 40: // down
                guy.attr('class', posMove);
                break;

            default:
                return; // exit this handler for other keys
        }
        e.preventDefault(); // prevent the default action (scroll / move caret)
    });
    $(document).keyup(function(e) {
        if (e.which === 27) {
            guy.attr('class', 'guy');
        }
        e.preventDefault(); // prevent the default action (scroll / move caret)
    });