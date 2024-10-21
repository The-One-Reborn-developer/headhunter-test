import requests

# Replace with the actual task ID you want to update
task_id_to_update = 3
url = f"http://127.0.0.1:5000/tasks/{task_id_to_update}"

# New data for the task
updated_data = {
    "title": "Updated Task Title",
    "description": "Updated Task Description"
}

# Sending PUT request
response = requests.put(url, json=updated_data)

print(f"Response status code: {response.status_code}")

if response.status_code == 204:
    print(f"Task with ID {task_id_to_update} updated successfully.")
else:
    print("Failed to update task:", response.text)
