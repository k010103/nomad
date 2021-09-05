const API_KEY = "6324f26d4ec971dd0f59a8d0027b8d9b";

function onGeoOk(position) {
	const lat = position.coords.latitude;
	const lon = position.coords.longitude;
	const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
	console.log(url);
	fetch(url)
		.then(response => response.json())
		.then(data => {
			const weather = document.querySelector("#weather span:first-child");
			const city = document.querySelector("#weather span:last-child");
			const temperature = data.main.temp;
			city.innerText = data.name;
			weather.innerText = `${data.weather[0].main} / ${temperature}°`;
	});
}

function onGeoError() {
	alert("can't find you. No weather for you.")
}

function changeColor() {
	weather.style.color = colors[Math.floor(Math.random() * colors.length)];
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
setInterval(changeColor, 200);