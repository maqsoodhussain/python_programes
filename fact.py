n  = int(input("Enter number: "))
fact = 1
    
for i in range(n,1,-1):
    if n == 0:
        fact = 1
    else:
        fact = fact * i

print(fact)


