class Student:

    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []

    def add(self,grade):
        self.grades.append(grade)

    def avg(self):
        return sum(self.grades)/len(self.grades)

    def fcount(self):
        i=0
        for p in self.grades:
                if p < 60:
                    i+=1
        return i
                
                
       
    def __str__(self):
        return f"Name:{self.name} Avg:{self.avg()} 不及格:{self.fcount()}"

    @classmethod
    def top(cls, *students):
        set1={0}
        for s in students:    
            set1.add(s.avg())
        for s in students:    
            if s.avg()== max(set1):
                return s
        
                
                


    
s1 = Student("Tom","M")
s2 = Student("Jane","F")
s3 = Student("John","M")
s4 = Student("Ann","F")
s5 = Student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)


print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

tops = Student.top(s1,s2,s3,s4,s5)
print(f"最高分的同學:{tops.name} 平均分數:{tops.avg()}")
