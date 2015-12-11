class BasketballPlayer:

    def __init__(self, firstN, lastN, num):
        self.__firstName = firstN
        self.__lastName = lastN
        self.__number = num


    def get_number(self):
        return self.__number

    def set_number(self, new_num):
        self.__number = new_num

