#Print The Specific String as Pattern in Python Programming (Alphabet Pattern In Python)


s1= str(input("Enter any string you like to create a pattern"))

def specefic_string_pattern(s1):
    for i in range(0,len(s1)):
        for j in range (0,i+1):
            print(s1[j], end= " ")
        print( )  

specefic_string_pattern (s1)         
