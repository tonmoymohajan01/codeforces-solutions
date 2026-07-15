a = input().split('+')
a.sort()
for i,x in enumerate(a):
    if i < len(a)-1:
        print(x,end = "+")
    else:
        print(x,end = " ")
    
#print('+'.join(sorted(input().split('+'))))
'''
a = input().split('+')
a.sort()
print(*a, sep='+')

'''