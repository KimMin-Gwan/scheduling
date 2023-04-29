from T_ARRAY.TA_Que import Cir_Que
from UTILITY.constance import MY_PROCESS_SJF
from UTILITY.static_class import Static

class RR(): 
    def __init__(self, file):
        self._process_list = file.get_conversion_list()
        self._process_list = sorted(self._process_list, key = lambda x : x[2])
        print(self._process_list)
        self._Ready_Que = Cir_Que(len(self._process_list))
        self._statics = Static()

    def __call__(self):
        pass

    def get_gantt(self):
        return self._statics.get_gantt_member()

    def get_statics(self):
        return self._statics

    def _enReadyQue(self, index):
        print("enReady Queue")
        temp = dict(MY_PROCESS_SJF)
        itor = 0
        for k in MY_PROCESS_SJF.keys():
            if k == 'remain_time':
                temp[k] = self._process_list[index][1]
            else:
                temp[k] = self._process_list[index][itor]
                itor += 1
        self._Ready_Que.enqueue(temp)
        self._Ready_Que.sort('burst_time')

    def _treat_done_proces(self, process):
        arrive_time = process['arrive']
        burst_time = process['burst_time']

        index = process['index']
        # 대기시간
        waiting_time = self._time - arrive_time - burst_time
        # 최종 시간
        turnarround_time = self._time - arrive_time
        # 기록
        self._statics.update_data(index,
                                    self._time, 
                                    turnarround_time,
                                    waiting_time
                                )
        
    def processing_RR(self):
        self._time = 0
        index = 0  # 현재 까지 들어온 인덱스
        start = 0
        end = 0
        count = 0
        max = len(self._process_list)
        element = dict(MY_PROCESS_SJF)
        #running_index = -1
        while(True):

            print(self._time)

            if count >= max:
                break

            if self._time > 20:
                break

            if index < len(self._process_list):
                if self._process_list[index][2] <= self._time:
                    print("Input process Ready :", self._process_list[index])
                    self._enReadyQue(index)
                    index += 1


            # 현재 실행중인 프로세스가 None 일때
            # 다음 프로세스 실행
            if self._Ready_Que.glance_output() is not None :
                if not self._Ready_Que.isEmpty():
                    element = self._Ready_Que.dequeue()
                    start = self._time
                print("Now Processing :", element)

            for i in range(element['time_slice']):
                element['remain_time'] -= 1
                self._time += 1


            # 현재 실행중인 프로세스가 존재할때
            # 프로세스 진행하고, 다음 행동 처리
            if element['index'] is not None:
                # 실행시간이 끝났으면 처리하고 초기화
                if element['remain_time'] <= 0:
                    end = self._time
                    done_element = element
                    print(done_element)
                    self._statics.set_gantt_member(start, end, element['index'])
                    self._treat_done_proces(done_element)
                    element = MY_PROCESS_SJF
                    self._statics()
                    count += 1

                # 만약 다음이 있으면 RR으로 다시 빼주기
                end = self._time
                self._statics.set_gantt_member(start, end, element['index'])
                self._Ready_Que.enqueue(element)
                element = MY_PROCESS_SJF
                start = end
            else:
                self._time += 1

        return
