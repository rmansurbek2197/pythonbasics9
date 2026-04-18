class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class Status:
    def __init__(self, name):
        self.name = name

class TaskManagementApp:
    def __init__(self):
        self.users = []
        self.projects = []
        self.tasks = []
        self.statuses = []

    def add_user(self, name, email):
        self.users.append(User(name, email))

    def add_project(self, name):
        self.projects.append(Project(name))

    def add_task(self, name, status_name):
        for status in self.statuses:
            if status.name == status_name:
                task = Task(name, status)
                self.tasks.append(task)
                for project in self.projects:
                    project.tasks.append(task)

    def add_status(self, name):
        self.statuses.append(Status(name))

    def print_users(self):
        for user in self.users:
            print(user.name, user.email)

    def print_projects(self):
        for project in self.projects:
            print(project.name)

    def print_tasks(self):
        for task in self.tasks:
            print(task.name, task.status.name)

    def print_statuses(self):
        for status in self.statuses:
            print(status.name)

app = TaskManagementApp()
app.add_status("New")
app.add_status("In Progress")
app.add_status("Done")
app.add_user("John Doe", "johndoe@example.com")
app.add_project("Project 1")
app.add_task("Task 1", "New")
app.print_users()
app.print_projects()
app.print_tasks()
app.print_statuses()