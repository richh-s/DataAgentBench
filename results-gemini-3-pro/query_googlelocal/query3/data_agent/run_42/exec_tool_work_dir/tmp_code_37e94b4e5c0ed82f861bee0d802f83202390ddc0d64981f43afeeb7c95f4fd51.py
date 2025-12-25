code = """import json
import ast
import re

# Load data
# Reading business data from file
with open('var_function-call-598133683777434274.json', 'r') as f:
    businesses = json.load(f)

# Reading ratings data
ratings_list = locals()['var_function-call-598133683777433787']
ratings_map = {item['gmap_id']: float(item['avg_rating']) for item in ratings_list}

def parse_time_to_float(time_str):
    # Returns 24h time as float (e.g. 18.5 for 6:30 PM)
    # Returns None if parse fails
    try:
        match = re.match(r'(\d+)(?::(\d+))?(AM|PM)', time_str)
        if not match:
            return None
        h, m, meridiem = match.groups()
        h = int(h)
        m = int(m) if m else 0
        
        if meridiem == 'PM':
            if h != 12:
                h += 12
        elif meridiem == 'AM':
            if h == 12:
                h = 0
        
        return h + m / 60.0
    except:
        return None

def is_open_after_6pm(hours_list):
    # hours_list structure: [['Day', 'TimeRange'], ...]
    # Check only Weekdays: Monday, Tuesday, Wednesday, Thursday, Friday
    weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    
    if not hours_list or hours_list == 'None':
        return False
    
    # Parse string list if necessary
    if isinstance(hours_list, str):
        try:
            hours_data = ast.literal_eval(hours_list)
        except:
            return False
    else:
        hours_data = hours_list
        
    if not isinstance(hours_data, list):
        return False

    for day_info in hours_data:
        if len(day_info) != 2:
            continue
        day, time_range = day_info
        
        if day in weekdays:
            if 'Open 24 hours' in time_range:
                return True
            if 'Closed' in time_range:
                continue
            
            # Extract closing time
            # Format usually "Start–End" with en-dash or hyphen
            # Unicode en-dash is \u2013
            parts = re.split(r'[\u2013-]', time_range) # split by en-dash or hyphen
            if len(parts) >= 2:
                closing_str = parts[-1].strip()
                closing_float = parse_time_to_float(closing_str)
                
                if closing_float is not None:
                    # Check if > 18.0 (6 PM)
                    # Logic: If > 18.0, valid. 
                    # If 0 <= t < 8.0 (e.g. 1 AM, 2 AM), valid (late night).
                    if (closing_float > 18.0) or (0.0 <= closing_float < 8.0):
                        return True
    return False

# Filter businesses
qualified_businesses = []

for b in businesses:
    gmap_id = b['gmap_id']
    name = b['name']
    hours_str = b['hours']
    
    # Check hours
    if is_open_after_6pm(hours_str):
        # Get rating
        rating = ratings_map.get(gmap_id, 0.0)
        qualified_businesses.append({
            'name': name,
            'hours': hours_str,
            'avg_rating': rating
        })

# Sort by rating (desc), then name (asc)
qualified_businesses.sort(key=lambda x: (-x['avg_rating'], x['name']))

# Get top 5
top_5 = qualified_businesses[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-15362908564980689109': ['business_description'], 'var_function-call-15362908564980689624': ['review'], 'var_function-call-1021495359917368364': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-4842042733303639925': [{'count': '79'}], 'var_function-call-12831551950630835323': [{'count(*)': '2000'}], 'var_function-call-598133683777434274': 'file_storage/function-call-598133683777434274.json', 'var_function-call-598133683777433787': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
