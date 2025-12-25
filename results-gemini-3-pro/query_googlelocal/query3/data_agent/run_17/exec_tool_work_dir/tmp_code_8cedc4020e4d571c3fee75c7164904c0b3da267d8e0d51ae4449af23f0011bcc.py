code = """import json
import ast
from datetime import datetime

# Access the file path from the variable
file_path = locals()['var_function-call-3043783580466555497']

# Load businesses
with open(file_path, 'r') as f:
    businesses = json.load(f)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False
        
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True
            if time_range == 'Closed':
                continue
            
            # Parse time range, e.g., "6:30AM–6PM" or "11AM–9:30PM"
            # Normalize dash
            time_range = time_range.replace('–', '-')
            
            if '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
                
            if len(parts) == 2:
                end_time_str = parts[1].strip()
                # Parse end time
                try:
                    dt = None
                    if ':' in end_time_str:
                         dt = datetime.strptime(end_time_str, "%I:%M%p")
                    else:
                         dt = datetime.strptime(end_time_str, "%I%p")
                    
                    hour = dt.hour
                    minute = dt.minute
                    
                    # Logic:
                    # If closes early morning (00:00 - 05:00), it's open past 6PM.
                    if 0 <= hour <= 5: 
                        return True
                    
                    # If closes after 18:00
                    if hour > 18:
                        return True
                    if hour == 18 and minute > 0:
                        return True
                    
                except ValueError:
                    pass

    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_businesses.append(b)

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-4784077454714328516': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-12420282615059275630': [{'count': '79'}], 'var_function-call-3043783580466555497': 'file_storage/function-call-3043783580466555497.json'}

exec(code, env_args)
