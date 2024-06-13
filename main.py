def maxVal_sub(A):
  n = len(A)
  dProg = [0] * n
  dProg[0] = A[0]

  start = end = s = 0

  max_sum = A[0]

  for i in range(1, n):
      if A[i] > dProg[i-1] + A[i]:
          dProg[i] = A[i]
          s = i
      else:
          dProg[i] = dProg[i-1] + A[i]
      if dProg[i] > max_sum:
          max_sum = dProg[i]
          start = s
          end = i

  return max_sum, start, end

A = [3, -2, 5, -1, 6, -3, 2, 1, -4, 7, 8, -4]
max_sum, start_index, end_index = maxVal_sub(A)
print(f"Max sum: {max_sum}")
print(f"Subsequence: {A[start_index:end_index + 1]}")