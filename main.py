def teskari_sozlarni_chiqar(matn):
    sozlar = matn.split()
    teskari_sozlar = sozlar[::-1]
    for soz in teskari_sozlar:
        print(soz)

def asosiy_dastur():
    matn = input("Matn kiriting: ")
    print("Teskari so'zlar:")
    teskari_sozlarni_chiqar(matn)

asosiy_dastur()