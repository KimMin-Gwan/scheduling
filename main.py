## 설명 : 다양한 방식의 스케줄러를 만들어 볼것이다.
## 상세 : FCFS방식, RR 방식, FJS 방식, 자작으로 만든 방식 총 4개를 만든다.
## 
## 총 4개의 패키지가 필요하다.
## 하나의 메인문에서 실행한다.
## 인터페이스를 출력하기 위한 UI.py를 만든다. (ticker를 사용한다)
## 간단한 연산이나 파일 입출력을 담당할 utils.py를 만든다.

import GUI
import T_ARRAY 
import UTILITY as UT
from UTILITY.constance import FILE_FATH, FILE_NAME, MY_PROCESS
import SCHEDULER as SCH

class main_function():
    def __init__(self):
        print('Main Start')

    def getFile(self):
        self._file = open(FILE_FATH+FILE_NAME, "r")
        self._processer_data = UT.FileInput(self._file)
        #processer_data()
        return
    
    def call_FCFS(self):
        self.fcfs = SCH.FCFS(self._processer_data)
        self.fcfs.makeReadyQue()
        self.fcfs.processing_FCFS()
        self.fcfs()
        member = self.fcfs.get_gantt()
        static = self.fcfs.get_statics()
        return member, static

    def call_SJFS(self):
        self.sjfs = SCH.SJF(self._processer_data)
        self.sjfs.processing_SJF()
        member = self.sjfs.get_gantt()
        static = self.sjfs.get_statics()
        return member, static

    def call_RR(self):
        self.rr= SCH.RR(self._processer_data)
        self.rr.processing_RR()
        member = self.rr.get_gantt()
        static = self.rr.get_statics()
        return member, static




def main():
    gui = GUI.MyGUI()
    gui.mainloop()


if __name__ == "__main__":
    main()