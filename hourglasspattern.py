# to print the hour glass pattern using for loop
num= int(input("Enter your number for your hour glass pattern"))



def hour_glass(num): # inverted traingle 
    for i in range(0,num):
        for j in range (0,i):
            print (" ", end= " ")
        for k in range(0,num-i):
            print (" * ", end= " ") 
        print( )
    # normal traingle
    for x in range(0,num - 1): 
        for y in range (0,num-x-2):
            print(" ", end = " ")
        for z in range(0,x+2):
            print(" * ", end = " ")
        print( )

hour_glass(num)


