code = """import json
import pandas as pd
import re

# Load business data
# The previous tool result for business data is in a file
with open(locals()['var_function-call-16097457463105501373'], 'r') as f:
    businesses = json.load(f)

# Load rating data
ratings = locals()['var_function-call-6332380505774060116']
rating_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings}

weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

def is_open_after_6pm(time_str):
    # Handle simple cases
    if not time_str or time_str == 'Closed':
        return False
    if 'Open 24 hours' in time_str:
        return True
    
    # Extract end time. Format usually "Start–End"
    # Separator can be en-dash, hyphen, etc.
    # Split by common separators
    parts = re.split(r'\u2013|-', time_str)
    if len(parts) < 2:
        return False
    
    end_time_raw = parts[-1].strip() # e.g. "6PM", "9:30PM", "12AM"
    
    # Parse end time
    # Regex to find hour, minute, am/pm
    match = re.match(r'(\d+)(?::(\d+))?\s*(AM|PM)', end_time_raw, re.IGNORECASE)
    if not match:
        return False
    
    hour = int(match.group(1))
    minute = int(match.group(2) or 0)
    ampm = match.group(3).upper()
    
    # Convert to 24h roughly for comparison
    # We want to know if it's strictly > 18:00
    
    if ampm == 'AM':
        # 12AM is 00:00 (midnight). If it closes at 12AM or 1AM, it stayed open past 6PM.
        # Generally, if it closes in AM, it's late night / next morning.
        # Assuming start time was during the day. 
        # Most businesses won't open at 5AM and close at 6AM same day in this context.
        # Safe to assume AM closing means late night.
        # Exception: 11AM closing (lunch only?). But "remain open after 6PM".
        # If open 11PM to 5AM -> yes. 
        # If open 7AM to 11AM -> no.
        # Let's look at start time? No, usually AM closing implies next day or late night if start is PM or early AM.
        # But if it's "Start–End", e.g. "9AM-11AM", then no.
        # If "5PM-2AM", then yes.
        # Let's check if the range covers 18:00.
        
        # Actually, simpler: Is the closing time effectively "later" than 6PM on the same day?
        # A closing time of AM usually implies crossing midnight, hence > 6PM.
        # Unless the business operates purely in the morning (e.g. 6AM-11AM).
        # So we must check start time too or assume AM closing < start time implies crossing midnight.
        # Let's check start time to be safe.
        start_time_raw = parts[0].strip()
        s_match = re.match(r'(\d+)(?::(\d+))?\s*(AM|PM)', start_time_raw, re.IGNORECASE)
        if s_match:
            s_hour = int(s_match.group(1))
            s_ampm = s_match.group(3).upper()
            if s_hour == 12: s_hour = 0 if s_ampm == 'AM' else 12
            elif s_ampm == 'PM': s_hour += 12
            
            # Start time in 24h
            # If closing is AM, it's < 12:00.
            # If start is > closing (e.g. start 17:00, close 02:00), it crosses midnight -> Open after 6PM.
            # If start < closing (e.g. start 06:00, close 11:00), it's morning -> Not open after 6PM.
            
            c_hour = hour
            if c_hour == 12: c_hour = 0 # 12AM
            # AM is just c_hour
            
            if s_hour > c_hour: # Crosses midnight
                return True
            else:
                return False # Morning business
        
        return True # Default assume AM is late if parse fails? Or False?
        
    elif ampm == 'PM':
        # 12PM is noon.
        if hour == 12:
            return False # Closes at noon, not after 6PM
        
        # PM hours: 1PM = 13:00 ... 6PM = 18:00
        closing_24 = hour + 12
        
        # Check if > 18:00
        if closing_24 > 18:
            return True
        if closing_24 == 18:
            if minute > 0:
                return True
            else:
                return False
                
    return False

valid_businesses = []

for b in businesses:
    hours_str = b.get('hours')
    gid = b['gmap_id']
    
    if not hours_str or hours_str == 'None':
        continue
        
    try:
        hours_list = json.loads(hours_str)
    except:
        continue
        
    if not isinstance(hours_list, list):
        continue
        
    is_valid = False
    for day_info in hours_list:
        if len(day_info) != 2: continue
        day_name = day_info[0]
        time_range = day_info[1]
        
        if day_name in weekdays:
            if is_open_after_6pm(time_range):
                is_valid = True
                break
    
    if is_valid and gid in rating_map:
        b['avg_rating'] = rating_map[gid]
        valid_businesses.append(b)

# Sort by rating desc
valid_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Top 5
top_5 = valid_businesses[:5]

# Format output
result_list = []
for b in top_5:
    result_list.append({
        "name": b['name'],
        "hours": b['hours'],
        "avg_rating": b['avg_rating']
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-1877423527007371043': ['business_description'], 'var_function-call-12547541902673983578': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-5327697699952054455': [{'count': '79'}], 'var_function-call-9597841534618896024': [{'COUNT(*)': '2000'}], 'var_function-call-16097457463105501373': 'file_storage/function-call-16097457463105501373.json', 'var_function-call-6332380505774060116': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
