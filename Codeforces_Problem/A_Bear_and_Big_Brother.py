a,b = map(int,input().split())
i = 1
count = 0
while True :
    r1 = a * ( 3**i)
    r2 = b * (2**i)
    i += 1
    count += 1
    if r1 > r2 :
        break 
print(count)

'''
a, b = map(int, input().split())

year = 0

while a <= b:
    a *= 3
    b *= 2
    year += 1

print(year)

'''