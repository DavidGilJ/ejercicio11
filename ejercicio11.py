def count_paths(laberinto):
  m = len(laberinto)
  n = len(laberinto[0])
  dp = [[0] * n for _ in range(m)]

  if laberinto[0][0] == 1 or laberinto[m-1][n-1] == 1:
      return 0

  dp[0][0] = 1

  for i in range(1, m):
      if laberinto[i][0] == 0:
          dp[i][0] = dp[i-1][0]

  for j in range(1, n):
      if laberinto[0][j] == 0:
          dp[0][j] = dp[0][j-1]

  for i in range(1, m):
      for j in range(1, n):
          if laberinto[i][j] == 0:
              if laberinto[i-1][j] == 0:
                  dp[i][j] += dp[i-1][j]
              if laberinto[i][j-1] == 0:
                  dp[i][j] += dp[i][j-1]

  return dp[m-1][n-1]

laberinto = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]
print(count_paths(laberinto))
