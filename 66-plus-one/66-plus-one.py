class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        sum = 0
        
        for i in range(len(digits)):
            sum += digits[i] * 10**(len(digits) - i - 1)
        
        sum += 1

        sum_chr = str(sum)

        result_list = []

        for j in range(len(sum_chr)):
            result_list.append(sum_chr[j])
        
        return result_list