code = """import json
import ast

def parse_time(t_str):
    t_str = t_str.strip()
    if t_str == 'Open 24 hours':
        return 24.0
    
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    
    t_clean = t_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in t_clean:
        parts = t_clean.split(':')
        h = int(parts[0])
        m = int(parts[1])
    else:
        try:
            h = int(t_clean)
        except:
            return 0.0
        m = 0
        
    if is_pm:
        if h != 12:
            h += 12
    elif is_am:
        if h == 12:
            h = 0 
            
    return h + m/60.0

def is_late_open(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        hours_list = json.loads(hours_str)
    except:
        try:
            hours_list = ast.literal_eval(hours_str)
        except:
            return False
            
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day_item in hours_list:
        if len(day_item) != 2:
            continue
        day, time_range = day_item
        
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True
            if time_range == 'Closed':
                continue
                
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) < 2:
                continue
                
            end_time_str = parts[1]
            try:
                is_pm = 'PM' in end_time_str
                is_am = 'AM' in end_time_str
                
                t_val = parse_time(end_time_str)
                
                if is_pm:
                    if t_val > 18.0:
                        return True
                if is_am:
                    if t_val < 6.0: 
                             return True
                        
            except Exception:
                continue
                
    return False

# Get file path from variable
file_path = locals()['var_function-call-9505002775633145034']

with open(file_path, 'r') as f:
    businesses = json.load(f)

filtered_businesses = []
for b in businesses:
    if is_late_open(b['hours']):
        filtered_businesses.append(b)

filtered_gmap_ids = [b['gmap_id'] for b in filtered_businesses]
print("__RESULT__:")
print(json.dumps(filtered_gmap_ids))"""

env_args = {'var_function-call-16930252738869414104': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-13480375080291303633': [{'count': '79'}], 'var_function-call-9505002775633145034': 'file_storage/function-call-9505002775633145034.json'}

exec(code, env_args)
