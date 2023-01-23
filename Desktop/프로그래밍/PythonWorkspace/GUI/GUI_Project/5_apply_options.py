import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image


# 2번줄에서 모든 tkinter 모듈을 불러왔지만, filedialog는 서브 모듈이므로


root = Tk()
root.title("사진 붙이기")

# 파일 추가
def add_file(): # files 변수에 사용할 이미지들을 저장
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir=(r"/Users/shinjeongsub/Desktop"))
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
    elif folder_selected == "C:/":
        msgbox.showinfo("알림", "해당 위치에 대한 권한이 없습니다.")
    # askdirectory()를 사용했을 때, 사용자가 취소를 누르면 is None이 아니라 ""이 입력된다.
    txt_dest_path.delete(0, END) # 해당 위젯이 Entry이기 때문에 이렇게 적은 것이고, text였다면 ("0.1", END)로 적어야 한다.
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합
def merge_image():
    print("가로 넓이: ", cmb_width.get())
    print("간격: ", cmb_space.get())
    print("포맷: ", cmb_format.get())

    try:
        # 가로 넓이
        img_width = cmb_width.get()
        if img_width == "원본 유지":
            img_width = -1  # -1일때는 원본 기준으로
        else:
            img_width = int(img_width) # 문자열 형태로 값을 받기 때문에 int 형태로 바꿔줌

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
                img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower() # PNG, JPG, BMP 값을 받아와 소문자로 변경

        ###################################################################


        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈를 리스트에 넣어 하나씩 처리
        image_sizes = [] # [(width1, height1), (width2, height2), ...]
        if img_width > -1: # 원본 사이즈가 아닐 때
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0]))for x in images]
            # 변경된 가로 크기, (변경된 가로 크기*원래 세로 크기)/원래 가로 크기
        else:
            # 원본 사이즈 사용할 때
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))

        # 최대 넓이, 전체 넓이
        max_width, total_height = max(widths), sum(heights)
        
        # 스케치북
        if img_space > 0: # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images)-1))

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 흰색
        y_offset = 0 # y 위치
        
        for idx, img in enumerate(images):
            # width가 원본이 아닐 때에는 이미지 크기 조정 필요
            if img_width > -1:
                img = img.resize(image_sizes[idx]) # img의 사이즈를 image_sizes에 있는 사이즈로 resize

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) # height값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 # 실제 % 정보 계산
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "나도 포토."+img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name) # 이미지 저장 경로 및 이름 설정
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err: # 존재하지 않는 경로에 대한 에러 출력
        msgbox.showerror("에러", "존재하지 않는 경로입니다.")
# 시작
def start():
    # 각 옵션들의 값을 확인
    # print("가로 넓이: ", cmb_width.get())
    # print("간격: ", cmb_space.get())
    # print("포맷: ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0: # 하나의 파일도 선택이 안 됐다면?
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")

    # 이미지 통합 작업
    merge_image()


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