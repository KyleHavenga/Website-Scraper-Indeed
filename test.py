import re 
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost", 
	user="root",
	password="root",
	database="datascraper")
mycursor = mydb.cursor()

for i in range(0,500,10):
	sql = "SELECT job_desc FROM table_primary"
	mycursor.execute(sql)
	results = mycursor.fetchall()

	if(re.search(r'\bjava\b', results)):
		print("Java") 
	
	if(re.search(r'\bangular\b', results)):
		print("Angular")
	
	if(re.search(r'\bc#\b', results)):
		print("C#")
	
	if(re.search(r'\bgolang\b', results)):
		print("GO")
	
	if(re.search(r'\bswift\b', results)):
		print("Swift")
	
	if(re.search(r'\bshell\b', results)):
		print("Shell")
	
	if(re.search(r'\bruby\b', results)):
		print("Ruby")
	
	if(re.search(r'\bjavascript\b', results)):
		print("JavaScript")
	
	if(re.search(r'\bhtml\b', results)):
		print("HTML")
	elif(re.search(r'\bhtml5\b', results)):
		print("HTML")
	
	if(re.search(r'\bcss\b', results)):
		print("CSS")
	elif(re.search(r'\bcss3\b', results)):
		print("CSS")
	
	if(re.search(r'\bsql\b', results)):
		print("SQL")
	
	if(re.search(r'\bcdisc\b', results)):
		print("CDISC")
	
	if(re.search(r'\bphp\b', results)):
		print("PHP")
	
	if(re.search(r'\bxml\b', results)):
		print("XML")
	
	if(re.search(r'\bsdtm\b', results)):
		print("SDTM")
	
	if(re.search(r'\btypescript\b', results)):
		print("Typescript")
	
	if(results.find("c++ ") != -1): 
		print("C++")
	if(results.find("c++,") != -1): 
		print("C++")
	if(results.find("c++/") != -1):
		print("C++")
	if(results.find(" c++") != -1): 
		print("C++")
	
	if(re.search(r'\benglish\b', results)):
		print("English")
	
	if(re.search(r'\bafrikaans\b', results)):
		print("Afrikaans")
	
	if(re.search(r'\bvenda\b', results)):
		print("Venda")
	
	if(re.search(r'\bzulu\b', results)):
		print("Zulu")
	
	if(re.search(r'\bxhosa\b', results)):
		print("Xhosa")
	
	if(re.search(r'\bsotho\b', results)):
		print("Sotho")
	
	if(re.search(r'\bbachelor\b', results)):
		print("Bachelors degree")
	elif(re.search(r'\bdegree\b', results)):
		print("Bachelors degree")
	elif(re.search(r'\bbsc\b', results)):
		print("Bachelors degree")
	
	if(re.search(r'\bdiploma\b', results)):
		print("Diploma")
	
	if(re.search(r'\bcertificate\b', results)):
		print("Certificate")
	
	if(re.search(r'\bdocterate\b', results)):
		print("Certificate")
	elif(re.search(r'\bdocters\b', results)):
		print("Certificate")
	
	if(re.search(r'\bmasters\b', results)):
		print("Masters")
	
	rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(years?)", re.I)
	exp_temp = rx.search(results)
	if exp_temp:
		print(exp_temp.groups())
	
	if(re.search(r'\bfull time\b', results)):
		print("Full time")
	elif(re.search(r'\bpart time\b', results)):
		print("Part time")
	else:
		rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(months?)", re.I)
		exp_temp = rx.search(results)
		if exp_temp:
			print(exp_temp.groups())
	print("_____________________________________________________________________________________")
	counter = counter + 1