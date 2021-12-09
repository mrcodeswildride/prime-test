def is_divisible(a, b):
  return a % b == 0  

print()

number = int(input("Enter a number [2-100]: "))

is_prime = True

for n in range(2, number):
  if is_divisible(number, n):
    is_prime = False

if is_prime:
  print(f"\n{number} is a prime number.")
else:
  print(f"\n{number} is a composite number.")
