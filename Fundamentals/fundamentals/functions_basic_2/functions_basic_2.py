#Countdown function
def countdown(user_input): #As the code is read it will not execute the function but will instead save until it is called.
    number = [] #List that will be manipulated by the loop.
    for num in range(user_input,-1,-1): #Loop will take the user_input and decrement the number until the loop reaches -1 but num will = 0.
        number.append(num) #This will append the number onto the end of the number list defined above.
        if num == 0: 
            print(number) #Once num reaches 0, it will print the output of the collected decremented list.
countdown(int(input("Choose a number: "))) #This line calls the function and starts the process by utilizing the user's input.

#Print and return
def print_and_return(a,b): #This is the start of the function
    print(a)
    return(b)
print_and_return(3,5) #This is the line which recalls the function

#First plus length
def first_plus_length(num_list): 
    sum = num_list[0] + len(num_list) #This line creates a new variable sum and defines it as the sum of the first number in the list and the length of the list.
    print(sum)
first_plus_length([7,2,3,4,9]) #This line recalls the function and defines num_list

#Values greater than second
def values_greater_than_second(values):
    sum = []
    for x in range (0, len(values), 1):
        if values[x] > values[1]:
            sum.append(values[x])
    if x+1 == len(values):
        print(len(sum))
        return(sum)
    if len(sum) < 2:
        return(False)
values_greater_than_second([1,2,10,6,4])


#This length, that value
def this_length_that_value(size, value):
    list = []
    for num in range(0,size,1):
        list.append(value)
    if len(list) == size:
        return list
print(this_length_that_value(4,2))
