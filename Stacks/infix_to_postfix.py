class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
        stack = []
        result = []

        for ch in A:
            # Operand
            if ch.isalpha():
                result.append(ch)

            # Opening bracket
            elif ch == '(':
                stack.append(ch)

            # Closing bracket
            elif ch == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # remove '('

            # Operator
            else:
                while (stack and stack[-1] != '(' and (precedence[stack[-1]] >= precedence[ch])):
                    result.append(stack.pop())

                stack.append(ch)

        # Pop remaining operators
        while stack:
            result.append(stack.pop())

        return "".join(result)
