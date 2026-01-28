code = """import json

# Access data
businesses = locals()['var_functions.query_db:28']
reviews = locals()['var_functions.query_db:26']

# Calculate average ratings per business
rating_data = {}
for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    
    if gmap_id not in rating_data:
        rating_data[gmap_id] = {'sum': 0, 'count': 0}
    
    rating_data[gmap_id]['sum'] += rating
    rating_data[gmap_id]['count'] += 1

# Calculate averages and filter for businesses with at least 5 reviews
rating_data = {k: v for k, v in rating_data.items() if v['count'] >= 5}
for gmap_id in rating_data:
    rating_data[gmap_id]['avg'] = rating_data[gmap_id]['sum'] / rating_data[gmap_id]['count']

# Process hours
def parse_closing_minutes(time_range):
    if not time_range or time_range == 'Closed':
        return None
    
    try:
        # Handle different dash characters
        for dash in ['–', '—', '-']:
            if dash in time_range:
                parts = time_range.split(dash)
                if len(parts) >= 2:
                    close_str = parts[1].strip()
                    break
        else:
            return None
        
        close_str = close_str.lower().replace(' ', '')
        
        if 'pm' in close_str:
            time_part = close_str.replace('pm', '')
            if ':' in time_part:
                h, m = time_part.split(':')
                h = int(h)
                if h != 12:
                    h += 12
                return h * 60 + int(m)
            else:
                h = int(time_part)
                if h != 12:
                    h += 12
                return h * 60
        elif 'am' in close_str:
            time_part = close_str.replace('am', '')
            if ':' in time_part:
                h, m = time_part.split(':')
                h = int(h)
                if h == 12:
                    h = 0
                return h * 60 + int(m)
            else:
                h = int(time_part)
                if h == 12:
                    h = 0
                return h * 60
    except:
        pass
    
    return None

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None' or 'Open 24 hours' in hours_str:
        return False
    
    try:
        hours_list = eval(hours_str)
        target_minutes = 18 * 60  # 6PM = 1080 minutes
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_entry in hours_list:
            if not isinstance(day_entry, list) or len(day_entry) != 2:
                continue
            
            day, hours = day_entry
            if day not in weekdays or hours == 'Closed':
                continue
            
            minutes = parse_closing_minutes(hours)
            if minutes and minutes > target_minutes:
                return True
                
    except Exception as e:
        pass
    
    return False

# Filter and collect results
candidates = []
for business in businesses:
    gmap_id = business['gmap_id']
    
    if gmap_id not in rating_data:
        continue
    
    if not is_open_after_6pm(business['hours']):
        continue
    
    avg_rating = rating_data[gmap_id]['avg']
    candidates.append({
        'name': business['name'],
        'operating_hours': business['hours'],
        'average_rating': round(avg_rating, 2)
    })

# Sort and get top 5
candidates.sort(key=lambda x: x['average_rating'], reverse=True)
result = candidates[:5]

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'PODS Sacramento Hub', 'gmap_id': 'gmap_19', 'hours': 'None', 'state': 'Open now'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': [{'gmap_id': 'gmap_44'}, {'gmap_id': 'gmap_41'}, {'gmap_id': 'gmap_43'}, {'gmap_id': 'gmap_38'}, {'gmap_id': 'gmap_45'}, {'gmap_id': 'gmap_74'}, {'gmap_id': 'gmap_17'}, {'gmap_id': 'gmap_22'}, {'gmap_id': 'gmap_29'}, {'gmap_id': 'gmap_25'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:34': {'available_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24', 'var_functions.query_db:26', 'var_functions.query_db:28'], 'target_keys': ['var_functions.query_db:28', 'var_functions.query_db:26']}}

exec(code, env_args)
