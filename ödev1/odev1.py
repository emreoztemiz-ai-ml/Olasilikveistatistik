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
