def solution(answers):
    supo1_grade, supo2_grade, supo3_grade = 0, 0, 0

    for ans in range(len(answers)):
        if ans % 5 == 0 and answers[ans] == 1:
            supo1_grade += 1

        elif ans % 5 == 1 and answers[ans] == 2:
            supo1_grade += 1

        elif ans % 5 == 2 and answers[ans] == 3:
            supo1_grade += 1

        elif ans % 5 == 3 and answers[ans] == 4:
            supo1_grade += 1

        elif ans % 5 == 4 and answers[ans] == 5:
            supo1_grade += 1

        # 여기까지는 1번 학생

        elif ans % 8 == 0 or ans % 8 == 2 or ans % 8 == 4 or ans % 8 == 6:
            if answers[ans] == 2:
                supo2_grade += 1

        elif ans % 8 == 1 and answers[ans] == 1:
            supo2_grade += 1

        elif ans % 8 == 3 and answers[ans] == 3:
            supo2_grade += 1

        elif ans % 8 == 5 and answers[ans] == 4:
            supo2_grade += 1

        elif ans % 8 == 7 and answers[ans] == 5:
            supo2_grade += 1


        # 여기까지 2번 학생

        if ans % 10 == 0 or ans % 10 == 1:
            if answers[ans] == 3:
                supo3_grade += 1

        elif ans % 10 == 2 or ans % 10 == 3:
            if answers[ans] == 1:
                supo3_grade += 1

        elif ans % 10 == 4 or ans % 10 == 5:
            if answers[ans] == 2:
                supo3_grade += 1

        elif ans % 10 == 6 or ans % 10 == 7:
            if answers[ans] == 4:
                supo3_grade += 1

        elif ans % 10 == 8 or ans % 10 == 9:
            if answers[ans] == 5:
                supo3_grade += 1

        else:
            return False

        # 여기까지 3번 학생


    grades = [supo1_grade, supo2_grade, supo3_grade]
    answer = []
    for idx, grade in enumerate(grades):
        if grade == max(grades):
            answer.append(idx + 1)
    answer.sort()

    return answer

def solution2(answers):
    supo1_grade, supo2_grade, supo3_grade = 0, 0, 0
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for ans in range(len(answers)):
        idx1 = ans % 5
        idx2 = ans % 8
        idx3 = ans % 10

        if answers[ans] == supo1[idx1]:
            supo1_grade += 1

        if answers[ans] == supo2[idx2]:
            supo2_grade += 1

        if answers[ans] == supo3[idx3]:
            supo3_grade += 1

    grades = [supo1_grade, supo2_grade, supo3_grade]
    answer = []
    for idx in range(len(grades)):
        if grades[idx] == max(grades):
            answer.append(idx + 1)

    answer.sort()

    return answer




