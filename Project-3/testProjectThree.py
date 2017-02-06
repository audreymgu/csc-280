import ProjectThree as p
import unittest
#import random

class Test_Project15Game(unittest.TestCase):
    def test_isInRange(self):
        self.assertTrue(p.isInRange('1'))
        self.assertTrue(p.isInRange('2'))
        self.assertTrue(p.isInRange('3'))
        self.assertTrue(p.isInRange('4'))
        self.assertTrue(p.isInRange('5'))
        self.assertTrue(p.isInRange('6'))
        self.assertTrue(p.isInRange('7'))
        self.assertTrue(p.isInRange('8'))
        self.assertTrue(p.isInRange('9'))
        self.assertFalse(p.isInRange('0'))
        self.assertFalse(p.isInRange(''))
        self.assertFalse(p.isInRange('10'))
        self.assertFalse(p.isInRange('x'))
        self.assertFalse(p.isInRange('1234'))
        self.assertFalse(p.isInRange('daafds'))
        
    def test_isNotWinner(self):
        self.assertFalse(p.winner([1,2,3])[0])
        self.assertFalse(p.winner([1,2])[0])
        self.assertFalse(p.winner([])[0])
        self.assertFalse(p.winner([1,2,3,4])[0])
        self.assertFalse(p.winner([1,2,3,5])[0])
        self.assertFalse(p.winner([5,10])[0])
        self.assertFalse(p.winner([7,7,2])[0])
        self.assertFalse(p.winner([2,5,6,9])[0])

    def test_isWinner(self):
        self.assertTrue(p.winner([1,5,9])[0])
        self.assertTrue(p.winner([2,9,4])[0])
        self.assertTrue(p.winner([8,3,4])[0])
        self.assertTrue(p.winner([7,6,2])[0])
        self.assertTrue(p.winner([5,3,7])[0])
        self.assertTrue(p.winner([5,2,8])[0])
        self.assertTrue(p.winner([5,4,6])[0])
        self.assertTrue(p.winner([6,1,8])[0])
        self.assertTrue(p.winner([1,5,9,2])[0])
        self.assertTrue(p.winner([2,9,4,3])[0])
        self.assertTrue(p.winner([8,3,4,7])[0])
        self.assertTrue(p.winner([7,6,2,8])[0])
        self.assertTrue(p.winner([5,3,7,4])[0])
        self.assertTrue(p.winner([5,2,8,7])[0])
        self.assertTrue(p.winner([5,4,6,2])[0])
        self.assertTrue(p.winner([6,1,8,3])[0])
        self.assertTrue(p.winner([1,5,9,4])[0])
        self.assertTrue(p.winner([2,9,4,6])[0])
        self.assertTrue(p.winner([8,3,4,7])[0])
        self.assertTrue(p.winner([7,6,3,2,1])[0])
        self.assertTrue(p.winner([5,3,2,7,4])[0])
        self.assertTrue(p.winner([5,2,4,8,1])[0])
        self.assertTrue(p.winner([2,5,4,6,1])[0])
        self.assertTrue(p.winner([3,2,6,1,8])[0])

    def test_makeMove(self):
        A=[1,2,3]
        B=[4,5,6]
        p.makeMove(3,B,A)
        self.assertEqual(A,[1,2])
        self.assertEqual(B,[4,5,6,3])
        p.makeMove(3,A,B)
        self.assertEqual(A,[1,2,3])
        self.assertEqual(B,[4,5,6])
        P=[]
        M=[3,4,5,6]
        p.makeMove(5,P,M)
        self.assertEqual(P,[5])
        self.assertEqual(M,[3,4,6])
        p.makeMove(6,P,M)
        self.assertEqual(P,[5,6])
        self.assertEqual(M,[3,4])

    #user interface grading guidelines:
    #Were user names collected and used consistently in the game play?
    #Was proper winner (or tie) game summarized at the end?
    #Did the play appropriately prompt alternate users until end of game?
    #Did game terminate properly for both wins and ties?

unittest.main()
    
