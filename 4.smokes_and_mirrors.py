def transpose(matrix): #mirror 1 and 3
    mat=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
   
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j]=matrix[j][i]
    return mat


def weird_transpose(matrix):
    mat=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j]=matrix[len(matrix)-j-1][len(matrix[0])-1-i]
    return mat


n=int(input())


for i in range(n):
    order=[int(i) for i in input().split()]
    matrix=[[(i) for i in input().split()] for j in range(order[0])]
    mirror=int(input())
   
    if mirror%2:
        result=transpose(matrix)
        for j in result:
            [print(k,end=" ") for k in j]
            print()
    else:
        result=weird_transpose(matrix)
        for j in result:
            [print(k,end=" ") for k in j]
            print()
