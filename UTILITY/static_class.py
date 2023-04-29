from typing import Any


class Static():
    def __init__(self):
        self._mean_turnarround_time = 0
        self._mean_waiting_time = 0
        self._turnarround_time = []
        self._waiting_time = []
        self._num_expired = 0
        self._now_time = 0
        self._ordinary = []
        self._gantt = []

    def get_data(self):
        temp = [self._mean_turnarround_time,
                self._mean_waiting_time,
                self._num_expired
                ]
        return temp
    
    def __call__(self):
        print("mean turnaround time : ", self._mean_turnarround_time)
        print("mean waiting time : ", self._mean_waiting_time)
        print("Now turnarround_time : ", self._turnarround_time )
        print("Now waiting time : ", self._waiting_time)
        print("number of expired process : ", self._num_expired)
        print("now time : ", self._now_time)
        print("ordinary : ", self._ordinary)
        
    def update_data(self, index, time, turnarround_time, waiting_time):
        self._num_expired += 1
        self._ordinary.append(index)
        self._now_time = time
        self._turnarround_time.append(turnarround_time)
        self._waiting_time.append(waiting_time)
        self._mean_turnarround_time = self._get_mean(self._turnarround_time)
        self._mean_waiting_time = self._get_mean(self._waiting_time)

    def _get_mean(self, array):
        time_sum = sum(array)
        mean = time_sum / self._num_expired
        return mean

    def get_turnarround_time(self):
        print(self._turnarround_time)
        return self._turnarround_time

    def get_waiting_time(self):
        print(self._waiting_time)
        return self._waiting_time
    
    def get_gantt_member(self):
        print(self._gantt)
        return self._gantt
    
    def set_gantt_member(self, start, end, index):
        member = (start, end, index)
        self._gantt.append(member)




    