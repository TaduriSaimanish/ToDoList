console.log("hello");

const checkButtons = document.querySelectorAll(".check-button");

checkButtons.forEach((checkButton) => {
  checkButton.addEventListener("click", (obj) => {
    descNode = checkButton.previousElementSibling;
    titleNode = descNode.previousElementSibling;
    descNode.style.textDecoration = "line-through";
    titleNode.style.textDecoration = "line-through";
  });
});
