class Zoo:
    #برای همه ابجکتیو هاست
    num = 0
    def __init__(self, name, high):
        #حتمی زو رو اولش باید اورد
        Zoo.num = Zoo.num +1
        self.name = name
        self.high = high
    def dimention(self):
        return   self.high *2
    def naming (self):
        return "this animal is %s" %self.name
    def count_zoo(self):
        return f'animals number {Zoo.num}'
#ارث بری
class   Zoo_Food(Zoo):
    #البته میتونیم این بخش تعریف متغییر رو کلا نذاریم
    #دابل تب خودش پر میکنه
    def __init__(self,name,high,color):
        #حتمی سوپر استفاده شود تا مشخص شود چه چیزهایی ارث برده میشودُ
        super(Zoo_Food, self).__init__(name,high)
        #چیزهای مخصوص این کلاس
        self.color = color
    def food_amount(self):
        #میتونیم پایین بهش ورودی اضافه کنیم.مثلا لنگف در اینجا
        return 1 + 2*self.high + self.length
    def colory(self):
        print(f"{self.name} is {self.color} ")

zeb = Zoo("zebra", 10)
print(zeb.dimention())
lion = Zoo_Food("lion",20,"red")
lion.naming()
lion.colory()
lion.length = 6
print(lion.food_amount())
#نمیشود سه تا وروردی(اسم،اعرض و ارتفاع داد)فقط از مادر یعنی دو ورودی طبعیت میکنه
dog = Zoo_Food("dog",3,"yellow")
print(lion.count_zoo(),dog.count_zoo())

#میتونیم ویژگی ها رو تغییر بدیم
zeb.high = 9
print(zeb.dimention())
Zoo.num = 6
print(lion.count_zoo(),dog.count_zoo())


