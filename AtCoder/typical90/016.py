def main():
  N = int(input())
  A, B, C = reversed(sorted(list(map(int, input().split()))))

  ans = 99999
  for ac in range(9999):
    if (A * ac > N):
      break
    for bc in range(9999 - ac):
      t = N - (A * ac + B * bc)
      if (t < 0):
        break
      if (t % C == 0):
        cc = t // C
        ans = min(ac + bc + cc, ans)

  print(ans)

if __name__ == '__main__':
  main()
