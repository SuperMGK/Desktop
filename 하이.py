password = '1234'
pass_flag = False

for i in range(5):
    user_id = input("이름을 입력 해 주세요: ")
    user_input = input("비밀번호를 입력 해 주세요: ")
    cnt = 5 - (i + 1)

    if user_input == password:
        print(user_id, '님 환영합니다.')
        pass_flag = True
        break

    else:
        print('잘못 된 비밀번호 입니다. 다시 시도하세요.')

        if cnt > 0:
            print('잔여 시도 횟수는 %s 회 입니다,' %cnt)

if pass_flag == False:
    print('비정상적인 접근입니다.')
