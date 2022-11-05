//Detecting Button Press
for (let index = 0; index<document.querySelectorAll(".drum").length; index++) {
    document.querySelectorAll("button")[index].addEventListener("click",function(){
       var buttonInnerHtml=this.innerHTML;
       makeSound(buttonInnerHtml);
    buttonAnimation(buttonInnerHtml);
    });}
//Detect Keyboard Press
document.addEventListener("keydown",function(event){
    makeSound(event.key);
    buttonAnimation(event.key)
});
function makeSound(key){
        switch (key) {
             case "w":
               var tom1=new Audio('sounds/tom-1.mp3');
               tom1.play();
                break;
            case "a":
                var tom2=new Audio('sounds/tom-2.mp3');
                tom2.play();
                 break;
            case "s":
               var tom3=new Audio('sounds/tom-3.mp3');
               tom3.play();
                break;
            case "d":
                var tom4=new Audio('sounds/tom-4.mp3');
                tom4.play();
                 break;  
            case "j":
               var kick=new Audio('sounds/kick.mp3');
               kick.play();
                break;  
            case "k":
                var snare=new Audio('sounds/snare.mp3');
                snare.play();
                 break;   
            case "l":
               var sounds=new Audio('sounds/crash.mp3');
               sounds.play();
                break; 
        default:
            break;
       }
    };

function buttonAnimation(currentKey){
var activeButton=document.querySelector("."+currentKey);
activeButton.classList.add("pressed");
setTimeout(function () {
    activeButton.classList.remove("pressed");
},100);
}