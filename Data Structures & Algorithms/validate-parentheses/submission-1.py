class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")" : "(", "]" : "[", "}" : "{"}

        # loop through the characters
            # check if character is an opening parenthisis and if the corresponding closed parentheses is in the bracket map
            # else add opening parenthesis to the stack 
        for char in s:
            if char in bracketMap:
                if stack and stack[-1] == bracketMap[char]:
                    stack.pop()
                else:
                    return False
            
            else: 
                stack.append(char)
            
        return True if not stack else False