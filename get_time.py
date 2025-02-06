import random
from datetime import datetime, timedelta
import json
# Time expression production
exact_hour_word_gr = ['δώδεκα', 'μία', 'δύο', 'τρεις', 'τέσσερις', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννιά', 'δέκα', 'έντεκα', 'δώδεκα', 'μία', 'δύο', 'τρεις', 'τέσσερις', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα']
exact_hour_word_en = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
exact_hour_12 = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
exact_hour_24 = ['00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
minutes_gr = [' ακριβώς', ' και ένα', ' και δύο λεπτά', ' και 3', ' και τέσσερα', ' και πέντε', ' και έξι', ' και κάτι', ' και 8', ' και 9', ' και δέκα',
              ' και 11\'', ' και 12', ' και δεκατρία', ' και 14 λεπτά', ' και τέταρτο', ' και 16', ' και 17\'', ' και δεκαοκτώ', ' και δεκα εννέα', ' και είκοσι', ' και 21', ' και εικοσιδύο', ' και εικοσιτρία λεπτά', ' +24', ' και 25', ' και είκοσι έξι', ' κ 27', ' και 28', ' κ εικοσιεννιά', ' και μισή',
              ' και 31', ' και 32 λεπτά', ' kai 33', ' και τριάντατέσσερα', ' και 35', ' και τριανταέξι', ' κ 37', ' και 38', ' και 39', ' και 40',
              ' και 41 λεπτά', ' και σαράντα δύο λεπτά', ' και 43', ' +44', ' και σαρανταπέντε', ' kai 46', ' και 47 λεπτά', ' και 48\'', ' kai 49', ' και πενήντα', ' κ 51', ' και πενήντα δύο λεπτά', ' κ 53', ' και πενήντα τέσσερα', ' και 55', ' κ 56', ' και 57', ' και πενήντα οκτώ', ' και πενηντα εννιά', ' τζαστ', ''
]
minutes_gr2 = ['', ' και 1 λεπτό', ' και 2', ' και τρία λεπτά της ώρας', ' και 4', ' και πέντε', ' και έξι', ' και εφτά', ' και 8 min', ' και 9\'', ' και 10 λεπτά',
              ' κ 11', ' k 12', ' + 13', ' και 14 λεπτά της ώρας', ' και τέταρτο', ' και δεκάξι', ' και δέκα επτά λεπτά', ' κ 18', ' κ 19', ' και είκοσι λεπτά της ώρας', ' και εικοσιένα', ' kai eikosidyo', ' kai eikositria ', ' κ 24', ' και 25\'', ' κ 26\'', ' και 27', ' k eikosiokto', ' κ 29', ' και 30',
              ' παρά 29', ' παρά είκοσι οκτώ', ' para 27', ' παρά 26', ' παρά εικοσιπέντε', ' παρά εικοσιτέσσερα', ' παρα 23 λεπτά', ' para 22 lepta', ' παρά 21 λεπτά της ώρας', ' para 20',
              ' παρά 19', ' para 18', ' παρα 17', ' παρά δεκάξι', ' παρά τέταρτο', ' παρά 14', ' παρά δεκατρία', ' παρά 12 λεπτά', ' παρά 11 ολόκληρα λεπτά', ' παρά δέκα', ' παρά 9', ' παρά οχτω', ' para efta', ' παρά 6 λεπτά', ' παρά 5', ' παρά τέσσερα λεπτά', ' παρά 3', ' παρά 2', ' παρά ένα', ' just', ''
]
minutes_en = [
    "", '1 past ', '2 past ', '3 past ', '4 past ', '5 past ', '6 past ', 'some past ', '8 past ', '9 past ', '10 past ',
    '11 past ', '12 past ', '13 minutes past ', '14 minutes past ', 'a quarter past ', '16 past ', 'seventeen past ', '18 past ', 'nineteen past', '20 past ', '21 past ', '22 past ', '23 past ', 'twenty four minutes past ', '25 minutes past ', '26 past ', '27 past ', '28 min past ', '29 past ', 'half past ',
    '31 past ', '32 past ', '33 past ', '34 past ', '35 past ', '36 past ', '37 past ', '38 past ', '39 past ', '40 past ',
    '41 min past ', 'fourty two mins past ', '43 past ', '44 past ', '45 past ', '46 mins past ', '47 minutes past ', 'fourty eight past ', '49 past ', '50 past ', '51 past ', '52 past ', '53 past ', '54 past ', '55 past ', '56 past ', '57 past ', '58 past ', '59 past ', "o'clock"
]

minutes_en2 = [
    ' sharp', '1 past ', '2 past ', '3 past ', '4 past ', '5 past ', '6 past ', '7 past ', '8 past ', '9 past ', '10 past ',
    '11 minutes past ', "12' past ", '13 past ', '14 past ', 'a quarter past ', '16 past ', '17 past ', 'eighteen mins past ', '19 past ', '20 past ', '21 past ', '22 past ', '23 past ', 'twenty four minutes past ', '25 past ', '26 past ', '27 past ', '28 past ', '29 past ', 'half past ',
    '29 to ', '28 to ', 'twenty seven mins to ', '26 to ', '25 to ', '24 to ', '23 to ', '22 to ', '21 to ', '20 to ',
    'nineteen to ', 'eighteen minutes to ', '17 to ', '16 tio ', 'quarter to ', '14 to ', '13 to ', '12 to ', '11 to ', '10 to ', '9 to ', '8 to ', '7 to ', 'six to ', '5 to ', '4 to ', '3 minutes to ', '2 to ', '1 minute to ', "o'clock", ''
]

minutes_en4 = [
    ' ', ' o 1', ' 02', ' o 3 ', ' o four', ' o five', ' o6', ' o 7', ' o eight', ' o 9', ' ten',
    ' 11', "  twelve", ' 13', ' fourteen', ' fifteen', ' 16', ' 17', ' eighteen', ' 19', ' 20', ' 21', ' 22', ' 23', ' twenty four', ' 25', ' 26', ' 27', ' 28', ' 29', ' thirty',
    ' 31', ' 32', ' 33', ' thirty four', ' 35', ' 36', ' 37', ' 38', ' 39', ' 40',
    ' 41', ' fourty two', ' 43', ' 44', ' fourty 5', ' 46', ' 47', ' 48', ' 49', ' fifty', ' 51', ' 52', ' 53', ' fifty four', ' 55', ' 56', ' 57', ' 58', ' 59', "o'clock", ''
]

def create_dictionaries(hour_range):
    
    day_times_descr1 = {}
    day_times_descr2 = {}
    day_times_descr3 = {}
    day_times_descr4 = {} # dictionary with start - end time e.g. 6-7
    start_hour = 0
    end_hour = 24
    start_minutes = 0
    end_minutes = 60
    hour_ranges = {
        "morning": (8, 12),
        "afternoon": (12, 18),
        "evening": (18, 22),
        "night": (22, 24),
        "midnight": (0, 4),
        "early_morning": (4, 8),
        "noon": (12, 14),
        "midday": (12, 14)
    }
    if hour_range:
        if hour_range in hour_ranges:
            start_hour, end_hour = hour_ranges[hour_range]
        else:
            split_range = hour_range.split(":")
            start_hour = int(split_range[0])
            end_hour = int(split_range[0]) + 1
            start_minutes = int(split_range[1])
            end_minutes = int(split_range[1]) + 1
    
    hour_expressions_gr = [exact_hour_word_gr, exact_hour_12]
    hour_expressions_en = [exact_hour_word_en, exact_hour_12]

    exact_hour_gr = random.choice(hour_expressions_gr)
    exact_hour_en = random.choice(hour_expressions_en)

    add_at = random.random() < 0.7
    at_gr = "στις " if add_at else ""
    at_en = "at " if add_at else ""
    for j in range(start_hour, end_hour): # hour representation
        for i in range(start_minutes, end_minutes): #minute representation 
            time = f"{j:02d}:{i:02d}:00"
            if i > 30:
                day_times_descr1[str(j)+str(i)] = {
                    "en" : at_en + minutes_en[i] + exact_hour_en[j],
                    "gr" : at_gr + exact_hour_gr[j] + minutes_gr[i],
                    "time" : time
                }
            else:
                day_times_descr1[str(j)+str(i)] = {
                    "en" : at_en + minutes_en[i] + exact_hour_en[j],
                    "gr" : at_gr + exact_hour_gr[j] + minutes_gr[i],
                    "time" : time
                }

    for j in range(start_hour, end_hour): # hour representation
        for i in range(start_minutes, end_minutes): #minute representation
            time = f"{j:02d}:{i:02d}:00"
            if i > 30:
                day_times_descr2[str(j)+str(i)] = {
                    "en" : at_en + minutes_en2[i] + exact_hour_en[j + 1],
                    "gr" : at_gr + exact_hour_gr[j + 1] + minutes_gr2[i],
                    "time" : time
                }
            else:
                day_times_descr2[str(j)+str(i)] = {
                    "en" : at_en + exact_hour_en[j] + minutes_en4[i],
                    "gr" : at_gr + exact_hour_gr[j] + minutes_gr[i],
                    "time" : time
                }

    for j in range(start_hour, end_hour): # hour representation
        for i in range(start_minutes, end_minutes): #minute representation
            time = f"{j:02d}:{i:02d}:00"
            if j == 0 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " τα μεσάνυχτα",
                    "en" : at_en + exact_hour_en[j] + " in the midnight",
                    "time" : time
                }
            if 0 < j < 5 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : [exact_hour_gr[j] + " τα ξημερώματα"],
                    "en" : [exact_hour_en[j] + " in the early morning"],
                    "time" : time
                }
            if 5 <= j < 12 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " το πρωί",
                    "en" : at_en + exact_hour_en[j] + " in the morning",
                    "time" : time
                }
            if j == 12 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " το μεσημέρι",
                    "en" : at_en + exact_hour_en[j] + " at noon",
                    "time" : time
                }
            if 12 < j < 16 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " το μεσημέρι",
                    "en" : at_en + exact_hour_en[j] + " in the evening",
                    "time" : time
                }
            if 16 <= j < 20 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : exact_hour_gr[j] + " το απόγευμα",
                    "en" : exact_hour_en[j] + " in the evening",
                    "time" : time
                }
            if 20 <= j < 24 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " το βράδυ",
                    "en" : at_en + exact_hour_en[j] + " at night",
                    "time" : time
                }
    
    for j in range(start_hour, end_hour): # hour representation
        for i in range(start_minutes, end_minutes): #minute representation
            time = f"{j:02d}:{i:02d}:00"
            if j == 0 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " το βράδυ",
                    "en" : at_en + exact_hour_en[j] + " midnight",
                    "time" : time
                }
            if 0 < j < 12 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " π.μ.",
                    "en" : at_en + exact_hour_en[j] + " a.m.",
                    "time" : time
                }
            if 12 <= j <= 24 and i == 0:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : "στις " + exact_hour_gr[j] + " μ.μ.",
                    "en" : "at " + exact_hour_en[j] + " p.m.",
                    "time" : time
                }
            if 0 < j < 12 and i == 15:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : exact_hour_gr[j] + " και τέταρτο προ μεσημβρίας",
                    "en" : "at quarter past " + exact_hour_en[j] + " am",
                    "time" : time
                }
            if 12 <= j <= 24 and i == 15:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : at_gr + exact_hour_gr[j] + " και τέταρτο μετά μεσημβρίας",
                    "en" : at_en + "quarter past " + exact_hour_en[j] + " pm",
                    "time" : time
                }           
            if 0 <= j <= 12 and i == 30:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : exact_hour_gr[j] + "μισή πμ",
                    "en" : "at half past " + exact_hour_en[j] + " am",
                    "time" : time
                }
            if 12 < j <= 24 and i == 30:
                day_times_descr3[str(j)+str(i)] = {
                    "gr" : "στις " + exact_hour_gr[j] + " και 30 μμ",
                    "en" : "at 30 past " + exact_hour_en[j] + " pm",
                    "time" : time
                }
    if day_times_descr1:total_dict = [day_times_descr1]
    if day_times_descr2:total_dict.append(day_times_descr2)
    if day_times_descr3:total_dict.append(day_times_descr3)
    return total_dict


def get_time(hour_range=""):
  """
  Function to get a random time expression in Greek or English
    :param range: if not None, the function returns a time expression within the specified range like "morning", "afternoon", "evening", "night"
  """
  dictionaries = create_dictionaries(hour_range)

  # Use the random_index to select the appropriate dictionary
  selected_dict = dictionaries[random.randint(0, len(dictionaries)-1)]

  # Get a random key from the selected dictionary
  random_key = random.choice(list(selected_dict.keys()))
  
  #return selected_dict[random_key]
  return {'time': selected_dict[random_key], 'selected_time_dictionary': selected_dict, 'selected_time_index': random_key}

def get_end_time(start_time, duration, dictionary, selected_index):
    # Parse start_time
    time_format = "%H:%M:%S"
    start_datetime = datetime.strptime(start_time, time_format)
    #print("start datetime ", start_datetime)
    # Calculate duration in seconds
    duration_seconds = int(duration * 3600)
    
    # Compute the end time
    end_datetime = start_datetime + timedelta(seconds=duration_seconds)
    end_datetime = end_datetime.time().strftime(time_format)
    
    #print("dictionary ", dictionary['00'])
    #print("key ", key)
    # Retrieve record of dictionary on 'time' value
    end_datetime_dict = next((dictionary[key] for key in dictionary if dictionary[key]['time'] == end_datetime), None)
    #print("end datetime")
    #print(end_datetime)
    if not end_datetime_dict:
        end_datetime_dict = {'en':end_datetime[:5],'gr':end_datetime[:5], 'time':end_datetime}
    #print("end datetime dict size", len(end_datetime_dict))
    # Return formatted end time dictionary with 'time' 'en' 'gr' keys
    return end_datetime_dict

def get_time_space(hour_range="", space=0):
  """
  Function to get a random time expression in Greek or English
    :param range: if not None, the function returns a time expression within the specified range like "morning", "afternoon", "evening", "night"
  """
  start_time = get_time(hour_range)
  
  if space:
        try:
            # Assuming the time format is "HH:MM:SS"
            time_obj = datetime.strptime(start_time["time"], "%H:%M:%S")
            # Add the hours specified in space
            time_obj += timedelta(hours=int(space))
            # Update the time dictionary with the new time
            count_end_time = time_obj.strftime("%H:%M")
        except ValueError:
            print("Invalid time format or space value")
            return None
        end_time = get_time(count_end_time)
        # Change expressions to end date
        if "στις" in end_time["expr_gr"]:
            end_time["expr_gr"] = end_time["expr_gr"].replace("στις", "έως ")
        else:
            end_time["expr_gr"] = "μέχρι " + end_time["expr_gr"]

        if "at" in end_time["expr_en"]:
            end_time["expr_en"] = end_time["expr_en"].replace("at", "to ")
        else:
            end_time["expr_en"] = "until " + end_time["expr_en"]
  return [start_time, end_time]
    
  
