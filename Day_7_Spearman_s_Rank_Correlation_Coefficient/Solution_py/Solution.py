def getRank(X, n):
    rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [rank[x] for x in X]

def rxy(n, X, Y):
  rx = getRank(X, n)
  ry = getRank(Y, n)

  d = [(rx[i] -ry[i])**2 for i in range(n)]
  return round(1 - (6 * sum(d)) / (n * (n*n - 1)), 3)


if __name__ == "__main__":
  n = int(input())
  X = list(map(float, input().strip().split()))
  Y = list(map(float, input().strip().split()))

  print(rxy(n, X, Y))
