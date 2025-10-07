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
