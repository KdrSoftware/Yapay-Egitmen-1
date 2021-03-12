import colorama
from colorama import Fore, Back, Style
veri = open("veri.txt","a")
veri2 = open("veri.txt","r")
veri3 = open("ayarlar.txt","r")
colorama.init()
ilk = veri3.readline()
renkarka = veri3.readline()
if (renkarka=="mavi"):
  print(Back.BLUE)
if (renkarka=="kırmızı"):
  print(Back.RED)
if (renkarka=="yeşil"):
  print(Back.GREEN)

print("Yapay Eğitmene Hoş geldiniz - Kadir Çamuryapan,Şeyma Nur Summak 9/C MZFL")
print("")
girdi = input("İstediğiniz işlemi giriniz : ")
if (girdi=="Kayıt"):
  a = input("Doğrusu : ")
  b = input("Yanlışı  : ")
  c = input("Açıklama : ")
  veri.write(a+ "\n")
  veri.write(b+ "\n")
  veri.write(c+ "\n")
  print("Yuppi yeni bir kelime öğrendim")
  input("Çıkmak için bir tuşa basınız.")
elif (girdi=="Sorgu"):
  dogru = veri2.readline()
  yanlis = veri2.readline()
  konu = veri2.readline()
  a = input("Sorgulamak istediğiniz kelimeyi girin \n ")
  while (dogru!=""):
   if (a in yanlis):
    print("Bu kelimenin doğrusu : " + dogru + "Konu açıklaması ise : " + konu)
    input("Çıkmak için bir tuşa basınız.")
    break
   else:
    dogru = veri2.readline()
    yanlis = veri2.readline()
    konu = veri2.readline()
elif (girdi=="Cümle sorgu"):
  a =input("Sorgulamak istediğiniz cümleyi kelime arasına iki boşluk  koyarak giriniz \n")
  b = a.split("  ")
  dogru = veri2.readline()
  yanlis = veri2.readline()
  y = yanlis.rstrip("\n")
  konu = veri2.readline()
  while (dogru!=""):
   if (y in b):
    print("Yanlış kelime : " +y )
    print("Bu kelimenin doğrusu : " + dogru + "Konu açıklaması ise : " + konu)
    input("Çıkmak için bir tuşa basınız.")
    break
   else:
    dogru = veri2.readline()
    yanlis = veri2.readline()
    konu = veri2.readline()
    y = yanlis.rstrip("\n")
elif (girdi=="Cümle kayıt"):
  a = input("Doğru cümleyi giriniz. \n")
  b = input("Yanlış cümleyi giriniz \n")
  c = a.split("  ")
  d = b.split("  ")
  print (c + d)
  for sayı in range(0,len(d)):
    if (c[sayı] !=  d[sayı]):
      veri.write(c[sayı]+ "\n")
      veri.write(d[sayı]+ "\n")
      veri.write("Oto"+ "\n")
      print(c[sayı] + " Kaydedildi !")
      input("Çıkmak için bir tuşa basınız.")
elif (girdi=="Yardım"):
  input("Kayıt : Kelime kaydı yapar \n Sorgu : Kelime sorgusu yapar \n Cümle sorgu : Cümle içinde hatalı kelime bulur \n Cümle kayıt : Cümleleri kullanrak hatalı kelimeyi bulur.")
elif(girdi=="Yazım kuralları"):
  a = input("Gir :")
  b = []
  son = ["f","s","t","k","ç","ş","h","p"]
  bas = ["b","c","d","g"]
  son1 = ["p","ç","t","k"]
  bas1 = ["a","e","ı","i","u","o","ü","ö"]
  for sayı in range (0,len(a)):
    b.append(a[sayı])
  for sayı in range(0,len(a)):
    if (sayı+1<len(a)):
      c = sayı + 1
      d = sayı
      e = a[d]
      f = a[c]
      if (e in son and f in bas ):
        print("Ünsüz benzeşmesinden kaynaklı yanlış ")
        input("Çıkmak için bir tuşa basınız.")
        break
      elif (e in son1 and f in bas1):
        print("Ünsüz yumuşaması kaynaklı yanlış ")
        input("Çıkmak için bir tuşa basınız.")
        break
else: 
  input("Böyle bir komut bilmiyorum. 'Yardım' komutunu giriniz.")
#Oto renk düzenleme
#Sadece 2 Komutla diğerlerine de ulaşabilme
#Dosya okuyabilme
#Apa Güncellemesi