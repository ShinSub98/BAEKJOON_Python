from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다.")

menu  = Menu(root) # 메뉴 기능 활성화

# 메뉴
menu_file = Menu(menu, tearoff=0) # 메뉴 선언
menu_file.add_command(label="New File", command=create_new_file) # label=메뉴 이름, command=명령어
menu_file.add_command(label="New Window")
menu_file.add_separator() # 메뉴 내부 구분선
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # disable: 비활성화(클릭 불가)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) #root.quit: 프로그램 종료
menu.add_cascade(label="File", menu=menu_file) # 메뉴 구현

# 빈 메뉴
menu.add_cascade(label="Eidt")

# Radiobutton 메뉴
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# 체크박스 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show Breadcrumbs")
menu_view.add_checkbutton(label="Render Whitespace")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu) # 메뉴 활성화에 필요
root.mainloop()