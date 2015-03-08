class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        '''
        Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

click to show corner cases.
Corner Cases:

    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
        '''
        names = path.split('/')
        stack = []
        for name in names:
            if name == '.' or name == '':
                continue
            elif name == '..':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(name)
        return '/' + '/'.join(stack)

p1 = '/.././'
p2 = "/home/"
p3 = "/a/./b/../../c/"
p4 = "/home//foo/"
p = p4
print(p)
print(Solution.simplifyPath(Solution(), p))