print("""*******************
hesap makinesi programı

İşlemler:

1. Toplama işlemi

2. Çıkarma işlemi

3. Çarpma İşlemi

4. Bölme İşlemi
*******************
""")

a = int( input("Birinci Sayı:"))
b = int( input("İkinci Sayı:"))

işlem = input("İşlemi Giriniz:")

if işlem == "1":
    print("{} ile {} in toplamı {} dır".format(a,b,a+b))

elif işlem == "2":
    print("{} ile {} in farkı {} dır".format(a,b,a-b))

elif işlem == "3":
    print("{} ile {} in çsrpımı {} dır".format(a, b, a * b))

elif işlem == "4":
    print("{} ile {} in bölümü {} dır".format(a,b,a / b))

else:
    print ("Geçersiz İşlem...")








