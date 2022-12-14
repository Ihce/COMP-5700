'''
‎Created on September ‎4, ‎2022
Last modified on October 10, 2022

@author: Dylan Stancil
'''

import rubik.verify as verify
import rubik.cube as cube

def _solve(parms):
    result = {}
    if parms.get('dir') == None or parms.get('dir') == '':
        parms['dir'] = 'F'
    parms_validate = verify._verify(parms)
    if parms_validate['status'] != 'ok':
        return parms_validate 
    myCube = cube.Cube(parms.get('cube'))
    myCube.solve()
    result['rotations'] = myCube.solutionList
    result['status'] = 'ok' 
    result['token'] = myCube.getToken()                    
    return result