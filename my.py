import math

def ildiz():
    son = float(input("Son kiriting: "))
    if son >= 0:
        print("Kvadrat ildiz:", math.sqrt(son))
    else:
        print("Manfiy sonning haqiqiy ildizi yo'q")

def faktorial():
    son = int(input("Son kiriting: "))
    if son >= 0:
        print("Faktorial:", math.factorial(son))
    else:
        print("Manfiy son uchun faktorial yo'q")

def perimetr_tortburchak():
    a = float(input("Uzunlik: "))
    b = float(input("Kenglik: "))
    print("Perimetri:", 2 * (a + b))

def yuza_tortburchak():
    a = float(input("Uzunlik: "))
    b = float(input("Kenglik: "))
    print("Yuzasi:", a * b)

def yuza_aylana():
    r = float(input("Radius: "))
    print("Yuzasi:", math.pi * r ** 2)

def perimetr_aylana():
    r = float(input("Radius: "))
    print("Uzunligi:", 2 * math.pi * r)

def pifagor():
    a = float(input("a katet: "))
    b = float(input("b katet: "))
    c = math.sqrt(a**2 + b**2)
    print("Gipotenuza:", c)

def foiz_hisobla():
    son = float(input("Asosiy son: "))
    foiz = float(input("Foiz (%): "))
    print("Natija:", son * foiz / 100)

def arifmetik_orta():
    n = int(input("Nechta son kiritasiz?: "))
    yigindi = 0
    for i in range(n):
        son = float(input(f"{i+1}-son: "))
        yigindi += son
    print("O'rtacha:", yigindi / n)

def tenglama_yechish():
    a = float(input("a: "))
    b = float(input("b: "))
    if a != 0:
        x = -b / a
        print("Yechim x =", x)
    else:
        print("a 0 bo'lishi mumkin emas")

def celsius_to_fahrenheit():
    c = float(input("Celsius: "))
    print("Fahrenheit:", (c * 9/5) + 32)

def masofa_tezlik_vaqt():
    tezlik = float(input("Tezlik (km/h): "))
    vaqt = float(input("Vaqt (soat): "))
    print("Masofa:", tezlik * vaqt, "km")

def salom_ber():
    ism = input("Ismingizni kiriting: ")
    print("Salom,", ism)

def yosh_hisobla():
    yosh = int(input("Yoshingizni kiriting: "))
    print("Siz 5 yildan keyin", yosh + 5, "yoshda bo'lasiz")

def ikki_son_qoshish():
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    print("Yig'indisi:", a + b)

def juft_toq():
    son = int(input("Son kiriting: "))
    if son % 2 == 0:
        print("Juft son")
    else:
        print("Toq son")

def kuch_hisobla():
    m = float(input("Massa (kg): "))
    a = float(input("Tezlanish (m/s^2): "))
    print("Kuch (F = m*a):", m * a, "N")

def energiya():
    m = float(input("Massa (kg): "))
    c = 300000000
    print("E = mc^2:", m * c**2)

def katta_kichik():
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    if a > b:
        print("Birinchi son katta")
    elif a < b:
        print("Ikkinchi son katta")
    else:
        print("Teng")

def kvadrat():
    son = int(input("Son kiriting: "))
    print("Kvadrati:", son ** 2)

def uzunlik():
    matn = input("Matn kiriting: ")
    print("Uzunligi:", len(matn))

def katta_harf():
    matn = input("Matn kiriting: ")
    print(matn.upper())

def kichik_harf():
    matn = input("Matn kiriting: ")
    print(matn.lower())

def teskari_matn():
    matn = input("Matn kiriting: ")
    print(matn[::-1])

def kopaytirish():
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    print("Natija:", a * b)

def bolish():
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    if b != 0:
        print("Natija:", a / b)
    else:
        print("0 ga bo'lish mumkin emas")

def daraja():
    a = int(input("Son: "))
    b = int(input("Daraja: "))
    print("Natija:", a ** b)

def baho():
    ball = int(input("Balingizni kiriting: "))
    if ball >= 90:
        print("A baho")
    elif ball >= 70:
        print("B baho")
    else:
        print("C baho")

def ism_familiya():
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    print("To'liq ism:", ism, familiya)

def harf_sanash():
    matn = input("Matn: ")
    harf = input("Qaysi harfni sanaymiz?: ")
    print("Soni:", matn.count(harf))

def uch_son_orta():
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    c = int(input("3-son: "))
    print("O'rtacha qiymat:", (a + b + c) / 3)

def bmi_hisobla():
    vazn = float(input("Vazn (kg): "))
    boy = float(input("Bo'y (metr): "))
    bmi = vazn / (boy ** 2)
    print("BMI:", bmi)

def yurak_urishi():
    yosh = int(input("Yosh: "))
    print("Taxminiy maksimal yurak urishi:", 220 - yosh)

def yoshini_top():
    tugilgan = int(input("Tug'ilgan yil: "))
    hozir = 2026
    print("Yoshingiz:", hozir - tugilgan)

def asr_aniqla():
    yil = int(input("Yil kiriting: "))
    print("Asr:", (yil - 1) // 100 + 1)

def bit_bayt():
    bit = int(input("Bit kiriting: "))
    print("Bayt:", bit / 8)

def parol_tekshir():
    parol = input("Parol kiriting: ")
    if len(parol) >= 8:
        print("Kuchli parol")
    else:
        print("Zaif parol")




# MENU
while True:
    print("\n--- MENU ---")
    print("1  - Salom berish")
    print("2  - Yosh hisoblash")
    print("3  - Ikki son qo'shish")
    print("4  - Juft yoki toq")
    print("5  - Katta yoki kichik")
    print("6  - Son kvadrati")
    print("7  - Matn uzunligi")
    print("8  - Katta harf")
    print("9  - Kichik harf")
    print("10 - Matnni teskari chiqarish")
    print("11 - Ko'paytirish")
    print("12 - Bo'lish")
    print("13 - Daraja")
    print("14 - Baho aniqlash")
    print("15 - Ism Familiya")
    print("16 - Harf sanash")
    print("17 - 3 son o'rtachasi")
    print("18 - Kvadrat ildiz")
    print("19 - Faktorial")
    print("20 - To'rtburchak perimetri")
    print("21 - To'rtburchak yuzasi")
    print("22 - Aylana yuzasi")
    print("23 - Aylana uzunligi")
    print("24 - Pifagor teoremasi")
    print("25 - Foiz hisoblash")
    print("26 - Arifmetik o'rtacha")
    print("27 - Chiziqli tenglama yechish")
    print("28 - Celsius → Fahrenheit")
    print("29 - Masofa hisoblash")
    print("30 - Kuch hisoblash")
    print("31 - Energiya (E=mc^2)")
    print("32 - BMI hisoblash")
    print("33 - Yurak urishi")
    print("34 - Yoshni topish")
    print("35 - Asr aniqlash")
    print("36 - Bit → Bayt")
    print("37 - Parol tekshirish")
    print("0  - Chiqish")

    tanlov = input("Tanlang (0-17): ")

    if tanlov == "1":
        salom_ber()
    elif tanlov == "2":
        yosh_hisobla()
    elif tanlov == "3":
        ikki_son_qoshish()
    elif tanlov == "4":
        juft_toq()
    elif tanlov == "5":
        katta_kichik()
    elif tanlov == "6":
        kvadrat()
    elif tanlov == "7":
        uzunlik()
    elif tanlov == "8":
        katta_harf()
    elif tanlov == "9":
        kichik_harf()
    elif tanlov == "10":
        teskari_matn()
    elif tanlov == "11":
        kopaytirish()
    elif tanlov == "12":
        bolish()
    elif tanlov == "13":
        daraja()
    elif tanlov == "14":
        baho()
    elif tanlov == "15":
        ism_familiya()
    elif tanlov == "16":
        harf_sanash()
    elif tanlov == "17":
        uch_son_orta()
    elif tanlov == "18":
        ildiz()
    elif tanlov == "19":
        faktorial()
    elif tanlov == "20":
        perimetr_tortburchak()
    elif tanlov == "21":
        yuza_tortburchak()
    elif tanlov == "22":
        yuza_aylana()
    elif tanlov == "23":
        perimetr_aylana()
    elif tanlov == "24":
        pifagor()
    elif tanlov == "25":
        foiz_hisobla()
    elif tanlov == "26":
        arifmetik_orta()
    elif tanlov == "27":
        tenglama_yechish()
    elif tanlov == "28":
        celsius_to_fahrenheit()
    elif tanlov == "29":
        masofa_tezlik_vaqt()
    elif tanlov == "30":
        kuch_hisobla()
    elif tanlov == "31":
        energiya()
    elif tanlov == "32":
        bmi_hisobla()
    elif tanlov == "33":
        yurak_urishi()
    elif tanlov == "34":
        yoshini_top()
    elif tanlov == "35":
        asr_aniqla()
    elif tanlov == "36":
        bit_bayt()
    elif tanlov == "37":
        parol_tekshir()
    elif tanlov == "0":
        print("Dastur tugadi 👋")
        break
    else:
        print("Noto'g'ri tanlov!")