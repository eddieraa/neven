def test():
  a = 0
  while True:
    a += 1
    yield a

a = [test()]

for i in range(int(float("inf"))):print(i)