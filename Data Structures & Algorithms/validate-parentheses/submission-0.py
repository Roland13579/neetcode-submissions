class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Input: s = "([{ }])"
        # 2. Stack append: '(' , '[' , '{'
        # 3. What is left in the list  '}' , ']', ')' 
        # 3. Use dict to check value of c -> '}' == '{' and matches last value in stack

        stack = []
        dictCloseToOpen = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in dictCloseToOpen: # Check if any closing 
                #If the top value in stack is the value to the 
                if stack and stack[len(stack)-1] == dictCloseToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack: #Stack has to be empty
            return True
        return False
            
