import os
from tkinter import *

root = Tk()
root.title("제목 없음 - 메모장")
root.geometry("640x480")

menu = Menu(root) # 메뉴 활성화

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일이 존재하면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))
    


menu_file = Menu(menu, tearoff=0) # 메뉴 선언
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file) # 파일 메뉴 구현

menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit) # 편집 메뉴 구현

menu_style = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_style)

menu_look = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_look)

menu_advice = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_advice)

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트 박스
txt = Text(root, yscrollcommand=scrollbar.set) # 스크롤바와 맵핑
txt.pack(fill="both", expand=True)


scrollbar.config(command=txt.yview) # 텍스트박스와 매핑
root.config(menu=menu) # 실질적으로 메뉴 삽입
root.mainloop()