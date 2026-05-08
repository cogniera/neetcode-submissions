class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mapping = { ")": "(", "}": "{", "]": "[" }

        isValid = False

        for i in range(len(s)) :
            if s[i] in '({[' :
                stack.append(s[i])
            else : 
                if s[i] in mapping :
                    
                    expected_open = mapping[s[i]]

                    if stack and stack[-1] == expected_open :
                        stack.pop()
                        isValid = True
                    else:
                        return False

                else : 
                    return isValid

        return not stack 
        
        