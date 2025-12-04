# Using List Comprehension
arr = [[4, 5, 6, 8],
       [1, 2, 3, 1],
       [7, 8, 9, 4],
       [1, 8, 7, 5]]

n = len(arr)
res = [*arr[0], *[arr[i][n - i - 1] for i in range(1, n - 1)], *arr[-1]]
print(*res)