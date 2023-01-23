from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")
# 체크박스: 체크/취소 할 수 있는 위젯

chkvar=IntVar() # chkvar에 "int"타입으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select() # 자동 체크 처리
chkbox.deselect() # 체크 된 체크박스를 체크 해제
chkbox.pack()
# variable에는 체크 데이터를 담을 변수를 작성

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 체크 해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()



root.mainloop()