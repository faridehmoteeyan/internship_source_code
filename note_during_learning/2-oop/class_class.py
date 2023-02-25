#برای پرایوت کردن ورودیمون اولش دوتا__میگذاریم
#__money_have مثلا
class Camputer:

    def __init__(self):
        self.__min_price = 300
    def sell(self):
        print("selling price:{}".format(self.__min_price))
    # to change a var name in all code : rightclick then refactor
    def change_name (self, price, country):
        self.__min_price = price
        print(f"you can find with{self.__min_price} $ in {country}")

a = Camputer()
a.sell()
a.change_name(1, "tivan")

#تغییری ایجاد نمیکنه
a.__min_price = 20
a.sell()