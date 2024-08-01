#!/usr/bin/python3
""" Records all tasks from all employees """
import json
import requests

def import_users():
    url = "https://jsonplaceholder.typicode.com/"
    users_data = requests.get(url + "users").json()
    exporting = {}
    for user in users_data:
        user_id = user["id"]
        user_url = url + f"todos?userId={user_id}"
        todos = requests.get(user_url).json()

        exporting[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todos
        ]

    return exporting

if __name__ == "__main__":
    exporting = import_users()

    with open("todo_all_employees.json", "w") as f:
        json.dump(exporting, f, indent=4)
