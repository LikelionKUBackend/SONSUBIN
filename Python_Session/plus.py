# 파이썬에서는 중괄호 없이 들여쓰기로 대체
# range 함수는 리스트를 반환하는 함수다.
# 파이썬 print end 속성의 default값은 \n이기 때문에, 바꿔주고 싶으면 end 속성값을 변경해주면 된다.


# 클래스 선언시에 괄호 생략은 상관없음
class Bird:
    def bird_say(self):
        say=input("말해봐: ")
        print(say)


def ex1():
    for i in range(1,4):
        print("회원님~!",i,"세트 시작하겠습니다!")
        for j in range(1,11):
            print(j)
            if 7<=j<10:
                print("하나만 더!")
        print()

def ex2():
    for i in range(1,10):
        print("2 *",i,"=",2*i)


def ex3():
    ang=Bird()
    ang.bird_say()

def ex4():
    for i in range(1,5):
        print("*"*i)

ex3()