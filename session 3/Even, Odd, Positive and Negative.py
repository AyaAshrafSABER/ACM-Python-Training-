num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num_of_negative = 0
num_of_pos = 0
num_of_odd = 0
num_of_even = 0 
if(num1 >= 0) :
    num_of_pos+=1
else :
    num_of_negative +=1
if(num2 >= 0) :
    num_of_pos +=1
else:
    num_of_negative +=1
if(num3 >= 0) :
    num_of_pos+=1
else:
    num_of_negative +=1
if(num4 >= 0) :
    num_of_pos+=1
else:
    num_of_negative +=1
if(num5 >= 0) :
    num_of_pos+=1
else:
    num_of_negative+=1
#calculate even and odd
if(num1 % 2 == 0) :
    num_of_even+=1
else :
    num_of_odd+=1
if(num2 % 2 == 0) :
    num_of_even+=1
else :
    num_of_odd+=1
if(num3 % 2 == 0) :
    num_of_even+=1
else :
    num_of_odd+=1
if(num4 % 2 == 0) :
    num_of_even+=1
else :
    num_of_odd +=1
if(num5 % 2 == 0) :
    num_of_even +=1
else :
    num_of_odd +=1
print(str(num_of_even) + " valor(es) par(es)")
print(str(num_of_odd) + " valor(es) impar(es)")
print(str(num_of_pos) + " valor(es) positivo(s)")
print(str(num_of_negative) + " valor(es) negativo(s)")
