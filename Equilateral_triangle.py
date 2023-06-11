"""
input:
    10, 10, 10
output:
    True
    All input numbers are the same and can be equilateral...

input:
    30, 20, 10
output
    False
    All input numbers are not equal and cannot be equilateral...
"""

numbers = []
for _ in range(3):
    numbers.append(int(input("enter anumber :")))
    # [int, int, int]
for indx, item in enumerate(numbers):
    print(f" indx => {indx} , item => {item}")

if numbers[0] != numbers[1] or numbers[0] != numbers[2]:
    print("All input numbers are not equal and cannot be equilateral...")
else:
    print("All input numbers are the same and can be equilateral...")
