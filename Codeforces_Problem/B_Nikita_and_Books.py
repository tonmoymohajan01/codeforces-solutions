t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    
    for i in range(n - 1):
        if a[i] >= a[i + 1] and a[i] > 1:
            a[i] -= 1
            a[i + 1] += 1