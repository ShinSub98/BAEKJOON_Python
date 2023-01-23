import tkinter.messagebox as msgbox # 메세지 박스 모듈 로드
from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")
# 팝업창(메세지 박스)

# 기차 예매 시스템
def info():
    msgbox.showinfo(title=None, message="정보") # "팝업창 제목", "팝업창 내용"

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.") # showwarning

def error():
    msgbox.showerror("에러", "잘못된 접근입니다.") # showerror


def okcancel():
    response = msgbox.askokcancel("확인 / 취소", "해당 좌석은 커플석입니다. 예매하시겠습니까?") # askokcancel
    if response == 1:
        print("확인")
    elif response == 0:
        print("취소")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?") #askretrycancel
    # response = 를 사용해 팝업창에서 받은 응답을 저장할 수 있다
    if response == 1: # 재시도
        print("재시도")
    elif response == 0: # 취소
        print("취소")


def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?") # askyesno

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # 네: 저장 후 종료
    # 아니오: 저장하지 않고 종료
    # 취소: 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response) # True(예): 1, False(아니오): 0, None(취소): 그외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")
# askyesnocancel / 팝업창의 제목을 비우고 싶을 때는 (title=None, message="내용")으로 작성

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack() # warn을 사용하면 경고 아이콘이 함께 출력되어 유저에게 에러임을 알림
Button(root, command=error, text="에러").pack() # error를 사용하면 치명적 오류가 있음을 알림
Button(root, command=okcancel, text="확인 취소").pack() # 확인 / 취소 선택지 출력
Button(root, command=retrycancel, text="재시도 취소").pack() # 유저에게 재시도 질문
Button(root, command=yesno, text="예 아니오").pack() # 예 / 아니오 선택지 출력
Button(root, command=yesnocancel, text="예 아니오 취소").pack() # 예 / 아니오 / 취소 선택지 출력

root.mainloop()