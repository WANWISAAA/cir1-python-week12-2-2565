def  addnumber(*number):
    sum = 0
    for num in number:
        sum = sum + num 
    return sum

result = addnumber(10,20,30,40,50)
print("sum =",result)
result2 = addnumber(100,200,300,400,500)
print("sum =",result2)
    