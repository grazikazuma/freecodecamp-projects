

def add_time(start, duration, weekday= ""):

  #print(add_time("11:06 PM", "2:02"))

  #spliting start

  s = start.split(':')
  hour = int(s[0])
  s2 = s[1].split()
  min = int(s2[0])
  period = s2[1]

  #split duration

  d = duration.split(":")
  d_hour = int(d[0])
  d_min = int(d[1])

  w = weekday.lower()

  #convert week days to numbers
  
  if w == "sunday":
    w = 0
  elif w == "monday":
    w = 1
  elif w == "tuesday":
    w = 2
  elif w == "wednesday":
    w = 3
  elif w == "thursday":
    w = 4
  elif w == "friday":
    w = 5
  elif w == "saturday":
    w = 6    
    
# create variables for new time
  n_min = 0
  n_hour = 0
  n_day = 0
  n_period = "AM"
  
# add 12 your to a period 
  if period == "PM":
    n_hour += 12

# calculate minutes
  n_min = min + d_min 
  if n_min > 60:
    n_min = n_min - 60
    n_hour += 1
    
# calculate hours
  n_hour = n_hour + hour + d_hour
  while n_hour >= 24:
    n_hour -= 24
    n_day += 1

# convert for period
  if n_hour == 12:
    n_period = 'PM'
  elif n_hour > 12:
    n_hour -= 12
    n_period = "PM"
  elif n_hour == 0:
    n_hour += 12

# calculate weekdays 

  if w == "":
    n_weekday = w
  else: 
    n_weekday = w + n_day
    print(n_weekday)
    while n_weekday > 6:
      n_weekday -= 7
    if n_weekday == 0:
      n_weekday = "Sunday"
    elif n_weekday == 1:
      n_weekday = "Monday"
    elif n_weekday == 2:
      n_weekday = "Tuesday"
    elif n_weekday == 3:
      n_weekday = "Wednesday"
    elif n_weekday == 4:
      n_weekday = "Thrusday"
    elif n_weekday == 5:
      n_weekday = "Friday"
    elif n_weekday == 6:
      n_weekday = "Saturday"
      

### fix format ###
    
# fix lack of 0 in minutes
  if n_min < 10:
    n_min = "0"+ str(n_min)
  else:
    n_min = str(n_min)

# converting days
  if n_day == 0:
    n_day = ""
  elif n_day == 1:
    n_day = str('(next day)')
  else:
    n_day = "(" + str(n_day) + " days later)"

# formating new time with and without days in the end 

  new_time = ""
  if n_day == "" and n_weekday == "":
    new_time = str(n_hour) + ':' + n_min +" "+ str(n_period)
  elif n_day == "":
    new_time = str(n_hour) + ':' + n_min +" "+ str(n_period) + ", " + str(n_weekday)
  elif n_weekday == "":
    new_time = str(n_hour) + ':' + n_min +" "+ str(n_period) + " " + str(n_day)
  else:
    new_time = str(n_hour) + ':' + n_min +" "+ str(n_period) + ", " + str(n_weekday) + " " + str(n_day)
  
  
    














  
    
  return new_time
  
  

  

  
  

  

  
  
  
  
