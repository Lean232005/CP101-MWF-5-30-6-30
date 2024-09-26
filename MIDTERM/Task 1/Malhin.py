def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Cannot divide by zero'

# Example usage
result_add = add(5, 3)
result_subtract = subtract(5, 3)
result_multiply = multiply(5, 3)
result_divide = divide(10, 2)

print('Addition result:', result_add)
print('Subtraction result:', result_subtract)
print('Multiplication result:', result_multiply)
print('Division result:', result_divide)
