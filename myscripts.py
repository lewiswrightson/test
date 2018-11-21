#Exercise 1 python basics

# 1
course ='python'
rating = 10
print(course)
print(rating)


#2

b=3
c=4
a=((b**2 + c**2)**0.5)
print(a)


#3

#a is a float because it is a decimal number
type(a)
type(b)
type(c)

#4
a=int(a)
type(a)


print(str(a) + " squared equals " + str(b) + " squared + " + str(c) + " squared.")

#Exercise 2

while 1:
    x=1
#ctrl C to kill
while 0:
    pass

gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0

while count < 4:
    item = gases[count]
    print(item, count)
    count += 1

name = "Lisa"

if name == "Lisa":
    print(name, "plays saxophone")
elis name == "Bart":
    print(name, "rides skateboard")
else:
    print(name, "lives in Springfield")

x = 1

if x:
    print(x, " is True"


#Exercise 3 lists and slicing
#actvity 1
x=[1,2,3,4,5]

#print 2nd item in list
print(x[1])

#print 2nd to last item
print(x[-2])

#use slicing to select whole list
whole_list=x[:]

#slice 2nd to 4th item
half_list=x[1:4]

#activity 2
#1-10 values
y=list(range(1,11))

#chaneg y1 to 10
y[0]=10

#add 11 to the end
y.append(11) 

#extend the range to include 12,13,14

y.extend([12,13,14])

#activity 3
forward = []
backward = []

values = ["a", "b", "c"]

for item in values:
    forward.append(item)
    backward.insert(0,item)

forward.reverse()
print(forward == reverse)

#activty 4
countries = ["uk", "usa", "uk", "uae"]
dir(countries)
help(countries.count)
countries.count("uk")

#Exercise 4 Tuples

#activty 1
t=(1,)
print(t[-1])

l=range(100,201)
tup=tuple(l)

print(tup[0],tup[-1])

#activity 2

mylist = [23, "hi", 2.4e-10]
for(count,item) in enumerate(mylist):
    print(count,item)

#activity 3

(first,middle,last)=mylast
(middle,last,first)=(first,middle,last)




