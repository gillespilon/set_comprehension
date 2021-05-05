#! /usr/bin/env python3
'''
Create a set of values greater than the mean from another set.
'''

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers_mean = sum(numbers) / len(numbers)
print(numbers_mean)
result = {number for number in numbers if number > numbers_mean}
print(result)
