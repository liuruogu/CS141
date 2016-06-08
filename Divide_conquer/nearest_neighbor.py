__author__ = 'liu'
import numpy as np
import scipy.spatial.distance as dis
import sys
import time

# Get the command from the terminal
# Edit the data file
# The matrix start from 0, different from Matlab
data = np.genfromtxt(sys.argv[1],delimiter = '')
# data = np.genfromtxt('input.txt',delimiter = '')

row, col = data.shape

# Brute force search
def Brute_force(data):

    best_so_far = 1000000000
    for i in range(row): # Calculate each pair of points
        for j in range(i+1, row):
            edis = euclidean(data[i,:],data[j,:])
            if best_so_far > edis:
                best_so_far = edis
        #         print("The best so far is "+str(best_so_far))
        # print('--------------------------')
    return best_so_far

# Divide and Conquer search
def Divide_conquer(data):
# sort the input as X coordinate
#     c = sorted(data, key=lambda x:(x[0]))
#     n = len(c)/2
# def Closest_pair(l,r):

# Divide into 2 group based on x and find the DL & DR, d is the minimum
    xc = data[:,0].copy()
    xc.sort()
    c = (xc[4]+xc[5])/2 # C divide the x equally
    L = [] # Nodes in the left side
    R = [] # Nodes in the right side
    M = [] # Nodes in the middle

    for i in range(row):
        if data[i,0]<c:
            L.append(data[i,:])
        elif data[i,0]>c:
            R.append(data[i,:])
    # print(L)
    # print(R)
    # print(data)
    bsf = 1000000000
    for i in range(5):
        for j in range(i+1,5):
            edis = euclidean(L[i],L[j])
            if bsf > edis:
                bsf = edis
        #         print("The best so far is "+str(bsf))
        # print('--------------------------')
        ldis = bsf
    # print(L)
    # print(str(ldis)+" is the minimum distance of left side.")
    # print(data)

    bsf = 1000000000
    for i in range(5):
        for j in range(i+1,5):
            edis = euclidean(R[i],R[j])
            if bsf > edis:
                bsf = edis
        #         print("The best so far is "+str(bsf))
        # print('--------------------------')
        Rdis = bsf
    # print(R)
    # print(str(Rdis)+" is the minimum distance of right side.")

    dminx = min(ldis,Rdis)
    # print(str(dminx)+" is the minimum so far.")

    for i in range(row):
        if data[i,0]>(c-dminx) and data[i,0]<(c+dminx):
            M.append(data[i,:])

    bsf = 1000000000
    for i in range(len(M)):
        for j in range(i+1,len(M)):
            edis = euclidean(M[i],M[j])
            if bsf > edis:
                bsf = edis
        #         print("The best so far is "+str(bsf))
        # print('--------------------------')
        mdis = bsf
    # print(M)
    return min(ldis,Rdis,mdis)

# Calculate the euclidean distance
def euclidean(a, b):
    Edis = dis.euclidean(a,b)
    # print(Edis)
    return Edis

# Write the output to the output file
def Write_to_File(filename, s):
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')

def main():
    start_time = time.time()
    # mindis = Brute_force(data)
    mindis = Divide_conquer(data)

    end_time = time.time()
    print(str(mindis)+' is the nearest distance of two points of the dataset.')
    print('This algorithm spend '+str((end_time - start_time)*1000)+' ms')
    Write_to_File('output.txt',mindis)

if __name__ == "__main__":
    main()