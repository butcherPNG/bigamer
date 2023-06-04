const registerBtn = document.getElementById("registerButton");
const registerModal = document.getElementById("registerModal");
const closeBtn = registerModal.querySelector(".close");

registerBtn.addEventListener("click", () => {
  registerModal.style.display = "block";
});

closeBtn.addEventListener("click", () => {
  registerModal.style.display = "none";
});


//window.addEventListener("click", (event) => {
//  if (event.target === registerModal) {
//    registerModal.style.display = "none";
//  }
//});