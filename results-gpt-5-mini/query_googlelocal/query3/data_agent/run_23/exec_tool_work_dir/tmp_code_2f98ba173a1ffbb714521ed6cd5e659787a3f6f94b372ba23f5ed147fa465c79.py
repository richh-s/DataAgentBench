code = """import json, ast
# Load data from storage variables
businesses_data = var_call_HsO6v0zk1XoAqEASeeSwfXso
reviews_data = var_call_YJnEsg4kh2BM8LaleOsRKu9B

# If businesses_data is a filepath, load it
if isinstance(businesses_data, str):
    with open(businesses_data, 'r', encoding='utf-8') as f:
        businesses = json.load(f)
else:
    businesses = businesses_data

# Convert reviews data to dict gmap_id -> avg_rating (float)
avg_rating_map = {r['gmap_id']: float(r['avg_rating']) for r in reviews_data}

# Helper to parse hours string into python list
def parse_hours_str(s):
    if s is None:
        return None
    if isinstance(s, str) and s.strip().lower() == 'none':
        return None
    # normalize dashes
    s2 = s.replace('\u2013','-').replace('\u2014','-').replace('–','-')
    try:
        return ast.literal_eval(s2)
    except Exception:
        # fallback try json loads
        try:
            return json.loads(s2)
        except Exception:
            return None

# parse time like '9:30AM' or '6PM' into minutes since midnight
def time_to_minutes(t):
    if t is None:
        return None
    t = t.strip()
    if not t:
        return None
    if t.lower() == 'closed':
        return None
    # normalize
    t = t.replace(' ', '').upper()
    # handle AM/PM
    if t.endswith('AM') or t.endswith('PM'):
        ampm = t[-2:]
        core = t[:-2]
        if core == '':
            return None
        if ':' in core:
            parts = core.split(':')
            try:
                hh = int(parts[0]); mm = int(parts[1])
            except:
                return None
        else:
            try:
                hh = int(core); mm = 0
            except:
                return None
        if ampm == 'AM':
            if hh == 12:
                hh = 0
        else: # PM
            if hh != 12:
                hh += 12
        return hh*60 + mm
    else:
        # try 24h format HH:MM or HH
        if ':' in t:
            try:
                hh,mm = t.split(':')
                return int(hh)*60 + int(mm)
            except:
                return None
        try:
            return int(t)*60
        except:
            return None

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

results = []
for b in businesses:
    gmap_id = b.get('gmap_id')
    hours_raw = b.get('hours')
    hours_list = parse_hours_str(hours_raw)
    if not hours_list:
        continue
    open_after_6 = False
    # hours_list expected as list of [day, timestr]
    for entry in hours_list:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        timestr = entry[1]
        if day not in weekdays:
            continue
        if not isinstance(timestr, str):
            continue
        if timestr.strip().lower() == 'closed':
            continue
        # normalize dashes
        timestr2 = timestr.replace('\u2013','-').replace('\u2014','-').replace('–','-')
        parts = timestr2.split('-')
        if len(parts) < 2:
            continue
        end_part = parts[-1].strip()
        end_min = time_to_minutes(end_part)
        if end_min is None:
            continue
        if end_min > 18*60:
            open_after_6 = True
            break
    if not open_after_6:
        continue
    if gmap_id not in avg_rating_map:
        continue
    results.append({
        'name': b.get('name'),
        'gmap_id': gmap_id,
        'hours': hours_raw,
        'avg_rating': avg_rating_map[gmap_id]
    })

# sort by avg_rating desc
results_sorted = sorted(results, key=lambda x: (-x['avg_rating'], x['name']))
 top5 = results_sorted[:5]

# Prepare output list with required fields (name, hours, avg_rating)
output = []
for r in top5:
    output.append({'name': r['name'], 'hours': r['hours'], 'avg_rating': r['avg_rating']})

print("__RESULT__:")
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_call_CVe2SIooeMpmtgCOwI0D8au2': ['review'], 'var_call_8LE5hyQLAvrQ48oUbdeVGqPe': ['business_description'], 'var_call_HsO6v0zk1XoAqEASeeSwfXso': 'file_storage/call_HsO6v0zk1XoAqEASeeSwfXso.json', 'var_call_YJnEsg4kh2BM8LaleOsRKu9B': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}]}

exec(code, env_args)
