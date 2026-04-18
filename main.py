class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}"

class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Project: {self.name}, Description: {self.description}"

class Status:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Status: {self.name}"

class Task:
    def __init__(self, name, description, status, user, project):
        self.name = name
        self.description = description
        self.status = status
        self.user = user
        self.project = project

    def __str__(self):
        return f"Task: {self.name}, Description: {self.description}, Status: {self.status}, User: {self.user}, Project: {self.project}"

class TaskManager:
    def __init__(self):
        self.users = []
        self.projects = []
        self.tasks = []
        self.statuses = []

    def add_user(self, user):
        self.users.append(user)

    def add_project(self, project):
        self.projects.append(project)

    def add_task(self, task):
        self.tasks.append(task)

    def add_status(self, status):
        self.statuses.append(status)

    def print_users(self):
        for user in self.users:
            print(user)

    def print_projects(self):
        for project in self.projects:
            print(project)

    def print_tasks(self):
        for task in self.tasks:
            print(task)

    def print_statuses(self):
        for status in self.statuses:
            print(status)

user1 = User("John Doe", "johndoe@example.com")
project1 = Project("Project 1", "This is project 1")
status1 = Status("In Progress")
task1 = Task("Task 1", "This is task 1", status1, user1, project1)
task_manager = TaskManager()
task_manager.add_user(user1)
task_manager.add_project(project1)
task_manager.add_task(task1)
task_manager.add_status(status1)
task_manager.print_users()
task_manager.print_projects()
task_manager.print_tasks()
task_manager.print_statuses()
project1.add_task(task1)
print(project1.tasks[0])