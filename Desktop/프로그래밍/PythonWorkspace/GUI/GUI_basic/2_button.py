from tkinter import *

root = Tk()
root.title("나도 GUI")

btn1 = Button(root, text="버튼1") # 버튼 생성
btn1.pack() # pack: 해당 기능을 화면에 표시

btn2 = Button(root, padx=5, pady=10, text="버튼22222222222") # padx: 버튼 너비 조절, pady: 버튼 높이 조절
btn2.pack()
# padx, pady는 버튼에 텍스트를 채우고 남을 여백을 결정하므로 텍스트가 길어지면 자동으로 버튼도 길어진다

btn2 = Button(root, padx=10, pady=5, text="버튼2")
btn2.pack()

btn4 = Button(root, width=10, height=3, text="버튼4444444444444")
btn4.pack()
# width, height는 버튼의 절대적 크기를 결정하므로 텍스트가 길면 잘릴 수 있다.

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()
# fg: 폰트 색상, bg: 버튼 배경 색상

# 버튼에 이미지 삽입
photo = PhotoImage(file="gui_basic/img.png") # 이미지 경로를 통해 먼저 이미지를 로드
btn6 = Button(root, image=photo) #image=이미지 변수명
btn6.pack()

# 실제 동작을 넣는 방법
def btncmd(): # 동작할 함수를 초기화
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) # ccommad = 동작할 함수
btn7.pack()



root.mainloop()