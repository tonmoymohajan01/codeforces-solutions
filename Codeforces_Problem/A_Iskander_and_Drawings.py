t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    
    import math
    
    mx = max(s.split("*"), key=len)
    print(math.ceil(len(mx) / 2))

    