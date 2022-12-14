'''
‎Created on September ‎4, ‎2022
Last modified on October 10, 2022

@author: Dylan Stancil
'''

import rubik.cube as cube
import rubik.verify as verify
import unittest

class CubeTest(unittest.TestCase):
    
    # Happy Path
    def test_100_001_initializeCube(self):
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        myCube = cube.Cube(incomingCube)
        self.assertIsInstance(myCube, cube.Cube)

    def test_100_010_F(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwwwwwwwwbrrbrrbrryyyyyyyyyoogoogoogbbbbbbooorrrgggggg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('F')
        self.assertEqual(expectedResult, myCube.Cube)
        
    def test_100_011_f(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwwwwwwwwgrrgrrgrryyyyyyyyyoobooboobbbbbbbrrrooogggggg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('f')
        self.assertEqual(expectedResult, myCube.Cube)        
        
    def test_100_012_R(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwgwwgwwgrrrrrrrrrbyybyybyyooooooooobbwbbwbbwggyggyggy'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('R')
        self.assertEqual(expectedResult, myCube.Cube)
        
    def test_100_013_r(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwbwwbwwbrrrrrrrrrgyygyygyyooooooooobbybbybbyggwggwggw'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('r')
        self.assertEqual(expectedResult, myCube.Cube)
        
    def test_100_014_B(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwwwwwwwwrrgrrgrrgyyyyyyyyyboobooboorrrbbbbbbggggggooo'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('B')
        self.assertEqual(expectedResult, myCube.Cube)   
        
    def test_100_015_b(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwwwwwwwwrrbrrbrrbyyyyyyyyygoogoogooooobbbbbbggggggrrr'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('b')
        self.assertEqual(expectedResult, myCube.Cube)    
        
    def test_100_016_L(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'bwwbwwbwwrrrrrrrrryygyygyygoooooooooybbybbybbwggwggwgg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('L')
        self.assertEqual(expectedResult, myCube.Cube) 
        
    def test_100_017_l(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'gwwgwwgwwrrrrrrrrryybyybyybooooooooowbbwbbwbbyggyggygg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('l')
        self.assertEqual(expectedResult, myCube.Cube)
        
    def test_100_018_U(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'rrrwwwwwwyyyrrrrrroooyyyyyywwwoooooobbbbbbbbbggggggggg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('U')
        self.assertEqual(expectedResult, myCube.Cube)  

    def test_100_019_u(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'ooowwwwwwwwwrrrrrrrrryyyyyyyyyoooooobbbbbbbbbggggggggg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('u')
        self.assertEqual(expectedResult, myCube.Cube)
        
    def test_100_019_D(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwwwwwooorrrrrrwwwyyyyyyrrrooooooyyybbbbbbbbbggggggggg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('D')
        self.assertEqual(expectedResult, myCube.Cube)
        
    def test_100_019_d(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwwwwwrrrrrrrrryyyyyyyyyooooooooowwwbbbbbbbbbggggggggg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('d')
        self.assertEqual(expectedResult, myCube.Cube)
        
    def test_100_019_(self):
        incomingCube =   'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'wwwwwwwwwbrrbrrbrryyyyyyyyyoogoogoogbbbbbbooorrrgggggg'
        myCube = cube.Cube(incomingCube)
        myCube.rotate('')
        self.assertEqual(expectedResult, myCube.Cube)
        
        
    # Test for iteration 2
    # Happy Path Tests
    def test_200_010_checkDaisyIsTrue(self):
        incomingCube = 'wrbbggobrygyoooyybbbrybrwggborgrroyywwrwywgwogogrwbwyo'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isDaisy())
        
    def test_200_011_checkBottomCrossIsTrue(self):
        incomingCube = 'bgrrbowbgbowwogoorbwyrgobgggwobrbrrgorobwgywwyyyyyyryw'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isBottomCrossed())   
        
    def test_200_012_solveForDaisy(self):
        incomingCube= 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        myCube._makeDaisy()
        self.assertEqual(expectedResult, myCube._isDaisy())
        
    def test_200_013_daisySolutionLength(self):
        incomingCube= 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = 1
        myCube = cube.Cube(incomingCube)
        myCube._makeDaisy()
        self.assertGreaterEqual(len(myCube.solutionList), expectedResult)  
        
    def test_200_014_bottomCrossFromDaisy(self):
        incomingCube = 'wrbbggobrygyoooyybbbrybrwggborgrroyywwrwywgwogogrwbwyo'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        myCube._makeBottomCross()
        self.assertEqual(expectedResult, myCube._isBottomCrossed())
        
    def test_200_015_bottomCrossFromDaisySolutionLength(self):
        incomingCube= 'wrbbggobrygyoooyybbbrybrwggborgrroyywwrwywgwogogrwbwyo'
        expectedResult = 1
        myCube = cube.Cube(incomingCube)
        myCube._makeBottomCross()
        self.assertGreaterEqual(len(myCube.solutionList), expectedResult)
        
    # def test_200_016_bottomCrossFromScrambled(self):
    #     incomingCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
    #     expectedResult = True
    #     myCube = cube.Cube(incomingCube)
    #     myCube.solve()
    #     self.assertEqual(expectedResult, myCube._isBottomCrossed()) 
        
    def test_200_017_createDictionary(self):
        incomingCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        expectedResult = {'F11': 'o', 'F12': 'o', 'F13': 'o', 'F21': 'w', 'F22': 'b', 'F23': 'r', 'F31': 'r', 'F32': 'g', 'F33': 'y',
                          'R11': 'w', 'R12': 'o', 'R13': 'b', 'R21': 'w', 'R22': 'r', 'R23': 'g', 'R31': 'g', 'R32': 'y', 'R33': 'g',
                          'B11': 'w', 'B12': 'g', 'B13': 'b', 'B21': 'w', 'B22': 'g', 'B23': 'r', 'B31': 'y', 'B32': 'y', 'B33': 'w',
                          'L11': 'r', 'L12': 'w', 'L13': 'y', 'L21': 'b', 'L22': 'o', 'L23': 'b', 'L31': 'g', 'L32': 'y', 'L33': 'w',
                          'U11': 'y', 'U12': 'r', 'U13': 'r', 'U21': 'o', 'U22': 'y', 'U23': 'b', 'U31': 'b', 'U32': 'y', 'U33': 'b',
                          'D11': 'g', 'D12': 'o', 'D13': 'r', 'D21': 'b', 'D22': 'w', 'D23': 'g', 'D31': 'o', 'D32': 'r', 'D33': 'o'}
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube.cubeDict)
        
    def test_200_018_solvedCube(self):
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 0
        myCube = cube.Cube(incomingCube)
        myCube.solve()
        self.assertEqual(expectedResult, len(myCube.solutionList))
             
    # Sad Path Tests   
    def test_200_910_checkDaisyIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isDaisy())
        
    def test_200_911_checkBottomCrossIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isBottomCrossed())
        
        
    # Iteration 3
    
    # Happy Path
    def test_300_010_checkBottomLayerIsTrue(self):
        incomingCube = 'rywrwbwwwbowyrbrrrroywywyyyobboowooobbbrbyyroggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isBottomLayered())
        
    def test_300_011_scrambleCube(self):
        verifyDict = {}
        incomingCube= 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = {'status': 'ok'}
        myCube = cube.Cube(incomingCube)
        myCube._scramble()
        verifyDict['cube'] = myCube.Cube
        verifyDict['dir'] = 'F'
        validateCube = verify._verify(verifyDict)
        self.assertEqual(expectedResult, validateCube)
        
    def test_300_012_solveFromBottomCross(self):
        incomingCube = 'robbwowworrgbrwbrowwooyrgygbbgyoyroryborbwwyybgwgggygy'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        myCube._makeBottomLayer()
        self.assertEqual(expectedResult, myCube._isBottomLayered())
        
    def test_300_013_solve100ScrambledCubes(self):
        passCount = 0
        expectedResult = 100
        myCubes = {}
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        for cubeNumber in range(100):
            myCubes[cubeNumber] = cube.Cube(incomingCube)
            myCubes[cubeNumber]._scramble()
            myCubes[cubeNumber].solve()
            if myCubes[cubeNumber]._isBottomLayered():
                passCount += 1
        self.assertEqual(expectedResult, passCount)
        
    def test_300_014_solveSolvedCube(self):
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        myCube.solve()
        self.assertEqual(expectedResult, myCube._isBottomLayered())
            
    def test_300_015_optimizeSolution(self):
        incomingSolutionList = 'FFFRRRBBBLLLUUUDDDfffrrrbbbllluuuddd'
        expectedResult = 'frbludFRBLUD'
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        myCube = cube.Cube(incomingCube)
        myCube.solutionList = incomingSolutionList
        myCube._optimize()
        self.assertEqual(expectedResult, myCube.solutionList)
         
    # Sad Path
    def test_300_910_checkBottomLayerIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isBottomLayered()) 
        
    # Iteration 4
    
    # Happy Path
    def test_400_010_checkMiddleLayerIsTrue(self):
        incomingCube = 'wyyoooooorywrrrrrryyrbbbbbbyyywwwwwwobbwyroobggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isMiddleLayered())
        
    def test_300_012_solveFromBottomLayer(self):
        incomingCube = 'yoywooooobywyrbrrroyrrbybbbbwrbwbwwwyryoyworwggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        myCube._makeMiddleLayer()
        self.assertEqual(expectedResult, myCube._isMiddleLayered())
        
    # def test_300_013_solveXScrambledCubes(self):
    #     incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
    #     mySolveCubes = {}
    #     myTestCubes = {}
    #     cubesPassed = 0
    #     expected = 50
    #     for cubeIndex in range(expected):
    #         mySolveCubes[cubeIndex] = cube.Cube(incomingCube)
    #         mySolveCubes[cubeIndex]._scramble()
    #         myTestCubes[cubeIndex] = cube.Cube(mySolveCubes[cubeIndex].Cube)
    #         mySolveCubes[cubeIndex].solve()
    #         rotationList = mySolveCubes[cubeIndex].solutionList
    #         myTestCubes[cubeIndex]._rotateList(rotationList, False)
    #         mLBool = bool(myTestCubes[cubeIndex]._isMiddleLayered())
    #         lenOfSolution = len(mySolveCubes[cubeIndex].solutionList)
    #         if mLBool and lenOfSolution > 0:
    #             cubesPassed += 1
    #     self.assertEqual(expected, cubesPassed)
        
    # Sad Path    
    def test_400_910_checkMiddleLayerIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isMiddleLayered())    
        
    
    # Iteration 5
    def test_500_010_checkTopCrossIsTrue(self):
        incomingCube = 'wyrwwwwwwyryrrrrrrowwyyyyyybobooooooobbbbbrbbggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopCrossed())
        
    def test_500_011_checkTopSurfaceIsTrue(self):
        incomingCube = 'roowwwwwwwyyrrrrrrorryyyyyyywwoooooobbbbbbbbbggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopSurfaced())
        
    # def test_500_012_solveXScrambledCubes(self):
    #     incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
    #     mySolveCubes = {}
    #     myTestCubes = {}
    #     cubesPassed = 0
    #     expected = 50
    #     for cubeIndex in range(expected):
    #         mySolveCubes[cubeIndex] = cube.Cube(incomingCube)
    #         mySolveCubes[cubeIndex]._scramble()
    #         myTestCubes[cubeIndex] = cube.Cube(mySolveCubes[cubeIndex].Cube)
    #         mySolveCubes[cubeIndex].solve()
    #         rotationList = mySolveCubes[cubeIndex].solutionList
    #         myTestCubes[cubeIndex]._rotateList(rotationList, False)
    #         mLBool = bool(myTestCubes[cubeIndex]._isTopSurfaced())
    #         lenOfSolution = len(mySolveCubes[cubeIndex].solutionList)
    #         if mLBool and lenOfSolution > 0:
    #             cubesPassed += 1
    #     self.assertEqual(expected, cubesPassed)
    
    def test_500_013_testCreateHashLength(self):
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 8
        myCube = cube.Cube(incomingCube)
        myCube._scramble()
        myCube.solve()
        result = len(myCube.getToken())
        self.assertEqual(expectedResult, result)
        
    def test_500_013_testRedundOptimize(self):
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = 'UFuf'
        myCube = cube.Cube(incomingCube)
        myCube.solutionList = "FUfuFUfuFUfuFUfuFUfu"
        myCube._optimize()
        self.assertEqual(expectedResult, myCube.solutionList)
    # Sad Path    
    def test_500_910_checkTopCrossIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopCrossed())  
    
    def test_500_911_checkTopSurfaceIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopSurfaced())  
    
    
    
    # Iteration 6
    def test_600_010_checkTopCorneredIsTrue(self):
        incomingCube = 'wrwwwwwwwryrrrrrrrywyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopCornered())
        
    def test_600_011_checkTopLayerIsTrue(self):
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = True
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopLayered())
    #
    def test_600_012_solveXScrambledCubes(self):
        incomingCube = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        mySolveCubes = {}
        myTestCubes = {}
        cubesPassed = 0
        expected = 50
        for cubeIndex in range(expected):
            mySolveCubes[cubeIndex] = cube.Cube(incomingCube)
            mySolveCubes[cubeIndex]._scramble()
            myTestCubes[cubeIndex] = cube.Cube(mySolveCubes[cubeIndex].Cube)
            mySolveCubes[cubeIndex].solve()
            rotationList = mySolveCubes[cubeIndex].solutionList
            myTestCubes[cubeIndex]._rotateList(rotationList, False)
            mLBool = bool(myTestCubes[cubeIndex]._isTopLayered())
            lenOfSolution = len(mySolveCubes[cubeIndex].solutionList)
            if mLBool and lenOfSolution > 0:
                cubesPassed += 1
        self.assertEqual(expected, cubesPassed)
                
    #Sad Path    
    def test_600_910_checkTopCorneredIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopCornered())  
    
    def test_600_911_checkTopLayerIsFalse(self):
        incomingCube = 'wbowgybwwwgogoorygywbbbrrbwroggrrboyyggyyoorbobgwwrryy'
        expectedResult = False
        myCube = cube.Cube(incomingCube)
        self.assertEqual(expectedResult, myCube._isTopLayered())  
    
    
    
    
    
    
    
    
    
    
    