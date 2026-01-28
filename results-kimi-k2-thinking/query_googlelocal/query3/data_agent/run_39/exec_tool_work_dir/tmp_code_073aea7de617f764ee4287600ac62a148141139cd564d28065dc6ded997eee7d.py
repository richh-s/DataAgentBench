code = """import json
import re
from datetime import datetime

# Get the business data file path
business_file_path = locals()['var_functions.query_db:32']

# Read the complete business data
with open(business_file_path, 'r') as f:
    business_data = json.load(f)

# Function to parse time string to minutes since midnight
def time_to_minutes(time_str):
    time_str = time_str.strip()
    
    if time_str == "Open 24 hours":
        return 24 * 60
    
    time_str = time_str.replace('\u2013', '').replace('\u2014', '').replace('–', '').replace('—', '')
    
    is_pm = 'PM' in time_str.upper()
    is_am = 'AM' in time_str.upper()
    
    time_str = time_str.replace('AM', '').replace('PM', '').replace('am', '').replace('pm', '')
    time_str = time_str.strip()
    
    if ':' in time_str:
        hours, minutes = map(int, time_str.split(':'))
    else:
        hours = int(time_str)
        minutes = 0
    
    if is_pm and hours != 12:
        hours += 12
    elif is_am and hours == 12:
        hours = 0
    
    return hours * 60 + minutes

# Function to check if a business is open after 6 PM on any weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = eval(hours_str)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        six_pm_minutes = 18 * 60
        
        for day_hours in hours_list:
            if len(day_hours) >= 2:
                day = day_hours[0]
                hours_range = day_hours[1]
                
                if day not in weekdays or hours_range == 'Closed':
                    continue
                
                if '\u2013' in hours_range:
                    _, closing_time = hours_range.split('\u2013')
                elif '–' in hours_range:
                    _, closing_time = hours_range.split('–')
                elif '-' in hours_range:
                    _, closing_time = hours_range.split('-')
                elif hours_range == 'Open 24 hours':
                    return True
                else:
                    continue
                
                closing_time = closing_time.strip()
                
                if closing_time in ['Closed', 'None', '']:
                    continue
                
                try:
                    closing_minutes = time_to_minutes(closing_time)
                    if closing_minutes > six_pm_minutes:
                        return True
                except:
                    continue
        
        return False
    except:
        return False

# Filter businesses that are open after 6 PM on weekdays
businesses_open_late = []
for business in business_data:
    if is_open_after_6pm(business.get('hours', '')):
        businesses_open_late.append(business)

# Get the list of gmap_ids for businesses open late
gmap_ids = [b['gmap_id'] for b in businesses_open_late]

print('__RESULT__:')
print(json.dumps({
    'total_filtered': len(businesses_open_late),
    'businesses': businesses_open_late
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:22': {'data_directory_contents': [], 'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:12', 'var_functions.query_db:14']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_businesses': 63, 'sample': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}}, 'var_functions.execute_python:28': {'total_businesses_open_late': 21, 'sample_businesses': [{'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}]}, 'var_functions.query_db:30': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_43', 'rating': '3'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '1'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '4'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_45', 'rating': '5'}, {'gmap_id': 'gmap_45', 'rating': '1'}, {'gmap_id': 'gmap_45', 'rating': '5'}, {'gmap_id': 'gmap_45', 'rating': '1'}, {'gmap_id': 'gmap_45', 'rating': '4'}, {'gmap_id': 'gmap_45', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '4'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '1'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '4'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_74', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '4'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '5'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
