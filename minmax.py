# R-1.3 Write a short python function , minmax(data) that takes a sequence of one or more numbers and return the smallest and largest numbers, in the form of a tuple of length two, Donot use built in function min or max in implementing your solution.

def minmax(data):
    min = data[0]
    max = data[0]
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    return {'min': min, 'max': max}


print(minmax([45, 67, 23, 43, 34, 76, 56, 31, 14, 27, 86, 90]))
