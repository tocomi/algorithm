from bisect import bisect_left

def bs(l: list, b: int) -> int:
  ln = len(l)
  li = 0
  mi = ln - 1

  if b < l[0]:
    return abs(l[0] - b)
  if b > l[ln - 1]:
    return abs(l[mi] - b)

  while li <= mi:
    if li == mi:
      return abs(l[li] - b)

    m = int((li + mi) // 2)
    if b >= l[m] and b <= l[m + 1]:
      return min(abs(l[m] - b), abs(l[m + 1] -b))

    if b < l[m]:
      mi = m
      continue
    if b > l[m + 1]:
      li = m + 1
      continue

def main():
  N = int(input())
  A = list(map(int, input().split()))
  sA = sorted(A)
  Q = int(input())
  B = [int(input()) for _ in range(Q)]

  for b in B:
    print(bs(sA, b))

if __name__ == '__main__':
  main()
