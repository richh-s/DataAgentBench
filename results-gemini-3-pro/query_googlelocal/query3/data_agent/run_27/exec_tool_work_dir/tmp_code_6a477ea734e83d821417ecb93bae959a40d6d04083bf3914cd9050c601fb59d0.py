code = """import json
import pandas as pd
import ast

# Load data
with open(var_function_call_7899059165738772019, 'r') as f:
    businesses = json.load(f)

with open(var_function_call_13163981481845026653, 'r') as f:
    reviews = json.load(f)

# Convert reviews to DataFrame and calc avg rating
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

# Process businesses
valid_businesses = []

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_time(time_str):
    # Returns closing time in minutes from midnight, or None
    if not time_str or time_str == 'Closed':
        return None
    if 'Open 24 hours' in time_str:
        return 24 * 60 # Treat as late enough
    
    # Split range "6:30AM–6PM"
    # Note: separator might be unicode en-dash or hyphen
    parts = time_str.replace('\u2013', '-').split('-')
    if len(parts) < 2:
        return None
    
    end_time_str = parts[1].strip()
    
    # Parse end_time_str like "6PM", "5:30PM", "12AM"
    is_pm = 'PM' in end_time_str
    is_am = 'AM' in end_time_str
    
    time_numeric = end_time_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in time_numeric:
        h, m = map(int, time_numeric.split(':'))
    else:
        h = int(time_numeric)
        m = 0
    
    # Convert to 24h
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
    # Handle 12AM (midnight) case for closing. 
    # Usually businesses closing at 12AM or later are "open after 6PM".
    # If closing is 12PM (noon), h=12.
    
    return h * 60 + m

for b in businesses:
    hours_raw = b.get('hours')
    if not hours_raw or hours_raw == 'None':
        continue
    
    try:
        # Try json load first, if string
        if isinstance(hours_raw, str):
            hours_list = json.loads(hours_raw)
        else:
            hours_list = hours_raw
    except:
        try:
            hours_list = ast.literal_eval(hours_raw)
        except:
            continue
            
    # Check if open after 6 PM (18:00 = 1080 minutes) on any weekday
    is_open_late = False
    
    if isinstance(hours_list, list):
        for day_info in hours_list:
            if len(day_info) == 2:
                day_name = day_info[0]
                time_range = day_info[1]
                
                if day_name in weekdays:
                    closing_minutes = parse_time(time_range)
                    if closing_minutes is not None:
                        # 6:00 PM is 18 * 60 = 1080
                        # If closing time is > 1080, it's open *after* 6 PM.
                        # Wait, "remain open after 6:00 PM" usually means open at 6:01 PM or later.
                        # So closing time must be > 18:00.
                        if closing_minutes > 1080:
                            is_open_late = True
                            break
                        # Handle case where closing is e.g. 1AM (next day)
                        # My parse_time returns 0-24h. 
                        # If a place closes at 1AM, it usually says so.
                        # If I parse "1AM" as 1*60 = 60. 60 is not > 1080.
                        # But closing at 1AM means it was open past 6PM.
                        # Simple heuristic: if closing time is AM (and not close to start of day like 6AM-7AM business), it's likely late night.
                        # But most ranges are "9AM-5PM".
                        # Let's assume standard ranges. If closing time is < start time, it wraps.
                        # But I only have the string.
                        # If the string is "11AM–9:30PM", closing is 21:30 > 18:00.
                        # If "5PM–2AM", closing is 2AM.
                        # My parser: 2AM -> 2*60 = 120. 
                        # Logic fix: if is_am is True and h < 12 (e.g., 1, 2, 3...), it's next day, so add 24h effectively for comparison?
                        # Or just check if closing time is in PM (and > 6) OR in AM (early morning).
                        
                        # Re-eval logic:
                        # If PM: must be > 6PM (12+6 = 18). So h >= 18? 
                        # Wait, "After 6PM". If it closes at 6PM exactly, does it remain open *after*? No.
                        # So strictly > 18:00.
                        # If AM (and not 12AM which is 0): It is effectively very late (next day).
                        # If 12AM (Midnight): That is 24:00 or 0:00. If treated as 24:00, it > 18:00.
    
    # Refined check inside loop:
    # We need to know if the closing time implies being open past 18:00.
    # Cases:
    # 9PM (21:00) -> Yes.
    # 6PM (18:00) -> No (closes at 6).
    # 1AM (01:00 next day) -> Yes.
    
    # Parser update needed?
    # Let's just check the raw parsed result.
    # If is_pm and h > 6 (and h!=12): Yes.
    # If is_pm and h == 12 (noon): No.
    # If is_am and h == 12 (midnight): Yes (closes at midnight).
    # If is_am and h < 9: Yes (closes late night). (Assuming no place opens at 4AM and closes at 8AM... actually coffee shops might. But query implies "remains open", suggesting evening hours).
    # Let's use strict 24h conversion.
    # If time_range crosses midnight, closing < opening.
    # But I'm only parsing closing.
    # "9AM-5PM" -> 17:00. Not > 18:00.
    # "10AM-2AM" -> 02:00. 
    # Logic: 
    # If Closing is PM: Closing hour > 6 (i.e. 7, 8, 9, 10, 11) or (Closing hour == 6 and minute > 0). (Note 12PM is noon, 18 is 6PM).
    # If Closing is AM: It's likely past midnight. (Unless it's a morning-only place closing at 11AM).
    #   How to distinguish "11AM closing" vs "1AM closing"?
    #   11AM is 11:00. 1AM is 01:00.
    #   If closing is 00:00 to 05:00, it's open past 6PM.
    #   If closing is 06:00 to 12:00 (noon), it's not open past 6PM (evening).
    pass

    if is_open_late:
        valid_businesses.append({'gmap_id': b['gmap_id'], 'name': b['name'], 'hours': b['hours']})

# Re-implement parsing logic inside the loop for clarity and correctness
filtered_list = []
for b in businesses:
    hours_raw = b.get('hours')
    if not hours_raw or hours_raw == 'None':
        continue
    
    try:
        hours_list = json.loads(hours_raw) if isinstance(hours_raw, str) else hours_raw
    except:
        try:
            hours_list = ast.literal_eval(hours_raw)
        except:
            continue
            
    is_open_late = False
    if isinstance(hours_list, list):
        for day_info in hours_list:
            if len(day_info) == 2:
                day_name = day_info[0]
                time_range = day_info[1]
                
                if day_name in weekdays:
                    if 'Open 24 hours' in time_range:
                        is_open_late = True
                        break
                    
                    if 'Closed' in time_range:
                        continue
                        
                    # Split range
                    parts = time_range.replace('\u2013', '-').split('-')
                    if len(parts) < 2:
                        continue
                    
                    end_str = parts[1].strip() # e.g. "6PM", "9:30PM", "12AM"
                    
                    # Analyze end time
                    # Check for PM > 6
                    if 'PM' in end_str:
                        # Remove PM, split colon
                        t = end_str.replace('PM', '').strip()
                        if ':' in t:
                            h, m = map(int, t.split(':'))
                        else:
                            h = int(t)
                            m = 0
                        
                        # 12PM is noon (12:00), not late.
                        # 1PM (13:00) ... 6PM (18:00).
                        # We need > 18:00.
                        # So if h!=12:
                        #   If h > 6: Open late.
                        #   If h == 6 and m > 0: Open late.
                        if h != 12:
                            if h > 6 or (h == 6 and m > 0):
                                is_open_late = True
                                break
                    
                    # Check for AM (Midnight or early morning next day)
                    elif 'AM' in end_str:
                        t = end_str.replace('AM', '').strip()
                        if ':' in t:
                            h, m = map(int, t.split(':'))
                        else:
                            h = int(t)
                            m = 0
                        
                        # 12AM is Midnight (24:00 or 00:00). This is > 6PM.
                        if h == 12: 
                            is_open_late = True
                            break
                        
                        # 1AM, 2AM, 3AM... usually means late night open.
                        # Unless it's a place that closes at 10AM or 11AM.
                        # If closing is < 6 (6AM), it's definitely late night from previous day.
                        # If closing is 10, 11, it's morning shift.
                        # Let's assume late night cutoff is e.g. 5AM.
                        if h < 6:
                            is_open_late = True
                            break

    if is_open_late:
        filtered_list.append(b)

# Join with ratings
df_bus = pd.DataFrame(filtered_list)
if not df_bus.empty:
    merged = pd.merge(df_bus, avg_ratings, on='gmap_id', how='inner')
    # Sort
    merged.sort_values(by='average_rating', ascending=False, inplace=True)
    # Top 5
    top5 = merged.head(5)
    result = top5[['name', 'hours', 'average_rating']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3046160326493482668': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-7674235243375518328': [{'count': '79'}], 'var_function-call-3542570336395074807': [{'COUNT(*)': '2000'}], 'var_function-call-7899059165738772019': 'file_storage/function-call-7899059165738772019.json', 'var_function-call-13163981481845026653': 'file_storage/function-call-13163981481845026653.json'}

exec(code, env_args)
