def login():
    username = (input("Masukkan Username: ").upper())
    i=0
    while True:
        try:
            x = int(input("Please enter a number: "))
            i+=1
            if x == 6969:
                print(username, " Berhasil Login")
                break
            else:
                if i<=3:
                    print("Pin salah, masukkan ulang pin yang benar." + str(i) + "/3")
                elif i>3:
                    exit("Terlalu banyak salah pin")
        except ValueError:
            print("Oops! Pin yang dimasukkan bukan angka.")
