s = input().lower()
for i in s :
    if i not in "aeiouy":
        print('.', i, sep ='', end = '')