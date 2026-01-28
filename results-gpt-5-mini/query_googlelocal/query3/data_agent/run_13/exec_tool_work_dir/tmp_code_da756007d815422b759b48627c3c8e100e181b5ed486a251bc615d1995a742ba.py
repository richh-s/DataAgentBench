code = """import json
import ast
from datetime import datetime, time

# Load data from storage variables
business_path = var_call_Ks9MkxjOqbLdfwTMoz4teoUl
with open(business_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
ratings = var_call_cZKhR76YD0EkpuJUbKy9kwge

# Build rating map
rating_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings}

# Helper functions

def parse_time_string(t):
    # Normalize en-dash to hyphen
    t = t.replace('\u2013', '-').replace('\u2014', '-')
    return t


def time_from_string(s, default_suffix=None):
    s = s.strip()
    # handle cases like 'Closed' or 'Open 24 hours'
    if s.lower() in ('closed', 'open 24 hours'):
        return None
    # If contains AM or PM, parse
    s_up = s.upper()
    if 'AM' in s_up or 'PM' in s_up:
        # remove spaces before AM/PM
        s_up = s_up.replace(' ', '')
        # Ensure format like H:MMAM or HAM
        try:
            dt = datetime.strptime(s_up, '%I:%M%p')
        except ValueError:
            try:
                dt = datetime.strptime(s_up, '%I%p')
            except ValueError:
                # try without minutes but with dot? fallback
                return None
        return time(dt.hour, dt.minute)
    else:
        # No AM/PM
        if default_suffix:
            return time_from_string(s + default_suffix)
        else:
            return None


def closes_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    # parse string to Python structure
    try:
        parsed = ast.literal_eval(hours_str)
    except Exception:
        # if it's just a string like 'Open 24 hours'
        if 'Open 24 hours' in hours_str or '24 hours' in hours_str:
            return True
        return False

    # parsed should be list of [day, time_range]
    weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])
    for entry in parsed:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        timespec = entry[1]
        if day not in weekdays:
            continue
        if not timespec or timespec == 'Closed':
            continue
        if 'Open 24 hours' in timespec or '24 hours' in timespec:
            return True
        # normalize dash
        ts = parse_time_string(timespec)
        # split on hyphen
        if '-' in ts:
            parts = [p.strip() for p in ts.split('-')]
        else:
            parts = [ts]
        if len(parts) == 1:
            # single token - could be like '9AM to 9PM'? if no dash skip
            continue
        start_s, end_s = parts[0], parts[1]
        # if end has AM/PM, use it for start if start lacks
        end_up = end_s.upper()
        start_up = start_s.upper()
        default = None
        if 'AM' in end_up:
            default = 'AM'
        elif 'PM' in end_up:
            default = 'PM'
        # If start lacks AM/PM but end has, append end suffix to start
        if ('AM' not in start_up) and ('PM' not in start_up) and default:
            start_s2 = start_s + default
        else:
            start_s2 = start_s
        # Parse end
        end_time = time_from_string(end_s)
        if end_time is None:
            # try appending default if missing
            if ('AM' not in end_up) and ('PM' not in end_up) and default:
                end_time = time_from_string(end_s + default)
        if end_time is None:
            continue
        # Check if end_time > 18:00
        if (end_time.hour > 18) or (end_time.hour == 18 and end_time.minute > 0):
            return True
    return False

# Find businesses that remain open after 6pm on at least one weekday
qualified = []
for b in businesses:
    gmap_id = b.get('gmap_id')
    hours = b.get('hours')
    if closes_after_6pm(hours):
        if gmap_id in rating_map:
            qualified.append({'gmap_id': gmap_id, 'name': b.get('name'), 'hours': hours, 'avg_rating': rating_map[gmap_id]})

# Sort by avg_rating desc and pick top 5
qualified_sorted = sorted(qualified, key=lambda x: x['avg_rating'], reverse=True)
top5 = qualified_sorted[:5]

# Prepare JSON-serializable output
output = []
for item in top5:
    output.append({'name': item['name'], 'hours': item['hours'], 'avg_rating': round(item['avg_rating'], 6)})

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_4X6GVf65njRVKQpuxJOTSwSc': ['business_description'], 'var_call_Ks9MkxjOqbLdfwTMoz4teoUl': 'file_storage/call_Ks9MkxjOqbLdfwTMoz4teoUl.json', 'var_call_cZKhR76YD0EkpuJUbKy9kwge': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'num_reviews': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'num_reviews': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'num_reviews': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'num_reviews': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'num_reviews': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'num_reviews': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'num_reviews': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'num_reviews': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'num_reviews': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'num_reviews': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'num_reviews': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'num_reviews': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'num_reviews': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'num_reviews': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'num_reviews': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'num_reviews': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'num_reviews': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'num_reviews': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'num_reviews': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'num_reviews': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'num_reviews': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'num_reviews': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'num_reviews': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'num_reviews': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'num_reviews': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'num_reviews': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'num_reviews': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'num_reviews': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'num_reviews': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'num_reviews': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'num_reviews': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'num_reviews': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'num_reviews': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'num_reviews': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'num_reviews': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'num_reviews': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'num_reviews': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'num_reviews': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'num_reviews': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'num_reviews': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'num_reviews': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'num_reviews': '3'}]}

exec(code, env_args)
