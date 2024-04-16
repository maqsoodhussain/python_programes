li = ["Apple", "Mango", "Orange",1,25,5,6]
li1= []
li2= []

# print(li)
# print(li2)

for ele in li:
    if type(ele) == int:
        li1.append(ele)
    else:
        li2.append(ele)   

print(li1)      
print(li2)
