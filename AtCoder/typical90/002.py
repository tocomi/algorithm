from itertools import product

def main():
  N  = int(input())

  if (N % 2 == 1):
    return

  for l in product(['(' , ')'], repeat=N):
    a = 0
    for p in l:
      if p == '(':
        a += 1
      elif p == ')':
        a -= 1
      if a < 0:
        break
    if a == 0:
      print(*l, sep='')

if __name__ == '__main__':
  main()
