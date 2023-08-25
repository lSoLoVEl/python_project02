#รับค่า/ป้อนทางแป้นพิมพ์ ใช้ฟังก์ชั้น input() โดยสิ่งีท่ป้อนทั้งหมดเป็นstring

#ตัวแปร variable เป็น identifier มีหน้าที่เก็บข้อมูลที่เกิดในโปรแกรม ข้อมูลที่เก็บอยุ่ใน RAM
#identifier คือชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป้นไปตามกฎการตั้งชื่อของภาษานั้นๆ
#input('ป้อนรหัสนักศึกษา :')
#input('ป้อนชื่อนักศึกษา :')
#2input('ป้อนปีเกิด :')

std_id = input('ป้อนรหัสนักศึกษา :')
std_name = input('ป้อมชื่อนักศึกษา :')
stdYearBorn = input('ป้อนปีเกิด :')
print('-------------------------------------------')
stdAge = 2023 - int(stdYearBorn) #ต้องแปลงstringเป็น number -> int(), float()
print(f'ยินดีต้อนรับ {std_id} ชื่อ {std_name}')
print(f'คุณเกิดปี {stdYearBorn} อายุ {stdAge}')
print('-------------------------------------------')
print('ยินดีต้อนรับ', str(std_id), 'ชื่อ', str(std_name))   #ใช้ ,
print('คุณเกิดปี',(stdYearBorn), 'อายุ', str(stdAge))
print('-------------------------------------------')
print('ยินดีต้อนรับ'+' '+ str(std_id), 'ชื่อ'+' '+ str(std_name))   #ใช้ +
print('คุณเกิดปี'+' '+ (stdYearBorn), 'อายุ'+' '+ str(stdAge))
print('-------------------------------------------')
print('ยินดีต้อนรับ {0} ชื่อ {1}'.format(std_id,std_name)) #ใช้ เมธอด format
print('คุณเกิดปี {0} อายุ {1}'.format(stdYearBorn,stdAge))
print('-------------------------------------------')
print('ยินดีต้อนรับ %s อายุ %s' %(std_id,std_name))   #ใช้ %
print('คุณเกิดปี %s อายุ %d' %(stdYearBorn,stdAge))