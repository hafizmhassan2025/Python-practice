def sum(n):
    if n != 0:
        return n + sum(n - 1)
    else:
        return 0


n = int(input("Enter a number: "))

result = sum(n)

print("Sum of first", n, "natural numbers is:", result)