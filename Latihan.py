print("Mencari bilangan terbesar dari 3 buah bilangan\n")

A = int(input("Masukkan Bilangan Pertama: "))
B = int(input("Masukan Bilangan Kedua: "))
C = int(input("Masukan Bilangan Ketiga: "))

if A>B>C:
    print("\nBilangan Pertama adalah Bilangan Terbesar = %s"%A)
elif B>C:
    print("\nBilangan Kedua adalah Bilanga Terbesar = %s"%B)
else:
    print("\nBilangan Ketiga adalah Bilangan Terbsar = %s"%C)