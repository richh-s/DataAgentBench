code = """import json
import pandas as pd

# Load businesses
# The key is 'var_function-call-17420300948470989546'
with open(locals()['var_function-call-17420300948470989546'], 'r') as f:
    businesses = json.load(f)

# Load ratings
# The key is 'var_function-call-7230598493686452378'
ratings_list = locals()['var_function-call-7230598493686452378']
# Convert to dict for lookup
ratings_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings_list}

def parse_time_str(t_str):
    # Returns (hour, minute, is_pm, is_am)
    t_str = t_str.strip().upper()
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    
    clean = t_str.replace('PM','').replace('AM','').strip()
    if ':' in clean:
        parts = clean.split(':')
        h = int(parts[0])
        m = int(parts[1])
    else:
        try:
            h = int(clean)
        except:
            return None, None, False, False
        m = 0
    return h, m, is_pm, is_am

def check_open_after_6pm(hours_json):
    if not hours_json or hours_json == 'None':
        return False
    
    try:
        hours_list = json.loads(hours_json)
    except:
        return False
        
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day not in weekdays:
            continue
            
        if time_range == 'Closed':
            continue
        if time_range == 'Open 24 hours':
            return True
            
        # Parse range "Start-End"
        # Handle en-dash
        r = time_range.replace('\u2013', '-').replace('–', '-')
        if '-' not in r:
            continue
            
        parts = r.split('-')
        if len(parts) < 2:
            continue
            
        # We only care about End Time
        end_str = parts[1]
        
        h, m, is_pm, is_am = parse_time_str(end_str)
        if h is None:
            continue
            
        # Logic:
        # PM case
        if is_pm:
            # 12 PM is Noon.
            if h == 12:
                # Noon. Not after 6 PM.
                continue
            # h is 1..11 PM.
            # Convert to 24h effectively?
            # 6 PM is threshold.
            if h > 6:
                return True
            if h == 6 and m > 0:
                return True
            # If h < 6 (e.g. 1PM, 5PM), No.
            
        # AM case
        elif is_am:
            # 12 AM is midnight.
            if h == 12:
                return True # Open until midnight (which is after 6 PM)
            # 1 AM to 11 AM.
            # If 1 AM .. 5 AM: Likely late night close.
            if h <= 5:
                return True
            # If 6 AM .. 11 AM: Likely morning shift.
            # No.
            
        # Missing AM/PM?
        else:
            # Fallback or strict?
            # If missing, it's ambiguous.
            # But let's check start time to infer?
            # "3-8PM". End has PM. My parser should catch it.
            # If end string is just "3"?
            # Re-check parser.
            # parse_time_str("8PM") -> is_pm=True.
            pass
            
    return False

# Filter businesses
eligible_businesses = []
for b in businesses:
    gid = b['gmap_id']
    if check_open_after_6pm(b['hours']):
        # Get rating
        if gid in ratings_map:
            b['avg_rating'] = ratings_map[gid]
            eligible_businesses.append(b)

# Rank
eligible_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Top 5
top_5 = eligible_businesses[:5]

# Format output
final_result = []
for b in top_5:
    final_result.append({
        "name": b['name'],
        "operating_hours": b['hours'], # Keep original string/list
        "average_rating": b['avg_rating']
    })

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-2313058406439082925': ['business_description'], 'var_function-call-1536968768987793813': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-4867298928114841222': [{'count': '79'}], 'var_function-call-10648580766582161317': [{'count(*)': '2000'}], 'var_function-call-17420300948470989546': 'file_storage/function-call-17420300948470989546.json', 'var_function-call-7230598493686452378': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
