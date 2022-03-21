import random
import time

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
            continue

        if stages[i] == stages[-1]:
            if stages[i] == N + 1:
                break

            else:
                fail_ratio = len(stages) - i / line
                dic[stages[i]] = fail_ratio
                break

        if stages[i] == stages[i + 1]:
            cnt += 1
            continue

        else:
            fail_ratio = cnt / line
            line -= cnt
            cnt = 1
            dic[stages[i]] = fail_ratio
            st_num += 1

    for i in range(1, N + 1):
        if i in dic.keys():
            continue

        else:
            dic[i] = 0

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
            dic[i] = cnt / line
            line -= cnt

    sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse=True)

    for k in sorted_dict:
        answer.append(k[0])

    return answer


def solution3(N, stages):
    cnt = [0] * (N + 1)
    for i in stages:
        cnt[i - 1] += 1

    line = len(stages)
    dic = {}

    for i in range(len(cnt) - 1):
        if cnt[i] == 0:
            dic[i + 1] = 0

        else:
            fail_ratio = cnt[i] / line
            line -= cnt[i]
            dic[i + 1] = fail_ratio

    sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse=True)

    answer = []
    for k in sorted_dict:
        answer.append(k[0])

    return answer
# time1 = time.time()
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution2(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution3(5, [2, 1, 2, 6, 2, 4, 3, 3]))
#
# print(solution(4, [4, 4, 4, 4, 4]))
# print(solution2(4, [4, 4, 4, 4, 4]))
# print(solution3(4, [4, 4, 4, 4, 4]))

# for i in range(1, 5000):
#     solution3(i, random_List(i))
    # print(solution2(i, random_List(i)))
    # print(solution2(i, random_List(i)) == solution3(i, random_List(i)))
# time2 = time.time()

# print(time2 - time1)

print(solution2(3, [1, 1, 1]))
print(solution3(3, [1, 1, 1]))

print(solution2(1, [2]))
print(solution3(1, [2]))

print(solution2(5, [2, 2, 2, 3, 3, 3, 4, 4, 4]))
print(solution3(5, [2, 2, 2, 3, 3, 3, 4, 4, 4]))