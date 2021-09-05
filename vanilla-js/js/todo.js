const toDoForm = document.querySelector("#todo-form");
const toDoInput = toDoForm.querySelector("input");
const todoList = document.querySelector("#todo-list");

const TODO_KEY = "todos";

let toDos = [];

function saveToDos() {
	localStorage.setItem(TODO_KEY, JSON.stringify(toDos));
}

function deleteToDo(event) {
	const li = event.target.parentElement;
	toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
	li.remove();
	saveToDos();
}

function paintToDo(newTodoObj) {
	const li = document.createElement("li");
	li.id = newTodoObj.id;
	const span = document.createElement("span");
	span.innerText = newTodoObj.text;
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
	const newTodoObj = {
		text:newTodo,
		id:Date.now(),
	}
	toDos.push(newTodoObj);
	paintToDo(newTodoObj);
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
	parsedToDos.filter
}