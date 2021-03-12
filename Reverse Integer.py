class Solution(object):
    def reverse(self, x):
        if x >= 0:
            y = str(x)
            if int(y[::-1]) < -2 ** 31 or int(y[::-1]) > 2 ** 31 - 1:
                return 0
            return int(y[::-1])
        if x < 0:
            y = str(-x)
            if int(y[::-1]) < -2 ** 31 or int(y[::-1]) > 2 ** 31 - 1:
                return 0
            return -int(y[::-1])
