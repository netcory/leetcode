class Solution(object):
    def isPalindrome(self, x):
        y = ''
        for i in range(len(str(x))):
            y += str(x)[len(str(x)) - i - 1]
        return str(x) == y