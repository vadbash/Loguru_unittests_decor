import unittest

#main func
def convert(s):
    return s.split()
convert("Hello world")

#testcase
class Test_convert(unittest.TestCase):
    #test1
    def test_simple(self):
        res = convert("Hello world")
        fin = ["Hello", "world"]
        self.assertEqual(res, fin)
    #test2
    def test_big_string(self):
        res = convert("Hello hello world")
        fin = ["Hello", "hello", "world"]
        self.assertEqual(res, fin)
    #test3
    def test_solid_text(self):
        res = convert("helloworld")
        fin = ["helloworld"]
        self.assertEqual(res, fin)
    #test4
    def test_spaces(self):
        res = convert("Hello   world")
        fin = ["Hello", "world"]
        self.assertEqual(res, fin)
        
#running
if __name__ == '__main__':
    unittest.main()
