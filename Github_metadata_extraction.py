import requests
import json
import os
import csv
csvData=[]
f=open("javascript.txt","r")
x=f.readlines()
f.close()

label=['filename','open_issues','stars_count','language']
csvData.append(label)
for i in x:
    
    y=i.strip().split('/')
    api_url="https://api.github.com/repos/"+y[-2]+"/"+y[-1]
    print(api_url)
    token=""
    url = "{}?access_token={}".format(api_url,token)
    response=requests.get(url)
    data=response.text
    parsed=json.loads(data)
    l=[]
    
    l.append(y[-1]+"-master")
    l.append(parsed["open_issues"])
    l.append(parsed["stargazers_count"])   
    l.append(parsed["language"])
    csvData.append(l)
    
    

with open('ALLissues.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

