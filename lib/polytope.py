# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:56:09 2018

@author: sadra
"""

import numpy as np
from pypolycontain.utils.utils import unique_rows


class polytope():
    def __init__(self,H,h):
        """
        Class Polytope. A Polytope is defined as (x \in R^n | Hx <= h)
        """
        if h.shape[1]!=1:
            ValueError("Error: not appropriate h size, it is",h.shape)
        if H.shape[0]!=h.shape[0]:
            ValueError("Error: not consistent dimension of H: %d and h: %d"%(H.shape[0],h.shape[0]))
        self.type="H-polytope"
        self.H,self.h=unique_rows(H,h)
        self.n=H.shape[1]
#        self.hash_value = hash(str(np.hstack([self.H, self.h])))

    def __repr__(self):
        return ("polytope in R^%d"%self.n)

    def __hash__(self):
        return self.hash_value

    def show(self):
        print(self)
        print("H=",self.H)
        print("h=",self.h)
        
    def if_inside(self,x):
        if x.shape[0]!=self.H.shape[1]:
            return ValueError("H and x dimensions mismatch")
        return all(np.dot(self.H,x)<=self.h)

    
def translate(p,d):
    """
    Given a polytope p, translate it by d 
    """
    return polytope(p.H,p.h+np.dot(p.H,d))

def Box(N,d=1):
    """
    returns N-dimensional Box
    """
    H=np.vstack((np.eye(N),-np.eye(N)))
    h=d*np.ones((2*N,1))
    return polytope(H,h)