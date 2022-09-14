#!/usr/bin/python3
"""Gather data from an API and Export to CSV """
import csv
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
    with open('{}.csv'.format(employeeID), 'w', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for item in todo:
            writer.writerow([employeeID, employeeUserName, item.get(
                'completed'), item.get('title')])
