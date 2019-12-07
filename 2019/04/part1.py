import sys

def get_digits(n: int) -> list:
  digits = []
  while n > 0:
    digits.append(n % 10)
    n //= 10
  digits.reverse()
  return digits

def is_good(password: int) -> bool:
  digits = get_digits(password)
  
  double = False
  for i in range(len(digits) - 1):
    if digits[i] > digits[i + 1]:
      return False
    if digits[i] == digits[i + 1]:
      double = True
  return double

min_pass = 125730
max_pass = 579381

print(sum([is_good(password) for password in range(min_pass, max_pass + 1)]))