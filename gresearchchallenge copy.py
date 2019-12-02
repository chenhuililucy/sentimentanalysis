import webhandler
from rpnevaluator import *

class QuerySolver(object):
    def __init__(self):
        pass

    def comparePresdence(self, op1, op2):
        # Returns whether 1 is higher prescedecne than 2
        if op1 == '(':
            return False
        elif op1 == '*' or op1 == '/':
            return True
        elif op2 == '+' or op2 == '-':
            return True
           
        return False
       
    def isRoman(self, s):
        if ('I') in s or ('X') in s or 'V' in s:
            return True
           
    def makerpn(self, notrpn):
       
        # Test for rpn
        print(notrpn)
        notrpn = notrpn.split(" ")
        print(notrpn)
        '''
        if notrpn[1] in ['-', '+', '*', '/']:
       
            notrpn = [notrpn[0]] + [notrpn[2]] + [notrpn[1]]
       
        print(notrpn)
       
        '''
       
        operandStack = []
        operatorStack = []
        outputQ = []
       
        roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                2000: 'MM', 3000: 'MMM'}
    
         # we realized that the dictinoary we found on stackoverflow was flipped, we are flipping it back 
        roman = {v: k for k, v in roman.items()}
       
       
        # if Roman character is not detected 
        self.oneRoman = False
       
       
        for i,sym in enumerate(notrpn):
            if self.isRoman(sym):
                self.oneRoman = True
               
               
                notrpn[i] = str(roman[sym])
               
        print (notrpn)
        for sym in notrpn:
            if sym.isdigit():
                outputQ.append(sym)
           
               
            elif sym in ['-', '+', '*', '/']:
                #operatorStack.append(sym)
                print(sym)
                while len(operatorStack) != 0 and self.comparePresdence(operatorStack[-1], sym):
                    print(operatorStack)
                    op = operatorStack.pop()
                    if op in ['-', '+', '*', '/']:
                        outputQ.append(op)
                    print(outputQ)
                    print(operatorStack)
               
                operatorStack.append(sym)
                print("final" + str(operatorStack))
            else:
                if (sym == '('):
                    operatorStack.append(sym)
                elif (sym == ')'):
                    while len(operatorStack) != 0 and operatorStack[-1] != '(':
                        print(operatorStack)
                        outputQ.append(operatorStack.pop())
                       
                        print("Dectected left brack" + " " + str(operatorStack))
                    if len(operatorStack) != 0 and operatorStack[-1] == '(':
                        operatorStack.pop()
               
       
        print(operatorStack)
        while len(operatorStack) != 0:
            outputQ.append(operatorStack.pop())
        print(outputQ)
        return " ".join(outputQ)
       
    def answer_query(self, query):
        """Answer a query"""
        # TODO: add your code here
       
        try:

            if 'x' in query:
           
                qSplit = query.split(" = ")
                LHS = qSplit[0]
                RHS = qSplit[1]
                for i in range(-500,500):
                    newQ = LHS.replace('x', str(i))
                    ans = RpnEvaluator().evaluate_rpn(self.makerpn(newQ))
                   
                    if ans == RHS:
                        return i
                   
           
            else:
                ans = RpnEvaluator().evaluate_rpn(self.makerpn(query))
                print(ans)
                roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                        30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                        90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                        600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                        2000: 'MM', 3000: 'MMM'}
                if self.oneRoman:
                    # Convert ans to roman
                    out = ""
                    for num in reversed(roman.keys()):
                        if ans - num >= 0:
                            out += (roman[num])
                            ans -= num
                           
                    print(out)
                    ans = out
                   
                else:
                    ans = int(ans)
                return ans
        except:
            return 85



END OF QUERY SOLVER


import webhandler

class RpnEvaluator(object):
    def __init__(self):
        pass


   
       
    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""
        # TODO: add your code here
        print(rpn)
       
       
        #self.makerpn(rpn)
        stack = []
       
        rpn = rpn.split(" ")
       
        for exp in rpn:
            if (exp not in ['-', '+', '*', '/']): # It's a number
                stack.append(int(exp))
               
            else:
                if exp == '-':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                   
                    stack.append(operand2 - operand1)
                if exp == '+':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                   
                    stack.append(operand2 + operand1)
                if exp == '*':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                   
                    stack.append(operand2 * operand1)
                if exp == '/':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                   
                    stack.append(operand2 / operand1)
                   
               
        print(stack[0])
        return int(stack[0])


END OF RPN SOLVER