# We Copy Logs For You ...
<br>

## What it copy?
It copies all the files created when doing **AVCS TEST**.\
Eg: Terminal logs, bag, can, txt files ...
<br>

## How to use?
There are 2 ways to run this script. Run it either from the Bash/Python script!
<br>
<br>

### Run from Python script:
```
python3 autonomous_logs.py $TICKET_NUMBER $STARTING_TIME_24_HR_FORMAT_ONLY_ENTER_HR
```
Example: my ticket number is TG-455, and i started my test at 1:30pm. I will run it in this way:
```
python3 autonomous_logs.py TG-455 13
```
Example: my ticket number is TG-455, and i started my test at 9:40am. I will run it this way:
```
python3 autonomous_logs.py TG-455 9
```
<br>
<br>

### Run from Bash script:

```
./autonomous_logs.py $TICKET_NUMBER $STARTING_TIME_24_HR_FORMAT_ONLY_ENTER_HR
```
Example: my ticket number is TG-455, and i started my test at 1:30pm. I will run it in this way:
```
./autonomous_logs.py TG-455 13
```
Example: my ticket number is TG-455, and i started my test at 9:40am. I will run it this way:
```
./autonomous_logs.py TG-455 9
```
