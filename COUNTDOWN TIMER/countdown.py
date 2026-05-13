# COUNTDOWN TIMER IN PTHON

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1): # x is our counter that starts at my_time
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) # % 24 would have been included if we we had days in our timer
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # :02[no spaces] formats the seconds to always be 2 digits, adding a leading zero
    time.sleep(1)
        

# CREATING A RECTANGLE WITH NESTED LOOPS
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()