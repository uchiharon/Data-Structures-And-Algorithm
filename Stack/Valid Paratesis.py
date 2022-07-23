class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        closeToOpen = {')':'(',']':'[','}':'{'}
        
        if ((len(s) >= 1) and (len(s) <= 10**4)):
            for c in s:
                if c in closeToOpen:
                    if stack and stack[-1] == closeToOpen[c]:
                        stack.pop(c)
                    else:
                        return False
                else:
                    stack.append(c)
            
            return True if not stack else False
        
        
