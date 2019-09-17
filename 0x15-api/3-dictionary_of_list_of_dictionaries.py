#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


if __name__ == "__main__":
    user_list = []
    url = 'https://jsonplaceholder.typicode.com/users/'
    dict1 = requests.get(url).json()
    dict_tasks = {}
    for users in dict1:
        my_id = users.get('id')
        username = users.get('username')
        url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
               format(my_id)
        list2 = requests.get(url2).json()
        dict_tasks[my_id] = []
        for tasks in list2:
            status = tasks.get('completed')
            text = tasks.get('title')
            dict_tasks[my_id].append({"task": text, "completed":
                                      status, "username": username})
    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(dict_tasks, outfile)
