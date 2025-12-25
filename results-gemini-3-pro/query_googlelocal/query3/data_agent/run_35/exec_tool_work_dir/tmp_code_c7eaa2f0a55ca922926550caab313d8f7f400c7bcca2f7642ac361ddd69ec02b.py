code = """import json
import pandas as pd
import re

# Load businesses
# The previous result for businesses is in a file
with open(locals()['var_function-call-11433873086712815087'], 'r') as f:
    businesses = json.load(f)

# Load ratings
ratings = locals()['var_function-call-7627484695008641346']
ratings_dict = {r['gmap_id']: float(r['avg_rating']) for r in ratings}

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def parse_time(t_str):
    # t_str example: "6PM", "6:30AM", "12AM", "12:30PM"
    # Returns minutes from start of day, e.g. 18*60 = 1080
    # 12AM is 0 or 24*60? Usually 12AM at the end of range means midnight (24:00).
    # 12PM is noon (12:00).
    
    match = re.match(r"(\d+)(?::(\d+))?(AM|PM)", t_str)
    if not match:
        return None
    
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    period = match.group(3)
    
    if period == "PM" and h != 12:
        h += 12
    if period == "AM" and h == 12:
        h = 0 # 00:00
        # But if it's closing time 12AM, it usually means 24:00 (next day) for comparison purposes
        # Let's handle 12AM as 24:00 if it's closing time?
        # Actually 12AM is 00:00. If open until 12AM, that is 24:00 from the previous day perspective.
        # Simple check: 12AM = 0 hours.
        pass
        
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == "None":
        return False
    
    try:
        # The string is like "[['Day', 'Time'], ...]"
        # It seems to be a JSON string
        schedule = json.loads(hours_str)
    except:
        return False
        
    if not isinstance(schedule, list):
        return False
        
    for day_item in schedule:
        if len(day_item) != 2:
            continue
        day_name = day_item[0]
        time_range = day_item[1]
        
        if day_name not in weekdays:
            continue
            
        if "Open 24 hours" in time_range:
            return True
            
        if "Closed" in time_range:
            continue
            
        # Split range. usually separated by \u2013 (en dash)
        # Check for different dash types
        parts = re.split(r'[\u2013\-\u2014]', time_range)
        if len(parts) != 2:
            continue
            
        start_str = parts[0].strip()
        end_str = parts[1].strip()
        
        # Parse end time
        # If end time is something like 12AM (next day), it is definitely after 6PM.
        # If end time is AM (e.g. 1AM, 2AM), it is next day, so it is after 6PM.
        # If end time is PM: check if > 6PM.
        
        # Helper logic for end time specifically
        # Check AM/PM
        if "AM" in end_str:
            # Closes in the morning.
            # If it opens in AM/PM and closes in AM, it usually crosses midnight.
            # Example: 9AM - 2AM.
            # Exception: 12AM (midnight).
            # If it closes at 10AM, it's not after 6PM (unless it opened previous day? No, daily hours).
            # Usually hours are "Open - Close".
            # If close is AM and != 12AM (00:00), it's likely next day -> Open late.
            # If close is 12AM, that is midnight -> 24:00 -> After 6PM (18:00).
            # Let's parse strictly.
            
            # Special case: 12AM
            if end_str.startswith("12") and "AM" in end_str:
                 # Midnight. 24:00 > 18:00. Yes.
                 return True
            
            # Other AM times (1AM, 6AM, 11AM).
            # If it's 1AM, 2AM... it's "late night" / next day. Definitely after 6PM.
            # If it's 11AM... it closes before 6PM.
            # How to distinguish? 
            # Usually hours like "9AM–5PM". Close 5PM.
            # "5PM–2AM". Close 2AM.
            # "6AM–11AM". Close 11AM.
            
            # Assume if closing time is AM and < 12 (noon), it might be next day OR morning.
            # Need to compare with start time?
            # Or just assume standard business logic:
            # If close is e.g. 00:00 to 05:00 range, it's late.
            # If close is 06:00 to 11:59 range, it's morning.
            # But simpler:
            # Convert to minutes. 6PM = 18*60 = 1080.
            # 12AM = 0.
            # 1AM = 60.
            # If minutes < 1080?
            # We need to treat 0-morning as > 1080 effectively (next day).
            # Let's rely on the assumption that if closing time is < start time, it crosses midnight.
            pass
            
        end_mins = parse_time(end_str)
        start_mins = parse_time(start_str)
        
        if end_mins is None or start_mins is None:
            continue
            
        # Adjust for crossing midnight
        # If end < start, add 24h (1440 mins) to end
        if end_mins < start_mins:
            end_mins += 1440
            
        # Check if end_mins > 18:00 (1080 mins)
        if end_mins > 1080:
            return True
            
    return False

qualified_businesses = []

for b in businesses:
    if is_open_after_6pm(b['hours']):
        gmap_id = b['gmap_id']
        avg_rating = ratings_dict.get(gmap_id, 0)
        qualified_businesses.append({
            "name": b['name'],
            "hours": b['hours'],
            "avg_rating": avg_rating
        })

# Rank by avg_rating descending
qualified_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Top 5
top_5 = qualified_businesses[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-4253295284542680562': ['business_description'], 'var_function-call-9582934265062463107': ['review'], 'var_function-call-8110400149210488132': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-14626990465061631294': [{'count': '79'}], 'var_function-call-1041329143436646749': [{'COUNT(*)': '2000'}], 'var_function-call-11433873086712815087': 'file_storage/function-call-11433873086712815087.json', 'var_function-call-7627484695008641346': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
