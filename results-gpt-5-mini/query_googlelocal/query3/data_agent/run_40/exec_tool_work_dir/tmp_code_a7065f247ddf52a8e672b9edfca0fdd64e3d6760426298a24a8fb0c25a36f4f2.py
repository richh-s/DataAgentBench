code = """import json, re
from datetime import datetime

# Load data from storage variables
business_records = json.load(open(var_call_hJtF2jkOiGV4Q32VJwYy8qs5))
ratings = var_call_zEmitJtcdEyZNssGHkr8ubdG

# Build rating map
rating_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings}

WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

# helper to parse time strings to minutes since midnight
def parse_time_to_minutes(t, default_meridiem=None):
    t = t.strip()
    # handle formats like '9AM', '9:30AM', '12PM', '12:30 PM'
    m = re.match(r'^(?P<h>\d{1,2})(?::(?P<min>\d{2}))?\s*(?P<meridiem>AM|PM|am|pm)?$', t)
    if not m:
        return None
    h = int(m.group('h'))
    minute = int(m.group('min')) if m.group('min') else 0
    mer = m.group('meridiem')
    if not mer and default_meridiem:
        mer = default_meridiem
    if not mer:
        return None
    mer = mer.upper()
    if mer == 'AM':
        if h == 12:
            h = 0
    else: # PM
        if h != 12:
            h += 12
    return h*60 + minute


def closes_after_6pm(time_str):
    time_str = time_str.strip()
    if not time_str or time_str.lower() == 'closed':
        return False
    if 'open 24' in time_str.lower():
        return True
    # split on dash characters
    parts = re.split(r'[-–—]', time_str)
    if len(parts) < 2:
        return False
    open_part = parts[0].strip()
    close_part = parts[1].strip()
    # find meridiem in close_part
    close_mer = None
    m = re.search(r'(AM|PM|am|pm)', close_part)
    if m:
        close_mer = m.group(1).upper()
    # if open lacks meridiem but close has, use close's for open
    open_mer = None
    m2 = re.search(r'(AM|PM|am|pm)', open_part)
    if m2:
        open_mer = m2.group(1).upper()
    default_for_open = close_mer if (not open_mer and close_mer) else None
    close_minutes = parse_time_to_minutes(re.sub(r'\s*(AM|PM|am|pm)\s*$', lambda mm: mm.group(1).upper(), close_part).strip(), None)
    # try parsing close with its meridiem
    if close_minutes is None:
        # try parse with found meridiem explicitly
        if close_mer:
            close_minutes = parse_time_to_minutes(re.sub(r'(AM|PM|am|pm)','', close_part).strip(), close_mer)
    if close_minutes is None:
        return False
    # parse open if needed (not actually necessary for closing check)
    # check strictly after 6:00 PM -> > 18*60
    return close_minutes > 18*60

results = []
for b in business_records:
    name = b.get('name')
    gid = b.get('gmap_id')
    hours_str = b.get('hours')
    try:
        hours = json.loads(hours_str)
    except Exception:
        # fallback: try eval (not ideal), else skip
        try:
            hours = eval(hours_str)
        except Exception:
            hours = []
    qualifies = False
    for day_entry in hours:
        if len(day_entry) < 2:
            continue
        day = day_entry[0]
        time = day_entry[1]
        if day in WEEKDAYS:
            if closes_after_6pm(time):
                qualifies = True
                break
    if not qualifies:
        continue
    if gid not in rating_map:
        continue
    results.append({'name': name, 'gmap_id': gid, 'hours': hours_str, 'avg_rating': rating_map[gid]})

# sort by avg_rating desc
results_sorted = sorted(results, key=lambda x: (-x['avg_rating'], x['name']))[:5]

# prepare output list with rounded avg_rating
out = []
for r in results_sorted:
    out.append({'name': r['name'], 'hours': r['hours'], 'avg_rating': round(r['avg_rating'], 6)})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_hJtF2jkOiGV4Q32VJwYy8qs5': 'file_storage/call_hJtF2jkOiGV4Q32VJwYy8qs5.json', 'var_call_zEmitJtcdEyZNssGHkr8ubdG': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
