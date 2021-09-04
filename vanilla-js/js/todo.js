const toDoForm = document.querySelector("#todo-form");
const toDoInput = toDoForm.querySelector("input");
const todoList = document.querySelector("#todo-list");

const TODO_KEY = "todos";

let toDos = [];

function saveToDos() {
	localStorage.setItem(TODO_KEY, JSON.stringify(toDos));
}

function deleteToDo(event) {
	console.log(event.target.parentElement);
	const li = event.target.parentElement;
	li.remove();
}

function paintToDo(newTodo) {
	const li = document.createElement("li");
	const span = document.createElement("span");
	span.innerText = newTodo;
	const button = document.createElement("button");
	button.innerText = "❌";
	button.addEventListener("click", deleteToDo);
	li.appendChild(span);
	li.appendChild(button);
	todoList.appendChild(li);
}

function handleToDoSubmit(event) {
	event.preventDefault();
	const newTodo = toDoInput.value;
	toDoInput.value = "";
	toDos.push(newTodo);
	paintToDo(newTodo);
	saveToDos();
}

toDoForm.addEventListener("submit", handleToDoSubmit);

function sayHello() {
	console.log("hello");
}

const savedToDos = localStorage.getItem(TODO_KEY);
if (savedToDos) {
	const parsedToDos = JSON.parse(savedToDos);
	toDos = parsedToDos;
	parsedToDos.forEach(paintToDo);
}