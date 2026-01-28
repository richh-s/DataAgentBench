code = """import json
import re

# Read the business hours data from file
business_hours_path = locals()['var_functions.query_db:4']
with open(business_hours_path, 'r') as f:
    businesses = json.load(f)

# Parse hours to find businesses open after 6:00 PM on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_time_to_minutes(time_str):
    if not time_str or time_str == 'Closed' or time_str == 'Open 24 hours':
        return None
    
    time_str = time_str.strip()
    
    if 'AM' in time_str or 'PM' in time_str:
        if 'AM' in time_str:
            period = 'AM'
            time_str = time_str.replace('AM', '')
        else:
            period = 'PM'
            time_str = time_str.replace('PM', '')
        
        if ':' in time_str:
            hours, minutes = map(int, time_str.split(':'))
        else:
            hours = int(time_str)
            minutes = 0
        
        if period == 'PM' and hours != 12:
            hours += 12
        elif period == 'AM' and hours == 12:
            hours = 0
        
        return hours * 60 + minutes
    
    return None

def is_open_after_6pm(hours_list):
    if not hours_list:
        return False
    
    try:
        if isinstance(hours_list, str):
            hours_data = eval(hours_list)
        else:
            hours_data = hours_list
            
        for day_info in hours_data:
            day = day_info[0]
            time_range = day_info[1]
            
            if day in weekdays:
                if time_range == 'Open 24 hours':
                    return True
                
                if time_range == 'Closed':
                    continue
                
                if u'\u2013' in time_range:
                    start_time, end_time = time_range.split(u'\u2013')
                elif '-' in time_range:
                    start_time, end_time = time_range.split('-')
                else:
                    continue
                
                end_minutes = parse_time_to_minutes(end_time)
                if end_minutes is not None and end_minutes > 1080:
                    return True
        
        return False
    except Exception:
        return False

open_after_6pm = []
for business in businesses:
    if is_open_after_6pm(business['hours']):
        open_after_6pm.append(business)

result = {
    'count': len(open_after_6pm),
    'businesses': open_after_6pm[:3]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'num_of_reviews': '6'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
