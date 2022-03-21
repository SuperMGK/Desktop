start = [8, 0, 6, 5, 2, 4, 7, 3, 1]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

class Node:
    def __init__(self, value, present, goal):
        self.value = value
        self.present = present
        self.goal = goal

def node_maker(start, goal):
    present_nodes = []
    for i in range(len(start)):
        globals()['node{}'.format(i)] = Node(start[i], i, goal.index(start[i]))
        present_nodes.append(globals()['node{}'.format(i)])

    return present_nodes

my_nodes = node_maker(start, goal)
# for i in a:
#     print('해당 노드의 값: ', i.value)
#     print('해당 노드의 현 위치: ', i.present)
#     print('해당 노드의 목표 위치: ', i.goal)

check = []
n = int(len(goal)**(1/2))

for i in my_nodes:
    c = i.value
    check.append(c)


last_node = -1

cnt = 50

print('현재 퍼즐: ', check)
while cnt > 0:
    check = []
    dif = 9999

    for node in my_nodes:
        if node.value == 0:
            if my_nodes.index(node) % n == 0:
                prob = [my_nodes.index(node)+1, my_nodes.index(node)-n, my_nodes.index(node)+n]
                for idx in prob:
                    if idx <= n:
                        if idx != last_node and my_nodes[idx].goal - node.present <= dif:
                            dif = my_nodes[idx].goal - node.present
                print(dif)
                print("라스트 노드를 ", node.present)
                last_node = node.present
                will_zero_position = my_nodes[dif]  # 바꿀 노드
                will_change = node  # 현재 0
                will_zero_position.present = node.present   # 현재 0의 위치를 바꿀 노드의 present 로
                will_change.present = my_nodes[dif].present  # 바꿀 노드의 현재 위치를 현재 0의 present 로
                my_nodes[my_nodes.index(node)] = will_zero_position  # 바꿀 노드를 0의 자리로
                my_nodes[dif] = will_change  # 현재 0을 바꿀 자리로

                for i in my_nodes:
                    c = i.value
                    check.append(c)
                break

            elif my_nodes.index(node) % n == n - 1:
                prob = [my_nodes.index(node) - 1, my_nodes.index(node) - n, my_nodes.index(node) + n]
                for idx in prob:
                    if idx <= n and idx >= 0:
                        if idx != last_node and my_nodes[idx].goal - node.present <= dif:
                            dif = my_nodes[idx].goal - node.present
                print(dif)
                print("라스트 노드를 ", node.present)
                last_node = node.present
                will_zero_position = my_nodes[dif]  # 바꿀 노드
                will_change = node  # 현재 0
                will_zero_position.present = node.present  # 현재 0의 위치를 바꿀 노드의 present 로
                will_change.present = my_nodes[dif].present  # 바꿀 노드의 현재 위치를 현재 0의 present 로
                my_nodes[my_nodes.index(node)] = will_zero_position  # 바꿀 노드를 0의 자리로
                my_nodes[dif] = will_change  # 현재 0을 바꿀 자리로

                for i in my_nodes:
                    c = i.value
                    check.append(c)
                break

            elif my_nodes.index(node) < n:
                prob = [my_nodes.index(node) - 1, my_nodes.index(node) + 1, my_nodes.index(node) - n]
                for idx in prob:
                    if idx <= n and idx >= 0:
                        if idx != last_node and my_nodes[idx].goal - node.present <= dif:
                            dif = my_nodes[idx].goal - node.present
                print(dif)
                print("라스트 노드를 ", node.present)
                last_node = node.present
                will_zero_position = my_nodes[dif]  # 바꿀 노드
                will_change = node  # 현재 0
                will_zero_position.present = node.present  # 현재 0의 위치를 바꿀 노드의 present 로
                will_change.present = my_nodes[dif].present  # 바꿀 노드의 현재 위치를 현재 0의 present 로
                my_nodes[my_nodes.index(node)] = will_zero_position  # 바꿀 노드를 0의 자리로
                my_nodes[dif] = will_change  # 현재 0을 바꿀 자리로

                for i in my_nodes:
                    c = i.value
                    check.append(c)
                break

            elif my_nodes.index(node) >= n * n - n:
                prob = [my_nodes.index(node) - 1, my_nodes.index(node) + 1, my_nodes.index(node) + n]
                for idx in prob:
                    if idx <= n and idx >= 0:
                        if idx != last_node and my_nodes[idx].goal - node.present <= dif:
                            dif = my_nodes[idx].goal - node.present
                print(dif)
                print("라스트 노드를 ", node.present)
                last_node = node.present
                will_zero_position = my_nodes[dif]  # 바꿀 노드
                will_change = node  # 현재 0
                will_zero_position.present = node.present  # 현재 0의 위치를 바꿀 노드의 present 로
                will_change.present = my_nodes[dif].present  # 바꿀 노드의 현재 위치를 현재 0의 present 로
                my_nodes[my_nodes.index(node)] = will_zero_position  # 바꿀 노드를 0의 자리로
                my_nodes[dif] = will_change  # 현재 0을 바꿀 자리로

                for i in my_nodes:
                    c = i.value
                    check.append(c)
                break
            else:
                prob = [my_nodes.index(node) - 1, my_nodes.index(node) + 1, my_nodes.index(node) + 1, my_nodes.index(node) + n]
                for idx in prob:
                    if idx <= n and idx >= 0:
                        if idx != last_node and my_nodes[idx].goal - node.present <= dif:
                            dif = my_nodes[idx].goal - node.present
                print(dif)
                print("라스트 노드를 ", node.present)
                last_node = node.present
                will_zero_position = my_nodes[dif]  # 바꿀 노드
                will_change = node  # 현재 0
                will_zero_position.present = node.present  # 현재 0의 위치를 바꿀 노드의 present 로
                will_change.present = my_nodes[dif].present  # 바꿀 노드의 현재 위치를 현재 0의 present 로
                my_nodes[my_nodes.index(node)] = will_zero_position  # 바꿀 노드를 0의 자리로
                my_nodes[dif] = will_change  # 현재 0을 바꿀 자리로

                for i in my_nodes:
                    c = i.value
                    check.append(c)
                break

    print("현재 퍼즐: ", check)
    print("현재 라스트 노드: ", last_node)
    cnt -=1

# def puzzle_solve(start, goal):
#     my_nodes = node_maker(start, goal)
#     check = []
#     n = int(len(goal)**(1/2))
#
#     for i in my_nodes:
#         c = i.value
#         check.append(c)
#
#     last_node = None
#
#     while not check == goal:
#
#
#         for node in my_nodes:
#             dif = 9999
#
#             if node.value == 0:  # 0을 움직인다
#                 if my_nodes.index(node) % n == 0:  # 노드가 좌변임
#                      # 우, 상, 하로 움직일 수 있다.
#                     prob = [my_nodes.index(node)+1, my_nodes.index(node)-n, my_nodes.index(node)+n] #  우, 상, 하로 이동
#                     for idx in prob:
#                         if my_nodes[idx].goal - my_nodes[node] < dif and last_node !=
#
#                 elif my_nodes.index(node) % n == n - 1:  # 노드가 우변임
#                      # 좌, 상, 하로 움직일 수 있다.
#
#                 elif my_nodes.index(node) < n:  # 노드가 상변임
#                      # 좌, 우, 하로 움직일 수 있다.
#
#                 elif my_nodes.index(node) >= n*n - n:  # 노드가 하변임
#                      # 좌, 우, 상으로 움직일 수 있다.
#
#                 else:  # 노드의 움직임이 자유롭다
#                      # 상, 하, 좌, 우로 움직일 수 있다.






