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
    arr=[0]*13
    a=[]
    flag=0
    temp=[]
    f.open(st,"r")
    for i in range(v):
        y=(f.readline()).strip()
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
            arr[4]+=num
            #print(x)
            i+=1
        elif y == "********** LAZY OBJECT **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[5]+=num
            #print(x)
            i+=1
        elif y == "********** LONG MESSAGE **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[6]+=num
            #print(x)
            i+=1
        elif y == "********** LONG METHOD/FUNCTION **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[7]+=num
            #print(x)
            i+=1
        elif y == "********** LONG PARAMETER LIST **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[8]+=num
            #print(x)
            i+=1
        elif y == "********** NESTED CALLBACK **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[9]+=num
            #print(x)
            i+=1
        elif y == "********** REFUSED BEQUEST **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[10]+=num
            #print(x)
            i+=1
        elif y == "********** SWITCH STATEMENT **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[11]+=num
            #print(x)
            i+=1
        elif y == "********** UNREACHABLE CODE **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[12]+=num
            #print(x)
            i+=1
        elif y == "********** EMPTY CATCH **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[2]+=num
            #print(x)
            i+=1
        elif y == "********** COUPLING JS/HTML **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[1]+=num
            #print(x)
            i+=1
        elif y == "********** CLOSURE SMELL **********":
            x=(f.readline()).strip()
            z=x.index(":")+1
            num=int(x[z:])
            arr[0]+=num
            #print(x)
            i+=1
    
    arr[3]+=len(set(a))
    temp+=arr
    csvData.append(temp)
with open('games-output-78.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()
