__author__='goldy'

def fibbonacci(num):
    a=0
    b=1
    fiblist=[]
    fib=0
    for i in range(0,num):
        fib=a+b
        a=b
        b=fib
        #print('fib val:,a:,b:',fib,a,b)
        fiblist.append(fib)
        print('fiblist:',fiblist)
    return fiblist
print ('fiblast:',fibbonacci(10))