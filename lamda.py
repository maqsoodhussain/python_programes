r = lambda num : num % 2
print(r(10))

r1 = lambda num1 : num1+10
print(r1(10))

r3 =(lambda num2 : num2+1)(5)
print(r3)


Li = [2,5,3,6,7,8,11,5,4]
result = list(filter(lambda x :x%2==0,Li))
print(result)

Li = [2,5,3,6,7,8,11,5,4]
result = list(map(lambda x : x%2,Li))
print(result)

