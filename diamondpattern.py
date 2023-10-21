num= int(input("Enter your pattern number:"))

def diamond_pattern(num):
   for x in range(0,num-1):
        for y in range (0,num-x-2):
            print(" ", end = " ")
        for z in range(0,x+2):
            print(" * ", end = " ")
        print( )
   for i in range(0,num):
        for j in range (0,i):
            print (" ", end= " ")
        for k in range(0,num-i):
            print (" * ", end= " ") 
        print( )    

diamond_pattern(num)
