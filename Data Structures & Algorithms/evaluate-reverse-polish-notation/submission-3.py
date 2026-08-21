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