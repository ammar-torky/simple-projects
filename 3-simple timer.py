import time
your_time = int(input("Enter The Time in Seconds You Need : "))
for i in range(your_time,0,-1):
    seconds = i % 60 
    minutes = i // 60
    hourrs = i // 3600
    print(f"{hourrs:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)