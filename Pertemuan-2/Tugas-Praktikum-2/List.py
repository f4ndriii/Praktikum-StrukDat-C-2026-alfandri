#1.1.Membuat List

nama_list = ['ayam', 'ikan', 'sapi']
print(nama_list)


#1.2.Boleh Duplikat

daging = ['ayam', 'ikan', 'sapi', 'ayam']
print(daging)


#1.3.List Lenght
#Untuk mengetahui berapa banyak data yang tersimpan dalam satu list

buah = ["apel", "pisang", "pepaya"]
print(len(buah))


#1.4.List Items - Data Types
#Isi dari list bisa berisi tipe data apapun
#Dalam sebuah list juga bisa terdapat beberapa tipe data berbeda

bilangan = [1, 2, 3, 4]
boolean = [True, False]
string = ['abdul', 'asep', 'udin']
gabungan = ['abdul', True, 5, False]


#2.1.Mengakses List
#List dapat diakses menggunakan indeks isinya

buah = ["apel", "pisang", "pepaya"]
print(buah[0])

#2.2.Negative Indexing

buah = ["apel", "pisang", "pepaya"]
print(buah[-1])

#2.3.Range of Indexes

buah = ["apel", "pisang", "ceri", "jeruk", "kiwi", "melon", "mangga"]
print(buah[2:5])

#2.4.Cek Isi Item List

buah = ["apel", "pisang", "pepaya"]
if "apel" in buah:
    print('Ya ya ya, ada')


#3.1.Mengganti Item dalam List

buah = ["apel", "pisang", "pepaya"]
buah[2] = 'mangga'

#3.2.Menggunakan range

buah = ["apel", "pisang", "ceri", "jeruk", "kiwi", "melon", "mangga"]
buah[1:3] = ["blackcurrant", "semangka"]
print(buah)

buah = ["apel", "pisang", "pepaya"]
buah[1:2] = ["blackcurrant", "semangka"]
print(buah)

#3.3.Memasukkan Item

buah = ["apel", "pisang", "pepaya"]
buah.insert(2, 'semangka')
print(buah)

#4.1.Menambah Item dalam List
#Menggunakan method append

buah = ["apel", "pisang", "pepaya"]
buah.append('semangka')
print(buah)

#4.2.Method extend

buah = ["apel", "pisang", "pepaya"]
buah_tuple = ("blackcurrant", "semangka")
buah.extend(buah_tuple)
print(buah_tuple)

#5.1.Remove List

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#5.2.Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#5.3.Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#6.1. Loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#6.2.Sort Ascending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#6.3.Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#6.4.Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#6.5.Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#7.1.Copy List
#Menggunakan method copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Menggunakan method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Menggunakan slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#8.1. Join List
#Menggunakan operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Menggunakan loop dan append
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)


'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''