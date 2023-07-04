import sys
input=sys.stdin.readline

n, m = map(int, input().split(' '))

pocket_id_dict = {}
pocket_name_dict = {}
for i in range(1,n+1):
    pocket = input().rstrip()
    pocket_id_dict[i] = pocket
    pocket_name_dict[pocket] = i


for j in range(m):
    x = input().rstrip()
    if x.isdigit():
        print(pocket_id_dict[int(x)])
    else:
        print(pocket_name_dict[x])