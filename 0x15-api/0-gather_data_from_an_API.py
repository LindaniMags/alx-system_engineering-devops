#!/usr/bin/python3
"""
Returns todo list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_data = requests.get(url + "users/{}".format(employee_id)).json()
    params = {"userId": employee_id}
    todos_data = requests.get(url + "todos", params=params).json()
    completed = [task.get("title") for task in todos_data if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user_data.get("name"), len(completed), len(todos_data)))
    [print("\t {}".format(complete)) for complete in completed]
