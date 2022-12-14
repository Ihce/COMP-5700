'''
Created on September 25, 2022
Last modified on October 10, 2022

@author: Dylan Stancil
'''
import unittest
import rubik.solve as solve
import rubik.cube as cube

class SolveTest(unittest.TestCase):
    
    #Happy Path
    def test_100_010_validCube(self):
        inputDict = {}
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = {}
        expectedResult['status'] = 'ok' 
        result = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))
   
    # Iteration 2
    # def test_100_011_solveSolvedCube(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
    #     expectedResult = {}
    #     expectedResult['rotations'] = ''
    #     expectedResult['status'] = 'ok' 
    #     result = solve._solve(inputDict)
    #     self.assertEqual(expectedResult, result)
        
    # def test_100_011_solveScrambledCube(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
    #     expectedResult = True
    #     result = solve._solve(inputDict)
    #     rotationList = result.get('rotations')
    #     testCube = cube.Cube(inputDict['cube'])
    #     testCube._rotateList(rotationList)
    #     self.assertEqual(expectedResult, testCube._isBottomCrossed())
    
    # The rest of the design requirement tests for a non valid cube is covered by verifyTest
    def test_300_910_invalidCubeWithWrongAmountOfCharacters(self):
        inputDict = {}
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbgggggggg'
        expectedResult = {}
        expectedResult['status'] = 'error: the cube does not have 54 characters' 
        result = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))

    # Iteration 3
    # Happy 
    # def test_100_010_solveScrambledCube(self):
    #     inputDict = {}
    #     # expectedResult = {'rotations': 'rUBLuFrRuUluUBBLLFFRRuRUruRUruRUruUBUbuBUbuBUbuBUbuBUbuLUluLUluLUluFUfuFUfuFUfuFUfuFUfuFUfu', 'status': 'ok'}
    #     expectedResult = True
    #     actualResults = False
    #     inputDict['cube'] = 'ryogygygwyoyorwbwbryoowrwborrwwgbwrbybbybrooggygboggwr'
    #     result = solve._solve(inputDict)
    #     testCube = cube.Cube(inputDict['cube'])
    #     testCube._rotateList(result['rotations'])
    #     if testCube._isBottomLayered() and len(result['rotations']) > 0 and result['status'] == 'ok':
    #         actualResults = True
    #     self.assertEqual(expectedResult, actualResults)
        
    # def test_100_010_solveSolvedCube(self):
    #     inputDict = {}
    #     inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
    #     expectedResult = {'rotations': '', 'status': 'ok'}
    #     result = solve._solve(inputDict)
    #     self.assertEqual(expectedResult, result)
        
    # Iteration 4
    # def test_100_010_solveScrambledCube(self):
    #     inputDict = {}
    #     expectedResult = True
    #     actualResults = False
    #     inputDict['cube'] = 'ryogygygwyoyorwbwbryoowrwborrwwgbwrbybbybrooggygboggwr'
    #     result = solve._solve(inputDict)
    #     testCube = cube.Cube(inputDict['cube'])
    #     testCube._rotateList(result['rotations'], False)
    #     if testCube._isMiddleLayered() and len(result['rotations']) > 0 and result['status'] == 'ok':
    #         actualResults = True
    #     self.assertEqual(expectedResult, actualResults)
        
    # Iteration 5
    # def test_100_010_solveSolvedCube(self):
    #     inputDict = {}
    #     expectedResult = True
    #     actualResults = False
    #     inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
    #     result = solve._solve(inputDict)
    #     testCube = cube.Cube(inputDict['cube'])
    #     testCube._rotateList(result['rotations'], False)
    #     if testCube._isTopSurfaced() and len(result['rotations']) == 0 and result['status'] == 'ok' and len(result['token']) == 8:
    #         actualResults = True
    #     self.assertEqual(expectedResult, actualResults)
    #
    # def test_100_010_solveScrambledCube(self):
    #     inputDict = {}
    #     expectedResult = True
    #     actualResults = False
    #     inputDict['cube'] = 'ryogygygwyoyorwbwbryoowrwborrwwgbwrbybbybrooggygboggwr'
    #     result = solve._solve(inputDict)
    #     testCube = cube.Cube(inputDict['cube'])
    #     testCube._rotateList(result['rotations'], False)
    #
    #     if testCube._isTopSurfaced() and len(result['rotations']) > 0 and result['status'] == 'ok' and len(result['token']) == 8:
    #         actualResults = True
    #     self.assertEqual(expectedResult, actualResults)
        
    # Iteration 6
    def test_600_010_solveSolvedCube(self):
        inputDict = {}
        expectedResult = True
        actualResults = False
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        result = solve._solve(inputDict)
        testCube = cube.Cube(inputDict['cube'])
        testCube._rotateList(result['rotations'], False)
        if testCube._isTopLayered() and len(result['rotations']) == 0 and result['status'] == 'ok' and len(result['token']) == 8:
            actualResults = True
        self.assertEqual(expectedResult, actualResults)
        
    def test_600_011_solveScrambledCube(self):
        inputDict = {}
        expectedResult = True
        actualResults = False
        inputDict['cube'] = 'ryogygygwyoyorwbwbryoowrwborrwwgbwrbybbybrooggygboggwr'
        result = solve._solve(inputDict)
        testCube = cube.Cube(inputDict['cube'])
        testCube._rotateList(result['rotations'], False)
        if testCube._isTopLayered() and len(result['rotations']) > 0 and result['status'] == 'ok' and len(result['token']) == 8:
            actualResults = True
        self.assertEqual(expectedResult, actualResults)
    
    def test_600_012_checkSubtokenIsInFullToken(self):
        inputDict = {}
        expectedResult = True
        actualResults = False
        inputDict['cube'] = 'ryogygygwyoyorwbwbryoowrwborrwwgbwrbybbybrooggygboggwr'
        result = solve._solve(inputDict)
        testCube = cube.Cube(inputDict['cube'])
        testCube._rotateList(result['rotations'], True)
        testCube._hashString()
        if result['token'] in testCube._fullToken:
            actualResults = True
        self.assertEqual(expectedResult, actualResults)
    
    
        
        
        
        
