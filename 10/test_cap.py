"""
85: Running test with unittest library
"""
from unittest import TestCase, main
from cap import cap_text


class TestCap(TestCase):
    """
    Test cases for capitalize
    """

    def test_one_word(self):
        """
        Check if the function capitalize a word
        """
        text = "python"
        result = cap_text(text)
        self.assertEqual(result, "Python")

    def test_multiple_word(self):
        """
        Check if the function capitalize multiple words
        """
        text = "monty python"
        result = cap_text(text)
        self.assertEqual(result, "Monty Python")


if __name__ == "__main__":
    main()
