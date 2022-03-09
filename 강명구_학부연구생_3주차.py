import numpy as np

sample_board = [[0,0,0,0,0],
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    board = np.array(board)
    my_space = [0]  # 뽑기로 뽑아온 인형을 저장하는 공간
    bang = []  # 짝이 맞아서 터진 인형

    for move in moves:
        tmp = 0  # 인덱싱을 하기 위한 변수 초기화
        for space in board[:, move - 1]:
            if space != 0: # 빈 공간은 지나침
                board[tmp, move - 1] = 0  # board 에서 인형을 뽑고 해당 자리를 0으로 바꿈
                if space == my_space[-1]:  # 제일 최근에 뽑은 인형과 현재 뽑은 인형이 같을 시 bang 에 추가
                    bang.append(space)
                    my_space.pop()  # 제일 최근에 뽑은 인형을 my_space 에서 제거
                    break
                else:
                    my_space.append(space)  # 제일 최근에 뽑은 인형과 현재 인형이 다르면 my_space 에 추가
                    break

            else:
                tmp += 1  # 인덱싱



    return len(bang) * 2

print(solution(sample_board, moves))

