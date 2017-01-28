import ProjectZero
import unittest

class Test_ProjectZero(unittest.TestCase):
    def test_euclid(self):
        self.assertEqual(ProjectZero.euclid(100,10),10)
        self.assertEqual(ProjectZero.euclid(10,100),10)
        self.assertEqual(ProjectZero.euclid(100,13),1)
        self.assertEqual(ProjectZero.euclid(100,100),100)
        self.assertEqual(ProjectZero.euclid(13,39),13)
        self.assertEqual(ProjectZero.euclid(120,35),5)
        self.assertEqual(ProjectZero.euclid(1001,77),77)
        self.assertEqual(ProjectZero.euclid(1001,33),11)
        
    def test_coprime(self):
        self.assertEqual(ProjectZero.coprime([23,17]),True)
        self.assertEqual(ProjectZero.coprime([23,17,15]),True)
        self.assertEqual(ProjectZero.coprime([23,46,17]),False)
        self.assertEqual(ProjectZero.coprime([2,3,5,7,11,13,17]),True)
        self.assertEqual(ProjectZero.coprime([7,11,13]),True)
        self.assertEqual(ProjectZero.coprime([7,11,13,1001]),False)

    def test_fibonacci(self):
        self.assertEqual(len(ProjectZero.fibonacci(1)), 1)
        self.assertEqual(len(ProjectZero.fibonacci(2)), 2)
        self.assertEqual(len(ProjectZero.fibonacci(50)), 50)
        self.assertEqual(ProjectZero.fibonacci(55)[49], 12586269025L)

unittest.main()

#To execute script from within python:
#>> execfile('filename.py')
#To generate pyc code: 
#>> import py_compile
#>> py_compile.compile("file.py")
