#!/usr/bin/python3
"""Gather data from an API and Export to JSON"""
from json import dumps
import requests
from sys import argv

if __name__ == "__main__":
    try:
        int(argv[1])
    except Exception as e:
        exit(1)

    employeeID = int(argv[1])
    holder = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(holder, employeeID)).json()
    todo = requests.get(
        "{}/users/{}/todos".format(holder, employeeID)).json()
    employeeUserName = user.get('username')
    tasks = []
    for element in todo:
        dict = {
            "task": element.get('title'),
            "completed": element.get('completed'),
            "username": employeeUserName
        }
        tasks.append(dict)

    tasksDict = {employeeID: tasks}
    with open("{}.json".format(employeeID), "w") as f:
        f.write(dumps(tasksDict))
