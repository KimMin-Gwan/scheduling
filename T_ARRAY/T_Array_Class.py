class T_Array():
    # 초기화
    def __init__(self, capacity = 100):
        self._t_array = [None for i in range(capacity)]
        self._num_element = 0
        self._capacity = capacity

    def __call__(self):
        print("num_element = ", self._num_element)
        print("Capacity = ", self._capacity)
        print(self._t_array)

    # 어레이의 크기를 반환하는 함수
    def getSize(self):
        return self._capacity
    
    def getNumElement(self):
        return self._num_element

    # 비었으면 True를 반환하는 함수
    def empty(self):
        if self._num_element <= 0:
            return True
        else:
            return False

    def get_element(self, index):
        return self._t_array[index]

    
    # 인덱스 확인하는 함수
    def _isValidIndex(self, idx):
        if idx < 0 or idx > self._capacity:
            print("Syntex Errer")
            return False
        else:
            return True
    
    # 어레이에 삽입 하는 함수
    def insert(self, idx, element):
        if self._isValidIndex(idx):
            self._t_array[idx] = element
            self._num_element += 1

    # 어레이에 회수 하는 함수
    def remove(self, idx):
        if self._isValidIndex(idx):
            self._num_element -= 1
            element = self._t_array[idx]
            self._t_array[idx] = None
            return element
        else:
            return None
        
    def sort2(self, arg):
        n = len(self._t_array)
        array = self._t_array
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if array[j][arg] is None:
                    continue

                if array[j][arg] < array[min_idx][arg]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
        self._t_array = array

    def sort(self, arg):
        n = len(self._t_array)
        array = [elem for elem in self._t_array if elem is not None]  # None 값을 제외한 리스트 생성
        array.sort(key=lambda elem: elem[arg])  # key 값으로 arg 인덱스를 사용하여 정렬
        self._t_array = array + [None] * (n - len(array))

    def rebalance(self):
        for i in range(self._capacity-1):
            if self._t_array[i] == None and self._t_array[i+1] == None:
                break
            temp = self._t_array[i+1]
            self._t_array[i] = self._t_array[i+1]
            self._t_array[i+1] = temp





