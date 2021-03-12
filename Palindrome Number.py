class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x>=0 and x<10:
            return True
        else:
            x1 = int(x/10)
            x2 = x - int(x/10)*10
            a = []
            a.append(x2)
            while x1 != 0:
                x2 = x1 - int(x1/10)*10
                a.append(x2)
                x1 = int(x1/10)
            i = 0
            n = len(a) -1

            while 2*i < n:
                if a[i] != a[n -i]:
                    break
                i +=1
            if i == len(a)//2:
                return True
            else:
                return False