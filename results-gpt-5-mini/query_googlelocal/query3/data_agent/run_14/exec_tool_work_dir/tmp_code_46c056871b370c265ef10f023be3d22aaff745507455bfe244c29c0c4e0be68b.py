code = """import json
import pandas as pd
import re
from datetime import datetime

# Load business data from file path
business_file_path = var_call_KacYTzC5YIC552IKp4PaVOio
with open(business_file_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Load review averages from storage variable
reviews = var_call_pIyy4Y8YCvh3tT9Vw3L0uoxt

# Create DataFrames
df_bus = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Convert avg_rating to float
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)

# Merge on gmap_id
df = pd.merge(df_bus, df_rev[['gmap_id','avg_rating']], on='gmap_id', how='inner')

# Helper to parse time like '9:30AM' or '9AM' or '9'
def parse_time_component(t, default_ampm=None):
    t = t.strip()
    if t.lower() in ['closed', 'closed']:
        return None
    # extract am/pm
    m = re.search(r'(?i)(am|pm)$', t)
    ampm = m.group(1).upper() if m else None
    time_part = re.sub(r'(?i)(am|pm)$', '', t).strip()
    # if time_part empty, return None
    if not time_part:
        return None
    # handle cases like '3' or '3:30'
    if ':' in time_part:
        h_str, m_str = time_part.split(':',1)
        try:
            hour = int(h_str)
            minute = int(re.sub(r"[^0-9]","",m_str))
        except:
            return None
    else:
        try:
            hour = int(re.sub(r"[^0-9]","",time_part))
            minute = 0
        except:
            return None
    # decide am/pm
    if not ampm:
        ampm = default_ampm
    if not ampm:
        # default: assume AM if hour between 1-11 and there's no pm info — but safer to assume PM if hour between 1-11 and likely closing > 12? Hard to know. We'll assume AM for <=6 and PM for >=7?
        if hour >=7:
            ampm = 'PM'
        else:
            ampm = 'AM'
    ampm = ampm.upper()
    if ampm == 'AM':
        if hour == 12:
            hour24 = 0
        else:
            hour24 = hour
    else:
        if hour == 12:
            hour24 = 12
        else:
            hour24 = hour + 12
    return hour24*60 + minute

# Function to check if any weekday has closing time after 18:00 (1080 minutes)
def opens_after_6pm(hours_field):
    if not hours_field or hours_field == 'None':
        return False
    hs = hours_field
    # direct check for Open 24 hours
    if isinstance(hs, str) and 'Open 24 hours' in hs:
        return True
    # parse JSON-like list
    try:
        day_list = json.loads(hs)
    except Exception:
        # sometimes it's already a Python repr with single quotes — try eval safe
        try:
            import ast
            day_list = ast.literal_eval(hs)
        except Exception:
            return False
    weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])
    # iterate
    for entry in day_list:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        timespan = entry[1]
        if day not in weekdays:
            continue
        if not timespan or 'Closed' in timespan:
            continue
        # handle 'Open 24 hours'
        if 'Open 24 hours' in timespan:
            return True
        # split start and end by dash or unicode en-dash
        parts = re.split(r'[-–—]', timespan)
        if len(parts) < 2:
            continue
        start_raw = parts[0].strip()
        end_raw = parts[1].strip()
        # determine am/pm for end
        m = re.search(r'(?i)(am|pm)', end_raw)
        end_ampm = m.group(1).upper() if m else None
        # if start lacks am/pm, we'll pass default
        start_minutes = parse_time_component(start_raw, default_ampm=end_ampm)
        end_minutes = parse_time_component(end_raw, default_ampm=end_ampm)
        if end_minutes is None:
            continue
        # If end_minutes <= start_minutes, it might cross midnight; treat as after 6pm if end > 18:00 or if crossing midnight
        if end_minutes > 18*60:
            return True
        # if times cross midnight (end <= start), then it definitely is open after 6pm
        if start_minutes is not None and end_minutes <= start_minutes:
            # e.g., 8PM - 2AM
            return True
    return False

# Apply filter
df['opens_after_6pm_weekday'] = df['hours'].apply(opens_after_6pm)

df_filtered = df[df['opens_after_6pm_weekday'] == True].copy()
# Sort by avg_rating desc
df_filtered['avg_rating'] = df_filtered['avg_rating'].astype(float)
df_top5 = df_filtered.sort_values(by='avg_rating', ascending=False).head(5)

# Prepare result
result = []
for _, row in df_top5.iterrows():
    result.append({
        'name': row['name'],
        'hours': row['hours'],
        'avg_rating': round(float(row['avg_rating']), 3)
    })

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HcnddQ0m13il0doIdk4WlAPm': ['review'], 'var_call_30QIUVZQIGmEntktPVTU2pQ1': ['business_description'], 'var_call_KacYTzC5YIC552IKp4PaVOio': 'file_storage/call_KacYTzC5YIC552IKp4PaVOio.json', 'var_call_pIyy4Y8YCvh3tT9Vw3L0uoxt': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}]}

exec(code, env_args)
