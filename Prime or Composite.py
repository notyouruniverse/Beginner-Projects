n = int(input("Enter a number: "))

is_composite = False
i = 2  # Start at 2 to avoid division by zero and 1

while i < 10000 and i < n:  # Loop up to 9999, but stop if i reaches n
    if n % i == 0:
        print(n, "is a composite number divisible by", i)
        is_composite = True
        break
    i += 1

if not is_composite and n > 1:
    print(n, "is a prime number.")
