code = """import json
import pandas as pd
import datetime

# Load data
with open(locals()['var_function-call-9389753670053123735'], 'r') as f:
    businesses = json.load(f)

with open(locals()['var_function-call-1258569883968343709'], 'r') as f:
    reviews = json.load(f)

# Calculate average ratings
ratings_map = {}
for r in reviews:
    gid = r['gmap_id']
    try:
        val = float(r['rating'])
    except:
        continue
    if gid not in ratings_map:
        ratings_map[gid] = {'sum': 0, 'count': 0}
    ratings_map[gid]['sum'] += val
    ratings_map[gid]['count'] += 1

avg_ratings = {}
for gid, data in ratings_map.items():
    avg_ratings[gid] = data['sum'] / data['count']

# Helper to parse time
def parse_time_str(t_str):
    # formats: "6:30AM", "6PM", "12PM", "12:30PM"
    # return minutes from midnight
    t_str = t_str.strip()
    is_pm = t_str.upper().endswith('PM')
    is_am = t_str.upper().endswith('AM')
    if not (is_pm or is_am):
        return None # unknown format
    
    time_part = t_str[:-2]
    if ':' in time_part:
        h, m = map(int, time_part.split(':'))
    else:
        h = int(time_part)
        m = 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == "None":
        return False
    try:
        hours_list = json.loads(hours_str)
    except:
        return False
        
    weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    target_time = 18 * 60 # 6:00 PM in minutes
    
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if time_range == "Open 24 hours":
                return True
            if time_range == "Closed":
                continue
            
            # Range format e.g. "6:30AM–6PM" or "11AM–9:30PM"
            # Split by en-dash or hyphen. The data preview shows unicode en-dash likely.
            # \u2013 is en-dash.
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) == 2:
                # open_time = parts[0]
                close_time_str = parts[1]
                close_minutes = parse_time_str(close_time_str)
                
                if close_minutes is not None:
                    # If close time is very early morning (e.g. 2AM), it means next day.
                    # But usually "9AM–6PM" -> 18*60.
                    # "5PM–2AM". 2AM is 2*60 = 120. 120 < 18*60.
                    # But it remains open after 6PM.
                    # Logic: if close_minutes < open_minutes, it crosses midnight.
                    # But simplest check:
                    # If close_minutes > 18*60, it's open after 6PM.
                    # What if it opens at 7PM? It is open after 6PM?
                    # "Remain open after 6:00 PM". Yes.
                    # What if 5PM-2AM? It is open after 6PM.
                    # 2AM is (24+2)*60 = 1560 > 18*60.
                    # I need to handle the crossover.
                    
                    # Let's parse open time too to be sure.
                    open_time_str = parts[0]
                    open_minutes = parse_time_str(open_time_str)
                    
                    if open_minutes is not None:
                         # Case 1: Standard day hours, e.g. 9AM - 6PM.
                         # Close > 18*60? 
                         # Case 2: Cross midnight, e.g. 5PM - 2AM.
                         # If close < open, we assume it ends next day.
                         if close_minutes < open_minutes:
                             close_minutes += 24 * 60
                        
                         if close_minutes > target_time:
                             # Check if it *closes* after 6PM.
                             # If it opens at 7PM, it remains open after 6PM? 
                             # "Remain open" usually implies it is open *at* 6PM and stays open.
                             # Or does it mean "Is the business open at some point after 6PM?"
                             # "businesses that remain open after 6:00 PM".
                             # Interpretations:
                             # 1. Open at 6:00 PM and continues to be open. (Must cover 6PM).
                             # 2. Closing time is after 6:00 PM.
                             # Given the phrasing "remain open", interpretation 1 is stronger.
                             # So, open_time <= 6PM AND close_time > 6PM.
                             # But "remain open after" can also be interpreted as "closing time is later than".
                             # Let's assume the user means "Closing time > 6:00 PM".
                             # Wait, if I open at 8PM, do I "remain open after 6PM"? Not really, I wasn't open *at* 6PM.
                             # However, if I open at 8PM, I am "open after 6PM".
                             # Let's check the examples.
                             # "San Soo Dang": 6:30AM–6PM. Closes at 6PM. Does it remain open after? No.
                             # "Vons Chicken": 11AM–9:30PM. Open.
                             # "Happy Spa": 9:30AM–10PM. Open.
                             # "The Boochyard": 3–8PM. Open.
                             # If "remain" implies continuity, I'd check if open <= 18:00 < close.
                             # If just "open", I'd check ranges overlap (18:00, 24:00) etc.
                             # Usually "Open after X" implies closing time > X.
                             # Let's stick to Closing Time > 6:00 PM (18:00).
                             # But consider the case where it opens at 7PM. It closes at say 11PM. 11PM > 6PM.
                             # Does it "remain open after 6PM"? English is ambiguous.
                             # But typically businesses open during the day.
                             # Most likely: Closing time > 18:00.
                             pass
                         
                         if close_minutes > target_time:
                             return True

    return False

# Filter businesses
candidates = []
for b in businesses:
    gid = b['gmap_id']
    if gid in avg_ratings:
        if is_open_after_6pm(b['hours']):
            candidates.append({
                'name': b['name'],
                'hours': b['hours'],
                'rating': avg_ratings[gid],
                'gmap_id': gid
            })

# Sort
candidates.sort(key=lambda x: x['rating'], reverse=True)

# Top 5
top5 = candidates[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-15913772187449719917': [{'name': 'City Textile', 'hours': 'None', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'gmap_id': 'gmap_45'}], 'var_function-call-11216696636943698531': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-13950357780773001996': [{'count': '79'}], 'var_function-call-16242394026488001448': [{'count(*)': '2000'}], 'var_function-call-9389753670053123735': 'file_storage/function-call-9389753670053123735.json', 'var_function-call-1258569883968343709': 'file_storage/function-call-1258569883968343709.json'}

exec(code, env_args)
