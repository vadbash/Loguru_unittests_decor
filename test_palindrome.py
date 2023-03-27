import unittest

def mirror(text):
    return text == text[::-1]

class TestMirror(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(mirror("tat"))
        self.assertTrue(mirror("momom"))
    
    def test_non_palindrome(self):
        self.assertFalse(mirror("hello"))
        self.assertFalse(mirror("world"))

    def test_one(self):
        self.assertTrue(mirror("a"))
        self.assertTrue(mirror("2"))
        self.assertTrue(mirror("="))

if __name__ == '__main__':
    unittest.main()

