from pythonds.basic import Stack

def postExp(aStr):
    opStack = Stack()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 1
    prec["("] = 0
    tokenStr = aStr.split()
    postExpressen = []
    for token in tokenStr :
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token.isdigit():
            postExpressen.append(token)
        elif token == "(" :
            opStack.push(token)
        elif token == ")" :
            token = opStack.pop()
            while token != "(":
                postExpressen.append(token)
                token = opStack.pop()
        else:
            # operator
            while opStack.isEmpty() == False and \
                prec[opStack.peek()] >= prec[token] :
                postExpressen.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postExpressen.append(opStack.pop())
    endRes = ' '.join(postExpressen)
    print(endRes)
    return endRes

str1 = "12 + B * C"
str2 = "( A + B ) * ( C + E )"
postExp(str1)
postExp(str2)


def evalPost(postExpression):
    tokenStr = postExpression.split()
    operandStack = Stack()
    # index = 0
    # while index < len(tokenStr):
        # token = tokenStr[index]
    for token in tokenStr :
        if token in "+-*/" :
            rightOp = operandStack.pop()
            leftOp = operandStack.pop()
            tempRes = mathsOp(token, leftOp,rightOp)
            operandStack.push(tempRes)
        else :
            # tempStr = [token]
            # index = index + 1
            
            # while index < len(tokenStr) and token in "0123456789" :
            #     token = tokenStr[index]
            #     tempStr.append(token)
            #     index = index + 1
            # tempVal = float(str(tempStr))
            # operandStack.push(tempVal)
            operandStack.push(float(token))
    result = operandStack.pop()
    print(result)
    return result

def mathsOp(token, leftOp, rightOp):
    if token == "+" :
        return leftOp + rightOp
    elif token == "-" :
        return leftOp - rightOp
    elif token == "*" :
        return leftOp * rightOp
    elif token == "/" :
        return leftOp / rightOp
    
str3 = " 11 22 +"
evalPost(str3)