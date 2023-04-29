from T_ARRAY.TA_Que import Queue
from UTILITY.constance import MY_PROCESS_SJF
from UTILITY.static_class import Static

class SJF(): 
    def __init__(self, file):
        self._process_list = file.get_conversion_list()
        self._process_list = sorted(self._process_list, key = lambda x : x[2])
        print(self._process_list)
        self._Ready_Que = Queue(len(self._process_list))
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
        
    def processing_SJF(self):
        self._time = 0
        index = 0  # 현재 까지 들어온 인덱스
        start = 0
        end = 0
        element = dict(MY_PROCESS_SJF)
        #running_index = -1
        while(True):
            #print(self._time)
            #print("Now Processing :", element)
            if self._time >15 and self._Ready_Que.isEmpty and element['index'] is None:
                break
            if self._time > 20:
                break
            
            #현재 시점과 비교하여 도착한 프로세스를 레디큐에 할당
            if index < len(self._process_list):
                if self._process_list[index][2] <= self._time:
                    self._enReadyQue(index)
                    index += 1

            
            # 초기에 러닝중인 프로세스가 없으면 하나 뽑고
            if element['index'] is None:
                if not self._Ready_Que.isEmpty():
                    element = self._Ready_Que.dequeue()
                    start = self._time
            else:
                if not self._Ready_Que.isEmpty():
                    if element['burst_time'] > self._Ready_Que.glance_output()['burst_time']:
                        end = self._time
                        self._statics.set_gantt_member(start, end, element['index'])
                        self._Ready_Que.enqueue(element)
                        self._Ready_Que.sort('burst_time')
                        element = self._Ready_Que.dequeue()
                        start = end

            #1초 실행
            self._time += 1
            element['remain_time'] -= 1
            
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
        return
