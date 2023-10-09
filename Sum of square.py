# R-1.4: Write a short python function that takes a positive integer n and return the sum of square of all postive integer smaller than n.

n = int(input("Enter Positive Number:"))

res = []
res_sq = []

for i in range(1, n):
    res.append(i)
    res_sq.append(pow(i, 2))


print("Sum", sum(res))
print("Sum of square", sum(res_sq))
