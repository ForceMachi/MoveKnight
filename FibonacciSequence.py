# The fibonacci sequence


n = int(input())
f1, f2 = 1, 1

for i in range(n):
    print(f1, end=' ')
    f1, f2 = f2, f1 + f2
