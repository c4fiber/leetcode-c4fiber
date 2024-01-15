class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^0-9a-zA-Z]','',s)
        s = s.lower()
        
        return s == s[::-1]