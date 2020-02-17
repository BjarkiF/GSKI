class ArrayFull(Exception):
    pass

class ArrayDeque():
    def __init__(self):
        self.__cap = 8
        self.array = [0] * self.__cap
        self.__f_ind = 0
        self.__r_ind = 0
        self.__empty = True

    def __str__(self):
        return_string = ''
        if self.__r_ind >= self.__f_ind:
            for i in range(self.__f_ind, self.__r_ind):
                return_string += str(self.array[i]) + ' '
        else:
            for i in range (self.__f_ind, self.__cap):
                return_string += str(self.array[i]) + ' '
            for i in range (0, self.__r_ind):
                return_string += str(self.array[i]) + ' '
        return return_string[:-1]

    def push_back(self, value):
        if (self.__r_ind == self.__f_ind and self.__empty == False or
            self.__r_ind == self.__cap
        ):
            raise ArrayFull
        self.array[self.__r_ind] = value
        self.__r_ind += 1
        if self.__r_ind == self.__cap:
            self.__r_ind = 0
        self.__empty = False

    def push_front(self, value):
        if (self.__r_ind == self.__f_ind and self.__empty == False or
            self.__r_ind == self.__cap
        ):
            raise ArrayFull
        temp_arr = [0] * self.__cap
        for i in range(self.__f_ind, self.__r_ind):
            temp_arr[i+1] = self.array[i]
        if self.__f_ind == 0:
            temp_arr[0] = value
        else:
            temp_arr[self.__f_ind] = value
        self.array = temp_arr
        self.__r_ind += 1
        if self.__r_ind == self.__cap:
            self.__r_ind = 0
        self.__empty = False

    def pop_back(self):
        if self.__empty:
            return None
        self.__r_ind -= 1
        if self.__r_ind < 0:
            self.__r_ind = self.__cap - 1
        value = self.array[self.__r_ind]
        self.array[self.__r_ind] = 0
        if self.__r_ind == self.__f_ind:
            self.__empty = True
        return value

    def pop_front(self):
        if self.__empty:
            return None
        value = self.array[self.__f_ind]
        self.array[self.__f_ind] = 0
        self.__f_ind += 1
        if self.__f_ind == self.__cap:
            self.__f_ind = 0
        if self.__r_ind == self.__f_ind:
            self.__empty = True
        return value

    def get_size(self):
        if self.__r_ind >= self.__f_ind:
            size = self.__r_ind - self.__f_ind
        else:
            size = (self.__cap - self.__f_ind) + self.__r_ind
        return size

    def print_raw(self):
        print(self.array)
