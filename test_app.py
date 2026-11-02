import unittest
from app import hello_world, welcome_message

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(
            hello_world(),
            "Wrong Message!"
        )

    def test_hello_world_type(self):
        self.assertIsInstance(hello_world(), str)

    def test_welcome_message_ansh(self):
        self.assertEqual(
            welcome_message("Ansh"),
            "Welcome to DevOps, Ansh!"
        )

    def test_welcome_message_student(self):
        self.assertEqual(
            welcome_message("Student"),
            "Welcome to DevOps, Student!"
        )

if __name__ == "__main__":
    unittest.main()
