# Using Modulus and Integer Division
n = 1243
odd_sum = 0
even_sum = 0
flag = True

while n > 0:
    digit = n % 10
    if flag:
        odd_sum += digit
    else:
        even_sum += digit
    flag = not flag
    n //= 10

if abs(odd_sum - even_sum) == 0:
    print("Yes")
else:
    print("No")