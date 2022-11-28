#find a way to extract date and time from the pc
from datetime import datetime




currentDateAndTime = datetime.now()
#print(currentDateAndTime)



currentTime = currentDateAndTime.strftime("%H:%M:%S")
x = currentTime.split(":")
print(x)
