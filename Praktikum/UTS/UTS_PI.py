import time
import os
from loginFunct import login
from recFunct import gpuRec

needDict = {
    1 : "Browsing",
    2 : "Gaming Ringan",
    3 : "Gaming Berat",
    4 : "Mini PC",
    5 : "Kerja",
    6 : "Sekolah",
    7 : "Video Editing"
}

login()
time.sleep(2)
print(needDict)
while y=='y' or y=='Y':
    x = int(input("Masukkan Kebutuhan anda: "))
    gpuRec(int(x))
    if x>0 and x<=7:
        y = str(input("Ingin menggunakan program lagi? Y/y\n"))
        os.system('cls')
    else:
        print("Input salah, mohon coba lagi dengan input yang sesuai")
        time.sleep(2)
        os.system('cls')
        y='y'
