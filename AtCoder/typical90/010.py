def main():
  N = int(input())
  C = [list(map(int, input().split())) for _ in range(N)]
  Q = int(input())
  L = [list(map(int, input().split())) for _ in range(Q)]

  one_acc = []
  two_acc = []
  one_total = 0
  two_total = 0
  for c, p in C:
    if c == 1:
      one_total += p
    else:
      two_total += p
    one_acc.append(one_total)
    two_acc.append(two_total)

  for l, r in L:
    one_sum = one_acc[r - 1] - (one_acc[l - 2] if l > 1 else 0)
    two_sum = two_acc[r - 1] - (two_acc[l - 2] if l > 1 else 0)
    print('{} {}'.format(one_sum, two_sum))

if __name__ == '__main__':
  main()
