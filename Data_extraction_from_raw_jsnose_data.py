import os
import csv
filelist=[]
basepath = 'games-output-78'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        filelist.append(entry)
#print(filelist)
csvData=[]
label=['filename','closure','couplingJs','empty','globalv','largeobj','lazyobj','longmess','longmeth','longpara','nested','refused','switch','unreachable']
csvData.append(label)
for j in filelist:
    st='games-output-78/'+j
    f1=open(st,"r")
    v=f1.readlines()
    n=len(v)
    f1.close()
    closure=0
    couplingJs=0
    empty=0
    globalv=0
    largeobj=0
    lazyobj=0
    longmess=0
    longmeth=0
    longpara=0
    nested=0
    refused=0
    switch=0
    unreachable=0
    a=[]
    flag=0
    temp=[]
    
    for dline in v:
        y=dline.strip()
        #print(y)
        if "http://localhost:8000/" in y and flag==0:
            flag=1
            a=y.strip().split('/')
            temp.append(a[-2])
            print(a[-2])
    
            
        if y == '********** EXCESSIVE GLOBAL VARIABLES **********':
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            if num!=0:
                x1=(f.readline()).strip()
                #print(x1)
                z=x.index(":")+2
                x2=x1[z:-1]
                t=x2.split(",")
                #print(t)
                a+=t
                i+=2
            else:
                i+=1
        
            #print(x)
        
        
        elif y == "*********** LARGE OBJECT **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            largeobj+=num
            #print(x)
            i+=1
        elif y == "********** LAZY OBJECT **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            lazyobj+=num
            #print(x)
            i+=1
        elif y == "********** LONG MESSAGE **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            longmess+=num
            #print(x)
            i+=1
        elif y == "********** LONG METHOD/FUNCTION **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            longmeth+=num
            #print(x)
            i+=1
        elif y == "********** LONG PARAMETER LIST **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            longpara+=num
            #print(x)
            i+=1
        elif y == "********** NESTED CALLBACK **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            nested+=num
            #print(x)
            i+=1
        elif y == "********** REFUSED BEQUEST **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            refused+=num
            #print(x)
            i+=1
        elif y == "********** SWITCH STATEMENT **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            switch+=num
            #print(x)
            i+=1
        elif y == "********** UNREACHABLE CODE **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            unreachable+=num
            #print(x)
            i+=1
        elif y == "********** EMPTY CATCH **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            empty+=num
            #print(x)
            i+=1
        elif y == "********** COUPLING JS/HTML **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            couplingJs+=num
            #print(x)
            i+=1
        elif y == "********** CLOSURE SMELL **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            closure+=num
            #print(x)
            i+=1
    globalv=len(set(a))
    temp.append(closure)
    temp.append(couplingJs)
    temp.append(empty)
    temp.append(globalv)
    temp.append(largeobj)
    temp.append(lazyobj)
    temp.append(longmess)
    temp.append(longmeth)
    temp.append(longpara)
    temp.append(nested)
    temp.append(refused)
    temp.append(switch)
    temp.append(unreachable)
    csvData.append(temp)
with open('games-output-78.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()
