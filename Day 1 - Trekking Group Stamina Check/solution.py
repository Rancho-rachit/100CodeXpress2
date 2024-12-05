import sys
input = sys.stdin.read

data = input().split()

t_case = int(data[0])
index = 1

for t in range(t_case):
    trekkers = int(data[index])
    index += 1

    stamina = list(map(int, data[index:index + trekkers]))
    index += trekkers

    even = 0
    odd = 0

    for s in stamina:
        if s % 2 == 0:
            even += 1
        else:
            odd += 1

    if even > odd:
        print("Yes")
    else:
        print("No")
