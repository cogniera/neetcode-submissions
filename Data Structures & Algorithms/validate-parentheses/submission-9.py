class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mapping = { ")": "(", "}": "{", "]": "[" }

        isValid = False

        for i in s :
             
            if i in mapping :
                
                expected_open = mapping[i]

                if not stack or stack[-1] != expected_open :
                    return False
                stack.pop()
                        
            else : 
                stack.append(i)

        return not stack 
        
        