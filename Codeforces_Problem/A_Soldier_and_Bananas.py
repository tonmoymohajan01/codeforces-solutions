k,n,w = map(int,input().split())

total = sum(i*k for i in range(1,w+1))

print(max(0,total - n))

