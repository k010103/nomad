const h1 = document.querySelector("div.hello h1");
function handTitleClick() {
	const clickedClass = "clicked"
	h1.classList.toggle(clickedClass);
}

h1.addEventListener("click", handTitleClick);

console.log(document.querySelector(".home h1:first-child"));
// console.log(document.querySelectorAll(".home h1:first-child"));