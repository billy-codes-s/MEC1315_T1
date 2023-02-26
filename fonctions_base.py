import numpy as np
import struct
from MEC1315_STL import *

bob = LireSTL('cuphead.stl')


def translation(objet, coor):
    f = np.array(objet[0])
    v = np.array(objet[1]) + coor
    n = np.array(objet[2])
    
    return (f,v,n)

def fusion(*objets):
    f_f = objets[0][0]
    v_f = objets[0][1]
    n_f = objets[0][2]
    len_prev = len(v_f)
    
    for i in range(1, len(objets)):
        f_f = np.vstack((f_f, objets[i][0] + len_prev))
        v_f = np.vstack((v_f, objets[i][1]))
        n_f = np.vstack((n_f, objets[i][2]))
        len_prev += len(objets[i][1])
    return(f_f, v_f, n_f)

def rotation(objet, angle, axe):
    if axe == "x":
        rot_mat = Rx(angle)
    elif axe == "y":
        rot_mat = Ry(angle)
    elif axe == "z":
        rot_mat = Rz(angle)
    else:
        return ("axe invalide")
    
    f = np.array(objet[0])
    v = np.array(objet[1]).dot(rot_mat)
    n = np.array(objet[2]).dot(rot_mat)
    
    return(f, v, n)

def centrer(objet):
    f = np.array(objet[0])
    v = np.array(objet[1]) 
    n = np.array(objet[2])

    v -=   np.mean(v, axis = 0)
    
    return(f,v,n)

def homot(objet, fact):
    objet_2 = centrer(objet)
    v = objet_2[1]
    v_x = v * fact + np.mean(objet[1], axis = 0)
    
    return(objet_2[0], v_x, objet_2[2])
