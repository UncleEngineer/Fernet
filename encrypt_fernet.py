from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("คีย์สำหรับถอดรหัสคือ: ",key)
print('----------------')
text = 'ที่หมู่บ้านของเรามีนายพลอยู่จำนวน ๘๘๘ คนรับเงินเดือนเดือนละแสนห้า พร้อมรถประจำตำแหน่ง + บัตรเติมน้ำมัน + บ้านพูลวิลล่า'

f = Fernet(key)
message = f.encrypt(text.encode('utf-8'))
print('ข้อความที่เข้ารหัสแล้วคือ: ', message.decode('utf-8'))