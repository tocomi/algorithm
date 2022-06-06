def main():
  N, M = map(int, input().split())
  L = [list(map(int, input().split())) for _ in range(N)]

  row_sum = []
  for n in range(N):
    row_sum.append(sum(L[n]))

  col_sum = []
  for m in range(M):
    col_s = 0
    for n in range(N):
      col_s = col_s + L[n][m]
    col_sum.append(col_s)

  for n in range(N):
    result = []
    for m in range(M):
      result.append(row_sum[n] + col_sum[m] - L[n][m])
    print(" ".join(map(str, result)))

if __name__ == '__main__':
  main()
