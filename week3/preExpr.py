from pythonds.basic import Stack
from pythonds.basic import Queue
def preExpre(aStr) :
    operatorStack = Stack()
    operandStack = Queue()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 1
    prec["("] = 0
    tokenStr = aStr.split()
    preExpressen = []