#find a way to extract date and time from the pc
from datetime import datetime




currentDateAndTime = datetime.now()
#print(currentDateAndTime)



currentTime = currentDateAndTime.strftime("%H:%M:%S")
currentDate = currentDateAndTime.strftime("%d/%m/%Y")
pc_time_split = currentTime.split(":")
#print(x)
#print(currentTime)
pc_date_split = currentDate.split("/")
pc_extract_date = int(pc_date_split[0])

print(pc_extract_date)



print("mx need to respect girls")
