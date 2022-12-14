'''
‎Created on September ‎4, ‎2022
Last modified on September 26, 2022

@author: Dylan Stancil
'''

def _verify(parms):
    result = {}
    cubeString = parms.get('cube')
    dirString = parms.get('dir')
    if cubeString is None or len(cubeString) == 0:
        result['status'] = 'error: missing cube string'  
    elif len(cubeString) != 54:
        result['status'] = 'error: the cube does not have 54 characters' 
    elif any(char not in 'wryobg' for char in cubeString):
        result['status'] = 'error: illegal characters in cube string'
    elif countOccurrences(cubeString) == False:
        result['status'] = 'error: cube has wrong amount of occurrences'   
    elif len(set(cubeString[element] for element in range(4, 54, 9))) != 6:
        result['status'] = 'error: the cube does not have unique middle pieces'
    elif any(char not in 'FfRrBbLlUuDd' for char in dirString):
        result['status'] = 'error: the direction has illegal characters'        
    else:
        result['status'] = 'ok'      
    return result
    
def countOccurrences(cubeString):   
    w =  r = y = o = b = g = 0
    for char in cubeString:
        if char == 'w': w += 1
        elif char == 'r': r += 1
        elif char == 'y': y += 1
        elif char == 'o': o += 1
        elif char == 'b': b += 1
        else: g += 1
    if w == r == y == o == b == g == 9:
        return True
    else: return False
    