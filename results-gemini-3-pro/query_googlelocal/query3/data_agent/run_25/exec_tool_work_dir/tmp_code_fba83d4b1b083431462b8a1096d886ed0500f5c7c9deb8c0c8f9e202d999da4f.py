code = """import json
import pandas as pd
import datetime

# Load data
with open(locals()['var_function_call_15775885395275925339'], 'r') as f:
    businesses = json.load(f)

ratings_list = locals()['var_function_call_3398959721506765296']
ratings_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings_list}

def parse_time(t_str):
    # t_str example: "6PM", "6:30AM", "12PM", "12:30AM"
    # Returns minutes from midnight
    if not t_str: return -1
    t_str = t_str.strip()
    is_pm = t_str.upper().endswith('PM')
    is_am = t_str.upper().endswith('AM')
    if not (is_pm or is_am): return -1
    
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
    # hours_str example: '[["Thursday", "6:30AM–6PM"], ...]' or "None"
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_data = json.loads(hours_str)
    except:
        return False
        
    # Weekdays
    weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    
    target_time = 18 * 60 # 6:00 PM in minutes
    
    for day, time_range in hours_data:
        if day in weekdays:
            if time_range == "Open 24 hours":
                return True
            if time_range == "Closed":
                continue
            
            # Split by dash. It seems to be \u2013 (en dash) in the example
            # "6:30AM\u20136PM"
            # Let's try splitting by common separators
            separators = ['\u2013', '-', '–']
            parts = None
            for sep in separators:
                if sep in time_range:
                    parts = time_range.split(sep)
                    break
            
            if parts and len(parts) == 2:
                end_time_str = parts[1]
                end_minutes = parse_time(end_time_str)
                # Check if it closes after 6 PM (strictly greater)
                # Note: "12AM" (midnight) is 0 or 24?
                # Usually businesses closing at 12AM or 1AM or 2AM mean late night.
                # If end_minutes is small (e.g. 1AM -> 60), it actually closes next day.
                # Logic: if closes at 1AM, it is open after 6 PM.
                # If it opens at 9AM and closes at 1AM, end_minutes=60. 
                # But my parse_time returns 60.
                # If closing time is AM (and not 12PM/noon), it's likely next day => open after 6PM.
                
                # Refined logic:
                # If PM: check if > 18:00 (1080 min). 12PM is 12:00 (720 min).
                # If AM: usually implies late night / next day, so yes, open after 6PM.
                # Exception: Opens at 12AM closes at 2AM? Unlikely for normal businesses listed as Mon: 12AM-2AM.
                # Usually ranges are "9AM-5PM".
                # Let's check AM/PM.
                
                is_pm = end_time_str.upper().endswith('PM')
                is_am = end_time_str.upper().endswith('AM')
                
                parsed_end = parse_time(end_time_str)
                
                if is_pm:
                    # e.g. 6PM -> 1080. We want > 1080.
                    # 5PM -> 1020.
                    # 12PM -> 720.
                    if parsed_end > target_time:
                        return True
                    # If strictly 6PM (1080), it closes AT 6PM, not after.
                
                if is_am:
                    # e.g. 1AM. If a business is open during the day and closes at 1AM, it is open after 6PM.
                    # Unless it's a breakfast place 6AM-10AM.
                    # But usually "Start-End". If Start is AM and End is AM (smaller), it crosses midnight.
                    # We need start time to be sure?
                    # "6:30AM–6PM" -> Start=390, End=1080.
                    # "5PM-2AM" -> Start=1020, End=120 (next day).
                    
                    # Let's parse start time too.
                    start_time_str = parts[0]
                    start_minutes = parse_time(start_time_str)
                    
                    # If end < start, it crosses midnight => Open late.
                    if parsed_end < start_minutes:
                         return True
                    
                    # If both AM, e.g. 1AM-5AM. It is NOT open after 6PM (18:00).
                    # Wait, 1AM-5AM is early morning. 6PM is evening.
                    # If 11AM-2PM.
                    
                    # If end is AM and > start (e.g. 8AM-11AM), it's morning. Not after 6PM.
                    # So if end is AM, it must be < start (crossing midnight) or maybe it's effectively 24h?
                    # Actually, if end is 12AM (midnight), that counts as after 6PM.
                    # 12AM is 0 in my parse_time.
                    # If closes at 12AM, effectively it's 24:00 > 18:00.
                    if end_time_str.upper() == "12AM": 
                        return True
                    
            elif parts is None:
                 # maybe "Open 24 hours" was caught earlier.
                 pass
                 
    return False

qualified_businesses = []

for b in businesses:
    if b['gmap_id'] in ratings_map:
        if is_open_after_6pm(b['hours']):
            b_info = b.copy()
            b_info['avg_rating'] = ratings_map[b['gmap_id']]
            qualified_businesses.append(b_info)

# Sort by rating desc
qualified_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Top 5
top_5 = qualified_businesses[:5]

result = []
for item in top_5:
    result.append({
        "name": item['name'],
        "hours": item['hours'],
        "rating": item['avg_rating']
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10089718377243614854': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-12355428782833551091': [{'count': '79'}], 'var_function-call-15775885395275925339': 'file_storage/function-call-15775885395275925339.json', 'var_function-call-3398959721506765296': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
