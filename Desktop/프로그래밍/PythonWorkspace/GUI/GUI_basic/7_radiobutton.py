from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()
# 이처럼 변수 선언 뒤에 바로 .pack()를 입력해 위젯을 구현할 수 있으나, 변수값을 바꾸기 위해서는 따로 입력해야 함

# 라디오: 여러개의 묶인 선택지 중에서 특정 개수 이내로만 선택 가능한 체크박스

burger_var = IntVar() #int타입으로 값을 저장
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() # 한 선택지를 기본적으로 선택되어 있게 만들 수 있다
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var)
# value에는 선택지에 초기화할 값을 작성

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 라디오 항목 중 선택된 값(위 명령어의 value값)을 반환(출력)
    print(drink_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()