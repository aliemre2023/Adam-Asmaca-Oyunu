print("""
    _______
   |       '
   |       
   |      
   |      
   |      
   |       
___|___

""")

bes = ("""
    _______
   |       '
   |       O
   |      
   |      
   |      
   |       
___|___


""")

dort = ("""
    _______
   |       '
   |       O
   |       |
   |      
   |      
   |       
___|___


""")

uc = ("""
    _______
   |       '
   |       O
   |      /|
   |      
   |      
   |       
___|___


""")

iki = ("""
    _______
   |       '
   |       O
   |      /|)
   |      
   |      
   |       
___|___


""")

bir = ("""
    _______
   |       '
   |       O
   |      /|)
   |      /
   |      
   |       
___|___


""")

sifir = ("""
    _______
   |       '
   |       O
   |      /|)
   |      / )
   |      
   |       
___|___

OYUN BİTTİ
KAYBETTİN KARDEŞİM KB

""")


kelime = input("Kelime giriniz:")

print("_ " * len(kelime))

kelime_harfleri = []
for i in kelime:
    kelime_harfleri.append(i)
    
deneme_hakki= 6


harf_deneme_listesi = []
cikti_listesi = []

while True:
    sorgu = input("\nHarf Deneme: h\nCevap Deneme: c\n -- ")
    print()

    if sorgu == "h" and deneme_hakki != 0:

        harf = input("bir harf giriniz:")
        harf_deneme_listesi.append(harf)

        if harf in kelime_harfleri:
            print("Tebrikler, denemeniz doğru!\nKalan deneme hakkı:",deneme_hakki)
            
        else:
            deneme_hakki -= 1
            print("Maalesef, yanlış deneme.\nKalan deneme hakkı:",deneme_hakki)
        
        for i in kelime:
                if i in harf_deneme_listesi:
                    cikti_listesi.append(i)
                else:
                    cikti_listesi.append("_")
        
        print(cikti_listesi,"\n")
        cikti_listesi = []
    
    elif sorgu == "c" or deneme_hakki == 0:
        tahmin = input("Kelimeyi tahmin edin:")

        if tahmin == kelime:
            print("Tebrikler. Kelimeyi doğru bildiniz.")
        
        else:
            deneme_hakki -= 1
            print("Maalesef, tahmininiz yanlış.\nKalan tahmin hakkınız:",deneme_hakki)

            if deneme_hakki == 0:
                print("Oyunu kaybettiniz. :/")
            else:
                continue
    
    
    if deneme_hakki == 5:
        print(bes)
        bes = " "
    elif deneme_hakki == 4:
        print(dort)
        dort = " "
    elif deneme_hakki == 3:
        print(uc)
        uc = " "
    elif deneme_hakki == 2:
        print(iki)
        iki = " "
    elif deneme_hakki == 1:
        print(bir)
        bir = " "
    elif deneme_hakki == 0:
        print(sifir)
        break
        


