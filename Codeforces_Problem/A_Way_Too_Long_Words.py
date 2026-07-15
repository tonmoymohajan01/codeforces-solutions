WordNumber = int(input())
for i in range(0,WordNumber):
    user_input = input().lower()
    if len(user_input) > 10 :
        print(f"{user_input[0]}{len(user_input)-2}{user_input[-1]}")
    else:
        print(user_input)