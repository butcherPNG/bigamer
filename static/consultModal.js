const enterButtons2 = document.querySelectorAll(".consultEnterButton");
const enterModal2 = document.getElementById("consultModal");
const closeButton2 = document.getElementById("closeButton2");

enterButtons2.forEach(button => {
  button.addEventListener("click", () => {
    enterModal2.style.display = "block";
  });
});

closeButton2.onclick = function() {
  enterModal2.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == enterModal2) {
    enterModal2.style.display = "none";
  }
}