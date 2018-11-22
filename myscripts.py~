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

#Exercise 5 input and output
#activity 1

with open("weather.csv",'r') as reader:
    data = reader.read()

print(data)

#activity 2

with open("weather.csv) as reader:
    line = reader.readline()
    while line:
        print(line)
        line = reader.readline()

print("It's Over")

~# activity 3

with open("weather.csv") as reader:
    line = reader.readline()
    rain=[]
    for line in reader.readlines():
        r = line.strip().split(",")[-1]
        r = float(r)
        rain.append(r)

print(rain)

with open("myrain.txt","w") as writer:
    for r in rain:
         writer.write(str(r) + "\n")

#activty 4

import struct
bin_data = struct.pack("bbbb", 123, 12, 45, 34)

with open("mybinary.dat", "wb") as bwriter:
    writer.write(bin_data)

with open("mybinary.dat", "rb") as breader:
    bin_data2 = breader.read()

data = struct.unpack("bbbb", bin_data2)
print(data)


#exercise 6 strings

#activity 1

s = "I love to write python"
for letter in s:
    print(letter)

s[4]
s[-1]

print(len(s))

print(s[0])
print(s[0][0])
print(s[0][0][0])

#activity 2

s ="I love to write python"

split_s=split.s()

for word in split_s:
    if word.lower().find("i") > -1:
        print(f"I found 'i' in {word}")

#activity 3

something = "completely different"
print(dir(something))
something.count("t")
something.find("plete")

something.split("e")

thing2 = something.replace("different","silly")
something[0] = "B"

# Exercise 8 funciton

#activity 1
def double_it(number):
    answer=2*number
    return answer

a=double_it(2)
b=double_it(2.0)
c=double_it("2")

#activity 2

def calc_hypo(a,b):
    hypo = (a**2 + b**2)**0.5
    return hypo

a=3
b=4

print(calc_hyp(a,b))

#activity 3

def calc_hypo(a,b):
    if type(a) not in (int, float) or type(b) not in (int,float):
        print("Bad argument")
        return False
    if a <=0 or b <=0:
        print("Bad argument")
        return False
    hypo = (a**2 + b**2)**0.5
    return hypo

calc_hypo(0,-2)

calc_hypo("hi","bye")

calc_hypo(6,7)


#Exercise 10 sets and dictionaries

#activity 1

a = {0, 1, 2, 3, 4, 5}
b = {2, 4, 6, 8}

a|b
a.union(b) 

~#same syntax

a.intersection(b)


#activity 2

band = ["mel", "geri", "victoria", "mel", "emma"]

counts={}

for name in band:
    if name not in counts:
        counts[name]=1
    else:
        counts[name] += 1

print(name, counts[name])


#activity 3

d={"maggie" : "uk", "ronnie" : "usa"}
dir(d)
d.items()
for(person,place) in d.items():
    print("{0} is from the {1}".format(person,place))

print d.items()
print d.keys()
print d.values()

d.get("maggie", "nowhere")










