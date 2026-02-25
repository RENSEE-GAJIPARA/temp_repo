import datetime
# from datetime import datetime, timezone
import time

#Q1
'''
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.second)
'''

#Q2
'''

now = time.ctime()
print(now)

epoch = time.time()
print(epoch)
'''

#Q3
'''
now = datetime.datetime.now()
formated = datetime.datetime.strftime(now, "%d-%m-%Y")
formated2 = datetime.datetime.strftime(now, "%m-%d-%Y")

print(formated)
print(formated2)

time = datetime.datetime.strftime(now, "%H:%M:%S")
print(time)

time_12 = datetime.datetime.strftime(now, "%I:%M:%S %p")
print(time_12)
'''

#Q4
'''
print("Enter first date:")
y1 = int(input("Year: "))
m1 = int(input("Mounth: "))
d1 = int(input("Day: "))
d1 = datetime.datetime(y1,m1,d1)

print("Enter second date:")
y2 = int(input("Year: "))
m2 = int(input("Mounth: "))
d2 = int(input("Day: "))
d2 = datetime.datetime(y2,m2,d2)

if d2 > d1 :
    gap = d2 - d1
    print(gap)
else:
    gap = d1 - d2
    print(gap)

now = datetime.datetime.now()
new = now + datetime.timedelta(days=7)
print(f"New date: {new}")
'''

#Q5
'''
date = input("Enter a date(yyyy-mm-dd): ")
converted = datetime.datetime.strptime(date,"%Y-%m-%d")
print(converted)

formated = datetime.datetime.strftime(converted,"%Y-%m-%d %H:%M:%S")
print(formated)
'''

#Q6
'''
start = time.perf_counter()
time.sleep(5)
end = time.perf_counter()

print(f"Execution time is {end - start} sec")
'''

#Q7
'''
utc = datetime.now(timezone.utc)
print(f"Current time in UTC: {utc}")

local = datetime.now()
print(f"Local time: {local}")
'''

#Q8
'''
running = False
start_time = 0
elapsed = 0

while True:
    print("1 = Start | 2 = Stop/Pause | 3 = Reset | 4 = Quit")
    command = int(input("\nEnter command: "))

    match command:
        case 1:
            if not running:
                start_time = time.time() - elapsed
                running = True
                print("Stopwatch started...")

                while running:
                    elapsed = time.time() - start_time
                    hours = int(elapsed // 3600)
                    minutes = int((elapsed % 3600) // 60)
                    seconds = int(elapsed % 60)

                    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="", flush=True)
                    time.sleep(0.01)
            else:
                print("Already running!")

        case 2:
            if running:
                running = False
                elapsed = time.time() - start_time
                hours = int(elapsed // 3600)
                minutes = int((elapsed % 3600) // 60)
                seconds = int(elapsed % 60)
                print(f"\nPaused at: {hours:02}:{minutes:02}:{seconds:02}")
            else:
                print("Stopwatch is not running.")

        case 3:
            running = False
            elapsed = 0
            start_time = 0
            print("Reset! Time: 00:00:00")

        case 4:
            print("Exiting stopwatch.")
            break

        case _:
            print("Invalid command.")
'''

#Q9
'''
seconds = int(input("Enter number of seconds to countdown: "))

for i in range(seconds, 0, -1):
    print(f"Time remaining: {i} seconds", end="\r")
    time.sleep(1)

print("\nTime is up!")     
'''

#Q10
'''
year = int(input("Enter a year: "))
date = datetime(year, 1, 1)

if date.year % 4 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
'''

#Q11
'''
date = input("Enter a date(yyyy-mm-dd): ")
converted = datetime.datetime.strptime(date,"%Y-%m-%d")
day =  converted.strftime("%A")
print(f"Day of the week: {day}")
'''

#Q12
'''
remainder = input("Enter your remainder message: ")
rem_time = input("Enter time(HH:MM:SS): ")

now = datetime.datetime.now()
target = datetime.datetime.strptime(rem_time, "%H:%M:%S").replace(year=now.year, month=now.month, day=now.day)

wait = (target - now).total_seconds()

if wait < 0:
    print("Time already gone!!")

else:
    print(f"Remainder set for : {rem_time}")
    time.sleep(wait)
    print(f"Remainder : {remainder}")
'''