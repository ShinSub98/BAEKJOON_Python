from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")
# 리스트 박스: 여러 줄에 걸쳐 목록을 관리하는 위젯

listbox = Listbox(root, selectmode="extended", height=0) # height를 0으로 설정하면 리스트 내 모든 데이터를 출력, n을 적으면 n개의 데이터만 출력
listbox.insert(0, "사과") # 앞의 숫자는 데이터를 입력할 인덱스를 의미
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # END를 입력하면 가장 뒤 인덱스에 데이터 입력
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END)
    # 리스트 내 마지막(END) 데이터를 삭제, n번째 데이터를 지우고 싶다면 n 입력

    # 리스트 내 데이터 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx ~ 끝 idx)
    # print("1번째부터 3번째 까지의 항목: ", listbox.get(0,2))
    # 0~2번째의 데이터를 모두 출력

    # 선택된 항목 확인 (위치(idx값)를 반환)
    print("선택된 항목의 위치: ", listbox.curselection())



btn = Button(root, text="클릭", command=btncmd)
btn.pack()



root.mainloop()