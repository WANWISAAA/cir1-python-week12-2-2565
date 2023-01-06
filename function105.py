def fineadd(*number):
    sum = 0
    for num in number:
        sum = sum + num
    print("sum = ",sum)
    
fineadd(10,20,30,40,50,60)  
fineadd(10,100,500)