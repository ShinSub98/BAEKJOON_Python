import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog # 파일을 불러오는 모듈
# 2번줄에서 모든 tkinter 모듈을 불러왔지만, filedialog는 서브 모듈이므로
# __all__을 사용해야만 불러올 수 있기 때문에 3번줄과 같이 따로 로드함

root = Tk()
root.title("사진 붙이기")

# 파일 추가
def add_file(): # files 변수에 사용할 이미지들을 저장
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir=r"C:\Users\wjdtj\Desktop\Python Workspace\pygame_project\images")
        # filetypes에서는 선택 가능한 파일 형태를 콤보박스로
        # 보여주며 위의 코드에서는 이를 튜플로 묶어 작성했다.
        # 파일 경로 앞에 r을 붙이면 탈출문자를 무시하여 있는 그대로 인식한다.
    # 사용자가 선택한 파일 목록 표시
    for file in files:
        list_file.insert(END, file) # 마지막 순서에, 파일 경로 표시

# 선택 삭제
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
# lst.reverse()를 하면 해당 리스트의 순서를 영구적으로
# reversed(lst)를 하면 일시적으로만 리스트의 순서를 반전해 사용한다.

# list_file의 idx를 기준으로 삭제하는데, 빠른 idx부터 삭제하면 당겨진 idx의
# 순서 때문에 다른 파일이 삭제되므로 후순위의 idx부터 삭제한다.

# 저장 경로 (폴더에 사용자가 설정한 파일명으로 파일을 저장)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END) # 해당 위젯이 Entry이기 때문에 이렇게 적은 것이고, text였다면 ("0.1", END)로 적어야 한다.
    txt_dest_path.insert(0, folder_selected)

# 시작
def start():
    # 각 옵션들의 값을 확인
    print("가로 넓이: ", cmb_width.get())
    print("간격: ", cmb_space.get())
    print("포맷: ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0: # 하나의 파일도 선택이 안 됐다면?
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")


# 파일 프레임 (파일 추가, 선택, 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5) # ipady: 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

## 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보 박스
opt_width = ["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

## 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

## 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행 상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar() # 진행 정도
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()