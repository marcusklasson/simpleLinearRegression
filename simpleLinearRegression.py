# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 18:55:05 2016

@author: Marcus
"""
import numpy as np
import matplotlib.pyplot as plt
import pylab

def hypothesisFunction(x, theta0, theta1):
    h = []
    for i in range(len(x)) :
        h.append(theta0 + theta1*x[i])
    return h
    
def costFunction(x,y,theta0,theta1) :
    h = hypothesisFunction(x,theta0, theta1)
    tmp = np.subtract(h,y)
    #print str(np.power(tmp,2)) + 'sataattana'
    J = 1/float(2*len(x)) * np.sum(np.power(tmp,2))
    return J
    
def gradientDescent(x,y,theta0,theta1,alpha,tol):
    iter = 1
    J_old = 0
    J = costFunction(x,y,theta0,theta1)
    while np.absolute(J - J_old) > tol or iter < 2:
        J_old = J
        theta0_old = theta0
        theta1_old = theta1
        theta0 = updateTheta0(x,y,theta0_old,theta1_old,alpha)
        #print theta0
        theta1 = updateTheta1(x,y,theta0_old,theta1_old,alpha)
        #print theta1
        J = costFunction(x,y,theta0, theta1)
        #print J
        iter = iter + 1
    print 'Number of iterations: ' + str(iter)
    return [theta0, theta1]
        
def updateTheta0(x,y,theta0,theta1,alpha) :
    m = len(x)
    h = hypothesisFunction(x, theta0, theta1)
    return theta0 - alpha * (1/float(m) * np.sum(np.subtract(h,y)))
    
def updateTheta1(x,y,theta0,theta1,alpha) :
    m = len(x)
    h = hypothesisFunction(x, theta0, theta1)
    tmp = np.subtract(h,y)
    return theta1 - alpha * (1/float(m) * np.sum(np.multiply(tmp,x)))

def main() :
    x = [0, 1, 2, 4]
    y = [1, 2, 3, 5]
    #x = np.random.randint(100, size=100)
    #print x
    #y = np.random.randint(50, size=100)
    #print y
    theta0 = 1
    theta1 = 1
    tol = 0.001
    alpha = 0.2 # Learning rate
    Theta = gradientDescent(x,y,theta0,theta1,alpha,tol)
    print Theta
    
    h = hypothesisFunction(x, Theta[0], Theta[1])
    pylab.xlim([0,5])
    #pylab.ylim([0,50])
    plt.plot(x,y,'rx')
    plt.plot(x,h,'-')
    plt.show() 
    
main()