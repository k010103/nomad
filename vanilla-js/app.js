const h1 = document.querySelector("div.hello h1");

function handTitleClick() {
	h1.style.color = "blue";
}

function handleMouseEnter() {
	h1.innerText = "Mouse is here!";
}

function handleMouseLeave() {
	h1.innerText = "Mouse is gond!";
}

function handleWindowResize() {
	document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy() {
	alert("copy!");
}

h1.addEventListener("click", handTitleClick);
h1.addEventListener("mouseenter", handleMouseEnter);
h1.addEventListener("mouseleave", handleMouseLeave);

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);