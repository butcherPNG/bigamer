
// const enterButton = document.getElementById("enterButton");
// const enterModal = document.getElementById("enterModal");
// const closeButton = document.getElementById("closeButton");


// enterButton.onclick = function() {
//   enterModal.style.display = "block";
// }


// closeButton.onclick = function() {
//   enterModal.style.display = "none";
// }


// window.onclick = function(event) {
//   if (event.target == enterModal) {
//     enterModal.style.display = "none";
//   }
// }


//-----------------------------------------------------------------

const enterButtons = document.querySelectorAll(".enterButton");
const enterModal = document.getElementById("enterModal");
const closeButton = document.getElementById("closeButton");

enterButtons.forEach(button => {
  button.addEventListener("click", () => {
    enterModal.style.display = "block";
  });
});

closeButton.onclick = function() {
  enterModal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == enterModal) {
    enterModal.style.display = "none";
  }
}
