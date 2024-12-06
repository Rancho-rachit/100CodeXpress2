tests = int(input())

for test in range(tests):

    direction, noOfRotations, supplyBoxes = map(int, input().split())
    supplies = list(map(int, input().split()))

    newList = supplies.copy()
    noOfRotations = noOfRotations % supplyBoxes

    if direction == 0:
        for no in range(supplyBoxes):
            index = no + noOfRotations
            if index > supplyBoxes-1:
                index -= supplyBoxes
            newList[no] = supplies[index]
    elif direction == 1:
        for no in range(supplyBoxes):
            index = no - noOfRotations
            if index < 0:
                index += supplyBoxes
            newList[no] = supplies[index]

    print(*newList)
