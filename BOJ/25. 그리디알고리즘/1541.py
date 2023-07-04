str = input()

str = str.split('-')
ans = 0
tmp = []
if len(str) > 1:
    tmp = str[0].split('+')
    ans += sum(int(x) for x in tmp)
    for i in str[1:]:
        if '+' in i:
            i = i.split('+')
            ans -= sum(int(x) for x in i)
        else:
            i = i.split('-')
            ans -= int(i[0])
    print(ans)
else:
    str = str[0].split('+')
    ans += sum(int(x) for x in str)
    print(ans)