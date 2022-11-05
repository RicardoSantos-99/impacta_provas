alert("oi");

const botao = document.querySelector("button#botao");

const pesq = document.getElementById("campo_pesquisa");

botao.addEventListener(click, function (e) {
  if (pesq.value == "javascript" || pesq.value == "css") {
    console.log("ok");
    e.preventDefault();
  }
});
