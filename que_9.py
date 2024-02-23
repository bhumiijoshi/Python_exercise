from datetime import datetime
import portion

def count_hours(start, end, night_start=22, night_end=6):
  
    start_date = datetime.strptime(start, '%Y/%m/%d %I:%M:%S %p')
    end_date = datetime.strptime(end, '%Y/%m/%d %I:%M:%S %p')

    day_interval = portion.closed(start_date.replace(hour=night_end, minute=0), end_date.replace(hour=night_start,minute=0))
    night_interval = portion.closed(start_date.replace(hour=night_start,minute=0), end_date.replace(hour=night_end,minute=0))

    total_hours = (end_date - start_date).total_seconds() / 3600

    if day_interval.overlaps(night_interval):
        intersection_time = day_interval & night_interval
        overlap_time = (intersection_time.upper - intersection_time.lower).seconds / 3600
        total_hours -= overlap_time

    return total_hours

start = input("Enter start date in YYYY/MM/DD HH:MM:SS AM/PM: ")
end = input("Enter end date in YYYY/MM/DD HH:MM:SS AM/PM: ")

night_start = 22                   
night_end = 6

total_hours = count_hours(start, end, night_start, night_end)
print("Total hours excluding night hours:", total_hours)