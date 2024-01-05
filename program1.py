class Solution(object):
    def isValid(s):
        stack=[]
        mapping={')' : '(' , ']' : '[' , '}' :'{'}
        for char in s:
            if char in mapping:
                top_element=stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return false
                else:
                    stack.append(char)
                    return not stack
    



  

