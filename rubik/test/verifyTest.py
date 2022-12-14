'''
‎Created on September ‎4, ‎2022
Last modified on September 26, 2022

@author: Dylan Stancil
'''

import rubik.verify as verify
import unittest


class VerifyTest(unittest.TestCase):
    # Happy Path
    def test_100_010_validCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        inputDict['dir'] = 'F'
        expectedResult = {}
        expectedResult['status'] = 'ok' 
        result = verify._verify(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))
        
    def test_100_011_trueOccurrences(self):
        cubeString =  'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = True
        result = verify.countOccurrences(cubeString)
        self.assertEqual(expectedResult, result)   
        
    def test_100_910_invalidCubeLengthNot54(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbgggggggg'
        inputDict['dir'] = 'F'
        expectedResult = {}
        expectedResult['status'] = 'error: the cube does not have 54 characters' 
        result = verify._verify(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))
                
    def test_100_911_invalidCubeNoCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        expectedResult = {}
        expectedResult['status'] = 'error: missing cube string' 
        result = verify._verify(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))  
        
    def test_100_912_invalidCubeWrongChar(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        inputDict['cube'] = '5wwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbgggggggg1'
        expectedResult = {}
        expectedResult['status'] = 'error: illegal characters in cube string' 
        result = verify._verify(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))        
    
    def test_100_913_invalidCubeWrongOccurrences(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggb'
        expectedResult = {}
        expectedResult['status'] = 'error: cube has wrong amount of occurrences' 
        result = verify._verify(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))
    
    def test_100_914_invalidCubeWrongMiddle(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        inputDict['cube'] = 'wwwwwwwwrrrrrwrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = {}
        expectedResult['status'] = 'error: the cube does not have unique middle pieces' 
        result = verify._verify(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))      
        
    def test_100_914_invalidDirWrongChar(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'i'
        inputDict['cube'] = 'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggg'
        expectedResult = {}
        expectedResult['status'] = 'error: the direction has illegal characters' 
        result = verify._verify(inputDict)
        self.assertEqual(expectedResult.get('status'), result.get('status'))  
                
    def test_100_915_falseOccurrences(self):
        cubeString =  'wwwwwwwwwrrrrrrrrryyyyyyyyyooooooooobbbbbbbbbggggggggb'
        expectedResult = False
        result = verify.countOccurrences(cubeString)
        self.assertEqual(expectedResult, result)  
        
        
        
        
                     
        