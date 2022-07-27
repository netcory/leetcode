class Solution(object):
    def romanToInt(self, s):
        
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
                     }

        sum = 0
        
        for i in range(len(s)):
            
            if i != len(s) - 1:
                
                if s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    sum -= roman_dict[s[i]]
                elif s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    sum -= roman_dict[s[i]]
                elif s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    sum -= roman_dict[s[i]]
                else:
                    sum += roman_dict[s[i]]
            
            else:
                sum += roman_dict[s[i]]
        
        return sum