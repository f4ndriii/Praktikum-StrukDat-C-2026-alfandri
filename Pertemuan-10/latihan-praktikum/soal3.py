riwayat = []

# is empty
isEmpty = not bool(riwayat)
print("is empty:", isEmpty)

# push
riwayat.append("facebook.com")
riwayat.append("youtube.com")
riwayat.append("google.com")

# pop
pop_riwayat = riwayat[-1]
print("pop:", pop_riwayat)

# peek
top_riwayat = riwayat[-1]
print("peek:", top_riwayat)

# size
print("size:", len(riwayat))