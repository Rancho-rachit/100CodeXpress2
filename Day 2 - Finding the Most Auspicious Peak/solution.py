tests = int(input())

for test in range(tests):

    peaks, stamina = input().split()
    peaks_height = list(map(int, input().split()))
    auspiciuos_numbers = list(map(int, input().split()))

    luckiness_score_per_stamina = []

    for no in range(int(stamina)):
        lucky_number = 0

        for peak in range(int(peaks)):
            if peaks_height[peak] % auspiciuos_numbers[no] == 0:
                lucky_number += 1

        luckiness_score_per_stamina.append(lucky_number)

    max = [0 ,  float('inf')]

    for no in range(int(stamina)):
        if luckiness_score_per_stamina[no] > max[0]:
            max[0] = luckiness_score_per_stamina[no]
            max[1] = auspiciuos_numbers[no]
        elif luckiness_score_per_stamina[no] == max[0]:
            if max[1] > auspiciuos_numbers[no]:
                max[1] = auspiciuos_numbers[no]

    print(max[1])
