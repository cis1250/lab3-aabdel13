while True:
    user_input = input("Enter the number of terms in the Fibonacci sequence: ")
    
    if user_input.isdigit():
        n = int(user_input)
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    else:
        print("Please enter a positive integer.")

a, b = 0, 1
# Generate and print the Fibonacci sequence using a for loop
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()  # move to a new line after printing the sequence
