class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        """ Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
        tab = "+-*/"
        stack = []
        for token in tokens:
            if tab.find(token) == -1:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                op = token
                c = self.myEval(a, b, op)
                #print(c, "=", a, op, b)
                #stack.append(eval('%d%s%d' % (stack.pop(), token, tmp)))
                stack.append(c)
        return stack[0]

    def myEval(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return int(a * 1.0 / b)

tokens1 = ["2", "1", "+", "3", "*"]
tokens2 = ["4", "13", "5", "/", "+"]
tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokenss = tokens3
print(tokenss)
ss = Solution()
print(ss.evalRPN(tokenss))