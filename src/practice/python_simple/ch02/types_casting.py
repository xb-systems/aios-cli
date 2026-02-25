s = "23"
n = int(s)          # str -> int
f = float(s)        # str -> float
back = str(n)       # int -> str

print("s:", s, type(s))
print("n:", n, type(n))
print("f:", f, type(f))
print("back:", back, type(back))

# common pitfall
bad = "3.14"
print("float('3.14') =", float(bad))
# int("3.14") would raise ValueError
