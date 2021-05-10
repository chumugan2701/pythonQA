
print ('Nakkeeran Cumugan')

sum=0
for i in range(1,11):
    sum=sum+i
    i=i+1
print(sum)
   
x=int(input ('Enter Marks--'))
if x<101 and x>74:
     print('A')
elif x<76 and x>64:
     print('B')
elif x<66 and x>54:
     print('c')
elif x<56 and x>34:
     print('S')
elif x<36 and x>-1:
     print('F')
else:
    print('Fake Answer')


for x in range(0,101,1):
    
    if x<101 and x>74:
         print('A')
    elif x<76 and x>64:
         print('B')
    elif x<66 and x>54:
         print('c')
    elif x<56 and x>34:
         print('S')
    elif x<36 and x>-1:
         print('F')
    else:
        print('Fake Answer')


x=15
for i in range(1,16,1):
    print("TimesOf-15--"+ str(x)+ "*"+ str(i)+ "=" + str(x*i))

marks=[]
i=0
for y in range(1,11,1):
    y=int(input ('Enter Marks--'))
    marks.append(y)
    print(marks)
    i=i+y

print(i/len(marks))

x=int(input ('How many weeks you want?--'))
y=int(input ('How many days you want?--'))
if y<8 and y>0:
    for i in range(1,x+1,1):
        print('week'+str(i))
        for j in range(1,y+1,1):
            print('day'+str(j))
else:
    print("Invalid Value")

x=int(input ('How many weeks you want?--'))
y=int(input ('How many days you want?--'))
z=int(input('Which day you do not want?--'))
if z<y:
    if x>0 and y>0:
        for i in range(1,x+1,1):
            print('week'+str(i))
            for j in range(1,y+1,1):
                if j != z:
                    print('day'+str(j))
                
    else:
        print("Invalid Value")
else:
    print('invalid value')




    
    
    




