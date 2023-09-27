print("Time Converter")
time = input("Enter an integer for seconds: ")
minute = int(time) // 60
second = int(time) % 60
print(time, "seconds is", minute, "minutes and", second, "seconds")