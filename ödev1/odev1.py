import csv
import matplotlib.pyplot as plt

# 1. Dosyadan veri oku
veriler = {"x1": [], "x2": [], "x3": []}

with open("veri.csv", "r") as f:
    okuyucu = csv.reader(f)
    next(okuyucu)
    for s in okuyucu:
        x1, x2, x3 = map(float, s)
        veriler["x1"].append(x1)
        veriler["x2"].append(x2)
        veriler["x3"].append(x3)

# 2. Aykırı değerleri bul
def aykiri_bul(liste):
    n = len(liste)
    # basit sıralama
    for i in range(n):
        for j in range(n - i - 1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

    q1_index = int(n * 0.25)
    q3_index = int(n * 0.75)
    q1 = liste[q1_index]
    q3 = liste[q3_index]
    iqr = q3 - q1
    alt = q1 - 1.5 * iqr
    ust = q3 + 1.5 * iqr

    temiz = []
    aykiri = []
    for x in liste:
        if x < alt or x > ust:
            aykiri.append(x)
        else:
            temiz.append(x)
    return temiz, aykiri, (q1, q3)

# 3. Temel fonksiyonlar
def ortalama(veri):
    t = 0
    for x in veri:
        t += x
    return t / len(veri)

def ortanca(veri):
    v = veri[:]
    n = len(v)
    for i in range(n):
        for j in range(n - i - 1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    if n % 2 == 0:
        return (v[n//2 - 1] + v[n//2]) / 2
    else:
        return v[n//2]

def mod(veri):
    sayac = {}
    for i in veri:
        if i in sayac:
            sayac[i] += 1
        else:
            sayac[i] = 1
    max_t = 0
    mod_sayi = None
    for k, v in sayac.items():
        if v > max_t:
            max_t = v
            mod_sayi = k
    return mod_sayi

def varyans(veri):
    ort = ortalama(veri)
    t = 0
    for i in veri:
        t += (i - ort)**2
    return t / (len(veri) - 1)

def std_sapma(veri):
    var = varyans(veri)
    if var == 0:
        return 0
    x = var / 2
    for _ in range(8):
        x = (x + var / x) / 2
    return x

def ort_mutlak_sapma(veri):
    ort = ortalama(veri)
    t = 0
    for i in veri:
        t += abs(i - ort)
    return t / len(veri)

def degisim_araligi(veri):
    mn = veri[0]
    mx = veri[0]
    for i in veri:
        if i < mn:
            mn = i
        if i > mx:
            mx = i
    return mx - mn

def degisim_katsayisi(veri):
    return (std_sapma(veri) / ortalama(veri)) * 100

# 4. Hesaplama kısmı
sonuc = ""
for ad, liste in veriler.items():
    temiz, aykirilar, (q1, q3) = aykiri_bul(liste)
    sonuc += f"\n=== {ad.upper()} ===\n"
    sonuc += f"Aykırı değerler: {aykirilar}\n"
    sonuc += f"Ortalama: {ortalama(temiz):.2f}\n"
    sonuc += f"Ortanca: {ortanca(temiz):.2f}\n"
    sonuc += f"Mod: {mod(temiz)}\n"
    sonuc += f"Değişim Aralığı: {degisim_araligi(temiz):.2f}\n"
    sonuc += f"Ort. Mutlak Sapma: {ort_mutlak_sapma(temiz):.2f}\n"
    sonuc += f"Varyans: {varyans(temiz):.2f}\n"
    sonuc += f"Std Sapma: {std_sapma(temiz):.2f}\n"
    sonuc += f"Değişim Katsayısı: {degisim_katsayisi(temiz):.2f}%\n"
    sonuc += f"Çeyrekler Aralığı: {(q3 - q1):.2f}\n"

# 5. Boxplot çiz
plt.boxplot([veriler["x1"], veriler["x2"], veriler["x3"]], labels=["x1", "x2", "x3"])
plt.title("Kutu Grafiği")
plt.savefig("boxplot.png")
plt.close()

# 6. Sonucu yaz
with open("sonuc.txt", "w") as f:
    f.write(sonuc)

print("Tamamlandı, sonuc.txt dosyasına yazıldı.")
