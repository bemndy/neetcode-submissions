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
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        # Dictionary mapping string operators to lambda functions
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            # int() is used here instead of // to ensure truncation toward zero
            "/": lambda a, b: int(a / b) 
        }

        for token in tokens:
            if token in ops:
                # 1. ERROR CHECK: Stack Underflow (not enough numbers for the operator)
                # if len(stk) < 2:
                #     raise ValueError("Invalid RPN: Not enough operands for operator.")

                second = int(stk.pop())
                first = int(stk.pop())
                
                # 2. ERROR CHECK: Division by Zero
                # if token == "/" and second == 0:
                #     raise ZeroDivisionError("Invalid RPN: Division by zero.")

                # Call the lambda function dynamically
                stk.append(ops[token](first, second))
            else:
                # 3. ERROR CHECK: Garbage Input (token is not an operator or a number)
                # try:
                #     int_val = int(token)
                # except ValueError:
                #     raise ValueError(f"Invalid RPN: Unrecognized token '{token}'.")
                
                stk.append(int(token))
                
        # 4. ERROR CHECK: Final Stack Size (too many numbers left over)
        # if len(stk) != 1:
        #     raise ValueError("Invalid RPN: Too many operands left over.")
            
        return int(stk[0])
'''

