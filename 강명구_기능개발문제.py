def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        release = 0
        while progresses:
            if progresses[0] >= 100:
                del progresses[0]
                del speeds[0]
                release += 1
            else:
                break

        if release != 0:
            answer.append(release)

    return answer

samplep1 = [93, 30, 55]
samplep2 = [95, 90, 99, 99, 80, 99]
samples1 = [1, 30, 5]
samples2 = [1, 1, 1, 1, 1, 1]

print(solution(samplep1, samples1))
print(solution(samplep2, samples2))
