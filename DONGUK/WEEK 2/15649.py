import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []


def search():
    if len(nums) == M:
        for i in range(M):
            if i != M-1:
                print(nums[i], end=' ')
            else:
                print(nums[i])

    for i in range(1, N+1):
        if i not in nums:
            nums.append(i)
            search()
            nums.pop()

search()

'''
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 4, 3]
'''


