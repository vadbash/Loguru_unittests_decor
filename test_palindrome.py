import unittest

#main func
def mirror(text):
    return text == text[::-1]

#testcase
class TestMirror(unittest.TestCase):
    #test1
    def test_palindrome(self):
        self.assertTrue(mirror("tat"))
        self.assertTrue(mirror("momom"))
    #test2
    def test_non_palindrome(self):
        self.assertFalse(mirror("hello"))
        self.assertFalse(mirror("world"))
    #test3
    def test_one(self):
        self.assertTrue(mirror("a"))
        self.assertTrue(mirror("2"))
        self.assertTrue(mirror("="))

#running
if __name__ == '__main__':
    unittest.main()

