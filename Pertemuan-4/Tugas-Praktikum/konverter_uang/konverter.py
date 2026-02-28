from kurs import kurs

def idr_to_asing(jumlah, mata_uang):
    return jumlah/kurs[mata_uang]

def asing_to_idr(jumlah, mata_uang):
    return kurs[mata_uang] * jumlah