import random

def random_List(size):
    random.seed(1)
    result = []
    for v in range(100):
        result.append(random.randint(1, size))

    return result



def solution(N, stages):
    stages.sort()
    line = len(stages)
    cnt = 1
    dic = {}
    st_num = 1
    for i in range(len(stages)):
        if st_num < stages[i]:
            dic[st_num] = 0
            st_num += 1

        if stages[i] == stages[-1]:
            if stages[i] == N + 1:
                break

            else:
                fail_ratio = round((len(stages) - i) / line, 5)
                dic[stages[i]] = fail_ratio
                break

        if stages[i] == stages[i + 1]:
            cnt += 1
            continue

        else:
            fail_ratio = round(cnt / line, 5)
            line -= cnt
            cnt = 1
            dic[stages[i]] = fail_ratio
            st_num += 1

    sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    answer = []

    for k in sorted_dict:
        answer.append(k[0])

    return answer

"""
실패, 사이즈가 클수록 정확도가 급격히 떨어지나본데 이유를 모르겠음
"""

def solution2(N, stages):
    dic = {}
    answer = []
    line = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)
        if cnt == 0:
            dic[i] = 0

        else:
            dic[i] = round(cnt / line, 5)
            line -= cnt

    sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse=True)

    for k in sorted_dict:
        answer.append(k[0])

    return answer


print(solution(100, random_List(100)))
print(solution2(100, random_List(100)))
print(solution(100, random_List(100)) == solution2(100, random_List(100)))

# for i in range(1, 100):
#     # print(solution(i, random_List(i)))
#     # print(solution2(i, random_List(i)))
#     print(solution(i, random_List(i)) == solution2(i, random_List(i)))


