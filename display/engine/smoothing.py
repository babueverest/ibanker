
from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from scipy.stats import linregress

def readCsv(fname):
    try:
        my_data = genfromtxt(fname,dtype=None,delimiter=',')
        date = my_data[1:,0]
        data = my_data[1:,1]
        return date,data
    except IOError:
        print "File not found"


def singleExp(data,alpha):
	y = [float(i) for i in data] 					# creating the list of interest rate as y
	s = [y[0]]					 					# the forecast parameter s and setting s2 = y1 
	for i in range(1,y.__len__()): 					# iterating from y2 to y(n) and finding s3 to s(n)
		s.append( alpha * y[i] + (1-alpha) * s[-1]) #applying formula s(t+1) = alpha*y(t) + (1-alpha) * s(t)
	return y,s  									# returns y ans s of same length but the first y..
													#..and last s has to be removed before calculating error 

def findMSE(y,s):
	yarray = np.asarray(y[1:]) 						 #removing first y and changing into numpy array
	sarray = np.asarray(s[:-1]) 					 #removing predicted s and changing into numpy array
	sqerror = (yarray - sarray) * (yarray - sarray)
	return np.mean(sqerror)							 #returns the mean square error 

def getAllOfSingleExp(data): 
	alpha = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]  # list of alpha
	err = []										 # list of Mean square error corrosponding to each alpha
	for a in alpha:									 #iterating over alpha
		y,s = singleExp(data,a)
		err.append(findMSE(y,s))
	bestAlpha = alpha[err.index(min(err))]           #value of alpha having least MSE error
	worstAlpha = alpha[err.index(max(err))]			 #value of alpha having biggest MSE error
	yb,sb = singleExp(data,bestAlpha)                #sb holds best smoothed perdiction
	yw,sw = singleExp(data,worstAlpha)				 #sw holds worst smoothed prediciton 

	return sb ,bestAlpha, sw, worstAlpha,err,alpha   # returns sb and sw corrosponding to bestAlpha and worstAlpha and error with alpha variation


def simpelMovingAvg(data,n):						 #function to find simple moving average [n is the window length or ]
	y = [float(i) for i in data]					 #holds the input data in list
	s = []											 #holds the predicted values or smoothed values using moving avg 
	n = n-1 										 #to match the python indexing
	for i in range(0,y.__len__()-n):				 #iterate from beginning till the last possible index 
		tmp = y[i:n+1+i]							 #gets the n item and moves as i increase [the window]
		s.append(sum(tmp)/(n+1))					 #summing the number in list and getting the average
	return s 										 #the result is in s but first n-1 values will not be available if plotting



def linearReg(data):
	y = [float(i) for i in data]					 #The output interest rate as y
	x = [i for i in range(1,y.__len__()+1)]			 #The input time t taken as series of natural number
	slope, intercept, r, p, stderr = linregress(x, y)#scipy module for linear reg..fitting x and y 
	predicted = [intercept + x * slope for x in range(1,y.__len__()+2) ]#The list of predicted values for each training input and one next time frame
	return predicted,slope,intercept



     






