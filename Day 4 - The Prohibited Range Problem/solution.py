n, maxSum, bannedSize = map(int, input().split())
bannedSizes = list(map(int, input().split()))

acceptedSizes = list(range(1, n+1))

for k in range(bannedSize):
    currentSize = bannedSizes[k]
    if currentSize in acceptedSizes:
        acceptedSizes.remove(bannedSizes[k])

maxSize = 0
weightSum = 0

for value in range(len(acceptedSizes)):
    if maxSum > weightSum + acceptedSizes[value]:
        maxSize += 1
        weightSum += acceptedSizes[value]

print(maxSize)
