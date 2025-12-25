code = """import json
import ast
from datetime import datetime

# Load business data
with open(locals()['var_function-call-15343429406553025321'], 'r') as f:
    businesses = json.load(f)

# Load rating data
ratings = locals()['var_function-call-14073172494560852168']
rating_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings}

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_time(t_str):
    # t_str example: "6PM", "10:30PM", "12AM"
    # Returns minutes from midnight
    try:
        t = datetime.strptime(t_str, '%I:%M%p')
    except ValueError:
        try:
            t = datetime.strptime(t_str, '%I%p')
        except ValueError:
             return -1 # Parsing error
    return t.hour * 60 + t.minute

def is_open_after_6pm(hours_data):
    if not hours_data or hours_data == 'None':
        return False
    
    try:
        # The hours string is a string representation of a list of lists.
        # It looks like Python list syntax, so ast.literal_eval is safe or json.loads if it was valid json (but it has single quotes often).
        # The sample showed double quotes inside, so maybe json.loads works?
        # Sample: "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
        # That is valid JSON.
        hours_list = json.loads(hours_data)
    except:
        try:
            hours_list = ast.literal_eval(hours_data)
        except:
            return False

    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == "Open 24 hours":
                return True
            if time_range == "Closed":
                continue
            
            # Split by en-dash or hyphen
            # The sample output showed \u2013 which is en-dash
            if '\u2013' in time_range:
                separator = '\u2013'
            elif '-' in time_range:
                separator = '-'
            else:
                continue
            
            parts = time_range.split(separator)
            if len(parts) == 2:
                close_time_str = parts[1].strip()
                close_minutes = parse_time(close_time_str)
                
                # 6:00 PM is 18 * 60 = 1080 minutes
                # Special case: 12 AM (midnight) is 0 minutes in datetime, but effectively later than 6PM for closing.
                # Usually businesses closing at 12AM or 1AM or 2AM are "open after 6PM".
                # If close_minutes is 0 (12AM), it's > 18:00 in logic (next day).
                # If close_minutes < 12*60 (noon) and it's a closing time, it's likely next day (e.g. 2 AM).
                # So if close_minutes < 6*60 (6 AM), assume next day -> open after 6PM.
                
                if close_minutes == 0: # Midnight
                     return True
                if close_minutes < 600: # Early morning next day (up to 10AM? let's say 6AM)
                     return True
                
                if close_minutes > 1080: # 18:00
                    return True
                    
    return False

qualified_businesses = []

for b in businesses:
    gmap_id = b['gmap_id']
    if gmap_id in rating_map:
        avg_rating = rating_map[gmap_id]
        if is_open_after_6pm(b['hours']):
            qualified_businesses.append({
                'name': b['name'],
                'hours': b['hours'],
                'avg_rating': avg_rating
            })

# Sort: first by avg_rating desc
# To match "top 5", simply sort.
qualified_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

top_5 = qualified_businesses[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-601183759215383120': ['business_description'], 'var_function-call-260545375586009611': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-239738050126696821': ['review'], 'var_function-call-18162642024937623601': [{'count': '79'}], 'var_function-call-15343429406553025321': 'file_storage/function-call-15343429406553025321.json', 'var_function-call-14073172494560852168': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
