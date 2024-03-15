class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x for x in s if x.isalnum()]
        s = ''.join(s).lower()

        if s[::-1] == s:
            return True
        else:
            return False
        