from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")

# 레이블: 글자/이미지를 보여줄 뿐, 어떤 동작을 하지는 않는다
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png") # 이미지를 레이블로 삽입
label2 = Label(root, image=photo)
label2.pack()

# 버튼을 누르면 레이블 변경
def change(): # 레이블 변경 함수 초기화
    label1.config(text="또 만나요")

    global photo2 # Garbage Collection이 photo2 이미지 변수를 삭제하지 않도록 전역변수(global)로 설정
    # 함수 내에서, 레이블을 이미지로 변경하기 위해서는 해당 이미지를 전역변수로 설정해야 한다.
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2) # label2를 photo2로 변경하도록 명령

btn = Button(root, text="클릭", command=change)
btn.pack()






root.mainloop()