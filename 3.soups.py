def calc_col(col):
    for i in range(len(col)-1,0,-1):
        if col[i]==col[i-1]:
            del col[i]
    return col.count(1)


ings={"t":[1,0,0],
       "o":[0,1,0],
       "b":[0,0,1],
       "p":[1,1,0],
       "c":[1,0,1],
       "y":[0,1,1],
       "s":[1,1,1]}


n=int(input())


for i in range(n):
    num=int(input())
    bowls=input().split()
    mat=[ings[j] for j in bowls]
    count=0
    for j in range(3):
        count+=calc_col([k[j] for k in mat])
    print(count)
