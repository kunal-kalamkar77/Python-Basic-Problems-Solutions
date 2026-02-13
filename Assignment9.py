#Problem statement - Create a program to find angle formed bt hour hand on clock at given time.
time = input("Enter time in HH:MM format: ")
hour, minute = map(int, time.split(':'))
hour_angle = (hour % 12) * 30 + (minute / 60) * 30
print(f"The angle formed by the hour hand at {time} is: {hour_angle} degrees.")
