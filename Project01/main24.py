class Apple:
    def __init__(self):
        pass

    def f1(self):
        return self

    def f2(self, a):
        num = a(100)               # f3(group)인수
        return num * 3
def f3(group):
    print(group)                # 100 출력
    return group * 2


a = Apple()
b = a.f1().f2(f3)               # 함수 번호 1번에 return이 반드시 있어야한다
print(b)



