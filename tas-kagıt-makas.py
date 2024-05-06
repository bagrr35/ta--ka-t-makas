import time
import random

# Kodunuzu buraya yazınız
o = 0
b = 0

while True:
    a = input("Birini seçiniz taş / kağıt / makas :")
    if a == "taş" or a == "kağıt" or a == "makas": 
        print("taş, kağıt, makas")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        
        bs = random.randint(1,3)
        if bs == 1:
            bs = "taş"
        elif bs == "2":
            bs = "kağıt"
        else: 
            bs = "makas"

        print("Bilgisayarın seçimi:" , bs)
        if bs == a:
            print("Berabere")
        elif a == "taş" and bs == "makas":
            print("Sen Kazandın")
            o = o + 1   
        elif a == "kağıt" and bs == "taş" :
            print("Sen Kazandın!")
            o = o + 1
        elif a == "makas" and bs == "kağıt" :
            print("Sen Kazandın")
            o = o + 1
        
        elif bs == "taş" and a == "makas":
            print("Kaybettin")
            b = b + 1
            
        elif bs == "kağıt" and a == "taş":
            print("Kaybettin")
            b = b + 1
            
        elif bs == "makas" and a == "kağıt":
            print("Kaybettin")
            b = b + 1
            
        print('Şu anki puan durumu: Sen:', o, ', Bilgisayar:', b)
        
    else:
        print("Böyle bir seçenek yok!")
