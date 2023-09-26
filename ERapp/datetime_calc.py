from datetime import datetime

# Input date and time in the format (day month year hh:mm:ss)
input_date_time = "26 09 2023 1:30:00"

# Convert the input date and time to a datetime object
input_datetime = datetime.strptime(input_date_time, "%d %m %Y %H:%M:%S")

# Get the current date and time
current_datetime = datetime.now()

# Calculate the difference between the input datetime and current datetime
time_difference = current_datetime - input_datetime

# Extract days, seconds, and microseconds from the time difference
days = time_difference.days
seconds = time_difference.seconds
microseconds = time_difference.microseconds


# Calculate weeks, days, hours, minutes, and seconds
weeks, days = divmod(days, 7)
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

# Print the time difference
print(f"Time difference: {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")