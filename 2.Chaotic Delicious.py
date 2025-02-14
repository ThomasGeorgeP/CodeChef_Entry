from bisect import bisect_right
def longest_decreasing_subsequence(arr):
    lis = []
    for num in arr:
        pos = bisect_right(lis, -num)
        if pos == len(lis):
            lis.append(-num)
        else:
            lis[pos] = -num
    return len(lis)
N = int(input())
A = list(map(int, input().split()))
print(longest_decreasing_subsequence(A))