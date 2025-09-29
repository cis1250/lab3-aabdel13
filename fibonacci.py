# keep asking untill the user enters a valid positive integer
while True:
  user_input = input("enter the number of terms in the Fibonacci sequance: ")
  
        if user_input.isdigit():
          n = int(user_input)
          if n > 0:
            break
        else:
        print("please enter a positive integer.")

    else:
     print("please enter a positive integer.")
      
a, b = 0, 1
# generate and print the Fibonacci sequence using a for loop
for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b
print() # move to a new line after printing the sequence
