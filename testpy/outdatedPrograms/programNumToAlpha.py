def alpha(num):
    lo = {
        1:"a",
        2:"b",
        3:"c",
        4:"d",
        5:"e",
        6:"f",
        7:"g",
        8:"h",
        9:"i"
    }
    return "".join(map(lambda x:lo[int(x)],str(num)))
print(alpha(3456))