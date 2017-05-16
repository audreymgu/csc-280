import ProjectOne as p
import unittest

class Test_ProjectOne(unittest.TestCase):
    def test_gcf(self):
        self.assertEqual(p.gcf(100,10),10)
        self.assertEqual(p.gcf(10,100),10)
        self.assertEqual(p.gcf(100,13),1)
        self.assertEqual(p.gcf(100,100),100)
        self.assertEqual(p.gcf(13,39),13)
        self.assertEqual(p.gcf(120,35),5)
        self.assertEqual(p.gcf(1001,77),77)
        self.assertEqual(p.gcf(1001,33),11)
        
    def test_reduce(self):
        self.assertEqual(p.reduce((0,3)),(0,1))
        self.assertEqual(p.reduce((1,1)),(1,1))
        self.assertEqual(p.reduce((-1,1)),(-1,1))
        self.assertEqual(p.reduce((1,-1)),(-1,1))
        self.assertEqual(p.reduce((-1,-1)),(1,1))
        self.assertEqual(p.reduce((100,10)),(10,1))
        self.assertEqual(p.reduce((10,100)),(1,10))
        self.assertEqual(p.reduce((4,16)),(1,4))
        self.assertEqual(p.reduce((22,33)),(2,3))
        self.assertEqual(p.reduce((14,49)),(2,7))

    def test_add(self):
        self.assertEqual(p.add((1,4),(1,2)),(3,4))
        self.assertEqual(p.add((20,30),(2,3)),(4,3))
        self.assertEqual(p.add((10,40),(1,2)),(3,4))
        self.assertEqual(p.add((1,4),(10,20)),(3,4))
        self.assertEqual(p.add((1,7),(2,14)),(2,7))
        self.assertEqual(p.add((10,1),(10,1)),(20,1))
        self.assertEqual(p.add((10,1),(-10,1)),(0,1))

    def test_subtract(self):
        self.assertEqual(p.subtract((1,4),(1,2)),(-1,4))
        self.assertEqual(p.subtract((20,30),(2,3)),(0,1))
        self.assertEqual(p.subtract((10,40),(1,2)),(-1,4))
        self.assertEqual(p.subtract((1,4),(10,20)),(-1,4))
        self.assertEqual(p.subtract((1,7),(2,14)),(0,1))
        self.assertEqual(p.subtract((10,1),(10,1)),(0,1))
        self.assertEqual(p.subtract((10,1),(-10,1)),(20,1))

    def test_multiply(self):
        self.assertEqual(p.multiply((1,4),(1,2)),(1,8))
        self.assertEqual(p.multiply((-1,4),(1,2)),(-1,8))
        self.assertEqual(p.multiply((1,-4),(1,2)),(-1,8))
        self.assertEqual(p.multiply((-1,-4),(1,2)),(1,8))
        self.assertEqual(p.multiply((1,4),(-1,2)),(-1,8))
        self.assertEqual(p.multiply((-1,4),(1,-2)),(1,8))
        self.assertEqual(p.multiply((1,-4),(-1,-2)),(-1,8))
        self.assertEqual(p.multiply((-1,-4),(1,-2)),(-1,8))
        self.assertEqual(p.multiply((20,30),(2,3)),(4,9))
        self.assertEqual(p.multiply((10,40),(1,2)),(1,8))
        self.assertEqual(p.multiply((1,4),(10,20)),(1,8))
        self.assertEqual(p.multiply((1,7),(2,14)),(1,49))
        self.assertEqual(p.multiply((10,1),(10,1)),(100,1))
        self.assertEqual(p.multiply((10,1),(-10,1)),(-100,1))

    def test_square(self):
        self.assertEqual(p.square((1,2)),(1,4))
        self.assertEqual(p.square((3,2)),(9,4))
        self.assertEqual(p.square((-1,7)),(1,49))
        self.assertEqual(p.square((10,-2)),(25,1))

    def test_invert(self):
        self.assertEqual(p.invert((47,81)), (81,47))
        self.assertEqual(p.invert((4,-8)), (-2,1))
        self.assertEqual(p.invert((-47,81)), (-81,47))
        self.assertEqual(p.invert((-2,3)), (-3,2))
        self.assertEqual(p.invert((1,1)), (1,1))
        self.assertEqual(p.invert((-1,1)), (-1,1))
        self.assertEqual(p.invert((1,-1)), (-1,1))
        self.assertEqual(p.invert((-1,-1)), (1,1))

    def test_divide(self):
        self.assertEqual(p.divide((1,4),(1,2)),(1,2))
        self.assertEqual(p.divide((-1,4),(1,2)),(-1,2))
        self.assertEqual(p.divide((1,-4),(1,2)),(-1,2))
        self.assertEqual(p.divide((-1,-4),(1,2)),(1,2))
        self.assertEqual(p.divide((1,4),(-1,2)),(-1,2))
        self.assertEqual(p.divide((-1,4),(1,-2)),(1,2))
        self.assertEqual(p.divide((1,-4),(-1,-2)),(-1,2))
        self.assertEqual(p.divide((-1,-4),(1,-2)),(-1,2))
        self.assertEqual(p.divide((20,30),(2,3)),(1,1))
        self.assertEqual(p.divide((10,40),(1,2)),(1,2))
        self.assertEqual(p.divide((1,4),(10,20)),(1,2))
        self.assertEqual(p.divide((1,7),(2,14)),(1,1))
        self.assertEqual(p.divide((10,1),(10,1)),(1,1))
        self.assertEqual(p.divide((10,1),(-10,1)),(-1,1))

    def test_toFloat(self):
        self.assertEqual(p.toFloat((4,5)), 0.8)
        self.assertEqual(p.toFloat((1,64)), 0.015625)
        
    def test_typeTest(self):
        self.assertEqual(type(p.gcf(10,20)), int)
        self.assertEqual(type(p.reduce((10,20))), tuple)
        self.assertEqual(type(p.add((10,20),(1,2))), tuple)
        self.assertEqual(type(p.add((10,20),(1,2))[0]), int)
        self.assertEqual(type(p.add((10,20),(1,2))[1]), int)
        self.assertEqual(type(p.toFloat((3,5))), float)

unittest.main()

#To execute script from within python:
#>> execfile('filename.py')
#To generate pyc code: 
#>> import py_compile
#>> py_compile.compile("file.py")
