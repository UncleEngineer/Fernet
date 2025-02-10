# How to เข้ารหัสเอกสาร "ลับมาก" ด้วย Python?!?

วันนี้ลุงจะมาแนะนำวิธีเข้ารหัสข้อความลับมาก โดยใช้พลังของน้องไภฑ้อนกัน ซึ่ง Python มีไลบรารี่ที่ชื่อว่า cryptography สามารถเข้ารหัสและถอดรหัสได้ ซึ่งเราจะใช้เทคนิคการเข้ารหัสด้วยคลาสที่ชื่อว่า Fernet ซึ่งเป็นการเข้ารหัสแบบ Symmetric Encryption หรือการเข้ารหัสที่ใช้รหัสคีย์เดียวกันในการเข้ารหัสและถอดรหัส

อธิบายขั้นตอนง่ายๆคือ ...สมมติว่า พล.เอก ลุงวิศวกร สอนคำนวณต้องการเก็บจำนวน นายพลที่ประจำการอยู่ในหมู่บ้านแห่งหนึ่งในทะเลทรายบนดาวอังคาร โดยมีข้อความลับมากว่า "ที่หมู่บ้านของเรามีนายพลอยู่จำนวน ๘๘๘ คนรับเงินเดือนเดือนละแสนห้า พร้อมรถประจำตำแหน่ง + บัตรเติมน้ำมัน + บ้านพูลวิลล่า" ...555 สมมติจ้าาาาเพื่อการเรียนรู้นะจ๊ะ

Step 1
> ติดตั้ง package cryptography โดยพิมพ์คำสั่งใน cmd ว่า pip install cryptography
----------------
Step 2
> พิมพ์โค้ดเพื่อ "เข้ารหัส" ตามลุงได้เลย สร้างไฟล์ชื่อ encrypt_fernet.py
#-----Start------
```
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("คีย์สำหรับถอดรหัสคือ: ",key)
print('----------------')
text = 'ที่หมู่บ้านของเรามีนายพลอยู่จำนวน ๘๘๘ คนรับเงินเดือนเดือนละแสนห้า พร้อมรถประจำตำแหน่ง + บัตรเติมน้ำมัน + บ้านพูลวิลล่า'

f = Fernet(key)
message = f.encrypt(text.encode('utf-8'))
print('ข้อความที่เข้ารหัสแล้วคือ: ', message.decode('utf-8'))
```
#-----End------

Step 3
> Run code เราจะได้ output แบบนี้
คีย์สำหรับถอดรหัสคือ:  b'd-yf6gqteo18GAUuESLRlANE4iOL2XJqZibzStnvodc='
----------------
ข้อความที่เข้ารหัสแล้วคือ:  gAAAAABnqhXNIB2d9CqXlmhKlcecsLYupI-csJQH3EJ7uOlpFNecOy7nfH0-t5MVz6dZJ_PRWlnL6wydRjIexXYwqnxCuSoXdAD19_EBsUjjU7T-0vvM89R57qeLxU4ZTkTqPO1VZmoE11C8pQ3HWSAHifEqccLV7Gx2Awl8zvasK5uTMetzGj1aKzrWSZXfZfsGLNviNy4KjQdWu9bqBMTvEYhzEDyZ9sYtKhty5dnkVb5E2P5XeNDLHONmiGg8YtaCto1LkH0-WNQooUE8JEJ4xnzmsoVjT3ux5UoSb5qFzpSn0n4sL9_BnNX69l8_Y_kRRHWdHuWSHVsnk1TclWEb7-i1-NDfRIosqTD7rUUPjZvtSmA5L3t92UNNn0kbogPgJJ_rBAjWYYfjKD7NmCFz7w03qKCHys3oXeGZhKCrrg6_oRRtY3QJmstPTJLGDdYGlkczWArIF22nHtmQJFHAmMiQ-_s_jaiLpyleg-ZYDj-O2TN_49GxC-wrIbhYJKXSfb8j2MbJjC7X3gff-ex2kxkhY5QXbw==

Step 4
> เก็บรหัสที่ได้หลังข้อความ "คีย์สำหรับถอดรหัสคือ:" ไว้ดีๆ มันคือกุญแจสำคัญที่จะใช้ถอดรหัสลับของ "ข้อความลับ" ถ้าใครได้รหัสนี้ไป ข้อความจะถูกเปิดเผยทันที
> ส่วนรหัสลับหลังคำว่า "ข้อความที่เข้ารหัสแล้วคือ: " มันคือข้อความลับที่ถูกเข้ารหัสเป็นที่เรียบร้อย ปริ้นออกมาโชว์นักข่าวได้เลย เขาถอดรหัสไม่ได้แน่นอนถ้าไม่มีคีย์สำหรับถอดรหัส 

Step 5 
> การถอดรหัส ทำได้โดยสร้างไฟล์ decrypt_fernet.py โดยบรรทัด text = และ key = ต้องมีตัว b ติดกับ single quote คล้ายๆของลุง เพื่อแปลงเป็นคลาส bytes ก่อน
```
from cryptography.fernet import Fernet

text = b'gAAAAA......5QXbw==' #ตามรหัสด้านบน
key = b'd-yf6gq......Stnvodc==' #ตามรหัสด้านบน

f = Fernet(key)
message = f.decrypt(text).decode('utf-8')
print(message)
```
Step 6 กด Run ก็จะได้ output ดังนี้
> ที่หมู่บ้านของเรามีนายพลอยู่จำนวน ๘๘๘ คนรับเงินเดือนเดือนละแสนห้า พร้อมรถประจำตำแหน่ง + บัตรเติมน้ำมัน + บ้านพูลวิลล่า

Step 7
> ลุงขอตัวขับรถไปแหล่งกบดานก่อน หนังจบแล้ว แยกย้าย 555555

ปล. ถ้าสนใจอยากเรียนมากกว่านี้ แวะไปดูในเว็บไซต์ลุงได้ มีวิชาสนุกๆให้ฝึกอีกเยอะ หรือสอบถามลุงทาง inbox ได้ ลุงมีนายพล ...เอ้ย ...แอดมินคอยตอบแชทอยู่จ้าาา 555
