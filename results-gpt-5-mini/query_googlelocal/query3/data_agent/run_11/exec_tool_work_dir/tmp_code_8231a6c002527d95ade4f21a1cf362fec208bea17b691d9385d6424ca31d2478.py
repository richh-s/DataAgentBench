code = """import json
import ast
import re

# Load data from previous tool results
# var_call_E99KRpT8nd461prWqqmNzlNN is a file path to the large JSON result
with open(var_call_E99KRpT8nd461prWqqmNzlNN, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

reviews = var_call_iFqK0lnmfpPZGJABQ1hwyoL4

# Build avg rating map
avg_map = {r['gmap_id']: float(r['avg_rating']) for r in reviews}

# Helper to parse time strings to minutes since midnight
def parse_time(t):
    t = t.strip()
    # handle special cases
    if t.lower() == 'open 24 hours':
        return None  # signal for 24h
    if t.lower() == 'closed':
        return None
    # Regex to capture hour, optional minute, optional am/pm
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?\s*([AaPp][Mm])?$", t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3)
    if ampm:
        ampm = ampm.upper()
        if ampm == 'AM':
            if hour == 12:
                hour = 0
        else:  # PM
            if hour != 12:
                hour += 12
    else:
        # No AM/PM provided; ambiguous. We'll return hour in 24h if reasonable
        # If hour == 24 -> 0
        if hour == 24:
            hour = 0
    return hour * 60 + minute

# Split range like '3–8PM' or '9:30AM–10PM'
def split_range(s):
    parts = re.split(r'[\u2013\u2014\-]', s)
    parts = [p.strip() for p in parts]
    if len(parts) == 1:
        return parts[0], None
    return parts[0], parts[1]

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

qualified = []
for b in businesses:
    gid = b.get('gmap_id')
    hours_raw = b.get('hours')
    if not hours_raw or hours_raw == 'None':
        continue
    try:
        parsed = ast.literal_eval(hours_raw)
    except Exception:
        # If can't parse, skip
        continue
    # parsed expected as list of [day, hours]
    stays_open_after_6 = False
    for day_entry in parsed:
        if not isinstance(day_entry, (list, tuple)) or len(day_entry) < 2:
            continue
        day, hrs = day_entry[0], day_entry[1]
        if day not in weekdays:
            continue
        if not hrs or hrs.lower() == 'closed':
            continue
        if 'open 24' in hrs.lower():
            stays_open_after_6 = True
            break
        # hrs might be like '3–8PM' or '3–8 PM' or '11AM–9:30PM' or '3–8PM'
        start_s, end_s = split_range(hrs)
        if not end_s:
            continue
        # Determine am/pm inheritance
        # If end has AM/PM but start doesn't, append end's am/pm to start
        m_end = re.search(r'([AaPp][Mm])', end_s)
        m_start = re.search(r'([AaPp][Mm])', start_s)
        if m_end and not m_start:
            # append end's AM/PM to start
            start_s = start_s + m_end.group(1)
        # Clean spaces
        start_s = start_s.replace('.', '')
        end_s = end_s.replace('.', '')
        start_min = parse_time(start_s)
        end_min = parse_time(end_s)
        # If parse_time returned None for 'Open 24 hours' earlier handled
        if end_min is None:
            # could be because parse failed; try to detect 'PM' in string
            if 'PM' in end_s.upper() or 'AM' in end_s.upper():
                # fallback: try to extract numbers
                pass
            else:
                continue
        # If end_min indicates past 18:00 (1080 minutes)
        if end_min is not None and end_min > 18 * 60:
            stays_open_after_6 = True
            break
    if stays_open_after_6 and gid in avg_map:
        qualified.append({
            'gmap_id': gid,
            'name': b.get('name'),
            'hours': hours_raw,
            'avg_rating': avg_map[gid]
        })

# Sort by avg_rating desc, then by name
qualified_sorted = sorted(qualified, key=lambda x: (-x['avg_rating'], x['name']))
top5 = qualified_sorted[:5]

# Prepare JSON-serializable output
for item in top5:
    # round avg_rating to 6 decimals
    item['avg_rating'] = round(item['avg_rating'], 6)

import json
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_E99KRpT8nd461prWqqmNzlNN': 'file_storage/call_E99KRpT8nd461prWqqmNzlNN.json', 'var_call_iFqK0lnmfpPZGJABQ1hwyoL4': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'cnt': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'cnt': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'cnt': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'cnt': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'cnt': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'cnt': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'cnt': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'cnt': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'cnt': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'cnt': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'cnt': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'cnt': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'cnt': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'cnt': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'cnt': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'cnt': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'cnt': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'cnt': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'cnt': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'cnt': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'cnt': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'cnt': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'cnt': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'cnt': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'cnt': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'cnt': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'cnt': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'cnt': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'cnt': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'cnt': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'cnt': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'cnt': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'cnt': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'cnt': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'cnt': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'cnt': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'cnt': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'cnt': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'cnt': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'cnt': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'cnt': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'cnt': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'cnt': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'cnt': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'cnt': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'cnt': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'cnt': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'cnt': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'cnt': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'cnt': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'cnt': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'cnt': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'cnt': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'cnt': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'cnt': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'cnt': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'cnt': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'cnt': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'cnt': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'cnt': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'cnt': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'cnt': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'cnt': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'cnt': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'cnt': '3'}]}

exec(code, env_args)
