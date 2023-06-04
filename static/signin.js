const signinBtn = document.getElementById("signinButton");
const signinModal = document.getElementById("signinModal");
const closeBtn2 = document.getElementById("closeBtn2");

signinBtn.addEventListener("click", () => {
  signinModal.style.display = "block";
});

closeBtn2.addEventListener("click", () => {
  signinModal.style.display = "none";
  document.body.classList.remove("modal-open");
});

//window.onclick = function(event) {
//  if (event.target == signinModal) {
//    registerModal.style.display = "none";
//    signinModal.style.display = "none";
//  }
//}



// const signinBtn = document.getElementById("signinBtn");
// const signinModal = document.getElementById("signinModal");
// const closeBtn2 = document.querySelector(".close2");
//
// signinBtn.addEventListener("click", () => {
//   signinModal.style.display = "block";
// });
//
// closeBtn2.addEventListener("click", () => {
//   signinModal.style.display = "none";
// });
//
// window.addEventListener("click", (event) => {
//   if (event.target === signinModal) {
//     signinModal.style.display = "none";
//   }
// });

//$('#registerModal').on('hidden.bs.modal', function (e) {
//    if ($('#signinModal').hasClass('show')) {
//      $('body').addClass('modal-open');
//    }
//  });
//
//  $('#signinModal').on('show.bs.modal', function (e) {
//    $('#registerModal').modal('hide');
//  });
//
//  $("#signinModal").modal({
//  });