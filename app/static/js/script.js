const apiUrl = 'http://127.0.0.1:5000/tasks';


async function fetchTasks() {
    const response = await fetch(apiUrl);
    const tasks = await response.json();
    displayTasks(tasks.tasks);
}


function displayTasks(tasks) {
    const tasksContainer = document.getElementById('tasks');
    tasksContainer.innerHTML = '';
    tasks.forEach(task => {
        const taskDiv = document.createElement('div');
        taskDiv.className = 'task';
        taskDiv.innerHTML = `
            <strong>${task.title}</strong>: ${task.description}
            <button onclick="toggleEditForm(${task.id}, '${task.title}', '${task.description}')">Edit</button>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        tasksContainer.appendChild(taskDiv);
    });
}


function toggleForm(action) {
    const form = document.getElementById(`${action}-form`);
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}


async function addTask() {
    const title = document.getElementById('add-title').value;
    const description = document.getElementById('add-description').value;

    await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, description }),
    });

    document.getElementById('add-title').value = '';
    document.getElementById('add-description').value = '';
    toggleForm('add');
    fetchTasks();
}


function toggleEditForm(id, title, description) {
    const editForm = document.createElement('div');
    editForm.innerHTML = `
        <h2>Edit Task</h2>
        <input type="text" id="edit-title" value="${title}" required>
        <input type="text" id="edit-description" value="${description}" required>
        <button onclick="updateTask(${id})">Update</button>
        <button onclick="document.body.removeChild(this.parentNode)">Cancel</button>
    `;
    document.body.appendChild(editForm);
}


async function updateTask(id) {
    const title = document.getElementById('edit-title').value;
    const description = document.getElementById('edit-description').value;

    await fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, description }),
    });

    fetchTasks();
}


async function deleteTask(id) {
    await fetch(`${apiUrl}/${id}`, {
        method: 'DELETE',
    });

    fetchTasks();
}


fetchTasks();