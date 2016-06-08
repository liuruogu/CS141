import numpy as np

data = np.genfromtxt('input50small.txt', delimiter=',')
mat_index = []
mat_min = []
trace = []
triple = [1,2,3]

mat_index = np.copy(data)
mat_min = np.copy(data)

# Set the first line of index matrix as 0
for j in range(data.shape[1]):
    mat_index[0,j] = 0
    mat_min[0,j] = data[0,j]

#Get the index matrix and the seam carving matrix
for i in range(data.shape[0]-1):
    for j in range(data.shape[1]):
        if j == 0: #At the left most
             if min(mat_min[i,j],mat_min[i,j+1]) == mat_min[i,j]:
                 mat_index[i+1,j] = j
                 mat_min[i+1,j] = mat_min[i,j] + data[i+1,j]
             else:
                 mat_index[i+1,j] = j+1
                 mat_min[i+1,j] = mat_min[i,j+1] + data[i+1,j]
        elif j == data.shape[1]-1: # At the right most
             if min(mat_min[i,j],mat_min[i,j-1]) == mat_min[i,j]:
                 mat_index[i+1,j] = j
                 mat_min[i+1,j] = mat_min[i,j] + data[i+1,j]
             else:
                 mat_index[i+1,j] = j-1
                 mat_min[i+1,j] = mat_min[i,j-1] + data[i+1,j]
        else :
             if min(mat_min[i,j-1],mat_min[i,j],mat_min[i,j+1]) == mat_min[i,j-1]:
                mat_index[i+1,j] = j-1
                mat_min[i+1,j] = mat_min[i,j-1] + data[i+1,j]
             elif min(mat_min[i,j-1],mat_min[i,j],mat_min[i,j+1]) == mat_min[i,j]:
                mat_index[i+1,j] = j
                mat_min[i+1,j] = mat_min[i,j] + data[i+1,j]
             elif min(mat_min[i,j-1],mat_min[i,j],mat_min[i,j+1]) == mat_min[i,j+1]:
                mat_index[i+1,j] = j+1
                mat_min[i+1,j] = mat_min[i,j+1] + data[i+1,j]

# Find the trace
a = np.copy(mat_min[data.shape[0]-1])
m = min(a)
for j in range(data.shape[0]):
    if m == a[j]:
        index = j
min_seam = index

triple = [data.shape[0]-1,index, data[data.shape[0]-1,index]]
med = np.copy(triple)
trace.append(med)
index = mat_index[data.shape[0]-1,index]

for t in range(data.shape[0]-2,-1,-1):
    triple[0] = t
    triple[1] = mat_index[t+1,index]
    triple[2] = data[t,index]
    index = mat_index[t,triple[1]]
    med = np.copy(triple)
    trace.append(med)

text_file = open("output50small.txt", "w+")
first_lin = 'Min seam : '+str(mat_min[data.shape[0]-1,min_seam])+'\n'
text_file.write(first_lin)
for i in range(len(trace)):
    st = str(trace[i])
    st = st + '\n'
    text_file.write(st)
text_file.close()
