// Make chat box visible when clicked
function openForm() {
  document.getElementById("chatForm").style.display = "block";
}

// Hide chat box visible when closed
function closeForm() {
  document.getElementById("chatForm").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function () {
  const cookieModal = document.getElementById("cookieModal");
  const acceptCookiesButton = document.getElementById("acceptCookies");

  // Check if user previously accepted cookies
  const cookiesAccepted = localStorage.getItem("cookiesAccepted");

  if (!cookiesAccepted) {
    cookieModal.style.display = "flex";
  }

  document.getElementById("rejectCookies").onclick = function () {
    window.location.replace("https://www.google.co.uk");
  };

  acceptCookiesButton.addEventListener("click", function () {
    // Set a flag in local storage to remember user's choice
    localStorage.setItem("cookiesAccepted", "true");
    cookieModal.style.display = "none";
  });
});
