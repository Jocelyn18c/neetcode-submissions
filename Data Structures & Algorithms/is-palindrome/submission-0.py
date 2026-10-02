class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin_text = s.lower()
        cleaned = ""            # create an empty string
        for ch in palin_text:
            if ch.isalnum():
                cleaned += ch
        left = 0
        right = len(cleaned) - 1

        while(left < right):
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True 