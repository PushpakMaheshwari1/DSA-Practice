x = -1324
if x > 0:
    ans = int(str(x)[::-1])
else:
    ans = int(str(x * -1)[::-1]) * -1
        
mi = 2 ** 31 * (-1)
ma = 2 ** 31 - 1
        
if ans < ma or ans > mi:
        print(ans)
