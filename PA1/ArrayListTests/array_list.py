class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        #self.lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.lis = []
        self.order_check = 1

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(0, self.__get_length(self.lis)):
            return_string += str(self.lis[i]) + ", "
        return_string = return_string[:-2]
        return return_string
    # YA

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.order_check = 0
        self.__prepend_func(value)
    # YA

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        self.order_check = 0
        self.__insert_func(value, index)
    # YA

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.order_check = 0
        self.__append_func(value)
    # YA

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.order_check = 0
        leng = self.__get_length(self.lis)
        if index >= leng:
            raise IndexOutOfBounds
        new_lis = [0] * leng
        lis_count = 0
        for i in range(0, leng):
            if i == index:
                new_lis[i] = value
            else:
                new_lis[i] = self.lis[lis_count]
            lis_count += 1
        self.lis = new_lis
    # YA

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.__get_length(self.lis) == 0:
            raise Empty
        else:
            return self.lis[0]
    # YA

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index >= self.__get_length(self.lis):
            raise IndexOutOfBounds
        else:
            return self.lis[index]
    # YA

    #Time complexity: O(1) - constant time
    def get_last(self):
        temp_index = (self.__get_length(self.lis) - 1)
        if self.__get_length(self.lis) == 0:
            raise Empty
        else:
            return self.lis[temp_index]
    # YA

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO klára
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        leng = self.__get_length(self.lis)
        new_lis = [0] * (leng - 1)
        lis_count = 0
        if index >= leng:
            raise IndexOutOfBounds
        for i in range(0, leng):
            if i == index:
                temp_i = i
                lis_count += 1
                break
            else:
                new_lis[i] = self.lis[lis_count]
                lis_count += 1
        for i in range(temp_i, leng - 1):
            new_lis[i] = self.lis[lis_count]
            lis_count += 1
        self.lis = new_lis
    # YA

    #Time complexity: O(1) - constant time
    def clear(self):
        self.lis = []
        self.order_check = 1
    # TODO YA?

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if self.order_check == 0:
            raise NotOrdered
        leng = self.__get_length(self.lis)
        new_lis = [0] * (leng + 1)
        lis_count = 0
        for i in range(0, leng):
            if self.lis[i] <= value:
                if self.lis[i] >= value:
                    self.__insert_func(value, i)
                    return
            else:
                self.__insert_func(value, i)
                return
        self.__append_func(value)
    # YEET

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        leng = self.__get_length(self.lis)
        if self.order_check:
            self.__bin_find()
            pass
        else:
            for i in range(0, leng + 1):
                if i == value:
                    index = i - 1
                    return index
            raise NotFound

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        index = self.find(value)
        self.remove_at(index)
    # TODO Tékka

    def __get_length(self, list):
        count = 0
        for i in self.lis:
            count += 1
        #if count == 0:
        #    raise Empty
        return count

    def __insert_func(self, value, index):
        leng = self.__get_length(self.lis)
        new_lis = [0] * (leng + 1)
        lis_count = 0
        if index >= leng + 1:
            raise IndexOutOfBounds
        for i in range(0, leng + 1):
            if i == index:
                new_lis[i] = value
                break
            new_lis[i] = self.lis[lis_count]
            lis_count += 1
        for i in range(lis_count + 1, leng + 1):
            new_lis[i] = self.lis[lis_count]
            lis_count += 1
        self.lis = new_lis

    def __append_func(self, value):
        leng = self.__get_length(self.lis)
        new_lis = [0] * (leng + 1)
        lis_count = 0
        for i in range(0, leng + 1):
            if i == leng:
                new_lis[i] = value
                break
            new_lis[i] = self.lis[lis_count]
            lis_count += 1
        self.lis = new_lis

    def __prepend_func(self, value):
        leng = self.__get_length(self.lis)
        new_lis = [0] * (leng + 1)
        new_lis[0] = value
        lis_count = 0
        for i in range(1, leng + 1):
            new_lis[i] = self.lis[lis_count]
            lis_count += 1
        self.lis = new_lis

    def __bin_find(self):
        # TODO what
        pass



if __name__ == "__main__":
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    arr_lis = ArrayList()
    print(str(arr_lis))
    print(arr_lis.find(1))


