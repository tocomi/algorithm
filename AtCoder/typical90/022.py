from functools import reduce
import math

def my_gcd(*numbers):
  return reduce(math.gcd, numbers)

def main():
  A, B, C = map(int, input().split())
  gcd = my_gcd(A, B, C)

  a = A // gcd - 1
  b = B // gcd - 1
  c = C // gcd - 1

  print(a + b + c)

if __name__ == '__main__':
  main()
