'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

A = ["4", "13", "5", "/", "+"]


class Solution:
    # @param A : list of strings
    # @return an integer

    def evalRPN(self, A):

        stack = []
        i = len(A) - 1
        count = 0
        ans = 0

        while i >= 0:

            # Increment count when A[i] is an int
            if self.isInt(A[i]):
                count += 1
            else:
                count = 0

            # Push element onto the stack
            stack.append(A[i])
            i -= 1

            # When the last two elements have been numbers
            while count == 2:
                a = int(stack[-1]);
                stack.pop()
                b = int(stack[-1]);
                stack.pop()
                op = stack[-1];
                stack.pop()

                # Perform operation specified by the operator
                if op == "+":
                    ans = a + b
                elif op == "-":
                    ans = a - b
                elif op == "*":
                    ans = a * b
                elif op == "/":
                    ans = a / b

                # Set count to 1 if the next element is a number
                if len(stack) > 0 and self.isInt(stack[-1]):
                    count = 1
                else:
                    count = 0

                # Push ans onto stack and increment count
                stack.append(ans)
                count += 1

        print stack[-1]

    # Check if the value is an integer
    def isInt(self, x):
        try:
            int(x)
            return True
        except ValueError:
            return False

sol = Solution()
sol.evalRPN(A)
