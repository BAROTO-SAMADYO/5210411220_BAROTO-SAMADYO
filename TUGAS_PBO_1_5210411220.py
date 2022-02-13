#tugas 1

# BAROTO SAMADYO
# 5210411220



def luas_lingkaran():

  x = int(input("Inputkan diameter lingkaran : "))

  proses = 3.14 * ((x/2)**2)

  print("Luas dari lingkaran berdiameter",x,"adalah :",proses)
  menu()

def luas_persegi_panjang():

  p = int(input("Inputkan panjang : "))
  l = int(input("Inputkan lebar : "))

  proses = p * l

  print("Luas dari persegi panjang dengan panjang ",p,"dan lebar ",l,"adalah :",proses)
  menu()

def luas_persegi():

  s = int(input("Inputkan sisi persegi : "))

  proses = s**2

  print("Luas dari persegi yang memiliki sisi",s,"adalah :",proses)
  menu()

def luas_jajar_genjang():

  a = int(input("Inputkan alas : "))
  t = int(input("Inputkan tinggi : "))

  proses = a*t

  print("Luas dari jajar genjang yang memiliki alas ",a,"dan tinggi ",t,"adalah :",proses)
  menu()


def menu():
  print(75*"█")
  print(26*"█","APLIKASI PENGHITUNG LUAS",26*"█")
  print(26*"█","    BAROTO SAMADYO   ",26*"█")
  print(75*"█")
  print("█ 1 █ Menghitung luas lingkaran)")
  print("█ 2 █ Menghitung luas persegi panjang")
  print("█ 3 █ Menghitung luas perssegi")
  print("█ 4 █ Menghitung luas jajar genjang")
  print("█ 5 █ Selesai")
  print(75*"█")
  print()
  pilih = int(input('Pilih menu : '))
  print()
  if pilih == 1:
    luas_lingkaran()
  elif pilih == 2:
    luas_persegi_panjang()
  elif pilih == 3:
    luas_persegi()
  elif pilih == 4:
    luas_jajar_genjang()
  elif pilih == 5:
    print("Terima kasih")
  else:
    print("maaf pilihan anda tidak terdapat di menu silahkan coba lagi")
    menu()

menu()
