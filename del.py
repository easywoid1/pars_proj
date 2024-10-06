from datetime import datetime, time

start_of_day = datetime.combine(datetime.now().date(), time.min)
print(start_of_day)
print(type(start_of_day))
