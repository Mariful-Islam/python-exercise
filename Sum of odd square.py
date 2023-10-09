# R-1.4: Write a short python function that takes a positive integer n and return the sum of square of all odd postive integer smaller than n.


num = int(input("Number"))

result = []

for i in range(1, num):
    if i % 2 != 0:
        result.append(i)

print(sum(result))
