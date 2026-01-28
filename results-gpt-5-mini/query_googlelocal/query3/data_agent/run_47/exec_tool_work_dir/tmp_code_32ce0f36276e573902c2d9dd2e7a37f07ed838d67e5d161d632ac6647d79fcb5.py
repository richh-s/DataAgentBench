code = """import json, pandas as pd, re, ast

# Load review averages from storage variable
reviews = var_call_wEWNF5KA0w2TcLgcT64GyhrC

# Load business data from the file path stored in var_call_CTnigcrzhOcVJ5EonbzrSF1u
business_file_path = var_call_CTnigcrzhOcVJ5EonbzrSF1u
with open(business_file_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Build mapping from gmap_id to avg_rating (float)
rating_map = {}
for r in reviews:
    try:
        rating_map[r['gmap_id']] = float(r['avg_rating'])
    except:
        continue

# Helper to parse time like '9:30PM' or '6AM' -> minutes since midnight
def parse_time(t):
    t = t.strip()
    # handle cases like 'Closed' or 'None'
    if t.lower() == 'closed' or t.lower() == 'none' or t == '':
        return None
    # regex to extract hour, optional minute, am/pm
    m = re.match(r"^(\d{1,2})(?::(\d{1,2}))?\s*([AaPp][Mm])$", t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3).upper()
    if hour == 12:
        hour = 0
    if ampm == 'PM':
        hour += 12
    return hour*60 + minute

# Helper to determine if a given time range string ends after 6:00 PM
def closes_after_6pm(time_range_str):
    if not time_range_str or time_range_str.lower() == 'closed':
        return False
    # split on en-dash, em-dash, hyphen
    parts = re.split('[–—-]', time_range_str)
    if len(parts) < 2:
        return False
    closing = parts[-1].strip()
    close_min = parse_time(closing)
    if close_min is None:
        return False
    return close_min > 18*60  # strictly after 6:00 PM

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

results = []
for b in businesses:
    gmap = b.get('gmap_id')
    hours = b.get('hours')
    name = b.get('name')
    avg = rating_map.get(gmap)
    if avg is None:
        continue
    qualifies = False
    # hours may be a string representation of list or 'None'
    if hours and hours != 'None':
        # try to parse as JSON/list
        hrs = None
        try:
            hrs = json.loads(hours)
        except Exception:
            try:
                hrs = ast.literal_eval(hours)
            except Exception:
                hrs = None
        if isinstance(hrs, list):
            # hrs likely list of [day, time_range]
            for entry in hrs:
                if not isinstance(entry, (list, tuple)) or len(entry) < 2:
                    continue
                day = entry[0]
                time_range = entry[1]
                if day in weekdays and closes_after_6pm(time_range):
                    qualifies = True
                    break
    if qualifies:
        results.append({'name': name, 'gmap_id': gmap, 'hours': hours, 'avg_rating': round(avg, 4)})

# Sort by avg_rating desc and take top 5
results_sorted = sorted(results, key=lambda x: x['avg_rating'], reverse=True)[:5]

# Prepare output
out = []
for r in results_sorted:
    out.append({'name': r['name'], 'hours': r['hours'], 'avg_rating': r['avg_rating']})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_CTnigcrzhOcVJ5EonbzrSF1u': 'file_storage/call_CTnigcrzhOcVJ5EonbzrSF1u.json', 'var_call_wEWNF5KA0w2TcLgcT64GyhrC': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'num_reviews': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'num_reviews': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'num_reviews': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'num_reviews': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'num_reviews': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'num_reviews': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'num_reviews': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'num_reviews': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'num_reviews': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'num_reviews': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'num_reviews': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'num_reviews': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'num_reviews': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'num_reviews': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'num_reviews': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'num_reviews': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'num_reviews': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'num_reviews': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'num_reviews': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'num_reviews': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'num_reviews': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'num_reviews': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'num_reviews': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'num_reviews': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'num_reviews': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'num_reviews': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'num_reviews': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'num_reviews': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'num_reviews': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'num_reviews': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'num_reviews': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'num_reviews': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'num_reviews': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'num_reviews': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'num_reviews': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'num_reviews': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'num_reviews': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'num_reviews': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'num_reviews': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'num_reviews': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'num_reviews': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'num_reviews': '3'}]}

exec(code, env_args)
