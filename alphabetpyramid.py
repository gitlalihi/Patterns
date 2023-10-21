num= int(input( " Enter your  pattern number"))

def alphabet(num):
    asciiValue = 65
    for i in range(asciiValue, asciiValue+num+1):
        for j in range(i, 64, -1):
            print(chr(j), end="")
        print()
            
alphabet(num)