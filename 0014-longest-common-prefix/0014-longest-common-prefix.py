class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = len(strs[0])

        for i in range(len(strs)):
            if len(strs[i]) < min_length:
                min_length = len(strs[i])

        count = -1

        for j in range(min_length):
            letter_list = []
            for str in strs:
                letter_list.append(str[j])
            if len(set(letter_list)) == 1:
                count += 1
            else:
                break

        return strs[0][0:count+1]
        