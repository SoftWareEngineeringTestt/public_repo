def calculator(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y != 0: 
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

result = calculator(10, 5, '+')  
print(result)        
    