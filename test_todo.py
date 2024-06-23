# test_todo.py
import unittest
from todo import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.assertTrue(self.todo_list.add_task("Buy groceries"))
        self.assertIn("Buy groceries", self.todo_list.get_tasks())

    def test_remove_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertTrue(self.todo_list.remove_task("Buy groceries"))
        self.assertNotIn("Buy groceries", self.todo_list.get_tasks())

    def test_get_tasks(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Read a book")
        tasks = self.todo_list.get_tasks()
        self.assertEqual(tasks, ["Buy groceries", "Read a book"])

if __name__ == "__main__":
    unittest.main()
