class Solution:
    # @return a boolean
    def isValid(self, s):
        '''
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
        '''
        ldic = {'(': 1, '[': 2, '{': 4}
        rdic = {')': -1, ']': -2, '}': -4}
        stack = []
        for c in s:
            if c in ldic:
                stack.append(ldic[c])
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x != -rdic[c]:
                    return False
        if len(stack) > 0:
            return False
        return True
