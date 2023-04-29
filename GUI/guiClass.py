import tkinter as tk
import GUI
from main import main_function

class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.f_main = main_function()

        # GUI 설정
        self.title("My GUI")
        self.geometry("700x700")
        
        self.canvas = tk.Canvas(self, bg="white", height=400, width=600)
        # 기본 메뉴
        self._start_menu()

    def _start_menu(self):
        self.buttons = []
        for button in self.buttons:
            button.pack_forget()
        for i in range(2):
            self.my_button = tk.Button(self,
                                       text=GUI.MENU1[i],
                                       command = lambda index = i: self.button_click1(index))
            self.my_button.pack(pady = 10)
            self.buttons.append(self.my_button)
      
    def button_click1(self, index):
        # MyClass 객체 호출하여 결과를 출력
        print(f"Button {index} clicked. ")
        if index == 0:
            #파일 입력
            self.f_main.getFile()
            # 메뉴 초기화
            self._new_menu()
        else:
            exit()
        
    def _new_menu(self):
        for button in self.buttons:
            button.pack_forget()
        self.buttons = []
        for i in range(5):
            self.my_button = tk.Button(self,
                                    text=GUI.MENU2[i],
                                    command = lambda index = i: self.button_click2(index))
            self.my_button.pack(pady = 10)
            self.buttons.append(self.my_button)

    def button_click2(self, index):
        # MyClass 객체 호출하여 결과를 출력
        print(f"Button {index} clicked. ")
        self.canvas.delete("all")
        if index == 0:
            print("reset")
            self.canvas.delete("all")

        elif index == 1:
            print('FCFS START')
            gantt, static = self.f_main.call_FCFS()
            self.draw_gantt_chart(gantt, static)

        elif index == 2:
            print('SJF START')
            gantt, static = self.f_main.call_SJFS()
            self.draw_gantt_chart(gantt, static)

        elif index == 3:
            print('RR START')
            gantt, static = self.f_main.call_RR()
            self.draw_gantt_chart(gantt, static)

        else:
            exit()

    def draw_gantt_chart(self, task_data, static):
        # 캔버스 생성
        self.canvas.delete("all")

        static_list = static.get_data()

        # 각 task별로 사각형 그리기
        for i, task in enumerate(task_data):
            x1, x2 = task[0]*50 + 50, task[1]*50 + 50
            y1, y2 = i*30+20, i*30+50
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
            self.canvas.create_text(x1, 250, text=str(task[0]), fill="black")
            self.canvas.create_text(x2, 250, text=str(task[1]), fill="black")
            self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=task[2])

        # 데이터 출력
        y_pos = 300
        self.canvas.create_text(90, y_pos, text=f"mean turnaround time: {static_list[0]:.2f}", fill="black")
        y_pos += 30
        self.canvas.create_text(80, y_pos, text=f"mean waiting time: {static_list[1]:.2f}", fill="black")
        y_pos += 30
        self.canvas.create_text(93, y_pos, text=f"number of expired process: {static_list[2]}", fill="black")

        self.canvas.pack()


