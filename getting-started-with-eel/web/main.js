var whatever=1;
var loop_check=0;
function generateQRCode(data) {
//	var data = document.getElementById("data").value
    if(data==2){
    check()
//    change()
     if(whatever==1){
        eel.generate_qr(1)(setImage);
        whatever=0;
    }
    else
    {
    	eel.generate_qr(data)(setImage)

    }
    }
    else if(data==0){

    console.log('clicked');
    change_loop();


    }
    else{
	eel.generate_qr(data)(setImage)
	}
}
function change()
{
    var elem = document.getElementById("repeat");
    if (elem.value=="▶ Shower") elem.value = "On loop";
    else elem.value = "▶ Shower";

}
function change_loop() // no ';' here
{
console.log(loop_check);
    var remember = document.getElementById("togBtn");
    if (remember.checked){
        document.getElementById("loop").style.backgroundColor='#fff';

         if(loop_check%2==0)
        {
        document.getElementById("loop").style.backgroundImage="url('loop-dark.png')";
        console.log('chill pill babe')
        }
        else{
        document.getElementById("loop").style.backgroundImage="url('repeat-dark.png')";
        }
    }
    else{
        document.getElementById("loop").style.backgroundColor='#fe4963';
        if(loop_check%2==0)
        {
        document.getElementById("loop").style.backgroundImage="url('loop.png')";
        console.log('chill pill babe')
        }
        else{
        document.getElementById("loop").style.backgroundImage="url('repeat.png')";
        }
    }
    loop_check+=1;
    eel.generate_qr(0)(setImage);

}
fix=0
function check()
{
    var elem = document.getElementById("spl");
    console.log(elem.style.backgroundImage,elem)
//    if (elem.style.backgroundImage="url('https://cdn.pixabay.com/photo/2014/04/03/00/40/button-309040__340.png')"){ elem.style.backgroundImage="url('https://cdn-icons-png.flaticon.com/512/1666/1666806.png')";
//    alert('maybe its me')}
//    else {
//    elem.style.backgroundImage="url('https://cdn.pixabay.com/photo/2014/04/03/00/40/button-309040__340.png')";
//    alert('fishy');
//    }
    if (fix%2==0){
    $("#spl").removeClass("play");
    $("#spl").toggleClass("pause");
    }
    else{
    $("#spl").removeClass("pause");
    $("#spl").toggleClass("play");
    }
    fix++;

}
function setImage(base64) {
    console.log(base64[0],base64[1]);
	document.getElementById("qr").src = base64[0];
	document.getElementById("song-name").value=base64[1];
	console.log(base64[2]);
	document.getElementById("next-name").value=base64[2];
	console.log(document.getElementById("next-name").value);


}

function validate() {
var remember = document.getElementById("togBtn");

if (remember.checked) {
      $(".wellcome_area").removeClass("bright");

    $(".wellcome_area").toggleClass("dark");
        $(".wellcome-heading").toggleClass("dark");
        $("body").toggleClass("dark");

        $(".get-start-area .submit").toggleClass("dark");
        $(".get-start-area .submit:hover").toggleClass("dark");
        $(".play").removeClass("bright");
    $(".play").toggleClass("dark");
     $(".shuffle").removeClass("bright");
    $(".shuffle").toggleClass("dark");
    $(".shuffle1").toggleClass("dark");

        $(".pause").removeClass("bright");

    $(".pause").toggleClass("dark");
        $(".loop").toggleClass("dark");
        $(".me").toggleClass("dark");
        document.getElementById("output").style.color='#000';
        document.getElementById("song-name").style.color='#000';

         document.getElementById("output").style.textShadow= '2px 0 0 #fff, -2px 0 0 #fff, 0 2px 0 #fff, 0 -2px 0 #fff, 1px 1px #fff, -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff';
document.getElementById("slider").style.background='linear-gradient(to left,#ff0059,gold)';
         document.getElementById("song-name").style.textShadow= '2px 0 0 #fff, -2px 0 0 #fff, 0 2px 0 #000, 0 -2px 0 #fff, 1px 1px #fff, -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff';

// MOON


    document.getElementById("moon").src="https://cdn-icons-png.flaticon.com/512/982/982505.png";
 document.getElementById("headphone").src="earphone.png"
  document.getElementById("heart").src="https://cdn-icons-png.flaticon.com/512/4109/4109291.png";


  } else {
      $(".wellcome_area").removeClass("dark");
        $(".wellcome-heading").removeClass("dark");
      $("body").removeClass("dark");
      $(".get-start-area .submit").removeClass("dark");
      $(".get-start-area .submit:hover").removeClass("dark");
        $(".play").removeClass("dark");
    $(".play").toggleClass("bright");
$(".pause").removeClass("dark");
    $(".pause").toggleClass("bright");
    $(".shuffle").removeClass("dark");
    $(".shuffle").toggleClass("bright");
        $(".shuffle1").removeClass("dark");
        $(".loop").removeClass("dark");
        $(".me").removeClass("dark");

document.getElementById("slider").style.background='linear-gradient(to right,#ff0059,gold)';
        $(".wellcome_area").toggleClass("bright");

    document.getElementById("moon").src="https://cdn-icons-png.flaticon.com/512/4643/4643543.png";

 document.getElementById("headphone").src="music.png";
  document.getElementById("heart").src="https://cdn-icons-png.flaticon.com/512/1029/1029183.png";

  document.getElementById("output").style.color='#dfdfdf';
         document.getElementById("output").style.textShadow= '2px 0 0 #ff0080, -2px 0 0 #ff0080, 0 2px 0 #ff0080, 0 -2px 0 #ff0080, 1px 1px 0 #ff0080, -1px -1px 0 #ff0080, 1px -1px 0 #ff0080, -1px 1px 0 #ff0080';
        document.getElementById("song-name").style.color='#fff';
         document.getElementById("song-name").style.textShadow= '-1px -1px 0 #892cdc, 2px -1px 0 #fd0054, -1px 2px 0 #892cdc, 2px 2px 0 #892cdc';


  }
  }
eel.expose(fine1);
      function fine1(){
      console.log('ok');
      document.getElementById("spl").click();
      document.getElementById("spl").click();

      }

function showVal(value){
var output = document.getElementById("output");

  output.innerHTML = value;
  console.log('ojk');
  eel.adjustVol(value);
  console.log('called python for help',value);

}

// NAVBAR MISSION
window.onload=function(){
var container = document.querySelector('.container1'),
menu= document.querySelector('.menu'),
    btn = document.querySelector('#togBtn'),
    btn2 = document.querySelector('.show'),
    headings = document.querySelectorAll('.portf #h2,.portf #h3'),
    anchor = document.querySelectorAll('.menu a'),
    spany = document.querySelectorAll('.show span');
    btn.textContent='Light';

btn.addEventListener('click', function () {
    'use strict';
    if (this.textContent === 'Light') {
        container.classList.add('light-p');
        menu.classList.add('light');
        this.textContent = 'Dark';
        this.classList.add('light');
    } else {
        container.classList.remove('light-p');
        menu.classList.remove('light');

        this.textContent = 'Light';
        this.classList.remove('light');
    }

}, false);
btn2.addEventListener('click', function () {
    'use strict';
    spany.forEach(function (item) {
        return item.classList.toggle('show-icon');
    });
    container.classList.toggle('wide');
    anchor.forEach(function (item2) {
        return item2.classList.toggle('show-anchor');
    });
    headings.forEach(function (item3) {
        return item3.classList.toggle('big-font');
    });
}, false);

}