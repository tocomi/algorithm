def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  diff = 0
  for (a, b) in zip(A, B):
    diff += abs(a - b)

  if (K < diff):
    return print('No')

  return print('Yes' if (K % 2) == (diff % 2) else 'No')

if __name__ == '__main__':
  main()
