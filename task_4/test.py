import unittest
from task_manager import *

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task1=Task("Make HW", "Make uni homework", TaskStatus.IN_PROCCES)
        self.task2=Task("Buy food", "Buy food for a lunch", TaskStatus.PENDING)
        self.subtask_task2=Subtask("Buy milk", "Buy milk for a cat", TaskStatus.PENDING, id(task2))
        self.task3=Task("Buy gifts", "By presents for Christmas", TaskStatus.PENDING)
        self.complex_task=[Subtask("Buy teddy bear", "Buy teddy bear for child",TaskStatus.CLOSED, id(task3)),
        Subtask("Buy christmass tree", "Buy christmass tree for family on Amazon ",TaskStatus.PENDING, id(task3)),
        Subtask("Buy vodka", "Buy vodka for myself",TaskStatus.IN_PROCCES, id(task3))]

    def test_taks_get_name(self):
        self.assertEqual(self.task1.get_name(), 'Make HW')

    def test_subtaks_get_name(self):
        self.assertEqual(self.subtask_task2.get_name(), 'Buy milk')

    def test_print_task(self):
        self.assertEqual(self.manager.print_tasks(), '''#--------TASKS--------#
            Task 140298664592960
            Name: Make HW
            Description: Make uni homework
            Status: IN_PROCCES

            Task 140298664593056
            Name: Buy food
            Description: Buy food for a lunch
            Status: PENDING

            Task 140298664593248
            Name: Buy gifts
            Description: By presents for Christmas
            Status: PENDING ''')

    def test_print_subtask(self):
        self.assertEqual(self.manager.print_subtasks(), '''#--------SUBTASKS--------#
            Task 139995692995328
            Name: Buy milk
            Description: Buy milk for a cat
            Status: PENDING
            Parent id: 139995692999984''')

    def test_print_complextask(self):
        self.assertEqual(self.manager.print_complex_tasks(), '''#--------COMPLEX TASKS--------#
            Task 139650275833280
            Name: Buy teddy bear
            Description: Buy teddy bear for child
            Status: CLOSED
            Parent id: 139650275906208

            Task 139650275833280
            Name: Buy christmass tree
            Description: Buy christmass tree for family on Amazon 
            Status: PENDING
            Parent id: 139650275906208

            Task 139650275833280
            Name: Buy vodka
            Description: Buy vodka for myself
            Status: IN_PROCCES
            Parent id: 139650275906208''')

if __name__ == "__main__":
    unittest.main()