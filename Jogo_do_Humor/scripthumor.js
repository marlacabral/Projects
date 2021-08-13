const foto = document.getElementById("bh")

const botao = document.getElementById("btn")

botao.onclick = function(){
    if(btn.value === "mauhumor"){
        foto.src = "img/mhumor.png";
        btn.value = "bomhumor";
        
    }
    else if(btn.value === "bomhumor"){
        foto.src = "img/bhumor.png";
        btn.value = "mauhumor";
    }
}