import unittest


def reverse_string_words(string: str) -> str:
    words = string.split()
    return " ".join(words[::-1])


class TestReverseStringWords(unittest.TestCase):
    """Test suite for the reverse_string_words function."""

    def test_empty_string(self):
        """Test reversing words in an empty string."""
        self.assertEqual(reverse_string_words(""), "")

    def test_single_word(self):
        """Test reversing words in a string with a single word."""
        self.assertEqual(reverse_string_words("hello"), "hello")
        self.assertEqual(reverse_string_words("Python"), "Python")

    def test_multiple_words(self):
        """Test reversing words in a string with multiple words."""
        self.assertEqual(reverse_string_words("hello world"), "world hello")
        self.assertEqual(reverse_string_words("Python is fun"), "fun is Python")

    def test_leading_and_trailing_spaces(self):
        """Test with leading and trailing spaces.
        The split() method handles this by default, and join() uses single spaces.
        """
        self.assertEqual(reverse_string_words("  hello   world  "), "world hello")
        self.assertEqual(reverse_string_words("  leading spaces"), "spaces leading")
        self.assertEqual(reverse_string_words("trailing spaces   "), "spaces trailing")

    def test_multiple_spaces_between_words(self):
        """Test with multiple spaces between words."""
        self.assertEqual(reverse_string_words("hello   world"), "world hello")
        self.assertEqual(reverse_string_words("one  two   three"), "three two one")

    def test_string_with_punctuation(self):
        """Test with punctuation attached to words."""
        self.assertEqual(reverse_string_words("Hello, world!"), "world! Hello,")

    def test_string_with_numbers(self):
        """Test with numbers as words."""
        self.assertEqual(reverse_string_words("1 2 3"), "3 2 1")
        self.assertEqual(reverse_string_words("item1 item2"), "item2 item1")

    def test_string_with_only_spaces(self):
        """Test with a string containing only spaces.
        string.split() on '   ' results in [], and ' '.join([]) results in ''.
        """
        self.assertEqual(reverse_string_words("   "), "")


if __name__ == "__main__":
    unittest.main()
