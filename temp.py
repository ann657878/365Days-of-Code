f=open("num.txt","r")
sum=0

for i in range(0,100):
    n=f.readline()
    print(i)
    if i in ('0','1','2','3','4','5','6','7','8','9'):
        sum=sum+int(i)
   
print("sum=",sum)