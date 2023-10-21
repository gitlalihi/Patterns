# To print number mirror pyramid
num= int(input("Enter your pattern number:"))

def mirror_number_pyramid(num):
    for i in range (num):
        for j in range(num-i-1):
            print("",end = ' ')
        for k in range(i,1,-1):
            print(k, end = ' ')
        for l in range(1,i+1):
            print(l,end=' ')
        print(' ')

mirror_number_pyramid(num)           