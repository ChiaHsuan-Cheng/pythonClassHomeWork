inp = int(input('請輸入n，製造乘法表:'))
print("")
print("用if方式寫n*n乘法表")
for i in range(1,inp+1):
    print("")
    for j in range(1,inp+1):
        print(f"{i}*{j}:{i*j}")


print("")
print("用while方式寫n*n乘法表")
print("")
a = 1 
while 1 <= a <= inp:
    b = 1
    while 1 <= b <= inp:
        print(f"{a}*{b}:{a*b}")
        b += 1 
    print(" ")
    a +=1
