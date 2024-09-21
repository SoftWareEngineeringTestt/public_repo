def calculator(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0: raise ZeroDivisionError("cannot divide by zero")
        return x / y
    else:
        raise ValueError("invalid operation")

result = calculator(10, 5, '+')  
print(result)        
    