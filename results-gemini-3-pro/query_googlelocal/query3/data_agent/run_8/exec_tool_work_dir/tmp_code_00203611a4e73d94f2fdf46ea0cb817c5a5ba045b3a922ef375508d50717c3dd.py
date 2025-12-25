code = """import json
import pandas as pd
import re
from datetime import datetime

# Load average ratings
avg_ratings_data = locals()['var_function-call-7411679220032385794']
# It is a list of dicts.
# Convert to dict for easier lookup: gmap_id -> rating
rating_map = {item['gmap_id']: float(item['avg_rating']) for item in avg_ratings_data}

# Load business data
# The previous result is stored in a file path
file_path = locals()['var_function-call-7469405973918126151']
with open(file_path, 'r') as f:
    business_data = json.load(f)

# Function to parse time
def is_open_after_6pm(time_str):
    if not time_str or time_str == "Closed":
        return False
    if "Open 24 hours" in time_str:
        return True
    
    # Split start and end time
    # The separator seems to be \u2013 (en dash)
    parts = re.split(r'\u2013|-', time_str)
    if len(parts) != 2:
        return False # Unexpected format
    
    end_time_str = parts[1].strip()
    
    # Parse end time
    # Formats: "6PM", "9:30PM", "12AM" (midnight usually implies next day, so > 6PM)
    # But strictly 12AM is 00:00. If a place closes at 12AM, is it after 6PM? Yes.
    # What about 1AM? Yes.
    # What about 5PM? No.
    # We need to convert to minutes from start of day or similar value to compare.
    # 6:00 PM is 18:00.
    
    try:
        # Normalize time string
        # datetime.strptime can handle %I%M%p or %I%p
        dt = None
        # Try parsing
        formats = ["%I:%M%p", "%I%p"]
        for fmt in formats:
            try:
                dt = datetime.strptime(end_time_str, fmt)
                break
            except ValueError:
                continue
        
        if dt:
            # Check if PM and hour >= 6 (but 12PM is noon, 12AM is midnight)
            # 6:00 PM -> 18:00.
            # 12:00 AM -> 00:00.
            # If closing time is 12AM, 1AM, 2AM... it implies it's open late night, so technically open after 6PM.
            # But let's look at the hour in 24h format.
            hour = dt.hour
            minute = dt.minute
            
            # If hour > 18, it's after 6PM.
            if hour > 18:
                return True
            # If hour is 18, check minutes > 0
            if hour == 18 and minute > 0:
                return True
            # If hour is small (e.g. 0, 1, 2...), it means it closes after midnight, which is definitely after 6PM.
            # Assuming typical business hours, closing at 1 AM means open during evening.
            if hour < 6: # Arbitrary cutoff for "late night / early morning" closing
                return True
            
        return False
    except Exception as e:
        return False

# Function to check if open after 6pm on a weekday
def check_business_criteria(hours_json):
    if not hours_json or hours_json == "None":
        return False
    
    try:
        hours_list = json.loads(hours_json)
    except:
        return False
        
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    for day_info in hours_list:
        day = day_info[0]
        time_str = day_info[1]
        
        if day in weekdays:
            if is_open_after_6pm(time_str):
                return True
    return False

filtered_businesses = []

for bus in business_data:
    if check_business_criteria(bus['hours']):
        gmap_id = bus['gmap_id']
        rating = rating_map.get(gmap_id)
        if rating is not None:
            filtered_businesses.append({
                "name": bus['name'],
                "hours": bus['hours'],
                "avg_rating": rating
            })

# Sort by rating (desc)
filtered_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = filtered_businesses[:5]

# Format for output
print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-5550336343996203889': [{'name': 'City Textile', 'hours': 'None', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'gmap_id': 'gmap_45'}], 'var_function-call-7153141872577327009': [{'count(*)': '2000'}], 'var_function-call-7411679220032385794': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}], 'var_function-call-7469405973918126151': 'file_storage/function-call-7469405973918126151.json'}

exec(code, env_args)
