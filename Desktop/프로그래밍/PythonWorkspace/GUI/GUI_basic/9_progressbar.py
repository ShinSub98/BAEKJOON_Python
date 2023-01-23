import time
import tkinter.ttk as ttk # progress bar는 ttk 필요
from tkinter import *

root = Tk()
root.title("나도 GUI")
root.geometry("640x480")
# progress bar: 진행 정도를 나타내는 바

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # maximum: progress bar의 최대값
# indeterminate: 언제 끝날 지 모르는 작업에 대해서 사용하는 형식. 바가 차오르지 않고 왕복 운동
progressbar.start(10) # 10ms마다 움직임
progressbar.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
# determinate: 차오값르는 보편적인 progress bvr의 형태
progressbar2.start(10)
progressbar2.pack()

def btncmd():
    progressbar.stop() # progress bar의 작동 중지

btn = Button(root, text="중지", command=btncmd)
btn.pack()

###################################################################################

p_var2 = DoubleVar() # 퍼센티지는 소수점으로 반영되는 경우가 많으므로 실수를 반영하는 DoubleVar를 사용했다
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2) # length: 바의 길이 임의로 설정
progressbar3.pack()

def btncmd2():
    for i in range(101): # 0 ~ 100까지의 값
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar3.update() # progress bar가 올라가는 모습을 매번 업데이트 (ui 업데이트)
        print(p_var2.get())

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()


root.mainloop()