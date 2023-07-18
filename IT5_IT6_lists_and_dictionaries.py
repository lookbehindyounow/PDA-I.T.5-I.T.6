import datetime # this library has a bunch of classes & functions related to time

weekday_list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
month_dictionary={"January":31, "February":28, "March":31, "April":30, "May":31, "June":30,
                  "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

def return_weekday(weekday_list,month_dictionary):
    time=datetime.datetime.now() # this is a method from the imported library that returns the current date & time
    time_string=str(time)
    date=(int(time_string[8:10]),int(time_string[5:7]),int(time_string[:4])) # this formats the date as a tuple of integers
    
    days=5 # nye 2022 was a saturday so it's index in weekday_list is 5, which is where we'll start our day counter so that mondays are always 0
    for year in range(2023,date[2]+1): # runs through every year from 2023 to this year, inclusive
        if year%4==0 and year%100!=0 or year%400==0: # if it was/is a leap year
            month_dictionary["February"]=29
            leap=True
        else: # if it wasn't/isn't a leap year
            month_dictionary["February"]=28
            leap=False
        
        if year==date[2]: # stop the loop here at the current year because the year is not finished so we won't count all the days in it
            break
        days+=365 # if there are years between 2022 & the current year, add 365 for each one
        if leap:
            days+=1 # add an extra day if it was a leap year
    
    month_counter=1
    for month in month_dictionary:
        if month_counter==date[1]: # for the current month
            days+=date[0] # add the date (remember we were originally counting from nye)
            break # & stop counting
        days+=month_dictionary[month] # for any other months in the year, add the corresponding days
        month_counter+=1
    weekday=(days)%7 # days from monday 26/12/2022 mod 7 gives us the day of the week represented as an integer between 0 & 6
    return weekday_list[weekday] # indexing this list with said number gives us a string of what weekday it is

print(f"Today is {return_weekday(weekday_list,month_dictionary)}")

# Lists in python are ordered collections of data values that aren't necessarily unique.
# They are useful for anything you'd make a real world list out of, especially if the order is important.
# In this program I used a list to represent the names of the days of the week because they always happen in the same order.
# Dictionaries in python are collections of data which insted of being indexed with integers, are indexed
# with keys that you can set youself, which can be any object of any class or data type you want apart from another dictionary.
# Dictionaries are useful for collections of things that wouldn't necessarily be numbered but would be reffered to with some
# other kind of indicator, they are also useful for storing lots of different attributes of a given thing.
# In this program I used a dictionary to represent months although it would probably have been better to store the months as two
# seperate lists, one for how many days there are in each month & one for the month names.