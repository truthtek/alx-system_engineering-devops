#!/usr/bin/python3
import requests
import sys

def main():
   if len(sys.argv) < 2:
       print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
       return

   employee_id = int(sys.argv[1])
   url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
   response = requests.get(url)

   if response.status_code == 200:
       employee_data = response.json()
       name = employee_data.get("name")
       todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
       todo_response = requests.get(todo_url)
       if todo_response.status_code == 200:
           todo_data = todo_response.json()
           total_tasks = len(todo_data)
           done_tasks = sum(1 for task in todo_data if task.get("completed"))
           print(f"Employee {name} is done with tasks({done_tasks}/{total_tasks}):")
           for task in todo_data:
               if task.get("completed"):
                   print(f"\t {task.get('title')}")
   else:
       print("Failed to retrieve employee data.")

if __name__ == "__main__":
   main()
