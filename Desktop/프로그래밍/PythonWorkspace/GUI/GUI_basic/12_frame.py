from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")
# 프레임: 위젯들을 하나의 테두리로 묶는 것

Label(root, text="메뉴를 선택해주세요").pack(side="top")
# .pack(side = "left / right / top / bottom"): 위젯이나 프레임을 해당 방향 끝으로 이동
Button(root, text="주문하기").pack(side="bottom")



# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)
# relief=" ": 프레임의 형태
# bd= : 프레임의 두께
frame_burger.pack(side="left", fill="both", expand=True)
# fill = "both": 프레임의 높이를 최대로 설정
# expand = True: 프레임의 너비를 최대로 설정
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료") # 프레임에 음료라는 텍스트를 삽입
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop()