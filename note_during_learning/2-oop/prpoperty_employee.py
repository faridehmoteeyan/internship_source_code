class Employees:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first+"."+self.last+"@poyamail.com"

    def full_name(self):
        return self.first + self.last
    @property
    def dot(self):
       a = self.full_name() + "  welcome"
       self.last = "gggg"
       return a

    def dell(self, name):
        first , last = name.split(" ")
        self.first = first
        self.last = last
    def changename(self, last):
        self.last = last



emp = Employees("lina", "loyee")
print(emp.last)
print(emp.email)
emp.last = "fathi"
#کاربرد دیگر @پراپرتی اینه که اگر در اتربیوت متغیری باشه که مقدارش به متغییری که ما تغییر میدیم
print(emp.email)
#یا راه ساده تر کردن اینه که فانکشن ایمیل رو در قالب defبیاریم
#if we dont use @property we cant use it like attretebute,we shuld use print(emp.dot()
print(emp.dot)


print("property".center(100,"-"))
# در کل پراپرتی ابزاریه که یک تابع ،اتربیوت بشه
emp = Employees("lina", "loyee")
emp.changename("shafiyeean")
print(emp.full_name(),emp.dot,emp.full_name())

print("setter".center(100,"-"))
empo = Employees("saba","edrisi")
empo.dell("sima sarlak")
print(empo.last )
print(empo.email )
print(empo.dot )