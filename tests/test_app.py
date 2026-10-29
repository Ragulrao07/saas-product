import unittest
from src.app import get_greeting


class TestApp(unittest.TestCase):
    def test_get_greeting(self):
        """Test that get_greeting returns the expected string."""
        self.assertEqual(get_greeting(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
