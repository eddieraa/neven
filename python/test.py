import time

"""
numbers = [sum(map(int, list(str(time.time()).split(".")[1]))) for i in range(int(1e6))]
print(min(numbers),max(numbers))
for i in range(min(numbers), max(numbers)):
    print(i, ":", numbers.count(i))
"""

print(len(str(2 ** 256)))