from T_ARRAY.TA_Que import Cir_Que
from UTILITY.constance import MY_PROCESS
from UTILITY.static_class import Static

class FCFS(): #GUI를 상속받아야함
    def __init__(self, file):
        self._process = file
        self._Ready_Que = Cir_Que(self._process.getSize())
        self._statics = Static()

    def __call__(self):
        pass

    def get_gantt(self):
        return self._statics.get_gantt_member()
    
    def get_statics(self):
        return self._statics

    def makeReadyQue(self):
        print("Set Ready Que")
        print("EnQueue Operation Start")
        for args in self._process.get_conversion_list():
            itor = 0
            temp = dict(MY_PROCESS)
            print (args)
            for k in MY_PROCESS.keys():
                temp[k] = args[itor]
                itor += 1
            self._Ready_Que.enqueue(temp)
        self._Ready_Que.sort('arrive')
        print("EnQue Operation over")
    
    def processing_FCFS(self):
        self._time = 0
        start = 0
        while(True):
            if self._Ready_Que.isEmpty():
                break

            element = self._Ready_Que.dequeue()
            start = self._time
            print(element)
            arrive_time = element['arrive']

            # 만약 현재 시간보다 도착시간이 뒤라면 현재시간만 증가
            if self._time <= arrive_time:
                while(self._time == arrive_time - 1):
                    self._time += 1

            print(self._time, arrive_time)

            index = element['index']
            # 대기시간
            waiting_time = self._time - arrive_time
            # 실제시간
            self._time += element['burst_time']
            # 최종 시간
            turnarround_time = self._time - arrive_time
            # 기록
            self._statics.set_gantt_member(start, self._time, element['index'])
            self._statics.update_data(index,
                                     self._time, 
                                     turnarround_time,
                                     waiting_time
                                    )

            self._statics()
        return




