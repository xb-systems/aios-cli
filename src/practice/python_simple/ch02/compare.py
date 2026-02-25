# ch02 - comparison and chained comparison

a = 10
b = 20
c = 30

# 1️⃣ 基础比较
print(a < b)      # True
print(a > b)      # False
print(a == 10)    # True
print(a != 5)     # True


# 2️⃣ 链式比较（Python 独有优雅写法）
print(a < b < c)       # True
print(a < b > c)       # False
print(5 < a < 15)      # True


# 等价写法（对比理解）
print((a < b) and (b < c))


# 3️⃣ 字符串比较（按字典序）
print("apple" < "banana")     # True
print("A" < "a")              # True（ASCII 差异）


# 4️⃣ is vs ==
x = 100
y = 100

print(x == y)   # True（值相等）
print(x is y)   # True（小整数缓存）


m = 1000
n = 1000

print(m == n)   # True
print(m is n)   # 很可能是 False


# 5️⃣ None 比较（必须用 is）
value = None

print(value is None)      # 推荐写法
print(value == None)      # 不推荐


# 6️⃣ 布尔值参与比较
print(True == 1)      # True
print(False == 0)     # True