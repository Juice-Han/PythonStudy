import tkinter as tk #대표적인 GUI툴킷인 tkinter
import tkinter.messagebox as tmsg #메세지를 표시해주는 messagebox라는 패키지
import random

def ButtonClicked():
    b = editbox1.get()
    isOk = False

    if len(b) != 4:
            tmsg.showwarning("오류", "네 자릿수의 숫자인지 확인하세요")
    else:
        numberOk = True
        for i in range(4):
            if b[i] < "0" or b[i] > "9":
                tmsg.showwarning("오류", "숫자가 아닙니다")
                numberOk = False
                break
        if numberOk:
            isOk = True
    
    if isOk:
        hit = 0
        for i in range(4):
            if int(b[i]) == a[i]: # b[i]는 문자열이므로 숫자와 비교하기 위해 정수로 바꿔줘야 한다.
                hit += 1
        blow = 0
        for i in range(4):
            for j in range(4):
                if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (int(b[j]) != a[j]):
                    blow += 1
                    break
        if hit == 4 :
            tmsg.showinfo("맞췄다", "축하합니다. 정답입니다")
            root.destroy()
        else:
            historybox.insert(tk.END, b + "\t" + "/ H: " + str(hit) + " B: " + str(blow) + "\n")
    



# 메인 프로그램

# 랜덤 숫자 생성
a = [random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9)]

print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

# 윈도 만들기
root = tk.Tk() #윈도를 조작하는 객체 생성
root.geometry("600x400") #윈도의 크기를 픽셀 단위로 조절해주는 geometry 메서드
root.title("Hit and Blow")

# 라벨 만들기
label1 = tk.Label(root,text="숫자를 입력하세요", font=("Helvetica", 14))
label1.place(x = 20, y = 20) #윈도에 배치해주는 label을 배치해주는 place 메서드

# 텍스트 입력칸 만들기
editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x=100,y=60) #매개변수를 지정해서 입력할 수도 있다.

# 버튼 만들기
button1 = tk.Button(root, text="확 인", font=("Helvetica", 14), command=ButtonClicked) #버튼을 만들고 클릭되었을 때 실행할 함수 연결
button1.place(x=180, y=65)

# 이력 표시 텍스트 상자 만들기
historybox = tk.Text(root, font=("Helvetica", 14))
historybox.place(x=300,y=0,width=300,height=400)

# 윈도에 표시하기
root.mainloop() #윈도를 화면에 보여주는 메서드 실행