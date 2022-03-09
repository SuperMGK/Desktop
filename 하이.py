


def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisors.append(i)
            if (i != (n // i)):
                divisors_back.append(n//i)

    division = divisors + divisors_back[::-1]
    answer = []

    head, tail = 0, len(division) - 1

    while head < len(division) / 2:
        one = [division[head], division[tail]]
        answer.append(one)
        head += 1
        tail -= 1

    return answer

def solution(brown, yellow):
    yellow_tiles = []
    division = get_divisor(yellow)

    for div in division:
        if brown - 4 == div[0] * 2 + div[1] * 2:
            yellow_tiles = div

    answer = [yellow_tiles[1] + 2, yellow_tiles[0] + 2]


    return answer

print(solution(24, 24))
print(solution(10, 2))
print(solution(8, 1))