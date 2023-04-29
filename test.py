
import tkinter as tk

# 창 생성
root = tk.Tk()
root.title("Gantt Chart")

# 캔버스 생성
canvas = tk.Canvas(root, bg="white", height=200, width=500)
canvas.pack()

# 간트차트 데이터
task_data = [(0, 2, "task1"), (2, 4, "task2"), (4, 6, "task3"), (6, 8, "task4")]

# 각 task별로 사각형 그리기
for i, task in enumerate(task_data):
    x1, x2 = task[0]*50, task[1]*50
    y1, y2 = i*30+20, i*30+50
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
    canvas.create_text((x1+x2)/2, (y1+y2)/2, text=task[2])

# 창 실행
root.mainloop()
