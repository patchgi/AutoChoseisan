#coding utf-8

from selenium import webdriver
import sys
from datetime import date,timedelta
from calendar import weekday
import time
def calcDate():
	now = date.today()
	dateList=[]

	one_day = timedelta(days=1)
	calcDate=now
	charweek=("月","火","水","木","金","土","日")

	for i in range(7):
		calcDate=calcDate+one_day
		year=calcDate.year
		month=calcDate.month
		day=calcDate.day
		week=weekday(year,month,day)
		strdate=str(month)+"/"+str(day)+"("+charweek[week]+") 19:00〜\n"
		dateList.append(strdate)

	return dateList


if __name__=="__main__":
	event_name=sys.argv[1]
	driver = webdriver.PhantomJS()
	driver.get("https://chouseisan.com/")
	driver.find_element_by_name("name").send_keys(event_name)
	dateLists=calcDate()
	for day in dateLists:
		driver.find_element_by_name("kouho").send_keys(day)

	driver.find_element_by_id("createBtn").submit()
	time.sleep(1)
	driver.save_screenshot("ss.png")
	URL=driver.find_element_by_id("listUrl").get_attribute("value")
	print (URL)
