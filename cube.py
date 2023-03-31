import numpy as np
import random
n=9
w=6
m=1000
s=[2,4]
index=[[0]*(w-1)]*n
matrix=np.random.randint(0,100,(n,n))
stages=np.zeros([n,n,n])
stagepath = np.zeros([n, n, n], dtype='U30')
stagemin=np.zeros([n,n])
a=np.zeros([n])

matrix[0]=[0]*n
for i in range(len(s)):
    matrix[0][s[i]-1]=random.randint(1,100)
for i in range(n):
    for j in range(n):
        if ((abs(i-j)//(w+1)>0)):
            matrix[i][j]=0
        if (i==j):
            matrix[i][j]=0
        if (i>j):
            matrix[i][j]=matrix[j][i]
for i in range(n):
    for j in range(n):
        if i == 0:
            for bb in range(n):
                stages[i][0][bb] = matrix[i][bb]
                if matrix[i][bb] > 0:
                    string = ''.join(['1','-',str(bb+1)])
                    stagepath[i][0][bb] = string
        else:
            sumcheck=0
            for ii in stagemin[i-1]:
                if ii==0:
                    sumcheck+=1                    
                else:
                    for xx in range(n):
                        if(matrix[sumcheck][xx]!=0):
                            stages[i][sumcheck][xx]=matrix[sumcheck][xx]+stagemin[i-1][sumcheck]
                    sumcheck+=1
        row=stages[i,:,j]
        for x in row:
            if x>0 and x<m:
                m=x
                stagemin[i][j]=x
        m=1000
for i in range(1,n):
    for j in range(n):
        for k in range(n):
            row=stages[i-1,:,j]
            if stagemin[i-1][j]!=0:
                a=np.where(row==stagemin[i-1][j])[0]
                if(stages[i][j][k]!=0):
                    if (len(a)>0):
                        string=''.join([stagepath[i-1][int(max(a))][j],'-',str(k+1)])
                        stagepath[i][j][k]=string
print('Начальная матрица')
for row in matrix:
    print(row)
print()
for i in range(n-1):
    print('Этап ',n-i-1)
    for row in stages[i]:
        print(row)
    print()
    print('Минимальные значения')
    print(stagemin[i])
    print()
    print('Пути')
    for row in stagepath[i]:
        print(row)
    print()
    for j in range(n):
        row=stagemin[:,-1]
        for x in row:
            if x>0 and x<m:
                m=x
                lowest=x
minimum=np.where(stages[:,:,-1]==lowest)
x=minimum[0][0]
y=minimum[1][0]
print('Минимальный путь -',lowest)
print(stagepath[x][y][-1])
