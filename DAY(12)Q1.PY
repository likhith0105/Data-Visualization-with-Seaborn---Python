# Difference between Sums of Odd and Even Digits in Python
# Using List Comprehension and Slicing
n = 1212112
digits = list(map(int, str(n)))
odd_sum = sum(digits[1::2])
even_sum = sum(digits[0::2])

if abs(odd_sum - even_sum) == 0:
    print("Yes")
else:
    print("No")