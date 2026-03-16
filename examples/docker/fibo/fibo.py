print("This is my first Docker image")
print("It prints the first 50 Fibonacci numbers")

a = 0
b = 1

for i in range(1, 51):
    print("Fibonacci %i: %i" %(i, b))
    a, b = b, a + b
