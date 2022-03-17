def solution(s):
    bang = []
    for i in s:
        if len(bang) == 0:
            bang.append(i)

        else:
            if i == bang[-1]:
                bang.pop()

            else:
                bang.append(i)

    answer = 1 if len(bang) == 0 else 0

    return answer

print(solution('baabaa'))

