'''
‎Created on September ‎4, ‎2022
Last modified on October 10, 2022

@author: Dylan Stancil
'''
import random
import hashlib
import secrets
# States for transformation to rotate the cube.
NEW_F_STATE       = ['F11','F12','F13','F21','F22','F23','F31','F32','F33','U31','U32','U33','R11','R21','R31','D13','D12','D11','L33','L23','L13']
OLD_F_STATE       = ['F31','F21','F11','F32','F22','F12','F33','F23','F13','L33','L23','L13','U31','U32','U33','R11','R21','R31','D13','D12','D11']
OLD_F_PRIME_STATE = ['F13','F23','F33','F12','F22','F32','F11','F21','F31','R11','R21','R31','D13','D12','D11','L33','L23','L13','U31','U32','U33']
    
NEW_R_STATE       = ['R11','R12','R13','R21','R22','R23','R31','R32','R33','U13','U23','U33','B31','B21','B11','D13','D23','D33','F13','F23','F33']  
OLD_R_STATE       = ['R31','R21','R11','R32','R22','R12','R33','R23','R13','F13','F23','F33','U13','U23','U33','B31','B21','B11','D13','D23','D33']
OLD_R_PRIME_STATE = ['R13','R23','R33','R12','R22','R32','R11','R21','R31','B31','B21','B11','D13','D23','D33','F13','F23','F33','U13','U23','U33']
              
NEW_B_STATE       = ['B11','B12','B13','B21','B22','B23','B31','B32','B33','L31','L21','L11','D33','D32','D31','R13','R23','R33','U11','U12','U13']
OLD_B_STATE       = ['B31','B21','B11','B32','B22','B12','B33','B23','B13','U11','U12','U13','L31','L21','L11','D33','D32','D31','R13','R23','R33']
OLD_B_PRIME_STATE = ['B13','B23','B33','B12','B22','B32','B11','B21','B31','D33','D32','D31','R13','R23','R33','U11','U12','U13','L31','L21','L11'] 

NEW_L_STATE       = ['L11','L12','L13','L21','L22','L23','L31','L32','L33','D11','D21','D31','B33','B23','B13','U11','U21','U31','F11','F21','F31']
OLD_L_STATE       = ['L31','L21','L11','L32','L22','L12','L33','L23','L13','F11','F21','F31','D11','D21','D31','B33','B23','B13','U11','U21','U31']
OLD_L_PRIME_STATE = ['L13','L23','L33','L12','L22','L32','L11','L21','L31','B33','B23','B13','U11','U21','U31','F11','F21','F31','D11','D21','D31']   
    
NEW_U_STATE       = ['U11','U12','U13','U21','U22','U23','U31','U32','U33','L11','L12','L13','B11','B12','B13','R11','R12','R13','F11','F12','F13']
OLD_U_STATE       = ['U31','U21','U11','U32','U22','U12','U33','U23','U13','F11','F12','F13','L11','L12','L13','B11','B12','B13','R11','R12','R13']
OLD_U_PRIME_STATE = ['U13','U23','U33','U12','U22','U32','U11','U21','U31','B11','B12','B13','R11','R12','R13','F11','F12','F13','L11','L12','L13']    
 
NEW_D_STATE       = ['D11','D12','D13','D21','D22','D23','D31','D32','D33','F31','F32','F33','R31','R32','R33','B31','B32','B33','L31','L32','L33']
OLD_D_STATE       = ['D31','D21','D11','D32','D22','D12','D33','D23','D13','L31','L32','L33','F31','F32','F33','R31','R32','R33','B31','B32','B33']
OLD_D_PRIME_STATE = ['D13','D23','D33','D12','D22','D32','D11','D21','D31','R31','R32','R33','B31','B32','B33','L31','L32','L33','F31','F32','F33'] 

# Lists for the petals and their respective spots to be checked.
TOP_PETAL_LIST    = ['R23','D32','L21']
RIGHT_PETAL_LIST  = ['B21','D23','F23']
BOTTOM_PETAL_LIST = ['R21','D12','L23']
LEFT_PETAL_LIST   = ['F21','D21','B23']

# Lists to shift faces of the cube so that petals can be positioned properly.
BACK_SHIFT_LIST  = ['U12','B12','B32']
RIGHT_SHIFT_LIST = ['U23','R12','R32']
FRONT_SHIFT_LIST = ['U32','F12','F32'] 
LEFT_SHIFT_LIST  = ['U21','L12', 'L32']

DOWN_FACE = ['D11', 'D12', 'D13', 'D21', 'D22', 'D23', 'D31', 'D32', 'D33']
UP_FACE = ['U11', 'U12', 'U13', 'U21', 'U22', 'U23', 'U31', 'U32', 'U33']
SIDES = ['Front', 'Right', 'Left', 'Back']
class Cube:
     
    def __init__(self, initCube):
        self.Cube = initCube
        self.initialCube = initCube
        self._fullToken = ''
        self.__token = ''
        self.cubeDict = []
        self._createDict(self.Cube)
        self.frontColor = self.cubeDict['F22']
        self.rightColor = self.cubeDict['R22']
        self.backColor = self.cubeDict['B22']
        self.leftColor = self.cubeDict['L22']
        self.upColor = self.cubeDict['U22']
        self.downColor = self.cubeDict['D22']
        self.solutionList = ''
        self.currentLayerDict = []
        
    
    def toString(self, cubeDict):
        stringOutput = ''
        for sticker in cubeDict:
            stringOutput += cubeDict[sticker]
        return stringOutput     
    
    def _createDict(self, cubeString):
        cubeList = list(cubeString)
        varList = ['F11', 'F12', 'F13', 'F21', 'F22', 'F23', 'F31', 'F32', 'F33',
                   'R11', 'R12', 'R13', 'R21', 'R22', 'R23', 'R31', 'R32', 'R33',
                   'B11', 'B12', 'B13', 'B21', 'B22', 'B23', 'B31', 'B32', 'B33',
                   'L11', 'L12', 'L13', 'L21', 'L22', 'L23', 'L31', 'L32', 'L33',
                   'U11', 'U12', 'U13', 'U21', 'U22', 'U23', 'U31', 'U32', 'U33',
                   'D11', 'D12', 'D13', 'D21', 'D22', 'D23', 'D31', 'D32', 'D33',
                  ]
        self.cubeDict = dict(zip(varList, cubeList))
        
    def _createBottomLayerDict(self):
        self.currentLayerDict = {
            'Front': {
                'checkPosition': ['F33', 'R31', 'D13'],
                'checkForPiece': ['F13', 'R11', 'U33'],
                'colorMatch':[self.frontColor, self.rightColor, self.downColor],
                'algo': 'RUru'},
            'Right': {
                'checkPosition': ['R33', 'B31', 'D33'],
                'checkForPiece': ['R13', 'B11', 'U13'],
                'colorMatch':[self.rightColor, self.backColor, self.downColor],
                'algo': 'BUbu'},
            'Back': {
                'checkPosition': ['B33', 'L31', 'D31'],
                'checkForPiece': ['B13', 'L11', 'U11'],
                'colorMatch':[self.backColor, self.leftColor, self.downColor],
                'algo': 'LUlu'},
            'Left': {
                'checkPosition': ['L33', 'F31', 'D11'],
                'checkForPiece': ['L13', 'F11', 'U31'],
                'colorMatch':[self.leftColor, self.frontColor, self.downColor],
                'algo': 'FUfu'}
            } 
    
    def _createMiddleLayerDict(self):
        self.currentLayerDict = {
            'Front': {
                'checkPosition': ['F23', 'R21'],
                'checkForPiece': ['F12','U32'],
                'colorMatch':[self.frontColor, self.rightColor],
                'algo': 'URurufUF'},
            'Right': {
                'checkPosition': ['R23', 'B21'],
                'checkForPiece': ['R12','U23'],
                'colorMatch':[self.rightColor, self.backColor],
                'algo': 'UBuburUR'},
            'Back': {
                'checkPosition': ['B23', 'L21'],
                'checkForPiece': ['B12', 'U12'],
                'colorMatch':[self.backColor, self.leftColor],
                'algo': 'ULulubUB'},
            'Left': {
                'checkPosition': ['L23', 'F21'],
                'checkForPiece': ['L12', 'U21'],
                'colorMatch':[self.leftColor, self.frontColor],
                'algo': 'UFufulUL'}
            }  
    def _createTopCornersDict(self):
        self.currentLayerDict = {
            'Front': {
                'checkPositionLeft': ['L13', 'F11'],
                'checkPositionRight': ['F13','R11'],
                'colorMatchLeft': [self.leftColor, self.frontColor],
                'colorMatchRight': [self.frontColor, self.rightColor],
                'algo': 'fUBuFUb'},
            'Right': {
                'checkPositionLeft': ['F13', 'R11'],
                'checkPositionRight': ['R13','B11'],
                'colorMatchLeft': [self.frontColor, self.rightColor],
                'colorMatchRight': [self.rightColor, self.backColor],
                'algo': 'rULuRUl'},
            'Back': {
                'checkPositionLeft': ['R13', 'B11'],
                'checkPositionRight': ['B13','L11'],
                'colorMatchLeft': [self.rightColor, self.backColor],
                'colorMatchRight': [self.backColor, self.leftColor],
                'algo': 'bUFuBUf'},
            'Left': {
                'checkPositionLeft': ['B13', 'L11'],
                'checkPositionRight': ['L13','F11'],
                'colorMatchLeft': [self.backColor, self.leftColor],
                'colorMatchRight': [self.leftColor, self.frontColor],
                'algo': 'lURuLUr'}} 
    
    def _createTopLayerDict(self):
        self.currentLayerDict = {
            'Front': {
                'checkPosition': 'F12',
                'colorMatch': self.frontColor,
                'algo': 'BBUlRBBrLUBB'},
            'Right': {
                'checkPosition': 'R12',
                'colorMatch': self.rightColor,
                'algo': 'LLUfBLLbFULL'},
            'Back': {
                'checkPosition': 'B12',
                'colorMatch': self.backColor,
                'algo': 'FFUrLFFlRUFF'},
            'Left': {
                'checkPosition': 'L12',
                'colorMatch': self.leftColor,
                'algo': 'RRUbFRRfBURR'}
            } 
        
    def rotate(self, direction):
        self._createDict(self.Cube)
        newDict = self.cubeDict.copy()
        match direction: 
            case 'f':
                self.Cube = self._rotateDict(newDict, NEW_F_STATE, OLD_F_PRIME_STATE)
            case 'R':
                self.Cube = self._rotateDict(newDict, NEW_R_STATE, OLD_R_STATE)
            case 'r':
                self.Cube = self._rotateDict(newDict, NEW_R_STATE, OLD_R_PRIME_STATE)
            case 'B':
                self.Cube = self._rotateDict(newDict, NEW_B_STATE, OLD_B_STATE)
            case 'b':
                self.Cube = self._rotateDict(newDict, NEW_B_STATE, OLD_B_PRIME_STATE)
            case 'L':
                self.Cube = self._rotateDict(newDict, NEW_L_STATE, OLD_L_STATE)
            case 'l':
                self.Cube = self._rotateDict(newDict, NEW_L_STATE, OLD_L_PRIME_STATE)
            case 'U':
                self.Cube = self._rotateDict(newDict, NEW_U_STATE, OLD_U_STATE)
            case 'u':
                self.Cube = self._rotateDict(newDict, NEW_U_STATE, OLD_U_PRIME_STATE)
            case 'D':
                self.Cube = self._rotateDict(newDict, NEW_D_STATE, OLD_D_STATE)
            case 'd':
                self.Cube = self._rotateDict(newDict, NEW_D_STATE, OLD_D_PRIME_STATE)
            case _:
                self.Cube = self._rotateDict(newDict, NEW_F_STATE, OLD_F_STATE)
            
    def _rotateDict(self, newDict, newState, oldState):
        for i,j in zip(newState, oldState):
            newDict[i] = self.cubeDict[j]
        return self.toString(newDict)
        
    def solve(self):
        if self._isTopLayered() is False:
            if self._isTopCornered() is False:
                if self._isTopSurfaced() is False:
                    if self._isTopCrossed() is False:
                        if self._isMiddleLayered() is False:
                            if self._isBottomLayered() is False:
                                if self._isBottomCrossed() is False:
                                    if self._isDaisy() is False:
                                        self._makeDaisy()
                                    self._makeBottomCross()
                                self._makeBottomLayer()
                            self._makeMiddleLayer()
                        self._makeTopCross()
                    self._makeTopSurface()
                self._makeTopCorners()
            self._makeTopLayer()
        self._optimize()
        self._hashString()
        
    
    def _rotateList(self, rotateString, checkIfAddSolution):
        if checkIfAddSolution:
            self.solutionList += rotateString
        for element in rotateString:
            self.rotate(element)
            
    def _isDaisy(self):
        self._createDict(self.Cube)
        if self.cubeDict['U12'] == self.downColor and self.cubeDict['U21'] == self.downColor and self.cubeDict['U23'] == self.downColor and self.cubeDict['U32'] == self.downColor:
            return True
        else:
            return False
        
    def _isBottomCrossed(self):
        self._createDict(self.Cube)
        if self.cubeDict['D12'] == self.cubeDict['D21'] == self.cubeDict['D23'] == self.cubeDict['D32'] == self.downColor:
            if self.cubeDict['F22'] == self.cubeDict['F32'] == self.frontColor:
                if self.cubeDict['R22'] == self.cubeDict['R32'] == self.rightColor:
                    if self.cubeDict['B22'] == self.cubeDict['B32'] == self.backColor:
                        if self.cubeDict['L22'] == self.cubeDict['L32'] == self.leftColor:
                            return True
        return False
    
    def _isBottomLayered(self):
        self._createDict(self.Cube)
        if set(self.cubeDict[element] for element in DOWN_FACE):
            if self.cubeDict['D11'] == self.cubeDict['D13'] == self.cubeDict['D31'] == self.cubeDict['D33'] == self.downColor:
                if self.cubeDict['F22'] == self.cubeDict['F32'] == self.cubeDict['F31'] == self.cubeDict['F33'] == self.frontColor:
                    if self.cubeDict['R22'] == self.cubeDict['R32'] == self.cubeDict['R31'] == self.cubeDict['R33'] == self.rightColor:
                        if self.cubeDict['B22'] == self.cubeDict['B32'] == self.cubeDict['B31'] == self.cubeDict['B33'] == self.backColor:
                            if self.cubeDict['L22'] == self.cubeDict['L32'] == self.cubeDict['L31'] == self.cubeDict['L33'] == self.leftColor:
                                return True
        return False
    
    def _isMiddleLayered(self):
        if self._isBottomLayered():
            if self.cubeDict['F21'] == self.cubeDict['F23'] == self.frontColor:
                if self.cubeDict['R21'] == self.cubeDict['R23'] == self.rightColor:
                    if self.cubeDict['B21'] == self.cubeDict['B23'] == self.backColor:
                        if self.cubeDict['L21'] == self.cubeDict['L23'] == self.leftColor:
                            return True
        return False   
    
    def _isTopCrossed(self):
        if self._isMiddleLayered():
            if self.cubeDict['U12'] == self.cubeDict['U21'] == self.cubeDict['U23'] == self.cubeDict['U32'] == self.upColor:
                return True
        return False
    
    def _isTopSurfaced(self):
        if self._isTopCrossed():
            if all(self.cubeDict[element] == self.upColor for element in UP_FACE):
                return True
        return False
    
    def _isTopLayered(self):
        if self._isTopCornered():
            if self.cubeDict['F12'] == self.frontColor and self.cubeDict['R12'] == self.rightColor and self.cubeDict['B12'] == self.backColor and self.cubeDict['L12'] == self.leftColor:
                return True
        return False
    
    def _isTopCornered(self):
        if self._isTopSurfaced():
            if self.cubeDict['F11'] == self.frontColor and self.cubeDict['F13'] == self.frontColor:
                if self.cubeDict['R11'] == self.rightColor and self.cubeDict['R13'] == self.rightColor:
                    if self.cubeDict['B11'] == self.backColor and self.cubeDict['B13'] == self.backColor:
                        if self.cubeDict['L11'] == self.leftColor and self.cubeDict['L13'] == self.leftColor:
                            return True
        return False
    
    def _makeDaisy(self):
        while self._isDaisy() is False:
            self._movePetal(TOP_PETAL_LIST, 'U12', 'B')
            self._movePetal(RIGHT_PETAL_LIST, 'U23', 'R')
            self._movePetal(BOTTOM_PETAL_LIST, 'U32', 'F')
            self._movePetal(LEFT_PETAL_LIST, 'U21', 'L')
            if self._isDaisy() is False:
                self._shiftPetal(BACK_SHIFT_LIST, 'B')
                self._shiftPetal(LEFT_SHIFT_LIST, 'L')
                self._shiftPetal(FRONT_SHIFT_LIST, 'F')
                self._shiftPetal(RIGHT_SHIFT_LIST, 'R')
                
    def _movePetal(self, petalList, petal, direction):
        self._createDict(self.Cube)
        while any(self.cubeDict[element] == self.downColor for element in petalList):
            self._createDict(self.Cube)
            if self.cubeDict[petal] == self.downColor:
                self._rotateList('U', True)
            else:
                self._rotateList(direction, True)
                
    def _shiftPetal(self, shiftList, direction):
        self._createDict(self.Cube)
        while self.cubeDict[shiftList[0]] is self.downColor:
            self._createDict(self.Cube)
            if self.cubeDict[shiftList[1]] == self.downColor or self.cubeDict[shiftList[2]] == self.downColor:
                self._rotateList('U', True)
            else:
                break
        self._rotateList(direction, True)
        
    def _makeBottomCross(self):
        while self._isBottomCrossed() is False:
            self._createDict(self.Cube)
            if self.cubeDict['B12'] == self.backColor and self.cubeDict['B22'] == self.backColor and self.cubeDict['U12'] == self.downColor:
                self._rotateList('BB', True)
            elif self.cubeDict['L12'] == self.leftColor and self.cubeDict['L22'] == self.leftColor and self.cubeDict['U21'] == self.downColor:
                self._rotateList('LL', True)
            elif self.cubeDict['F12'] == self.frontColor and self.cubeDict['F22'] == self.frontColor and self.cubeDict['U32'] == self.downColor:
                self._rotateList('FF', True)
            elif self.cubeDict['R12'] == self.rightColor and self.cubeDict['R22'] == self.rightColor and self.cubeDict['U23'] == self.downColor:
                self._rotateList('RR', True)
            else: 
                self._rotateList('U', True)

    def _makeBottomLayer(self):
        self._createDict(self.Cube)
        self._createBottomLayerDict()
        for side in self.currentLayerDict:
            self._movePiece(side, 'bottom')
          
    def _makeMiddleLayer(self):
        self._createDict(self.Cube)
        self._createMiddleLayerDict()
        for sides in self.currentLayerDict:
            self._movePiece(sides, 'middle')
                
    def _movePiece(self, currentSide, currentDict):
        self._createDict(self.Cube)
        for sides in self.currentLayerDict:
            while set(self.cubeDict[element] for element in self.currentLayerDict[sides]['checkPosition']) == set(self.currentLayerDict[currentSide]['colorMatch']):
                self._rotateList(self.currentLayerDict[sides]['algo'], True)
                self._createDict(self.Cube)
                
        while set(self.cubeDict[element] for element in self.currentLayerDict[currentSide]['checkForPiece']) != set(self.currentLayerDict[currentSide]['colorMatch']):
            self._rotateList('U', True)
            self._createDict(self.Cube)
            
        while self._isPieceMatching(self.currentLayerDict[currentSide]['checkPosition'], self.currentLayerDict[currentSide]['colorMatch'] ) is False:
            self._rotateList(self.currentLayerDict[currentSide]['algo'], True)
            self._createDict(self.Cube)
            if (self._isPieceMatching(self.currentLayerDict[currentSide]['checkPosition'], self.currentLayerDict[currentSide]['colorMatch'] ) is False 
                    and currentDict == 'middle'):
                self._rotateList(self.currentLayerDict[currentSide]['algo'], True)
                self._rotateList('UU', True)
                self._rotateList(self.currentLayerDict[currentSide]['algo'], True)
                self._createDict(self.Cube)
                
    def _isPieceMatching(self, pieceToCheck, colorMatch):
        leftStickerCheck, leftColorToMatch = pieceToCheck[0], colorMatch[0]
        rightStickerCheck, rightColorToMatch = pieceToCheck[1], colorMatch[1]
        if len(colorMatch) != 2:
            downStickerCheck, downColorToMatch = pieceToCheck[2], colorMatch[2]
        if self.cubeDict[leftStickerCheck] == leftColorToMatch:
            if self.cubeDict[rightStickerCheck] == rightColorToMatch:
                if len(colorMatch) == 2:
                    return True
                if self.cubeDict[downStickerCheck] == downColorToMatch:
                    return True
        return False
    
    def _makeTopCross(self):
        while not self._isTopCrossed():
            self._createDict(self.Cube)
            if self.cubeDict['U21'] == self.cubeDict['U23'] == self.upColor:
                self._rotateList('FRUruf', True)
            elif self.cubeDict['U21'] == self.cubeDict['U12'] == self.upColor:
                self._rotateList('FURurf', True)
            elif self.upColor not in [self.cubeDict['U12'], self.cubeDict['U21'], self.cubeDict['U23'], self.cubeDict['U32']]:
                self._rotateList('FRUruf', True)
                self._createDict(self.Cube)
            else: 
                self._rotateList('U', True)

    def _makeTopSurface(self):
        while not self._isTopSurfaced():
            topCorners = [self.cubeDict['U11'], self.cubeDict['U13'], self.cubeDict['U31'], self.cubeDict['U33']]
            if topCorners.count(self.upColor) == 0:
                while self.cubeDict['L13'] != self.upColor:
                    self._rotateList('U', True)
                self._rotateList('RUrURUUr', True)
            elif topCorners.count(self.upColor) == 2:
                while self.cubeDict['U31'] == self.upColor:
                    self._rotateList('U', True)
                self._rotateList('RUrURUUr', True)
            elif topCorners.count(self.upColor) == 1:
                while self.cubeDict['U31'] != self.upColor:
                    self._rotateList('U', True)
                    self._createDict(self.Cube)
                self._rotateList('RUrURUUr', True)  
                     
    def _makeTopCorners(self):
        self._createTopCornersDict()
        while not self._countMatchingCorners():
            self._createDict(self.Cube)
            doubleFound, side = self._findMatchingCorners()
            if doubleFound == True:
                self._rotateList(self.currentLayerDict[side]['algo'], True)
                self._makeTopSurface()
            else:
                self._rotateList(self.currentLayerDict['Front']['algo'], True)
                self._makeTopSurface()
                self._createDict(self.Cube)
        while not self._isTopCornered():
            self._rotateList('U', True)   
               
    def _findMatchingCorners(self):
        for side in self.currentLayerDict:
            for _ in range(4):
                if (self._isPieceMatching(self.currentLayerDict[side]['checkPositionLeft'], self.currentLayerDict[side]['colorMatchLeft']) and 
                        self._isPieceMatching(self.currentLayerDict[side]['checkPositionRight'], self.currentLayerDict[side]['colorMatchRight'])):
                    return True, side
                else: 
                    self._rotateList('U', True)
                    self._createDict(self.Cube)
        return False, side
    
    def _countMatchingCorners(self):
        self._createTopCornersDict()
        self._createDict(self.Cube)
        count = 0
        for side in self.currentLayerDict:
            if self.cubeDict[self.currentLayerDict[side]['checkPositionLeft'][1]] == self.cubeDict[self.currentLayerDict[side]['checkPositionRight'][0]]:
                count += 1
        if count == 4:
            return True
        else: return False
        
    def _makeTopLayer(self):
        self._createTopLayerDict()
        self._createDict(self.Cube)
        while not self._isTopLayered():
            side = self._findCompletedSide()
            if side != None:
                self._rotateList(self.currentLayerDict[side]['algo'], True)
            elif side is None:
                self._rotateList('FFUrLFFlRUFF', True)
                
    def _findCompletedSide(self):
        self._createTopLayerDict()
        self._createDict(self.Cube)
        for side in self.currentLayerDict:
            if self.cubeDict[self.currentLayerDict[side]['checkPosition']] == self.currentLayerDict[side]['colorMatch']:
                return side                    
            
    def _scramble(self):
        rotations = 100
        direction = ['F', 'R', 'B', 'L', 'U', 'D', 'f', 'r', 'b', 'l', 'u', 'd']
        scrambleString = ''
        for _ in range(rotations):
            scrambleString += random.choice(direction)
        self._rotateList(scrambleString, False)
    
    def _hashString(self):
        itemToTokenize = self.initialCube + self.solutionList
        sha256Hash = hashlib.sha256()
        sha256Hash.update(itemToTokenize.encode())
        self._fullToken = sha256Hash.hexdigest()
        randPostion = secrets.randbelow(len(self._fullToken) - 8)
        self.__token = self._fullToken[randPostion:randPostion+8]
    
    def getToken(self):
        return self.__token
    
    def _optimize(self):
        replacementDict = {'FUfuFUfuFUfuFUfuFUfu': 'UFuf', 'RUruRUruRUruRUruRUru': 'URur', 'BUbuBUbuBUbuBUbuBUbu': 'UBub', 'LUluLUluLUluLUluLUlu': 'ULul',
                          'FFF': 'f', 'FFF': 'f', 'RRR':'r','BBB':'b','LLL':'l','UUU':'u','DDD':'d',
                          'fff':'F','rrr':'R','bbb':'B','lll':'L','uuu':'U','ddd':'D',
                          'Ff': '', 'fF': '', 'Rr': '', 'rR': '', 'Bb': '', 'bB': '',
                          'Ll': '', 'lL': '', 'Uu': '', 'uU': '','Dd': '', 'dD': ''
                          }
        changed = True
        while changed is True:
            copySolutionList = self.solutionList
            for key in replacementDict:
                self.solutionList = self.solutionList.replace(key, replacementDict[key])  
            if copySolutionList is self.solutionList:
                changed = False  
        

                
    
        
                    
        

    