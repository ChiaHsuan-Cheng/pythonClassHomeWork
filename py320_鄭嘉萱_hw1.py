#Q1
print('''Q1:
1.數學及格但英文不及格
2.數學不及格但英文及格的名單
3.兩科都及格的名單
4.全班總共有幾個同學\n''')
math= set()
clas= set()
eng=set()

math = {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}
eng = {"John", "Mary" ,"Tony" , "Bob" , "Pony", "Tom" , "Alice"}
clas= {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy","John", "Mary" ,"Tony" , "Bob" , "Pony", "Tom" , "Alice"}


print("數學及格但英文不及格名單:",math - eng)
print("數學不及格但英文及格名單:",eng - math)
print("兩科都及格:",eng & math)
print("全班總共有幾個同學:",len(clas))

#Q2
print('''Q2:
Tom 作業成績為 80, 100, 90, 95，John 作業成績為 100,93,75,80
請分別算出兩位同學的平均分數並且印出''')

name=["Tom","John"]
grades = [[80, 100, 90, 95], [100,93,75,80]]

student = {name[i]:grades[i] for i in range(len(name))}
print(student)
 

for name,grades in student.items():
     print(name, sum(grades)/len(grades))
