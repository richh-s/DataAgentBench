code = """import json
import re

# Load data from previous tool calls
# var_call_sSoNUWz7KZewdpSuYq6wPbGO is a file path to the large result
with open(var_call_sSoNUWz7KZewdpSuYq6wPbGO, 'r') as f:
    businesses = json.load(f)

# var_call_GjbVz3lyHigPoEmL25se4L2z is a list of dicts with avg ratings
ratings = var_call_GjbVz3lyHigPoEmL25se4L2z

# Create map gmap_id -> avg_rating (float)
rating_map = {}
for r in ratings:
    try:
        rating_map[r['gmap_id']] = float(r['avg_rating'])
    except:
        continue

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def parse_time_to_minutes(t):
    t = t.strip().upper()
    # Remove periods
    t = t.replace('.', '')
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*([AP]M)?$', t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3)
    if not ampm:
        return None
    if ampm == 'AM':
        hour = hour % 12
    else:
        hour = hour % 12 + 12
    return hour * 60 + minute


def range_has_close_after_6(range_str):
    if not range_str or range_str.strip() == 'None':
        return False
    s = range_str.strip()
    s_upper = s.upper()
    if 'OPEN 24' in s_upper:
        return True
    if 'CLOSED' in s_upper:
        return False
    # Normalize dash characters to '-'
    parts = re.split(r'\s*[–—-]\s*', s)
    if len(parts) < 2:
        return False
    start = parts[0].strip()
    end = parts[1].strip()
    # If end has AM/PM, capture suffix
    end_suffix_match = re.search(r'([APap][Mm])', end)
    start_suffix_match = re.search(r'([APap][Mm])', start)
    if not start_suffix_match and end_suffix_match:
        # Append the end suffix to start (e.g., '3' and '8PM' -> '3PM')
        start = start + end_suffix_match.group(1)
    # If end lacks am/pm but start has, append start's suffix to end
    if not end_suffix_match and start_suffix_match:
        end = end + start_suffix_match.group(1)
    # Parse end
    end_minutes = parse_time_to_minutes(end.upper())
    if end_minutes is None:
        return False
    return end_minutes >= 18 * 60

candidates = []
for b in businesses:
    gmap_id = b.get('gmap_id')
    hours_str = b.get('hours')
    if not hours_str or hours_str == 'None':
        continue
    # hours_str is a string representation of a list of [day, range]
    try:
        hours_list = json.loads(hours_str.replace("'", '"'))
    except Exception:
        # fallback to ast.literal_eval
        import ast
        try:
            hours_list = ast.literal_eval(hours_str)
        except Exception:
            hours_list = None
    if not hours_list or not isinstance(hours_list, list):
        continue
    open_after_6 = False
    for entry in hours_list:
        if not isinstance(entry, list) or len(entry) < 2:
            continue
        day = entry[0]
        time_range = entry[1]
        if day in weekdays:
            try:
                if range_has_close_after_6(time_range):
                    open_after_6 = True
                    break
            except Exception:
                continue
    if open_after_6:
        if gmap_id in rating_map:
            candidates.append({
                'name': b.get('name'),
                'gmap_id': gmap_id,
                'hours': hours_str,
                'avg_rating': rating_map[gmap_id]
            })

# Sort by avg_rating desc
candidates_sorted = sorted(candidates, key=lambda x: (-x['avg_rating'], x['name']))
# Top 5
top5 = candidates_sorted[:5]

# Prepare output - round ratings to 3 decimals
for item in top5:
    item['avg_rating'] = round(item['avg_rating'], 3)

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_sSoNUWz7KZewdpSuYq6wPbGO': 'file_storage/call_sSoNUWz7KZewdpSuYq6wPbGO.json', 'var_call_GjbVz3lyHigPoEmL25se4L2z': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'cnt': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'cnt': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'cnt': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'cnt': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'cnt': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'cnt': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'cnt': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'cnt': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'cnt': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'cnt': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'cnt': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'cnt': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'cnt': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'cnt': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'cnt': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'cnt': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'cnt': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'cnt': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'cnt': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'cnt': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'cnt': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'cnt': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'cnt': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'cnt': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'cnt': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'cnt': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'cnt': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'cnt': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'cnt': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'cnt': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'cnt': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'cnt': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'cnt': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'cnt': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'cnt': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'cnt': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'cnt': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'cnt': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'cnt': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'cnt': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'cnt': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'cnt': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'cnt': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'cnt': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'cnt': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'cnt': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'cnt': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'cnt': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'cnt': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'cnt': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'cnt': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'cnt': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'cnt': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'cnt': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'cnt': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'cnt': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'cnt': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'cnt': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'cnt': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'cnt': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'cnt': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'cnt': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'cnt': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'cnt': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'cnt': '3'}]}

exec(code, env_args)
