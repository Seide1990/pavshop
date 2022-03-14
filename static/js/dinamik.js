//let btn = document.getElementById("quinty");
let count = document.getElementById("mehsulsayi");

    
let select = document.createElement("select");  
 // alert(count.innerText)
 alert('salam')
     
for(let i = 0; i < 5; i++){

    let option = document.createElement("option");
   let text = document.createTextNode(i);
  option.appendChild(text);
 select.appendChild(option);            
}

document.getElementById("menu").appendChild(select);
btn.addEventListener("click",function () {
adi= document.getElementById("menu").value;
alert(adi)
});
