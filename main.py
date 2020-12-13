def Binary(inputfield):
    try:
        val = int(inputfield, 2)
        print('Octal      =  ' + str(oct(val))[2:])
        print('Decimal    =  ' + str(val))
        print('HexaDec    =  ' + str(hex(val))[2:])
    except:
        print("Salah Input")
def Octal(inputfield):
    try:
        val = int(inputfield, 8)
        print('Binary    =  ' + str(bin(val))[2:])
        print('Decimal   =  ' + str(val))
        print('HexaDec   =  ' + str(hex(val))[2:])
    except:
        print("Salah Input")
def Decimal(inputfield):
    try:
        val = int(inputfield)
        print('Binary    =  ' + str(bin(val))[2:])
        print('Octal     =  ' + str(oct(val))[2:])
        print('HexaDec   =  ' + str(hex(val))[2:])
    except:
        print("Salah Input")
def Hexadecimal(inputfield):
    try:
        val = int(inputfield, 16)
        print('Binary   =  ' + str(bin(val))[2:])
        print('Octal    =  ' + str(oct(val))[2:])
        print('Decimal  =  ' + str(val))
    except:
        print("Salah Input")

pilihan = 1
while pilihan != 0:
    print("")
    print("===============================")
    print("1.Input Biner")
    print("2.Input Octal")
    print("3.Input Decimal")
    print("4.Input HexaDecimal")
    print("0.Keluar")
    pilihan = int(input("Masukkan Pilihan [1/2/3/4/0] : "))
    print("===============================")
    if pilihan == 0 :
        break
    elif pilihan == 1:
        inputfield = input("Masukkan Bilangan Biner : ")
        Binary(inputfield)
    elif pilihan == 2:
        inputfield = input("Masukkan Bilangan Octal : ")
        Octal(inputfield)
    elif pilihan == 3:
        inputfield = input("Masukkan Bilangan Decimal : ")
        Decimal(inputfield)
    elif pilihan == 4:
        inputfield = input("Masukkan Bilangan HexaDecimal : ")
        Hexadecimal(inputfield)
    else :
        print("Pilihan Salah")
