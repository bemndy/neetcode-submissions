class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        result = 0
        operators = { "*", "/", "+", "-"}

        for op in tokens:
            # print(op, stk)
            if op in operators:
                second, first = int(stk.pop()), int(stk.pop())
                # print(first, second)
                if op == "*":
                    stk.append(first * second)
                elif op == "/":
                    stk.append(first / second)
                elif op == "+":
                    stk.append(first + second)
                elif op == "-":
                    stk.append(first - second)
            else:
                stk.append(op)
                
        return int(stk[0])

# class Solution2:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stk = []
        
#         # Dictionary mapping string operators to their respective functions
#         ops = {
#             "+": lambda a, b: a + b
#             "-": lambda a, b: a - b
#             "*": lambda a, b: a * b
#             "/": lambda a, b: int(a / b) # Using int() to truncate toward zero
#         }

#         for token in tokens:
#             if token in ops:
#                 second, first = int(stk.pop()), int(stk.pop())
#                 # Dynamically call the function from the dictionary
#                 stk.append(ops[token](first, second))
#             else:
#                 stk.append(token)
                
#         return int(stk[0])