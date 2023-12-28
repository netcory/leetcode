class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        match = 0

        if haystack_len < needle_len:
            match = -1
        else:
            for i in range(0, haystack_len - needle_len + 1):
                if haystack[i : i + needle_len] == needle:
                    match = i
                    break
                else:
                    match = -1
        return match
