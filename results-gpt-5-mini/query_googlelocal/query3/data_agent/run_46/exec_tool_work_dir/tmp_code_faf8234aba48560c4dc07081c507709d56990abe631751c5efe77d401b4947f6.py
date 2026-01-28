code = """import json, re
from datetime import datetime

# Load business data from the JSON file path
with open(var_call_iB654KRnDxW3HNSEjPW8er8n, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Load ratings data from the provided variable
ratings = var_call_RNwdvvvs19JlYOmyXhMcEyhd

# Convert ratings to dict
rating_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings}

WEEKDAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday']

# helper to parse a single time like '9:30AM' or '3PM' etc.
time_re = re.compile(r"^(\d{1,2})(?::(\d{2}))?\s*([AaPp][Mm])?$")

def parse_time_str(t, default_suffix=None):
    t = t.strip()
    m = time_re.match(t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    suffix = m.group(3)
    if suffix is None and default_suffix is not None:
        suffix = default_suffix
    if suffix:
        s = suffix.upper()
        if s == 'AM':
            if hour == 12:
                hour = 0
        elif s == 'PM':
            if hour != 12:
                hour += 12
    else:
        # no suffix and no default; ambiguous. Assume 24-hour? treat as hour as-is
        pass
    return hour*60 + minute


def is_open_after_18(time_range):
    # time_range examples: '9:30AM–9:30PM', '3–8PM', 'Open 24 hours', 'Closed'
    if not time_range or time_range.strip() == '' or 'Closed' in time_range:
        return False
    if 'Open 24' in time_range or 'Open 24 hours' in time_range:
        return True
    # split on dash variants
    parts = re.split('[\u2013\u2014-]+', time_range)
    if len(parts) < 2:
        return False
    start, end = parts[0].strip(), parts[1].strip()
    # detect AM/PM in end
    end_suffix_m = re.search('([AaPp][Mm])', end)
    start_suffix_m = re.search('([AaPp][Mm])', start)
    end_suffix = end_suffix_m.group(1) if end_suffix_m else None
    start_suffix = start_suffix_m.group(1) if start_suffix_m else None
    # If end contains words like 'PM' attached to number with no space, regex covers it
    try:
        end_min = parse_time_str(end, default_suffix=None if end_suffix else start_suffix)
        # if end has no suffix but start has, use start suffix
        if end_min is None:
            # try using start suffix as default
            end_min = parse_time_str(end, default_suffix=start_suffix)
        # If end still None, give up
        if end_min is None:
            return False
        # Handle cases where start lacks suffix but end has PM -> assume start same as end
        if not start_suffix and end_suffix:
            start_min = parse_time_str(start, default_suffix=end_suffix)
        else:
            start_min = parse_time_str(start, default_suffix=start_suffix)
        # If start_min None, set to 0
        if start_min is None:
            start_min = 0
    except Exception:
        return False
    # Check if end time is after 18:00 (1080 minutes)
    return end_min > 18*60

# Process businesses
results = []
for b in businesses:
    gmap = b.get('gmap_id')
    hours_raw = b.get('hours')
    qualifies = False
    if hours_raw and hours_raw != 'None':
        try:
            schedule = json.loads(hours_raw)
        except Exception:
            # fallback: treat as not qualifying
            schedule = None
        if schedule:
            # schedule is list of [day, time_str]
            for day, tstr in schedule:
                if day in WEEKDAYS:
                    if is_open_after_18(tstr):
                        qualifies = True
                        break
    if qualifies:
        avg = rating_map.get(gmap)
        if avg is None:
            continue
        results.append({'name': b.get('name'), 'gmap_id': gmap, 'hours': hours_raw, 'avg_rating': round(avg, 6)})

# sort by avg_rating desc
results_sorted = sorted(results, key=lambda x: x['avg_rating'], reverse=True)
top5 = results_sorted[:5]

# Prepare JSON string
out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0W3Tcfxh11VAqt2rSx0KMErY': ['review'], 'var_call_JGvOZHO81hBLgDNY4beS3gqJ': ['business_description'], 'var_call_iB654KRnDxW3HNSEjPW8er8n': 'file_storage/call_iB654KRnDxW3HNSEjPW8er8n.json', 'var_call_RNwdvvvs19JlYOmyXhMcEyhd': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
