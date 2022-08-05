class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        count_R, count_L, count_U, count_D = 0, 0, 0, 0
        
        for i in moves:
            if i == 'R':
                count_R += 1
            elif i == 'L':
                count_L += 1
            elif i == 'U':
                count_U += 1
            else:
                count_D += 1
        if count_R == count_L and count_U == count_D:
            return True
        else:
            return False