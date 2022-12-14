'''
‎Created on September ‎4, ‎2022
Last modified on September 26, 2022

@author: Dylan Stancil
'''


import rubik.verify as verify
import rubik.cube as cube

def _rotate(parms):
    result = {}
    if parms.get('dir') == None or parms.get('dir') == '':
        parms['dir'] = 'F'
    parms_validate = verify._verify(parms)
    if parms_validate['status'] != 'ok':
        return parms_validate 
    myCube = cube.Cube(parms.get('cube'))
    directionList = list(parms.get('dir'))
    for element in directionList:
        myCube.rotate(element)
    result['cube'] = myCube.Cube
    result['status'] = 'ok'                  
    return result