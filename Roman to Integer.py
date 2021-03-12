class Solution(object):
    def romanToInt(self, s):
        return s.count('CM') * 900 + s.count('CD') * 400 + s.count('XL') * 40 + s.count('XC') * 90 + s.count(
            'IV') * 4 + s.count('IX') * 9 + (s.count('M') - s.count('CM')) * 1000 + (
                           s.count('D') - s.count('CD')) * 500 + (
                           s.count('C') - s.count('CM') - s.count('CD') - s.count('XC')) * 100 + (
                           s.count('L') - s.count('XL')) * 50 + (
                           s.count('X') - s.count('XL') - s.count('XC') - s.count('IX')) * 10 + (
                           s.count('V') - s.count('IV')) * 5 + (s.count('I') - s.count('IV') - s.count('IX')) * 1







