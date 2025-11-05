class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        h=(self.__hour+other.__hour) % 24
        m=self.__minute+other.__minute
        s=self.__second+other.__second

        if s>=60:
            s %= 60
            m += 1
        if m>=60:
            m %= 60
            h += 1
        return Time(h,m,s)
    def __str__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
    
t1=Time(10,47,25)
t2=Time(11,11,11)
t=t1+t2
print("First time: ",t1)
print("Second time: ",t2)
print("Sum: ",t)
        