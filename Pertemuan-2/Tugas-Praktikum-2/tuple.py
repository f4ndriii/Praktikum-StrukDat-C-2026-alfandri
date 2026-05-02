#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Unpack Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Loop Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#Join Tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 
#ouput: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''