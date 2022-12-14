'''
‎Created on September ‎4, ‎2022
Last modified on September 26, 2022

@author: Dylan Stancil
'''


import unittest
import rubik.rotate as rotate

class RotateTest(unittest.TestCase):

    '''
    rotate Analysis
        inputs: 
            parms['cube']: length of 54, 9 occurences of each [w, r, y, o, b, g], arrives unvalidated, middle of cube is unique 
            parms['dir']: No length, must be limited to [F, f, R, r, B, b, L, l, U, u, D, d], defaults to F
    
        happy path analysis
        test_100_010 validate cube and direction that should be perfect

        sad path analysis
        test_100_910 validate cube that isnt 54 in length
        test_100_911 validate cube that has an illegal character

            
    '''

    #happy path
    def test_100_010_validCube(self):
        inputDict = {}
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        inputDict['dir'] = 'F'
        expectedResult = {}
        expectedResult['status'] = 'ok' 
        result = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))
        
    def test_100_011_multipleRotations(self):
        inputDict = {}
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        inputDict['dir'] = 'UdRlFbUd'
        expectedResult = {}
        expectedResult['status'] = 'ok' 
        expectedResult['cube'] = 'rrrrwrrrrbbbbrbbbbooooyooooggggoggggwwwwbwwwwyyyygyyyy'
        result = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))    
        self.assertEqual(expectedResult.get('cube'), result.get('cube')) 
        
    #sad path
    def test_100_910_invalidCubeWithWrongAmountOfCharacters(self):
        inputDict = {}
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbgggggggg'
        inputDict['dir'] = 'F'
        expectedResult = {}
        expectedResult['status'] = 'error: the cube does not have 54 characters' 
        result = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))
        
    def test_100_911_invalidCubeWithWrongAmountOfCharacters(self):
        inputDict = {}
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        inputDict['dir'] = 'i'
        expectedResult = {}
        expectedResult['status'] = 'error: the direction has illegal characters' 
        result = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))  
        
    def test_100_912_noDirection(self):
        inputDict = {}
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = {}
        expectedResult['cube'] = 'wwwwwwwwwbrrbrrbrryyyyyyyyyoogoogoogbbbbbbooorrrgggggg'
        expectedResult['status'] = 'ok' 
        result = rotate._rotate(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))   
        self.assertEqual(expectedResult.get('cube'), result.get('cube')) 
    

        
        
        
        
        
        
        
        
        
        