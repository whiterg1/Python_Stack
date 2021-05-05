#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #Will print 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Will print either an error due to one of the functions not being defined or will just return 5.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Will print 5 because once it returns a number it exits the function and prints without ever reading the next return.

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#It will print 5. Once return is executed, it will not read the next line inside of the function. 


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#5 will print on one line and x will hold no value because nothing was returned to the variable.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#3 will print first on one line, 5 will print on the next line, and 8 will print on final line.
#Edit - the final line did not print because there were no values returned by the function.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#The returned numbers would be assumed to equal 7 but because they are converted to strings in the function it will return 25.



#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#The function first defines b as 100, and then prints that 100. After running through the conditional it returns 10 which is what will print.



#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#1st print statement will return and print 7. 
#2nd print statement will return and print 14.
#3rd print statement will return 21.

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Function will return and print 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# b is defined as 500 and will print 500. The function is then recorded but not ran and a second print statement
#immediately follows. b still equals 500 at this point and will print a second time. The function is then called
#b becomes 300 within the function and prints as 300. Finally once the function ends without returning a number
#to the variable it will print the original 500 a third time. So we should see 500, 500, 300, 500 on four seperate lines.



#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#This code will operate identical to the one above with the exception that the function returns a new number to the original variable.
#Therefore the printed result should be 500, 500, 300, 300 on four seperate lines.
#Edit- My original prediction was wrong and the return within the function did not affect the variable outside.

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#This code is nearly identical to the last two but the addition of the new variable of b will allow b to become 300 outside of the function.
#The output of this code will be 500,500,300 on four seperate lines.

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#The code will read the two functions first but not execute as they have not yet been called. 
#Foo() will execute first as it was called on the bottom line of code. 
#This will print 1, and then activate bar(), which will print 3, and then it will return to foo() and print 2.


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# y is defined as foo() and when the code prints y it calls the function.
#foo() then prints one, defines x as bar(), activates the bar() function, prints three, and then returns 5.
#once it returns the 5, it will immediately break from the function and the code will stop.
#5 is returned but it has not variable to be sent to. 
#The output should be 1, and 3 on two seperate lines only
#Edit- When the function returns the 5 it prints the 5, and then returns to the previous function to return 10, which also prints.
#True output = 1,3,5,10