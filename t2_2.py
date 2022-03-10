import math
while True:
    a = int (input())
    b = int (input())
    print ("welcome to shamim's calculator")
    print ("+ sum")
    print ("- sub")
    print ("* mul")
    print ("/ div")
    print ("^ pow")
    print ("sin")
    print ("cos")
    print ("tan")
    print ("cot")
    print ("exit")
    op = input()
    if op == "+":
        result = a+b
    elif op == "-":
        result = a-b
    elif op == "*":
        result = a*b
    elif op == "/":
        if b!=0 :
            result= a/b
        else:
            result ='cannot divide by zero'
    elif op == "sin":
        print ( math.sin (math. radians(a)))
        print ( math.sin (math. radians(b)))
    elif op == "cos":
         print( math.cos(math.radians(a)))
         print ( math.cos(math.radians(b)))
    elif op == "tan":
        print (math.tan (math.radians(a)))
        print (math.tan (math.radians(b)))
    elif op == "cot":
        print (math.cot (math.radians(a)))
        print (math.cot (math.radians(b)))
               
    elif op == 'exit':
        break
    else:
        result= 'command not found'