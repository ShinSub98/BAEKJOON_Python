import tkinter.ttk as ttk # 콤보박스는 ttk 필요
from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")
# 콤보박스: 클릭하여 목록을 열어서 목록 중 선택하는 위젯

dates = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=dates) # height: 콤보박스를 클릭했을 때 한 번에 보여줄 리스트의 개수
combobox.pack()
combobox.set("카드 결제일") # 최초에 보일 목록 제목 설정
# *여기까지의 상태에서는 박스에 유저가 직접 값을 입력할 수 있음

readonly_combobox = ttk.Combobox(root, height=10, values=dates, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스의 값을 초기에 자동 선택
readonly_combobox.pack()
# 위젯 선언 시 state="readonly"을 작성함으로써 사용자가 임의의 값을 입력할 수 없도록 제한

def btncmd():
    print(combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()