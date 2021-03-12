class Solution(object):
    def twoSum(self, nums, target):
        num = list(nums)
        num.sort()
        x = 0
        y = len(num) - 1
        a = num[x]
        b = num[y]
        while a+b != target:
            if y == x+1:
                return None
            elif a + b > target:
                y -= 1
                b = num[y]
            elif a + b < target:
                x += 1
                a = num[x]
        if a == b:
            return [i for i in range(len(nums)) if nums[i] == a]
        else:
            n1 = nums.index(a)
            n2 = nums.index(b)
            return [n1, n2]
