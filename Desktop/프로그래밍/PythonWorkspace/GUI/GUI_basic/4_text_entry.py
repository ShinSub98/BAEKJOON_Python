from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5) # 유저가 적을 수 있는 텍스트 위젯 생성
txt.pack()

txt.insert(END, "글자를 입력하세요") # 텍스트 위젯에 기본값 입력


e = Entry(root, width=30) # 엔트리에서는 한줄로만 입력 가능(엔터 불가)
e.pack()
e.insert(0, "한 줄만 입력해요") # 엔트리 위젯에 기본값 입력 / 현재는 위젯이 비어있으므로 0 대신 END를 쓸 수 있음

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # "1.0"은 첫번째 줄 0번째 글자부터, 텍스트의 마지막(END)까지 가져오라는 뜻
    print(e.get()) # 엔트리는 괄호에 따로 안 적어도 됨

    # 위젯에 입력된 텍스트 삭제
    txt.delete("1.0", END) 
    e.delete(0, END) # e 엔트리를 초기화 할 때 0을 입력했으므로 똑같이 0을 입력

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


# Text와 Entry는 줄바꿈 가능 여부의 차이

root.mainloop()