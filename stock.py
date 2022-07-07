x=0
lastprice=0
target=0
g=1
def track():
    price= int(input("enter the price "))
    if(price>target):
        print("your order is place at ",price)
        place(price)
        x=price
        return
    else:
        track()
def place(value):
    global g,x
    x=value
    print(x)
    newprice=int(input("enter the value"))
    if(newprice>g):
        g=newprice    
          


   
  



  
    if(newprice<target):
        print("deal is reschedules")
        track()
    elif((x-newprice)>=buffer or (g-newprice)>buffer):
        print("deal is made at",newprice)  
    else:
        place(newprice)

target=int(input("enter the target"))
buffer=int(input("enter the buffer"))
      
    
    
track()