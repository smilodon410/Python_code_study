grid = [["1", "|", "2", "|", "3"], ["4", "|", "5", "|", "6"], ["7", "|", "8", "|", "9"]]

# 판 출력
for lst in grid:
    for cpn in lst:
        print("%2s" % cpn, end="")
    print()
nlst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 지정 위치 o, x 변경하기
def chngnum(num):
    global n
    if n == 1:
        p1 = "O"
    else:
        p1 = "X"
    if num > 0 and num <= 3:
        grid[0][grid[0].index(str(num))] = p1
    elif num > 3 and num <= 6:
        grid[1][grid[1].index(str(num))] = p1
    else:
        grid[2][grid[2].index(str(num))] = p1


# 승부 결정 함수
# 3가지 경우 ( 가로, 세로, 대각선 )
def decision():
    for i in range(3):
        if grid[0][i * 2] == grid[1][i * 2] == grid[2][i * 2]:
            return grid[0][i * 2]
        if grid[i][0] == grid[i][2] == grid[i][4]:
            return grid[i][0]
    if grid[0][0] == grid[1][2] == grid[2][4] or grid[0][4] == grid[1][2] == grid[2][0]:
        return grid[1][2]


n = 1
while True:
    # 입력값 받기
    inp = input("Player %s - please type a position(available position(s) are " % n + str(
        ",".join(list(map(str, nlst))) + ": "))
    # 예외 처리
    if int(inp) not in nlst:
        print("choose wrong position try another one")
        continue
    # 가능 위치에서 변경하기
    nlst.remove(int(inp))
    # 지정 위치 o, x로 변경하기
    chngnum(int(inp))
    # 표기된 판 보여주기
    for lst in grid:
        for cpn in lst:
            print("%2s" % cpn, end="")
        print()
    # 승부 결정
    if nlst == []:
        print("Draw")
        break
    elif decision() == "O":
        print("Player1 Win!!!")
        break
    elif decision() == "X":
        print("Player2 Win!!!")
        break
    # 플레이어 바꿔주기
    if n == 2:
        n = 1
    else:
        n += 1
