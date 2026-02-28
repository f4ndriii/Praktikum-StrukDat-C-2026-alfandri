from kurs import kurs
from konverter import idr_to_asing, asing_to_idr
from tabulate import tabulate

data = []

for key in kurs:
    baris = []
    baris.append(key)
    baris.append(kurs[key])
    data.append(baris)

print(data)