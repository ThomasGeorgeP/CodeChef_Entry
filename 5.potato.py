def break_apart(size: list):
    size.sort()
    #remaining cube splits up into two pieces
    new_size1=[size[0],size[0],size[1]-size[0]]#smaller chunk
    new_size2=[size[0],size[1],size[2]-size[0]]#bigger chunk
    return new_size1,new_size2
def calc_blocks(size: list):
    size.sort()
    #biggest cube is size[0],size[0],size[0]
   
    if 0 in size:#no cubes can be formed
        return 0
    elif 1 in size:#kind of a plane
        return size[1]*size[2]
    else:
        smaller_chunk,larger_chunk=break_apart(size)
        return calc_blocks(smaller_chunk)+calc_blocks(larger_chunk)+1
   
if __name__=="__main__":
    N=int(input())
    for i in range(N):
        dimensions=[int(i) for i in input().split()]
        print(calc_blocks(dimensions))
        volume=dimensions[0]*dimensions[1]*dimensions[2]
        print(round(volume*(1-(355/113)/6)))
