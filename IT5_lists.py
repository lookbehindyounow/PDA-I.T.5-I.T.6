import datetime # this library has a bunch of classes & functions related to time

weekday_list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
month_dictionary={"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

time=datetime.datetime.now() # this is a method from said library that returns the current time
time_string=str(time)
date=(int(time_string[8:10]),int(time_string[5:7]),int(time_string[:4])) # this just gets us the day

if date[2]%4==0 and date[2]%100!=0 or date[2]%400==0:
    month_dictionary["February"]=29

weekday=6 # January 1st 2023 was a sunday
# CALCULATIONS
# return weekday_list[weekday]