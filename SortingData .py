import re 
import mysql.connector
from datetime import datetime
from datetime import date
from datetime import timedelta
import random
from pymongo import MongoClient

connectionstring = "mongodb+srv://admin:admin@webcluster.9i5dp.mongodb.net/WebDB?retryWrites=true&w=majority"
client = MongoClient(connectionstring)
print(client.list_database_names())

job_desc = "44-months 31-years"
rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(months?)", re.I)
exp_temp_contract = rx.search(job_desc)
print(exp_temp_contract)
if exp_temp_contract:
	print(exp_temp_contract)

rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(years?)", re.I)
exp_temp = rx.search(job_desc)
if exp_temp:
	print(exp_temp.groups())



description = "skills Javascript, Angular, html5, (C++)"
date = "12 days ago"
setDescription = description
setDescription = setDescription.lower()
print(setDescription)
job_comb = ""
current_date = datetime.today()
date_posted = [int(s) for s in re.findall(r'\b\d+\b', date)]
date_posted_int = date_posted[0]
if(date_posted_int == 30): 
	date_posted_int = date_posted_int + random.randrange(70)
calculated_date = current_date - timedelta(date_posted_int)
print(date_posted_int)
print(calculated_date)

if(re.search(r'\bjava\b', setDescription)):
    job_comb = job_comb + ";java"

if(re.search(r'\bangular\b', setDescription)):
    job_comb = job_comb + ";angular"

if(re.search(r'\bc#\b', setDescription)):
    print("C#")

if(re.search(r'\bgolang\b', setDescription)):
    print("GO")

if(re.search(r'\bswift\b', setDescription)):
    print("Swift")

if(re.search(r'\bshell\b', setDescription)):
    print("Shell")

if(re.search(r'\bruby\b', setDescription)):
    print("Ruby")

if(re.search(r'\bjavascript\b', setDescription)):
    job_comb = job_comb + ";javascript"

if(re.search(r'\bhtml\b', setDescription)):
    print("HTML")
elif(re.search(r'\bhtml5\b', setDescription)):
    print("HTML")

if(re.search(r'\bcss\b', setDescription)):
    print("CSS")
elif(re.search(r'\bcss3\b', setDescription)):
    print("CSS")

if(re.search(r'\bsql\b', setDescription)):
    print("SQL")

if(re.search(r'\bcdisc\b', setDescription)):
    print("CDISC")

if(re.search(r'\bphp\b', setDescription)):
    print("PHP")
    
if(re.search(r'\bxml\b', setDescription)):
    print("XML")

if(re.search(r'\bsdtm\b', setDescription)):
    print("SDTM")

if(re.search(r'\btypescript\b', setDescription)):
    print("Typescript")

if(setDescription.find("c++") != -1): 
    print("C++")

if(re.search(r'\benglish\b', setDescription)):
    print("English")

if(re.search(r'\bafrikaans\b', setDescription)):
    print("Afrikaans")

if(re.search(r'\bvenda\b', setDescription)):
    print("Venda")

if(re.search(r'\bzulu\b', setDescription)):
    print("Zulu")

if(re.search(r'\bxhosa\b', setDescription)):
    print("Xhosa")

if(re.search(r'\bsotho\b', setDescription)):
    print("Sotho")

if(re.search(r'\bbachelor\b', setDescription)):
    print("Bachelors degree")
elif(re.search(r'\bdegree\b', setDescription)):
    print("Bachelors degree")
elif(re.search(r'\bbsc\b', setDescription)):
    print("Bachelors degree")



if(re.search(r'\bdiploma\b', setDescription)):
    print("Diploma")

if(re.search(r'\bcertificate\b', setDescription)):
    print("Certificate")

if(re.search(r'\bdocterate\b', setDescription)):
    print("Certificate")
elif(re.search(r'\bdocters\b', setDescription)):
    print("Certificate")

if(re.search(r'\bmasters\b', setDescription)):
    print("Masters")


rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(years?)", re.I)
exp_temp = rx.search(setDescription)
if exp_temp:
    print(exp_temp.groups())


if(re.search(r'\bfull time\b', setDescription)):
    print("Full time")
elif(re.search(r'\bpart time\b', setDescription)):
    print("Part time")
else:
    rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(months?)", re.I)
    exp_temp = rx.search(setDescription)
    if exp_temp:
        print(exp_temp.groups())

print(job_comb)

salary = "R20 000 - R25 000 a month"

int_sal = date_posted = [int(s) for s in re.findall(r"(\d+(?:\s+\d+)*)", salary)]
print(int_sal)













