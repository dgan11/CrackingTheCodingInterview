class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

# class Solution(object):
#     def sortedArrayToBST(self, nums):
#         if len(nums) == 0:
#             return None
#         return self.helper(nums, 0, len(nums)-1)


#     def helper(self, nums, left, right):
#         if (left > right):
#             return None
        
#         mid = int(left + right) / 2
#         print(nums[mid])
#         cur = Node(nums[mid])
#         cur.left = self.helper(nums, left, mid-1)
#         cur.right = self.helper(nums, mid+1, right)
#         return cur


def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    return helper(nums, 0, len(nums)-1)

def helper(nums, left, right):
    print(left, right)
    if (left > right):
        return None

    mid = int((left + right) / 2)
    print("nums[mid]: ", nums[mid])
    #print(nums[mid])
    cur = Node(nums[mid])
    cur.left = helper(nums, left, mid-1)
    cur.right = helper(nums, mid+1, right)
    print(cur.val)
    return cur

print(sortedArrayToBST([1,3,4,5,7,8,20]))


"""
Time: O(n*logn) -- doing n inserts which cost O(logn)
    for binary search trees

Space: O(n+m) where n is the number of 
"""