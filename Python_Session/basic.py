# split() 함수의 default는 공백 / 반환형은 list
# num=[1,2,3,4]라는 리스트가 있고, 그 리스트를 num*2 처리하면 각 요소의 값이 2배가 되는게 아니라 그냥 리스트가 2배가 된다.
# list 안에서도 자료형이 숫자형, string 등등 다양할 수 있다.

Today = '20180522Rainy'
#이곳부터 작성
date = Today[:8]
weather = Today[8:]

print(date)
print(weather)

#////////////////////////////////////////

dollars = 1300
#dollars를 통해 won을 계산하는 식
won = dollars*35
#계산한 원화를 출력하는 함수
print(won)

#////////////////////////////////////////

text1 = "내일 8시 깍뚝 ㄱㄱ~"
meeting_time = text1[3:5]

print(meeting_time)

#////////////////////////////////////////

text1 = "유튜브 시청"
text2 = "낮잠자기"
text3 = "밥먹기"
todo_list = []

todo_list.append(text1)
todo_list.append(text2)
todo_list.append(text3)

print(todo_list)
#////////////////////////////////////////
profile_list = ['김멋사', '01012341234', 21]
dic={}
dic['이름']=profile_list[0]
dic['전화번호']=profile_list[1]
dic['나이']=profile_list[2]

print(dic)