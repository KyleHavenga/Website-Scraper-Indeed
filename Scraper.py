from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient
import mysql.connector
import re 
import random
import datetime
from datetime import datetime
from datetime import timedelta
import string

## Download the chromedriver from link in description
## And give the location of executable here
driver = webdriver.Chrome("./chromedriver")
connectionstring = "mongodb+srv://admin:admin@webcluster.9i5dp.mongodb.net/WebDB?retryWrites=true&w=majority"
client = MongoClient(connectionstring)

mydb = mysql.connector.connect(
	host="localhost", 
	user="root",
	password="root",
	database="datascraper")
mycursor = mydb.cursor()

for i in range(600,1000,10):

	##Step1: Get the page
	driver.get("https://za.indeed.com/jobs?q=developer&l=South+Africa&start="+str(i))
	driver.implicitly_wait(50)

	all_jobs = driver.find_elements_by_class_name('result')

	for job in all_jobs: 

		result_html = job.get_attribute('innerHTML')
		soup = BeautifulSoup(result_html,'html.parser')

		try:
			title = soup.find("a",class_="jobtitle").text.replace('\n','')
		except:
			title = ""

		try:
			title_url = soup.find("a" ,class_="jobtitle")["href"]
			title_url = "https://za.indeed.com/jobs?q=programmer&l=South Africa&"+title_url 
		except:
			title_url = ""

		try:
			location = soup.find(class_="location").text
		except:
			location = ""

		try:
			company = soup.find(class_="company").text.replace("\n","").strip()
		except:
			company = ""

		try:
			current_date = datetime.today()
			date = soup.find(class_="date").text.replace("\n","").strip()
			date_posted = [int(s) for s in re.findall(r'\b\d+\b', date)]
			date_posted_int = date_posted[0]
			if(date_posted_int == 30): 
				date_posted_int = date_posted_int + random.randrange(70)
			calculated_date = current_date - timedelta(date_posted_int)
		except:
			date = ""
        
		try:
			salary = soup.find(class_="salary").text.replace("\n","").strip()
			salary.translate({ord(c): None for c in string.whitespace})
			result = re.sub(r"\s+", "", salary) 
			int_sal = [int(s) for s in re.findall(r"(\d+(?:\s+\d+)*)", result)]
			int_sal_fin = int_sal[0] 
			salary = int_sal_fin
		except:
			salary = 0 

		try:
			sponsored = soup.find(class_="sponsoredGray").text
			sponsored = "Sponsored"
		except:
			sponsored = "Organic"
	
		sum_div = job.find_elements_by_class_name("summary")[0]

		try:
			sum_div.click()
		except:
			close_button = driver.find_elements_by_class_name("popover-x-button-close")[0]
			close_button.click()
			sum_div.click()
		
		job_desc_init = driver.find_element_by_id('vjs-desc').text
		job_desc = job_desc_init.lower()
		job_comb = ""

		if(re.search(r'\bjava\b', job_desc)):
			job_comb = job_comb + ";java"

		if(job_desc.find("angular") != -1): 
			job_comb = job_comb + ";angular"
		
		if(job_desc.find("j#") != -1): 
			job_comb = job_comb + ";J#"
		
		if(job_desc.find("golang") != -1): 
			job_comb = job_comb + ";golang"
		
		if(job_desc.find("swift") != -1): 
			job_comb = job_comb + ";swift"
		
		if(job_desc.find("ruby") != -1): 
			job_comb = job_comb + ";ruby"
		
		if(job_desc.find("shell") != -1): 
			job_comb = job_comb + ";shell"	
		
		if(job_desc.find("javascript") != -1): 
			job_comb = job_comb + ";javascript"
		
		if(job_desc.find("html") != -1): 
			job_comb = job_comb + ";html"

		if(job_desc.find("css") != -1): 
			job_comb = job_comb + ";CSS"
		
		if(job_desc.find("sql") != -1): 
			job_comb = job_comb + ";SQL"
		
		if(job_desc.find("cdisc") != -1): 
			job_comb = job_comb + ";CDISC"
		
		if(job_desc.find("php") != -1): 
			job_comb = job_comb + ";PHP"
		
		if(job_desc.find("xml") != -1): 
			job_comb = job_comb + ";XML"

		if(job_desc.find("sdtm") != -1): 
			job_comb = job_comb + ";SDTM"
		
		if(job_desc.find("typescript") != -1): 
			job_comb = job_comb + ";TypeScript"
		
		if(job_desc.find("itil") != -1): 
			job_comb = job_comb + ";ITIL"
		
		if(job_desc.find("robot studio") != -1): 
			job_comb = job_comb + ";Robot Studio"
		
		if(job_desc.find("delfoi") != -1): 
			job_comb = job_comb + ";Delfoi"
		
		if(job_desc.find("motisim") != -1): 
			job_comb = job_comb + ";Motisim"
		
		if(job_desc.find("cobol") != -1): 
			job_comb = job_comb + ";Cobol"

		if(job_desc.find("asp.net") != -1): 
			job_comb = job_comb + ";ASP.NET"
		
		if(job_desc.find("vb.net") != -1): 
			job_comb = job_comb + ";VB.NET"
		
		if(job_desc.find("cics") != -1): 
			job_comb = job_comb + ";CICS"
		
		if(job_desc.find("mvc") != -1): 
			job_comb = job_comb + ";MVC"
		
		if(job_desc.find("c#") != -1): 
			job_comb = job_comb + ";C#"

		if(job_desc.find("c++") != -1): 
			job_comb = job_comb + ";C++"
		if(job_desc.find("j++") != -1): 
			job_comb = job_comb + ";J++"
        
		if(job_desc.find("matlab") != -1): 
			job_comb = job_comb + ";Matlab"
		
		if(job_desc.find("rust") != -1): 
			job_comb = job_comb + ";Rust"
		
		if(job_desc.find("delphi") != -1): 
			job_comb = job_comb + ";Delphi"

		languages_comb = "" 
		if(job_desc.find("english") != -1):
			languages_comb = languages_comb + ";english"

		if(job_desc.find("afrikaans") != -1):
			languages_comb = languages_comb + ";afrikaans"

		if(job_desc.find("venda") != -1):
			languages_comb = languages_comb + ";venda"

		if(job_desc.find("zulu") != -1):
			languages_comb = languages_comb + ";zulu"

		if(job_desc.find("xhosa") != -1):
			languages_comb = languages_comb + ";xhosa"
		
		if(job_desc.find("sotho") != -1):
			languages_comb = languages_comb + ";sotho"
		
		education_comb = ""
		if(job_desc.find("bachelor") != -1):
			education_comb = education_comb + ";Bachelor's Degree"
		elif(job_desc.find("degree") != -1):
			education_comb = education_comb + ";Bachelor's Degree"
		elif(job_desc.find("bsc") != -1):
			education_comb = education_comb + ";Bachelor's Degree in computer science"
		elif(job_desc.find("bsc it") != -1):
			education_comb = education_comb + ";Bachelor's Degree in information technology"
		

		if(job_desc.find("diploma") != -1):
			education_comb = education_comb + ";Diploma"
		
		if(job_desc.find("certificate") != -1):
			education_comb = education_comb + ";Certificate"
		
		if(job_desc.find("doctorate") != -1):
			education_comb = education_comb + ";Docterate"
		elif(job_desc.find("doctors") != -1):
			education_comb = education_comb + ";Docterate"
		elif(job_desc.find("doctor") != -1):
			education_comb = education_comb + ";Docterate"
		
		if(job_desc.find("master") != -1):
			education_comb = education_comb + ";Masters"
		

		
		rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(years?)", re.I)
		exp_temp = rx.search(job_desc)
		if exp_temp:
			num_ex = exp_temp.group(1) + (" - ") + exp_temp.group(2)
		else: 
			num_ex = ""

		job_info = ""
		if(job_desc.find("full time") != -1) or (job_desc.find("full-time") != -1):
			job_info = "full time"
		elif(job_desc.find("part time") != -1) or (job_desc.find("part-time") != -1):
			job_info = "part time"
		elif(job_desc.find("hourly") != -1) or (job_desc.find("per hour") != -1):
			job_info = job_info + ";hourly"
		else:
			rx = re.compile(r"(\d+(?:-\d+)?\+?)\s*(months?)", re.I)
			exp_temp_contract = rx.search(job_desc)
			if exp_temp_contract:
				job_info= exp_temp_contract.group(1) + " - " + exp_temp_contract.group(2)
			else:
				job_info = ""
			

		db = client.get_database("WebDB")
		collection = db.get_collection("JobCollection")
		
		document = {"Requirements":{"Experience":num_ex,
            "Languages":job_comb,"Education":education_comb},
            "Date_posted":calculated_date,
			"Job_title":title,
			"Search_indeed":"programmer - South Africa",
            "company_name":company,
            "Spoken_Languages":languages_comb,
			"location":location,
            "Site_link":title_url,
            "payment_type":{"type":job_info,"amount":salary}}
		
		collection.insert_one(document)



	