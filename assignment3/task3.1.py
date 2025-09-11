num = int(input("Enter a number: "))

def factorial(number):
    if number == 1:
        return number
    return number * factorial(number-1)


fact = factorial(num)
print("Factorial of",num,"is:", fact)