code = """import json
import datetime

# Load data
business_data = json.load(open(locals()['var_function-call-1669587993190886699']))
ratings_data = locals()['var_function-call-8865349672809443541']

# Create ratings map
ratings_map = {item['gmap_id']: float(item['avg_rating']) for item in ratings_data}

def parse_time(t_str):
    # t_str like "6:30AM", "6PM", "12PM", "12:30AM"
    # Returns minutes from midnight
    if not t_str: return 0
    t_str = t_str.strip()
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    if not is_pm and not is_am:
        # Maybe 24h format or something else? Assume AM if not specified? Unlikely.
        return 0
    
    time_part = t_str.replace('PM', '').replace('AM', '').strip()
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
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # The hours_str is a string representation of a python list. 
        # It uses single quotes or double quotes. JSON parser might fail if it's not valid JSON.
        # The output showed "[[...]]" which is valid JSON if quotes are double.
        # Let's try json.loads first.
        hours_list = json.loads(hours_str)
    except:
        # If simple json load fails (e.g. single quotes), use ast.literal_eval
        import ast
        try:
            hours_list = ast.literal_eval(hours_str)
        except:
            return False

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    target_time = 18 * 60 # 6:00 PM in minutes

    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == 'Closed':
                continue
            if time_range == 'Open 24 hours':
                return True
            
            # Split by en-dash or hyphen
            # The previous output showed \u2013 (en dash)
            if '\u2013' in time_range:
                start, end = time_range.split('\u2013')
            elif '-' in time_range:
                start, end = time_range.split('-')
            else:
                continue
            
            start_min = parse_time(start)
            end_min = parse_time(end)
            
            # Case 1: End time is > 18:00 (1080 min)
            # But wait, 12 AM is 0 min. 1 AM is 60 min.
            # If a place closes at 1 AM, end_min is 60. 60 < 1080.
            # But it opened in the day and closed next day.
            # How to detect wrap around?
            # Usually start < end. If start > end, it wraps.
            
            if start_min > end_min:
                # Wraps around midnight (e.g. 5PM to 2AM)
                # It is definitely open after 6 PM because it is open until midnight and beyond
                return True
            else:
                # Does not wrap (e.g. 9AM to 5PM, or 9AM to 9PM)
                if end_min > target_time:
                    return True
                    
    return False

eligible_businesses = []

for b in business_data:
    gmap_id = b['gmap_id']
    name = b['name']
    hours = b['hours']
    
    if gmap_id in ratings_map:
        avg_rating = ratings_map[gmap_id]
        if is_open_after_6pm(hours):
            eligible_businesses.append({
                'name': name,
                'hours': hours,
                'avg_rating': avg_rating
            })

# Sort by avg_rating desc
eligible_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Top 5
top_5 = eligible_businesses[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-699370870581995958': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-15579800850574457432': [{'count': '79'}], 'var_function-call-8100640394119854005': [{'COUNT(*)': '2000'}], 'var_function-call-1669587993190886699': 'file_storage/function-call-1669587993190886699.json', 'var_function-call-8865349672809443541': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
