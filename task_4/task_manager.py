import enum

class TaskStatus(enum.Enum):
    PENDING = 0
    IN_PROCCES = 1
    DECLINED = 2
    CLOSED = 3
    CANCELED = 4

class Task:
    def __init__(self, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

class Subtask(Task):
    # have comlex task id
    def __init__(self,name, description, status, parent_id):
        super().__init__(name, description, status)
        self.parent_id = parent_id
    
class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks   
       
        
class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}
    
    def create_task(self, task):
        self.tasks[id(task)]=task
    
    def create_subtask(self, subtask):
        self.subtasks[id(subtask)]=subtask
    
    def create_complex_task(self, complex_task):
        self.complex_tasks[id(complex_task)]=complex_task
    
    def get_tasks(self):
        return self.tasks

    def get_subtasks(self):
        return self.subtasks
    
    def get_complex_tasks(self):
        return self.complex_tasks
    
    def get_tasks_by_id(self, id):
        return self.tasks.get(id)
    
    def get_subtasks_by_id(self, id):
        return self.subtasks.get(id)
    
    def get_complex_tasks_by_id(self, id):
        return self.complex_tasks.get(id)
    
    def remove_tasks(self):
        self.tasks.clear()
    
    def remove_subtasks(self):
        self.subtasks.clear()
    
    def remove_complex_tasks(self):
        self.complex_tasks.clear()
    
    def remove_task_by_id(self, id):
        self.tasks.pop(id)
    
    def remove_subtask_by_id(self, id):
        self.subtasks.pop(id)
    
    def remove_complex_task_by_id(self, id):
        self.complex_tasks.pop(id)
    
    def update_status(self, task, new_status):
        self.get_tasks_by_id(id(task)).status=new_status

    def print_tasks(self):
        print("#--------TASKS--------#")
        for id,task in self.tasks.items():
            print("Task", id)
            print("Name:", (task.name))
            print("Description:",task.description)
            print("Status:", task.status.name)
            print()
    def print_subtasks(self):
        print("#--------SUBTASKS--------#")
        for id, subtask in self.subtasks.items():
            print("Task",id)
            print("Name:",subtask.name)
            print("Description:",subtask.description)
            print("Status:", subtask.status.name)
            print("Parent id:", subtask.parent_id)
            print()
    def print_complex_tasks(self):
        print("#--------COMPLEX TASKS--------#")
        for id_complex_tasks, complex_tasks in self.complex_tasks.items():
            for subtask in complex_tasks:
                print("Task",id_complex_tasks)
                print("Name:",subtask.name)
                print("Description:",subtask.description)
                print("Status:", subtask.status.name)
                print("Parent id:", subtask.parent_id)
                print()

manager = TaskManager()
task1=Task("Make HW", "Make uni homework", TaskStatus.IN_PROCCES)
task2=Task("Buy food", "Buy food for a lunch", TaskStatus.PENDING)
subtask_for_task2=Subtask("Buy milk", "Buy milk for a cat", TaskStatus.PENDING, id(task2))
task3=Task("Buy gifts", "By presents for Christmas", TaskStatus.PENDING)
complex_task=[Subtask("Buy teddy bear", "Buy teddy bear for child",TaskStatus.CLOSED, id(task3)),
        Subtask("Buy christmass tree", "Buy christmass tree for family on Amazon ",TaskStatus.PENDING, id(task3)),
        Subtask("Buy vodka", "Buy vodka for myself",TaskStatus.IN_PROCCES, id(task3))]

manager.create_task(task1)
manager.create_task(task2)
manager.create_subtask(subtask_for_task2)
manager.create_task(task3)
manager.create_complex_task(complex_task)

#Юнит тесты лень писать для всего, мы же один раз научились их писать, зачем это делать каждый раз?
#Понимаю, что полезно для привычки, и стоит с них начинать, но порой же не нужно усложнять себе жизнь