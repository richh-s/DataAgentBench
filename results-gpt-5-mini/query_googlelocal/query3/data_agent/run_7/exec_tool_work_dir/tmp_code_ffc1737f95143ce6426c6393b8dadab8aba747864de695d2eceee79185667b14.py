code = """import json
import re

# Load data from storage variables
reviews = var_call_bf4Huv1acdQsGYF9bmpjkbId
business_file_path = var_call_bonnVK8IljBQWU4obFbtNmOk

with open(business_file_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Build avg rating mapping
avg_map = {r['gmap_id']: float(r['avg_rating']) for r in reviews}

WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

# Helper to parse time token into minutes since midnight
def parse_time_token(token, ref_ampm=None):
    token = token.strip()
    # Normalize dots and spaces
    token = token.replace('.', '').upper()
    # Extract AM/PM
    m = re.search(r'(AM|PM)', token)
    ampm = m.group(1) if m else None
    # Remove AM/PM from token
    if ampm:
        token_core = token.replace(ampm, '').strip()
    else:
        token_core = token
    # Split hour and minute
    if ':' in token_core:
        h_str, m_str = token_core.split(':', 1)
        hour = int(h_str)
        minute = int(re.sub(r'\D', '', m_str) or 0)
    else:
        # token like '6' or '12'
        hour = int(re.sub(r'\D', '', token_core) or 0)
        minute = 0
    # Decide ampm if missing
    if not ampm:
        if ref_ampm:
            ampm = ref_ampm
        else:
            # Heuristic: assume PM for typical closing times >=7 or if hour between 1-6 and we expect PM for end times
            if hour == 12:
                ampm = 'PM'
            elif hour >= 7:
                ampm = 'PM'
            else:
                # default to AM (but this is unlikely for closing times)
                ampm = 'AM'
    # Convert to 24-hour
    if ampm == 'PM' and hour != 12:
        hour24 = hour + 12
    elif ampm == 'AM' and hour == 12:
        hour24 = 0
    else:
        hour24 = hour
    return hour24 * 60 + minute

# Helper to determine if a given time range string ends after 6:00 PM
def ends_after_6pm(time_str):
    if not time_str or time_str.strip().lower() == 'closed':
        return False
    ts = time_str.replace('\u2013', '-').replace('\u2014', '-').replace('\u2212','-')
    ts = ts.replace('\xa0', ' ')
    ts = ts.strip()
    if ts.lower() == 'open 24 hours':
        return True
    # Some entries like '3–8PM' or '12–9PM' or '10AM–8PM' etc
    parts = ts.split('-')
    if len(parts) < 2:
        return False
    start_tok = parts[0].strip()
    end_tok = '-'.join(parts[1:]).strip()
    # Try to find AM/PM from end token
    m = re.search(r'(AM|PM|am|pm)', end_tok)
    end_ampm = m.group(1).upper() if m else None
    # Parse end time
    try:
        end_minutes = parse_time_token(end_tok, ref_ampm=end_ampm)
    except Exception:
        return False
    return end_minutes > 18 * 60

# Process businesses
results = []
for b in businesses:
    gid = b.get('gmap_id')
    name = b.get('name')
    hours_raw = b.get('hours')
    if not hours_raw or hours_raw == 'None':
        continue
    try:
        hours_parsed = json.loads(hours_raw)
    except Exception:
        # if not JSON, skip
        continue
    # Check weekdays
    open_after_6 = False
    for day_entry in hours_parsed:
        if not isinstance(day_entry, (list, tuple)) or len(day_entry) < 2:
            continue
        day_name = day_entry[0]
        time_str = day_entry[1]
        if day_name in WEEKDAYS:
            if ends_after_6pm(time_str):
                open_after_6 = True
                break
    if not open_after_6:
        continue
    if gid not in avg_map:
        continue
    results.append({
        'gmap_id': gid,
        'name': name,
        'hours': hours_raw,
        'avg_rating': round(avg_map[gid], 3)
    })

# Sort by avg_rating desc and take top 5
results_sorted = sorted(results, key=lambda x: x['avg_rating'], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps(results_sorted, ensure_ascii=False))"""

env_args = {'var_call_bf4Huv1acdQsGYF9bmpjkbId': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}], 'var_call_bonnVK8IljBQWU4obFbtNmOk': 'file_storage/call_bonnVK8IljBQWU4obFbtNmOk.json'}

exec(code, env_args)
