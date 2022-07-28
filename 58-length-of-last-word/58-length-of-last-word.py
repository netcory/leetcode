class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        word_list = s.split(' ')
        word_list.reverse()
        
        for i in word_list:
            if i == '':
                pass
            else:
                break
        
        return len(i)