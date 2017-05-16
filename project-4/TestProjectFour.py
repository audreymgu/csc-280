import ProjectFour as p
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

    def test_findMoveToWin(self):
        self.assertEqual(p.findMoveToWin([4,5],[6]),6)
        self.assertEqual(p.findMoveToWin([4,5],range(1,10)),6)
        self.assertEqual(p.findMoveToWin([2,5],range(1,10)),8)
        self.assertEqual(p.findMoveToWin([2,4],range(1,10)),9)
        self.assertEqual(p.findMoveToWin([3,5],range(1,10)),7)
        self.assertEqual(p.findMoveToWin([1,6],range(1,10)),8)
        self.assertEqual(p.findMoveToWin([3,4],range(1,10)),8)
        self.assertEqual(p.findMoveToWin([1,5],range(1,10)),9)
        self.assertEqual(p.findMoveToWin([2,6],range(1,10)),7)
        self.assertEqual(p.findMoveToWin([4,5,2],[1,3,7,8]),8)
        self.assertEqual(p.findMoveToWin([4,5,2],[1,3,7,6]),6)
        self.assertEqual(p.findMoveToWin([4,5,2],[1,3,7,9]),9)
        self.assertEqual(p.findMoveToWin([4,5,2],[1,3,7]),False)
        self.assertTrue(p.findMoveToWin([4,5,2,7],[3,6,9]) in [3,6,9])
        self.assertFalse(p.findMoveToWin([1,3,7,9],[2,4,6,8]))

    def test_pickRandomly(self):
        ct=[0]*9
        for i in range(9000):
            n=p.pickRandomly(range(9))
            ct[n]+=1
        for i in range(9):
            self.assertTrue(ct[i]<1100)
            self.assertTrue(ct[i]>900)

    def test_childChoice(self):
        self.assertEqual(p.childChoice([2,1,4],[3,8,6],[5,7,9]),9)
        self.assertTrue(p.childChoice([2,1,4],[3,8,6],[5,7]) in [5,7])
        self.assertEqual(p.childChoice([3,8,6],[2,1,4],[5,7,9]),9)
        self.assertTrue(p.childChoice([],[],range(1,10)) in range(1,10))
        self.assertEqual(p.childChoice([4,6,9,8],[5,1,2,3],[7]),7)
        #more tests will be added which test the same skills in the "child"
        #that is: can the "child" win when possible? can the child block
        #opponent from winning? Can child start game? take last piece?
        #if multiple winning strategies, can child pick just one?

    def test_computerChoice(self):
        self.assertEqual(p.computerChoice([2,1,4],[3,8,6],[5,7,9]),9)
        self.assertTrue(p.computerChoice([2,1,4],[3,8,6],[5,7]) in [5,7])
        self.assertEqual(p.computerChoice([3,8,6],[2,1,4],[5,7,9]),9)
        self.assertTrue(p.computerChoice([],[],range(1,10)) in range(1,10))
        self.assertEqual(p.computerChoice([4,6,9,8],[5,1,2,3],[7]),7)

    #user interface grading guidelines:
    #Were user names collected and used consistently in the game play?
    #Was proper winner (or tie) game summarized at the end?
    #Did the play appropriately prompt alternate users until end of game?
    #Did game terminate properly for both wins and ties?
    #Was user given 4 options (HVH, CVH, HVC, CVC) and were all four
    # games playable?

unittest.main()
    
