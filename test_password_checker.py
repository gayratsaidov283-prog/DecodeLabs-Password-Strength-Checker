import unittest
from password_checker import check_password

class TestPasswordChecker(unittest.TestCase):

    def test_weak(self):
        self.assertEqual(check_password("abc123"), "Weak")

    def test_medium(self):
        self.assertEqual(check_password("Hello123!"), "Medium")

    def test_strong(self):
        self.assertEqual(check_password("SecurePass2026!"), "Strong")

    def test_empty(self):
        self.assertEqual(check_password(""), "Weak")
    def test_common_password(self):
        self.assertEqual(
            check_password("Password123"),
            "Weak"
        )
if __name__ == "__main__":
    unittest.main()
