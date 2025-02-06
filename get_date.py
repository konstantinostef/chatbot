import calendar
import random
from datetime import datetime, timedelta

greek_days = {'Monday':'Δευτέρα', 'Tuesday':'Τρίτη', 'Wednesday':'Τετάρτη', 'Thursday':'Πέμπτη', 'Friday':'Παρασκευή', 'Saturday':'Σάββατο', 'Sunday':'Κυριακή'}
greek_months = {'January':'Ιανουαρίου', 'February':'Φεβρουαρίου', 'March':'Μαρτίου', 'April':'Απριλίου', 'May':'Μαΐου', 'June':'Ιουνίου', 'July':'Ιουλίου', 'August':'Αυγούστου', 'September':'Σεπτεμβρίου', 'October':'Οκτωβρίου', 'November':'Νοεμβρίου', 'December':'Δεκεμβρίου'}
greek_months2 = {'January':'Γενάρη', 'February':'Φλεβάρη', 'March':'Μάρτη', 'April':'Απρίλη', 'May':'Μάη', 'June':'Ιούνη', 'July':'Ιούλη', 'August':'Αυγούστου', 'September':'Σεπτέμβρη', 'October':'Οκτώβρη', 'November':'Νοέμβρη', 'December':'Δεκέμβρη'}
WEEKDAYS_MAP = {
    'MO': 0, 'TU': 1, 'WE': 2, 'TH': 3, 'FR': 4, 'SA': 5, 'SU': 6
}
def get_date_suffix(day: int) -> str:
    if 11 <= day <= 13:
        return "th"
    last_digit = day % 10
    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"

def get_single_day(desired_weekday=""):
    year = 2025
    # Randomly select a date
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    weekday = calendar.weekday(year, month, day)
    
    # Select a day that is not in weekend
    if desired_weekday == "weekday":
        while weekday in [5, 6]:
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            weekday = calendar.weekday(year, month, day)
    
    # Select a day that is in weekend
    if desired_weekday == "weekend":
        while weekday not in [5, 6]:
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            weekday = calendar.weekday(year, month, day)

    # Convert calendar.weekday integer to day name string
    day_of_week = list(calendar.day_name)[weekday]
    month_name = calendar.month_name[month]
    day_of_week_gr = greek_days[day_of_week]
    
    # select random month name in Greek (Φεωρουάριος or Φλεβάρης)
    month_ind = random.randint(1, 2)
    month_name_gr = greek_months[month_name] if month_ind == 1 else greek_months2[month_name]
    
    format_en = [
        f" on {day_of_week} {day}/{month}",
        f"{day} {month_name} {year}", 
        f"{day}{get_date_suffix(day)} {month_name} {year}", 
        f"{day}/{month}/{year}",
        f"{month}/{day}", 
        f"{month}/{day}/{year}", 
        f"{month_name} {day}{get_date_suffix(day)}",
        f"{month_name} {day}{get_date_suffix(day)} {year}",
        f"{month_name[:3]}. {day}{get_date_suffix(day)}",
        f"{month_name[:3]}. {day}{get_date_suffix(day)} {year}",
        f"{day} {month_name[:3]}",
        f"{month_name[:3]} {day}",
    ]
    
    greek_article = ' το ' if day_of_week == 'Saturday' else ' την '
    format_gr = [
        f"{greek_article}{day_of_week_gr} {day}/{month}",
        f"{day} {month_name_gr} {year}", 
        f"{day}η {month_name_gr} {year}", 
        f"{day}/{month}/{year}",
        f"{day}/{month}", 
        f"{day}/{month}/{year}", 
        f"{day}η {month_name_gr}",
        f"{day} {month_name_gr} {year}",
        f"{month_name_gr[:3]}. {day}",
        f"{month_name_gr[:3]}. {day} {year}",
        f"{day} {month_name_gr[:3]}",
        f"{month_name_gr[:3]} {day}",
    ]
    # Select a random format for both languages
    ind = random.randint(0, len(format_en) - 1)
    return {
        "gr": format_gr[ind],
        "en": format_en[ind],
        "date": f"{year}-{month:02d}-{day:02d}"
    }

def get_start_date(given_rrule: dict) -> str:
    today = datetime.today()
    year = today.year
    if not given_rrule:
        return today
    if given_rrule['FREQ'] == 'WEEKLY' and 'BYDAY' in given_rrule:
        weekdays_str = given_rrule['BYDAY']
        weekdays = [day.strip() for day in weekdays_str.split(",")] if weekdays_str else []
        today_weekday = today.weekday()

        # Convert weekday names to integer values and sort
        target_days = sorted(WEEKDAYS_MAP[day] for day in weekdays if day in WEEKDAYS_MAP)
        #print("weekdays ", weekdays)
        # Find the minimum number of days to add to reach the next target weekday
        days_until_next = min((day - today_weekday) % 7 for day in target_days)

        next_date = today + timedelta(days=days_until_next)
    elif given_rrule['FREQ'] == 'MONTHLY' and 'BYMONTHDAY' in given_rrule:
        next_date = int(given_rrule['BYMONTHDAY'])
        # Check if target_day is valid for the current month or February
        if not (1 <= next_date <= 31):
            raise ValueError("Day must be between 1 and 31")


        # Current month
        month = today.month

        # Check if the target day has already passed in the current month
        if today.day > next_date:
            month += 1

        # Handle month/year overflow
        if month > 12:
            month = 1
            year += 1

        # Find the last valid day for the month in the given year
        while True:
            try:
                next_date = datetime(year, month, next_date)
                break
            except ValueError:
                # Decrement the target day until a valid date is found
                next_date -= 1
    elif given_rrule['FREQ'] == 'YEARLY':
        
        next_date = datetime(year, int(given_rrule['BYMONTH']), int(given_rrule['BYMONTHDAY']))
    else:
        next_date = today

    return next_date.strftime('%Y-%m-%d')

def get_end_date(given_datetime):

    dt = datetime.strptime(given_datetime, '%Y%m%dT%H%M%SZ')
    # Format to desired date string
    return dt.strftime('%Y-%m-%d')