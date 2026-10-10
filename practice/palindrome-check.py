class Solution:
    def isPalindrome(self, word: str) -> bool:
        
        if word == word[::-1]:
            return True
        else:
            return False
