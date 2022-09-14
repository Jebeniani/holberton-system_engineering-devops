#!/usr/bin/python3
"""Writing a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress"""
from ast import Try
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
    tada = requests.get(
        "{}/users/{}/todos".format(holder, employeeID)).json()
    EmployeeName = user.get('name')
    completed = 0
    total = 0
    for element in tada:
        if element.get('completed') is True:
            total += 1
            completed += 1
        else:
            total += 1

    print("Employee {} is done with tasks({}/{}):".format(
        EmployeeName, completed, total))

    for item in tada:
        if item.get('completed') is True:
            print("\t {}".format(item.get('title')))
