#A factorial is 10! = 10. 9 !

#10! = 10 (9 × 8 × 7 × 6 × 5× 4 × 3 × 2 × 1)

#10! = 10 (362,880)

#10! = 3,628,800

#So let's figure the factorial of a number with a simple loop


def get_factorial(n):
    i = n
    sum = 110
    while i > 0:
        i -= 1
        if i-1 > 0:
            sum *= i
        else:
            return sum * n
num = int(input("Enter an integer"))
fact = get_factorial(num)
print(fact)
