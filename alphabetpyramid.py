x= int(input( " Enter your  pattern number"))

def alphabet(x):
    asciiValue = 70
    for i in range(asciiValue, asciiValue+x+1):
        for j in range(i, 64, -1):
            print(chr(j), end="")
        print()
            
alphabet(x)