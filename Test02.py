#1. ใช้,
print("hello..",456,'Hi....',True,55+225,"Hey....")
#2. ใช้ + ,มีข้อแม้ว่าทุกตัวที่เอามาต่อกันต้องเป็นString ถ้าไม่ใช่String เอาStr()ไปครอบ
print("hello.."+str(456)+'Hi....'+str(True)+' '+str(55+225)+" Hey....")
#3. ใช้เมธอด format
print("Hello... {} Hi...{} {} Hey...".format(456, True, 55+255))
print("Hello... {0} Hi...{1} {2} Hey...".format(456, True, 55+255)) #index number
#4. ใช้ f-string
print(f"Hello... {456} Hi...{True} {55+225} Hey...")
#5. ใช้ modulas opeator (%) -> %d, %f, %c, %s, %i, .....
print('Hello... %d Hi... %s %d Hey...' %(456,True,55+225)) 
