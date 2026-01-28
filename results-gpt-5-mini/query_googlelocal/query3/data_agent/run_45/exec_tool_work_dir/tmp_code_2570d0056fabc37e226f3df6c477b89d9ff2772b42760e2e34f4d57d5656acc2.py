code = """import json
import re
import ast
import pandas as pd

# Load data from previous tool calls
# var_call_XDIyY7EbYvX7EJfRQJltuAa4 may be a file path (string) to a JSON file
business_data = None
if isinstance(var_call_XDIyY7EbYvX7EJfRQJltuAa4, str) and var_call_XDIyY7EbYvX7EJfRQJltuAa4.endswith('.json'):
    with open(var_call_XDIyY7EbYvX7EJfRQJltuAa4, 'r', encoding='utf-8') as f:
        business_data = json.load(f)
else:
    business_data = var_call_XDIyY7EbYvX7EJfRQJltuAa4

ratings_data = var_call_RYGtf0arDs5n3KEf3oWqG2LH

# Helper to parse time strings like '6:30AM', '6PM', etc.
def time_to_minutes(t):
    t = t.strip()
    # Normalize am/pm
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*([AaPp][Mm])$', t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3).upper()
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return hour * 60 + minute

# Helper to get closing time in minutes from a time range string
def parse_closing_minutes(range_str):
    if not range_str or range_str.strip().lower() == 'closed':
        return None
    # Split on various dash characters
    parts = re.split(r'\s*[\u2013\u2014-]\s*', range_str)
    if len(parts) < 2:
        return None
    end = parts[1].strip()
    # Some strings may include additional text like 'By appointment' or '/'
    # Keep only time component at start
    end_match = re.match(r'^(\d{1,2}(?::\d{2})?\s*[AaPp][Mm])', end)
    if not end_match:
        return None
    end_time = end_match.group(1)
    return time_to_minutes(end_time)

# Weekday names
weekdays = set(["Monday","Tuesday","Wednesday","Thursday","Friday"])

# Build ratings dict
ratings_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings_data}

# Evaluate businesses
qualified = []
for b in business_data:
    gmap_id = b.get('gmap_id')
    hours_raw = b.get('hours')
    name = b.get('name')
    if not hours_raw or hours_raw == 'None':
        continue
    # hours_raw is expected to be a JSON string representation of a list
    parsed = None
    try:
        parsed = json.loads(hours_raw)
    except Exception:
        try:
            parsed = ast.literal_eval(hours_raw)
        except Exception:
            parsed = None
    if not parsed or not isinstance(parsed, list):
        continue
    open_after_6 = False
    for entry in parsed:
        # entry expected like ["Thursday", "6:30AM–6PM"]
        if not (isinstance(entry, list) or isinstance(entry, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        time_range = entry[1]
        if day in weekdays:
            closing = parse_closing_minutes(time_range)
            if closing is not None and closing > 18*60:
                open_after_6 = True
                break
    if open_after_6 and gmap_id in ratings_map:
        qualified.append({
            'name': name,
            'gmap_id': gmap_id,
            'hours': hours_raw,
            'avg_rating': ratings_map[gmap_id]
        })

# Sort by avg_rating desc
qualified_sorted = sorted(qualified, key=lambda x: x['avg_rating'], reverse=True)
# Top 5
top5 = qualified_sorted[:5]

# Prepare output JSON
output = []
for item in top5:
    output.append({
        'name': item['name'],
        'gmap_id': item['gmap_id'],
        'hours': item['hours'],
        'avg_rating': round(item['avg_rating'], 6)
    })

print("__RESULT__:")
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_call_XDIyY7EbYvX7EJfRQJltuAa4': 'file_storage/call_XDIyY7EbYvX7EJfRQJltuAa4.json', 'var_call_RYGtf0arDs5n3KEf3oWqG2LH': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'cnt': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'cnt': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'cnt': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'cnt': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'cnt': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'cnt': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'cnt': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'cnt': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'cnt': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'cnt': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'cnt': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'cnt': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'cnt': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'cnt': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'cnt': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'cnt': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'cnt': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'cnt': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'cnt': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'cnt': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'cnt': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'cnt': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'cnt': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'cnt': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'cnt': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'cnt': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'cnt': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'cnt': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'cnt': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'cnt': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'cnt': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'cnt': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'cnt': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'cnt': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'cnt': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'cnt': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'cnt': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'cnt': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'cnt': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'cnt': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'cnt': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'cnt': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'cnt': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'cnt': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'cnt': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'cnt': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'cnt': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'cnt': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'cnt': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'cnt': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'cnt': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'cnt': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'cnt': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'cnt': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'cnt': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'cnt': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'cnt': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'cnt': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'cnt': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'cnt': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'cnt': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'cnt': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'cnt': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'cnt': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'cnt': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'cnt': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'cnt': '3'}]}

exec(code, env_args)
