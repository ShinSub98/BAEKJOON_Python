from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")

# 스크롤바는 스크롤바와, 그 대상이 되는 위젯을 하나의 프레임에 넣는 것이 편리
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# yscrollcomand~ 가 없으면 스크롤을 내려도 다시 올라온다.
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32): # 1 ~ 31
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

# scrollbar.config를 하지 않으면 스크롤바와 리스트박스가 상호작용하지 않는다.
scrollbar.config(command=listbox.yview)

root.mainloop()