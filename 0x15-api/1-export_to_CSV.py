#!/usr/bin/python3
"""
Export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    username = user_data.get("username")
    todos_data = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, task.get("completed"), task.get("title")]) for task in todos_data]
