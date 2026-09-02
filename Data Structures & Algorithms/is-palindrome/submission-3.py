class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNums = "abcdefghijklmnopqrstuvwxyz1234567890"
        nums = ""
        s = s.strip("?")
        s = s.replace(" ","")
        s = s.lower()

        cleaned_string = ""
        for char in s:
            if char in alphaNums:
                cleaned_string += char
        

        print(s)
        print(cleaned_string)
        left = 0
        right = len(cleaned_string) - 1

        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -= 1

        return True