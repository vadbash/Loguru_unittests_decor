import unittest

def convert(s):
    return s.split()
convert("Hello world")

class TestConvertStringToWordList(unittest.TestCase):
    def test_simple(self):
        res = convert("Hello world")
        fin = ["Hello", "world"]
        self.assertEqual(res, fin)

    def test_big_string(self):
        res = convert("Hello hello world")
        fin = ["Hello", "hello", "world"]
        self.assertEqual(res, fin)

    def test_solid_text(self):
        res = convert("helloworld")
        fin = ["helloworld"]
        self.assertEqual(res, fin)

    def test_spaces(self):
        res = convert("Hello   world")
        fin = ["Hello", "world"]
        self.assertEqual(res, fin)
        

if __name__ == '__main__':
    unittest.main()
