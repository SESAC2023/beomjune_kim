import sys
input=sys.stdin.readline

n = int(input())

office = {}
names = []
for _ in range(n):
    name, status = input().split()
    office[name] = status

for key, value in office.items():
    if value == "enter":
        names.append(key)

names.sort(reverse=True)
for i in range(len(names)):
    print(names[i])
