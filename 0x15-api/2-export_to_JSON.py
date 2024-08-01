#!/usr/bin/python3
""" Exports data in the JSON format. """

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(f"{url}users/{user_id}").json()
    username = user_data.get("username")
    params = {"userId": user_id}
    todos = requests.get(f"{url}todos", params=params).json()
    data_to_export = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

