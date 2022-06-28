#Fibonnaci Sequence Converter
while True:
 x=0
 y=1
 z=0
 while True:
     print("Fibonnaci Sequence Converter")
     n=int(input("Type a number greater than 1: "))
     if n>1:
        break
 print("1",end=" ")
 for i in range(0,n):
    z=x+y
    print(f"{z}",end=" ")
    x=y
    y=z
 print("") 
