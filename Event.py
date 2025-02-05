import random
from get_date import *
from get_time import *

custom_events = [
    'Το Νοέμβριο και το Δεκέμβριο κάθε Πέμπτη 5-9 έχω σεμινάριο εκτός απ τα Χριστούγεννα',
    'Όλο το καλοκαίρι θα δουλεύω σεζόν 5 με 12 το βράδυ',
    'Φυσικοθεραπεία για 3 μήνες από την Τετάρτη 5 Φεβρουαρίου και κάθε Τετάρτη 8-9',
]

event_data = [{'en': {'title': 'birthday party', 'pre': 'i have a', 'post': 'for my son', 'recurring': 'Yearly', 'duration': 3}, 'gr': {'title': 'πάρτυ γενεθλίων', 'pre': 'έχω ένα', 'post': 'για τον γιο μου', 'recurring': 'Yearly', 'duration': 3}},
{'en': {'title': 'job interview', 'pre': 'plan a', 'post': 'for a new job', 'recurring': 'Single', 'duration': 2}, 'gr': {'title': 'συνέντευξη', 'pre': 'με έχουν καλέσει για', 'post': 'για μια νέα δουλειά', 'recurring': 'Single', 'duration': 2}},
{'en': {'title': 'football match', 'pre': 'i am going to a', 'post': 'with my friends', 'recurring': 'Weekly', 'duration': 1.5}, 'gr': {'title': 'αγώνα ποδοσφαίρου', 'pre': 'πρόκειται να πάω σε', 'post': 'με τους φίλους μου', 'recurring': 'Weekly', 'duration': 1.5}},
{'en': {'title': 'doctor appointment', 'pre': 'i have a', 'post': 'with Dr. Smith', 'recurring': 'Single', 'duration': 1}, 'gr': {'title': 'ραντεβού για γιατρό', 'pre': 'έχω ένα', 'post': 'με τον γιατρό μου', 'recurring': 'Single', 'duration': 1}},
{'en': {'title': 'meeting with friends', 'pre': 'i am planning a', 'post': 'at the pub', 'recurring': 'Monthly', 'duration': 2}, 'gr': {'title': 'εξοδο με φίλους', 'pre': 'βάλε', 'post': 'στο μπαρ', 'recurring': 'Monthly', 'duration': 2}},
{'en': {'title': 'shopping', 'pre': 'i need to go', 'post': 'with my wife', 'recurring': 'Monthly', 'duration': 2.5}, 'gr': {'title': 'ψώνια', 'pre': 'χρειάζομαι να πάω για', 'post': 'με τη γυναίκα μου', 'recurring': 'Monthly', 'duration': 2.5}},
{'en': {'title': 'dinner with family', 'pre': 'i have a', 'post': 'at home', 'recurring': 'Monthly', 'duration': 2}, 'gr': {'title': 'δείπνο με την οικογένεια', 'pre': 'έχω', 'post': 'στο σπίτι', 'recurring': 'Monthly', 'duration': 2}},
{'en': {'title': 'visit to the dentist', 'pre': 'i have a', 'post': 'for a checkup', 'recurring': 'Single', 'duration': 1}, 'gr': {'title': 'επίσκεψη στον οδοντίατρο', 'pre': 'βάλε μια', 'post': 'για έλεγχο', 'recurring': 'Single', 'duration': 1}},
{'en': {'title': 'lunch with colleagues', 'pre': 'i have a', 'post': 'at the office', 'recurring': 'Yearly', 'duration': 2}, 'gr': {'title': 'γεύμα με συναδέλφους', 'pre': 'προγραμμάτισε', 'post': 'από το γραφείο', 'recurring': 'Yearly', 'duration': 2}},
{'en': {'title': 'visit to the hairdresser', 'pre': 'i need to go', 'post': 'for a haircut', 'recurring': 'Monthly', 'duration': 1}, 'gr': {'title': 'κομμωτήριο', 'pre': 'χρειάζομαι να πάω', 'post': 'οπωσδήποτε', 'recurring': 'Monthly', 'duration': 1}},
{'en': {'title': 'haircut', 'pre': 'i need to go', 'post': 'for a', 'recurring': 'Monthly', 'duration': 1}, 'gr': {'title': 'Κούρεμα', 'pre': 'χρειάζομαι', 'recurring': 'Monthly', 'duration': 1}},
{'en': {'title': 'doctor', 'pre': 'i have a', 'post': 'appointment', 'recurring': 'Single', 'duration': 1}, 'gr': {'title': 'ιατρικό ραντεβού', 'pre': 'έχω ένα', 'post': 'με τον κ. Χριστοδούλου', 'recurring': 'Single', 'duration': 1}},
{'en': {'title': 'doctor appointment', 'pre': 'i have a', 'post': 'with Dr. Smith', 'recurring': 'Single', 'duration': 1}, 'gr': {'title': 'ραντεβού με γιατρό', 'pre': 'έχω ένα', 'recurring': 'Single', 'duration': 1}},
{'en': {'title': 'meeting', 'pre': 'i have a', 'post': 'with John', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'συνάντηση', 'pre': 'έχω μια', 'post': 'με τον Τάσο', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'music lesson', 'pre': 'i have a', 'post': 'with my teacher', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'μάθημα κιθάρας', 'pre': 'έχω', 'post': 'με τον δάσκαλο μου', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'dance lesson', 'pre': 'i have a', 'post': 'with my instructor', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'μάθημα χορού', 'pre': 'γράψε', 'post': 'με τον δάσκαλο μου', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'yoga class', 'pre': 'i have a', 'post': 'with my yoga teacher', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'μάθημα γιόγκα', 'pre': 'βάλε', 'post': 'στις Ροές', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'pilates class', 'pre': 'i have a', 'post': 'with my husband', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'πιλάτες', 'pre': 'θα πάω για', 'post': 'με τον άντρα μου', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'gym workout', 'pre': 'i have a', 'post': 'at the gym', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'γυμναστήριο', 'pre': 'θα πάω', 'post': 'με την Βασιλική', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'swimming', 'pre': 'i am going', 'post': 'with Jessica', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'κολύμπι', 'pre': 'πρόκειται να πάω', 'post': 'με την Όλγα', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'running with Mike', 'pre': 'i am going', 'post': 'with my friend Mike', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'τρέξιμο', 'pre': 'θέλω να πάω για', 'post': 'με το γιο μου Δημήτρη', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'running with Edward', 'pre': 'i am going', 'post': 'with my friend Mike', 'recurring': 'Single', 'duration': 1}, 'gr': {'title': 'τρέξιμο με Αλέξη', 'pre': 'θέλω να πάω για', 'recurring': 'Single', 'duration': 1}},
{'en': {'title': 'boxing training', 'pre': 'i am going', 'post': 'with my friend John', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'προπόνηση μποξ', 'pre': 'πρόκειται να πάω', 'post': 'με τον φίλο μου τον Γιάννη', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'cycling', 'pre': 'i am going', 'post': 'with my friends', 'recurring': 'Weekly', 'duration': 1}, 'gr': {'title': 'ποδηλασία', 'pre': 'γράψε μου να πάω', 'post': 'με τους φίλους μου', 'recurring': 'Weekly', 'duration': 1}},
{'en': {'title': 'tennis match', 'pre': 'i have a', 'post': 'with my friend John', 'recurring': 'Weekly', 'duration': 2.5}, 'gr': {'title': 'αγώνα τέννις', 'pre': 'έχω', 'post': 'με τον φίλο μου τον Μήτσο', 'recurring': 'Weekly', 'duration': 2.5}},
{'en': {'title': 'football training', 'pre': 'i have a', 'post': 'with my team', 'recurring': 'Weekly', 'duration': 2}, 'gr': {'title': 'προπόνηση ποδοσφαίρου', 'pre': 'έχω', 'post': 'με την ομάδα μου', 'recurring': 'Weekly', 'duration': 2}},
{'en': {'title': 'basketball match', 'pre': 'i have a', 'post': 'with my friends', 'recurring': 'Weekly', 'duration': 2}, 'gr': {'title': 'αγώνα μπάσκετ', 'pre': 'έχω ένα', 'post': 'με τους φίλους μου', 'recurring': 'Weekly', 'duration': 2}},
{'en': {'title': 'school', 'pre': 'i have', 'post': 'on foot', 'recurring': 'Daily', 'duration': 6}, 'gr': {'title': 'σχολείο', 'pre': 'έχω', 'post': 'με τα πόδια', 'recurring': 'Daily', 'duration': 6}},
{'en': {'title': 'work', 'pre': 'i have to go to', 'post': 'by bus', 'recurring': 'Daily', 'duration': 8}, 'gr': {'title': 'δουλειά', 'pre': 'πρέπει να πάω στη', 'post': 'με το λεωφορείο', 'recurring': 'Daily', 'duration': 8}},
{'en': {'title': 'university', 'pre': 'i have', 'recurring': 'Daily', 'duration': 8}, 'gr': {'title': 'πανεπιστήμιο', 'pre': 'έχω', 'recurring': 'Daily', 'duration': 8}},
{'en': {'title': 'college', 'pre': 'i have', 'recurring': 'Daily', 'duration': 8}, 'gr': {'title': 'κολλέγιο', 'pre': 'έχω', 'recurring': 'Daily', 'duration': 8}},
{'en': {'title': 'meeting with the boss', 'pre': 'i have a', 'recurring': 'Monthly', 'duration': 2}, 'gr': {'title': 'συνάντηση με τον αφεντικό', 'pre': 'έχω μια', 'recurring': 'Monthly', 'duration': 2}},
{'en': {'title': 'meeting with the teacher', 'pre': 'i have a', 'recurring': 'Monthly', 'duration': 2}, 'gr': {'title': 'συνάντηση με τον καθηγητή', 'pre': 'έχω μια', 'recurring': 'Monthly', 'duration': 2}},
{'en': {'title': 'parent-teacher meeting', 'pre': 'i have a', 'recurring': 'Monthly', 'duration': 2}, 'gr': {'title': 'συνάντηση γονέων-καθηγητών', 'pre': 'έχω μια', 'recurring': 'Monthly', 'duration': 2}},
{'en': {'title': 'meeting with the principal', 'pre': 'i have a', 'recurring': 'Yearly', 'duration': 2}, 'gr': {'title': 'συνάντηση με τον διευθυντή', 'pre': 'έχω μια', 'recurring': 'Yearly', 'duration': 2}},
{'en': {'title': 'meeting with the school counselor', 'pre': 'i have a', 'recurring': 'Yearly', 'duration': 2}, 'gr': {'title': 'συνάντηση με τον σχολικό σύμβουλο', 'pre': 'έχω μια', 'recurring': 'Yearly', 'duration': 2}},
{'en': {'title': 'meeting with the university professor', 'pre': 'i have a', 'recurring': 'Monthly', 'duration': 2}, 'gr': {'title': 'συνάντηση με τον καθηγητή του πανεπιστημίου', 'pre': 'έχω μια', 'recurring': 'Monthly', 'duration': 2}},
]

frequency = ['DAILY', 'WEEKLY', 'MONTHLY', 'YEARLY']
days = {"all":['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU'], "weekdays":['MO', 'TU', 'WE', 'TH', 'FR'], "weekend":['SA', 'SU']}

# Mapping of short day codes to full day names
day_names_en = {
    "MO": "Monday",
    "TU": "Tuesday",
    "WE": "Wednesday",
    "TH": "Thursday",
    "FR": "Friday",
    "SA": "Saturday",
    "SU": "Sunday"
}
day_names_gr = {
    "MO": "Δευτέρα",
    "TU": "Τρίτη",
    "WE": "Τετάρτη",
    "TH": "Πέμπτη",
    "FR": "Παρασκευή",
    "SA": "Σάββατο",
    "SU": "Κυριακή"
}

month_names = {'en': {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}, 'gr': {'1':'Ιανουαρίου', '2':'Φεβρουαρίου', '3':'Μαρτίου', '4':'Απριλίου', '5':'Μαΐου', '6':'Ιουνίου', '7':'Ιουλίου', '8':'Αυγούστου', '9':'Σεπτεμβρίου', '10':'Οκτωβρίου', '11':'Νοεμβρίου', '12':'Δεκεμβρίου'}}

class Event:
    
    event: dict
    summary: dict # {    'summary': summary
    start: dict #       'start': {'dateTime': '2015-05-28T09:00:00-07:00', 'timeZone': 'America/Los_Angeles',}
    end: dict   #       'end': {'dateTime': '2015-05-28T09:00:00-07:00', 'timeZone': 'America/Los_Angeles',}
    recurrence: str #  'recurrence': ['RRULE:FREQ=DAILY;COUNT=2']
    time: dict
    selected_time_dictionary: str
    selected_time_index: int
    prompt: dict
    start_date: str
    end_date: str
    end_time_dict: dict
    end_time: dict
    rrule: dict
    expression: dict
    is_single: bool
    '''
    'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
    
    '''

    def __init__(self):
        # Pick an event
        self.event = self.get_event()
        #print(self.event['en'])
        # Pick a start time and keep which time dictionary was selected (format of time expression) and which index in order to calculate and time and get expression
        selected_time_data = get_time()
        self.time = selected_time_data['time']
        self.selected_time_dictionary = selected_time_data['selected_time_dictionary']
        self.selected_time_index = selected_time_data['selected_time_index']
        self.end_time_dict = get_end_time(self.time['time'], self.event['en']['duration'], self.selected_time_dictionary, self.selected_time_index)
        #print(self.end_time_dict)
        self.end_time = self.end_time_dict['time']
        #print(self.end_time)
        # According to event's data create rrule. Also picks random recurring days. Single events don't have rrule at all.
        self.rrule = self.create_rrule()
        #print(self.rrule)
        # Make human expressions on that rrule if one (Single events don't have rrule)
        if self.rrule: self.expression = self.express_rrule()
        # Create user prompt. Also picks a random date for single events
        self.prompt = self.get_prompt()
        #print(self.prompt)
        # Keep events title as 'summary'
        self.summary = {'en': self.event['en']['title'],
                        'gr': self.event['gr']['title']}
        #print(self.summary)
        # Count start date and assign it to start_date
        if not self.is_single: self.start_date = get_start_date(self.rrule)
        #print(self.start_date)
        self.end_date = get_end_date(self.rrule['UNTIL']) if not self.is_single else self.start_date
        
    def create_event(self):
        #print(self.summary)
        event_to_return = {}
        event_to_return = {
            'en': {
                'summary':self.summary['en'],
                'start': {
                    'dateTime': self.start_date + 'T' + self.time['time'] + "+02:00', 'timeZone':'Eastern European Time',"
                },
                'end': {
                    'dateTime': self.end_date + 'T' + self.end_time + "+02:00', 'timeZone':'Eastern European Time',"
                },
            },
            'gr': {
                'summary':self.summary['gr'],
                'start': {
                    'dateTime': self.start_date + 'T' + self.time['time'] + "+02:00', 'timeZone':'Eastern European Time',"
                },
                'end': {
                    'dateTime': self.end_date + 'T' + self.end_time + "+02:00', 'timeZone':'Eastern European Time',"
                },
            }
        }
        if not self.is_single:
            event_to_return['en']['recurrence'] = ['RRULE:' + str(self.rrule)]
            event_to_return['gr']['recurrence'] = ['RRULE:' + str(self.rrule)]
        return event_to_return
    
    @classmethod
    def get_event(cls):
        """
        Picks a random event from the event data list.

        Returns:
            dict: Event data dictionary with 'en' and 'gr' keys.
        """
        index = random.randint(0, len(event_data) - 1)
        event_en = event_data[index]['en']
        event_gr = event_data[index]['gr']
        return {'en': event_en, 'gr': event_gr}
    
    
    
    def get_prompt(self, single=0, separator=' '):
        """
        Creates user prompt with random syntax according to the rrules data. Also Picks a Day for single events.
        Also adds from - to or at to time expressions
        Args:
            single:
                If Single = 0 it follows recurrency of rrule.
                If single = 1 it forces all events to single
            separator: String to use between elements (default single space)
            
        Returns:
            Dictionary with 'en' and 'gr' keys for the user prompt
        """
        
        start_time = self.time
        end_time = self.end_time_dict
        to_en_choices = [' to ', ' until ', ' - ', ' ']
        to_gr_choices = [' με ', ' εως ',' - ', ' ']
        to_en = random.choice(to_en_choices)
        to_gr = random.choice(to_gr_choices)
        #print(start_time['en'], to_en, end_time)
        # Choose randomly if only start time is given (propability 0.3) or start to end time is given (propability 0,7)
        start_only_format = random.random() < 0.3
        if start_only_format:
            time_expr_en = start_time['en']
            time_expr_gr = start_time['gr']
        else:
            start_time['en'] = start_time['en'].replace('at', 'from')
            start_time['gr'] = start_time['gr'].replace('στις', 'από')
            end_time['en'] = end_time['en'].replace('at', 'to')
            end_time['gr'] = end_time['gr'].replace('στις', ' ως τις')
            time_expr_en = start_time['en'] + to_en + end_time['en']
            time_expr_gr = start_time['gr'] + to_gr + end_time['gr']
        #print("to_en " + to_en)
        #print("to_gr  " + to_gr)
        if self.event['en']['recurring'] == 'Single' or single == 1:
            self.is_single = True
        else:
            self.is_single = False

        if self.is_single == True:
            day = get_single_day()
            self.start_date = day['date']
            # Randomly decide whether to include 'pre' and/or 'post' with 33% chance each
            include_pre = random.random() < 0.7
            include_post = random.random() < 0.7
    
            title_en = ""
            title_gr = ""
            
            if include_pre and 'pre' in self.event['en']:
                title_en += self.event['en']['pre'] + " "
            if include_pre and 'pre' in self.event['gr']:
                title_gr += self.event['gr']['pre'] + " "

            title_en += self.event['en']['title']
            title_gr += self.event['gr']['title']

            if include_post and 'post' in self.event['en']:
                title_en += " " + self.event['en']['post']
            if include_post and 'post' in self.event['gr']:
                title_gr += " " + self.event['gr']['post']
            # Convert elements to list and shuffle
            elements_list_en = [title_en, day['en'], time_expr_en]
            elements_list_gr = [title_gr, day['gr'], time_expr_gr]
            random.shuffle(elements_list_en)
            random.shuffle(elements_list_gr)
            # Join elements with separator to make user prompt
            user_prompt_en = separator.join(elements_list_en)
            user_prompt_gr = separator.join(elements_list_gr)
        else:
            if self.event['en']['recurring'] == 'Weekly':
                elements_list_en = [self.event['en']['title'], self.expression['en'], time_expr_en]
                elements_list_gr = [self.event['gr']['title'], self.expression['gr'], time_expr_gr]
                random.shuffle(elements_list_en)
                random.shuffle(elements_list_gr)
                user_prompt_en = separator.join(elements_list_en)
                user_prompt_gr = separator.join(elements_list_gr)
            elif self.event['en']['recurring'] == 'Monthly':
                elements_list_en = [self.event['en']['title'], self.expression['en'], time_expr_en]
                elements_list_gr = [self.event['gr']['title'], self.expression['gr'], time_expr_gr]
                random.shuffle(elements_list_en)
                random.shuffle(elements_list_gr)
                user_prompt_en = separator.join(elements_list_en)
                user_prompt_gr = separator.join(elements_list_gr)
            elif self.event['en']['recurring'] == 'Yearly':
                elements_list_en = [self.event['en']['title'], self.expression['en']]
                elements_list_gr = [self.event['gr']['title'], self.expression['gr']]
                random.shuffle(elements_list_en)
                random.shuffle(elements_list_gr)
                user_prompt_en = separator.join(elements_list_en)
                user_prompt_gr = separator.join(elements_list_gr)
            else:
                elements_list_en = [self.event['en']['title'], self.expression['en'], time_expr_en]
                elements_list_gr = [self.event['gr']['title'], self.expression['gr'], time_expr_gr]
                random.shuffle(elements_list_en)
                random.shuffle(elements_list_gr)
                user_prompt_en = separator.join(elements_list_en)
                user_prompt_gr = separator.join(elements_list_gr)

        return {'en' : user_prompt_en, 'gr': user_prompt_gr}

    def create_rrule(self, days_of_week="all"):
        """
        Creates a recurrence rule for an event based on the event title and
        the selected days.

        Args:
            days_of_week (str): Days to select for the recurrence rule. One of "all", "weekdays", or "weekend".

        Returns:
            dict: Recurrence rule dictionary.
        """
        if self.event['en']['recurring'] == 'Weekly':
            rrule = {
            "FREQ": self.event['en']['recurring'].upper(),
            "BYDAY": self.select_random_days_of_week(days[days_of_week]),
            "UNTIL": "20250630T000000Z"
            }
        elif self.event['en']['recurring'] == 'Monthly':
            rrule = {
            "FREQ": self.event['en']['recurring'].upper(),
            "BYMONTHDAY": random.randint(1, 28),
            "UNTIL": "20251231T000000Z"
            }
        elif self.event['en']['recurring'] == 'Yearly':
            rrule = {
            "FREQ": self.event['en']['recurring'].upper(),
            "BYMONTH": random.randint(1, 12),
            "BYMONTHDAY": random.randint(1, 28),
            "UNTIL": "20300101T000000Z"
            }
        elif self.event['en']['recurring'] == 'Single':
            rrule = ""
        else:
            rrule = {
            "FREQ": "DAILY",
            "UNTIL": "20250630T000000Z"
            }
        
        return rrule

    def express_rrule(self):
        """
        Expresses a recurrence rule in natural language with random syntax
        
        Args:
            rrule: Dictionary with recurrence rule information
        
        Returns:
            List of strings with natural language expressions of the recurrence rule
        """
        # Get frequency and byday values
        
        if self.rrule["FREQ"] == "WEEKLY":
            byday = self.rrule.get("BYDAY", [])
        
            # Get full day names
            byday_names_en = [day_names_en[day] for day in byday]
            byday_names_gr = [day_names_gr[day] for day in byday]
            if len(byday_names_en) == 1:
                prompt_en = 'every ' + byday_names_en[0]
                prompt_gr = 'κάθε ' + byday_names_gr[0]
            else:
                # randomly select "and" or "," at the end of the list
                sel = random.randint(0, 1)
                add_and_en = " and " if sel == 1 else " "
                add_and_gr = " και " if sel == 1 else " "
                add_every_en = "every " if sel == 1 else ""
                add_every_gr = "κάθε " if sel == 1 else ""
                prompt_en = add_every_en + ", ".join(byday_names_en[:-1]) + add_and_en + byday_names_en[-1]
                prompt_gr = add_every_gr + ", ".join(byday_names_gr[:-1]) + add_and_gr + byday_names_gr[-1]
            
        elif self.rrule["FREQ"] == "MONTHLY":
            post_expr_en = [' of each month', ' of every month']
            post_expr_gr = [' του μήνα', ' του μηνός']
            pre_exp_en = ['monthly on the ']
            pre_expr_gr = ['κάθε μήνα στις ']
            prompt_list_en = ['every ' + str(self.rrule["BYMONTHDAY"]) + random.choice(post_expr_en), 'monthly on the ' + str(self.rrule["BYMONTHDAY"])]
            prompt_list_gr = 'κάθε ' + str(self.rrule["BYMONTHDAY"]) + random.choice(post_expr_gr), 'κάθε μήνα στις ' + str(self.rrule["BYMONTHDAY"])
            prompt_en = random.choice(prompt_list_en)
            prompt_gr = random.choice(prompt_list_gr)
        elif self.rrule["FREQ"] == "YEARLY":
            prompt_en = 'every year at ' + str(self.rrule["BYMONTHDAY"]) + ' of ' + month_names['en'][str(self.rrule["BYMONTH"])]
            prompt_gr = 'κάθε χρόνο στις ' + str(self.rrule["BYMONTHDAY"]) + ' ' + month_names['gr'][str(self.rrule["BYMONTH"])]
        else:
            prompt_en = 'every day'
            prompt_gr = 'κάθε μέρα'
        
        return {'en': prompt_en, 'gr': prompt_gr}
        
    def select_random_days_of_week(self, weekdays: list[str]) -> list[str]:
        """
        Selects a random subset of days from the input list and returns them
        in the same order as the input list.

        Args:
            weekdays (list[str]): List of weekday names.

        Returns:
            list[str]: Subset of days in the same order as the input.
        """
        # Weighted probabilities for selecting 1, 2, 3, ..., len(weekdays) days
        num_days_weights = [0.1 if i == 1 else 0.4 if i in (2, 3) else 0.1 for i in range(1, len(weekdays) + 1)]

        # Normalize weights
        total_weight = sum(num_days_weights)
        num_days_weights = [w / total_weight for w in num_days_weights]

        # Randomly choose a number of days to select based on weighted probabilities
        num_days_to_select = random.choices(range(1, len(weekdays) + 1), weights=num_days_weights, k=1)[0]

        # Select random days without replacement
        selected_days = random.sample(weekdays, num_days_to_select)

        # Return selected days sorted by their original positions
        return [day for day in weekdays if day in selected_days]
