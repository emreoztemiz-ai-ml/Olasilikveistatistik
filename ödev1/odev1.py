import csv
import matplotlib.pyplot as plt

# ----- 1. Veri okuma -----
veri = {"x1": [], "x2": [], "x3": []}
with open("veri.csv", "r") as dosya:
    okuyucu = csv.reader(dosya)
    next(okuyucu)  
    for satir in okuyucu:
        x1, x2, x3 = map(float, satir)
        veri["x1"].append(x1)
        veri["x2"].append(x2)
        veri["x3"].append(x3)
# ----- 2. Aykırı değer tespiti  -----
def aykiri_degerler(veri_listesi):
    n = len(veri_listesi)
    for i in range(n):
        for j in range(0, n - i - 1):
            if veri_listesi[j] > veri_listesi[j + 1]:
                veri_listesi[j], veri_listesi[j + 1] = veri_listesi[j + 1], veri_listesi[j]
    
    q1_index = int(n * 0.25)
    q3_index = int(n * 0.75)
    q1 = veri_listesi[q1_index]
    q3 = veri_listesi[q3_index]
    iqr = q3 - q1
    alt_sinir = q1 - 1.5 * iqr
    ust_sinir = q3 + 1.5 * iqr
    
    aykirilar = []
    temiz = []
    for x in veri_listesi:
        if x < alt_sinir or x > ust_sinir:
            aykirilar.append(x)
        else:
            temiz.append(x)
    
    return temiz, aykirilar, (q1, q3)
# ----- 3. Temel hesaplama araçları  -----
def ortalama(veri):
    toplam = 0
    for x in veri:
        toplam += x
    return toplam / len(veri)

def ortanca(veri):
    siralanmis = veri[:]
    n = len(siralanmis)
    for i in range(n):
        for j in range(0, n - i - 1):
            if siralanmis[j] > siralanmis[j + 1]:
                siralanmis[j], siralanmis[j + 1] = siralanmis[j + 1], siralanmis[j]
    
    if n % 2 == 1:
        return siralanmis[n // 2]
    else:
        return (siralanmis[n//2 - 1] + siralanmis[n//2]) / 2

def mod(veri):
    sayac = {}
    for sayi in veri:
        if sayi in sayac:
            sayac[sayi] += 1
        else:
            sayac[sayi] = 1
    
    en_sik = None
    max_tekrar = 0
    for sayi, tekrar in sayac.items():
        if tekrar > max_tekrar:
            max_tekrar = tekrar
            en_sik = sayi
    
    return en_sik

def varyans(veri):
    ort = ortalama(veri)
    toplam = 0
    for x in veri:
        toplam += (x - ort) ** 2
    n = len(veri)
    return toplam / (n - 1)

def std_sapma(veri):
    var = varyans(veri)
    if var == 0:
        return 0
    tahmin = var / 2
    for _ in range(10):  
        tahmin = (tahmin + var / tahmin) / 2
    return tahmin

def ort_mutlak_sapma(veri):
    ort = ortalama(veri)
    toplam = 0
    for x in veri:
        toplam += abs(x - ort)
    return toplam / len(veri)

def degisim_araligi(veri):
    min_deger = veri[0]
    max_deger = veri[0]
    for x in veri:
        if x < min_deger:
            min_deger = x
        if x > max_deger:
            max_deger = x
    return max_deger - min_deger

def degisim_katsayisi(veri):
    return (std_sapma(veri) / ortalama(veri)) * 100
