const images = [
	"0.gif",
	"1.gif",
	"2.gif",
]
const body = document.body;
const chosenImage = images[Math.floor(Math.random() * images.length)];

// const bgImage = document.createElement("img");
// body.style.backgroundImage = `url(static/img/Calcifer.gif)`;
body.style.backgroundImage = `url(static/img/${chosenImage})`;
// bgImage.src = `img/${chosenImage}`;

// document.body.appendChild(bgImage);