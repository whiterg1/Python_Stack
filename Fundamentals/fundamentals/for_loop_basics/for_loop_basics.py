
#Basic
for num in range (151):
    print(num)

#Multiples of 5
for num in range(0, 1001, 5):
    print(num)


#Counting, The Dojo Way
for x in range(0,101,1):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Coding Dojo")
    else:
        print(x)


#Whoa That Suckers Huge
total = 0               
for num in range(500001):   
    if num % 2 != 0:
        total += num
print(total)

#Countdown By Fours
for num in range (2018,0,-4):
    print (num)

#FLexible Counter
low_num = 0
high_num = 20
mult = 3
for num in range(low_num,high_num, 1):
    if num % mult == 0:
        print(num)