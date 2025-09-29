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
for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b
print()
