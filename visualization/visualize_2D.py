# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:35:05 2018

@author: sadra

This part is only for visualization of 2D Polytopes
"""

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import numpy as np
from cdd import Polyhedron,Matrix,RepType
from pyinpolytope.utilities.utils import vertices_cube as vcube

def visualize_2D_old(list_of_polytopes,a=1.5):
    """
    Given a polytope in its H-representation, plot it
    """ 
    p_list=[]
    x_all=np.empty((0,2))
    for polytope in list_of_polytopes:
        p_mat=Matrix(np.hstack((polytope.H,polytope.h)))
        poly=Polyhedron(p_mat)
        y=np.array(poly.get_generators())
        x=y[:,0:2]#/y[:,2].reshape(y.shape[0],1)
        x=x[ConvexHull(x).vertices,:]
        x_all=np.vstack((x_all,x))
        p=Polygon(x)
        p_list.append(p)
    p_patch = PatchCollection(p_list, color=[(np.random.random(),np.random.random(),np.tanh(np.random.random())) \
        for polytope in list_of_polytopes],alpha=0.6)
    fig, ax = plt.subplots()
    ax.add_collection(p_patch)
    ax.set_xlim([np.min(x_all[:,0])*a,a*np.max(x_all[:,0])])
    ax.set_ylim([np.min(x_all[:,1])*a,a*np.max(x_all[:,1])])
    ax.grid(color=(0,0,0), linestyle='--', linewidth=0.3)


def visualize_2D(list_of_polytopes,a=1.5):
    """
    Given a polytope in its H-representation, plot it
    """ 
    ana_color=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,0,1),(0,0,1)]
    p_list=[]
    x_all=np.empty((0,2))
    for polytope in list_of_polytopes:
        p_mat=Matrix(np.hstack((polytope.h,-polytope.H)))
        p_mat.rep_type = RepType.INEQUALITY
        poly=Polyhedron(p_mat)
        y=np.array(poly.get_generators())
        x=y[:,1:3]#/y[:,2].reshape(y.shape[0],1)
        x=x[ConvexHull(x).vertices,:]
        x_all=np.vstack((x_all,x))
        p=Polygon(x)
        p_list.append(p)
#    p_patch = PatchCollection(p_list, color=[(np.random.random(),np.random.random(),np.tanh(np.random.random())) \
#        for polytope in list_of_polytopes],alpha=0.7)
    p_patch = PatchCollection(p_list,color=ana_color[0:len(list_of_polytopes)], alpha=0.7)
    fig, ax = plt.subplots()
    ax.add_collection(p_patch)
    ax.set_xlim([np.min(x_all[:,0])-a,a+np.max(x_all[:,0])])
    ax.set_ylim([np.min(x_all[:,1])-a,a+np.max(x_all[:,1])])
    ax.grid(color=(0,0,0), linestyle='--', linewidth=0.3)
    
def visualize_2D_zonotopes(list_of_zonotopes,a=1.5,list_of_dimensions=None):
    """
    Given a polytope in its H-representation, plot it
    """ 
    if type(list_of_dimensions)==type(None):
        list_of_dimensions=[0,1]
    p_list=[]
    x_all=np.empty((0,2))
    for zono in list_of_zonotopes:
        y=zono.x.T+np.dot(zono.G,vcube(zono.G.shape[1]).T).T
        x=y[:,list_of_dimensions]#/y[:,2].reshape(y.shape[0],1)
        x=x[ConvexHull(x).vertices,:]
        x_all=np.vstack((x_all,x))
        p=Polygon(x)
        p_list.append(p)
    p_patch = PatchCollection(p_list, color=[(np.random.random(),np.random.random(),np.tanh(np.random.random())) \
        for zono in list_of_zonotopes],alpha=0.75)
#    p_patch = PatchCollection(p_list, color=[(1-zono.x[0,0]>=1,0,zono.x[0,0]>=1) \
#        for zono in list_of_zonotopes],alpha=0.75)
    fig, ax = plt.subplots()
    ax.add_collection(p_patch)
    ax.set_xlim([np.min(x_all[:,0])-a,a+np.max(x_all[:,0])])
    ax.set_ylim([np.min(x_all[:,1])-a,a+np.max(x_all[:,1])])
    ax.grid(color=(0,0,0), linestyle='--', linewidth=0.3)

def visualize_3D_zonotopes(list_of_zonotopes,a=1.5,list_of_dimensions=None):
    """
    Given a polytope in its H-representation, plot it
    """ 
    if type(list_of_dimensions)==type(None):
        list_of_dimensions=[0,1,2]
    p_list=[]
    x_all=np.empty((0,3))
    for zono in list_of_zonotopes:
        y=np.dot(zono.G,vcube(zono.G.shape[1]).T).T
        x=y[:,list_of_dimensions]#/y[:,2].reshape(y.shape[0],1)
        x=x[ConvexHull(x).vertices,:]
        p_mat=Matrix(x)
        p_mat.rep_type = RepType.GENERATOR
        x_all=np.vstack((x_all,x))
        p=Poly3DCollection([x])
        p_list.append(p)
#    p_patch = PatchCollection(p_list, color=[(np.random.random(),np.random.random(),np.tanh(np.random.random())) \
#        for zono in list_of_zonotopes],alpha=0.6)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlim3d([np.min(x_all[:,0])-a,a+np.max(x_all[:,0])])
    ax.set_ylim3d([np.min(x_all[:,1])-a,a+np.max(x_all[:,1])])
    ax.set_zlim3d([np.min(x_all[:,2])-a,a+np.max(x_all[:,2])])
    ax.add_collection3d(p)
    ax.grid3d(color=(0,0,0), linestyle='--', linewidth=0.3)