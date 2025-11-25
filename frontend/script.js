const apiUrl = "http://127.0.0.1:8000/tasks";

async function fetchTasks() {
    const res = await fetch(apiUrl);
    const tasks = await res.json();
    const list = document.getElementById("taskList");
    list.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.textContent = task.name;
        if(task.completed){
            li.classList.add("completed");
        }
        li.onclick = () => toggleTask(task.id);
        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById("taskInput");
    const name = input.value;
    if (!name) return alert("Enter task name");
    await fetch(apiUrl + "?name=" + name, { method: "POST" });
    input.value = "";
    fetchTasks();
}

async function toggleTask(id) {
    await fetch(`${apiUrl}/${id}`, { method: "PUT" });
    fetchTasks();
}

// Initial load
fetchTasks();
