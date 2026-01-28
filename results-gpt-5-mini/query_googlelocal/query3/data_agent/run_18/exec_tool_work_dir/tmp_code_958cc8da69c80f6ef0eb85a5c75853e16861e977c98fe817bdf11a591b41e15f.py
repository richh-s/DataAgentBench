code = """import json, re

# Load business records from the JSON file path variable
with open(var_call_UI4CNTlLUP09ht7ce95EWTjq, 'r') as f:
    businesses = json.load(f)

# Load ratings list variable
ratings_list = var_call_vCO5dE9ZUa6efeEjGH4nNVF5
ratings_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings_list}

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def parse_time(t):
    if not isinstance(t, str):
        return None
    s = t.strip().upper()
    # Normalize common unicode minus/dash to hyphen already handled elsewhere
    # Match formats like 6:30AM, 6AM, 12PM
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$", s)
    if not m:
        return None
    h = int(m.group(1))
    mns = int(m.group(2) or 0)
    ampm = m.group(3)
    if ampm == 'AM':
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    return h*60 + mns

qualifying = []
for b in businesses:
    gmap_id = b.get('gmap_id')
    name = b.get('name')
    hours_str = b.get('hours')
    if not hours_str:
        continue
    # hours_str is a JSON-formatted string representing a list of [day, time_range]
    try:
        hours = json.loads(hours_str)
    except Exception:
        # fallback: try eval (less safe but acceptable in this environment)
        try:
            hours = eval(hours_str)
        except Exception:
            continue

    open_after_6_weekday = False
    for entry in hours:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        time_range = entry[1]
        if not isinstance(time_range, str):
            continue
        if day not in weekdays:
            continue
        tr = time_range.strip()
        if tr.lower() == 'closed':
            continue
        # split on various dash characters
        parts = re.split(r'[\-\u2013\u2014]', tr)
        if len(parts) < 2:
            continue
        end_part = parts[-1].strip()
        end_minutes = parse_time(end_part)
        if end_minutes is None:
            continue
        if end_minutes > 18 * 60:
            open_after_6_weekday = True
            break
    if open_after_6_weekday and gmap_id in ratings_map:
        qualifying.append({
            'gmap_id': gmap_id,
            'name': name,
            'hours': hours_str,
            'avg_rating': ratings_map[gmap_id]
        })

# Sort by avg_rating desc, then name
qualifying_sorted = sorted(qualifying, key=lambda x: (-x['avg_rating'], x['name'] or ''))

top5 = qualifying_sorted[:5]
# Round ratings to 4 decimals for readability
for item in top5:
    item['avg_rating'] = round(item['avg_rating'], 4)

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_UI4CNTlLUP09ht7ce95EWTjq': 'file_storage/call_UI4CNTlLUP09ht7ce95EWTjq.json', 'var_call_vCO5dE9ZUa6efeEjGH4nNVF5': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
