code = """import json
import re

# Load business data from the provided file path variable
biz_file_path = var_call_PBzPUyXUc7SujFT4lVmAQrtc
with open(biz_file_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Load review aggregates from the storage variable
reviews = var_call_HqH2MGze2qRNOpoabHx9Aibs

# Build mapping gmap_id -> avg_rating (float)
rev_map = {r['gmap_id']: float(r['avg_rating']) for r in reviews}

# Helper to parse time strings like '6:30AM' or '6PM' into 24-hour float hours
time_re = re.compile(r"\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\s*$", re.I)

def parse_time(t):
    if t is None:
        return None
    m = time_re.match(t)
    if not m:
        return None
    h = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3).lower() if m.group(3) else None
    if ampm == 'pm' and h != 12:
        h += 12
    if ampm == 'am' and h == 12:
        h = 0
    return h + minute/60.0

# Splitter for ranges (handles en dash and hyphen variants)
range_split_re = re.compile(r'[\-\u2013\u2014\u2012]')

weekdays = set(["Monday","Tuesday","Wednesday","Thursday","Friday"])

results = []
for b in businesses:
    gmap = b.get('gmap_id')
    hours_field = b.get('hours')
    if not hours_field or hours_field == 'None':
        continue
    # hours_field is a JSON-like string; try to load
    try:
        hours_list = json.loads(hours_field)
    except Exception:
        # If parsing fails, skip
        continue
    open_after_6 = False
    for entry in hours_list:
        try:
            day = entry[0]
            times = entry[1]
        except Exception:
            continue
        if day not in weekdays:
            continue
        if not times or 'closed' in times.lower():
            continue
        # split start and end
        parts = range_split_re.split(times)
        if len(parts) < 2:
            # try em dash unicode explicitly
            parts = times.split('\u2013')
        start_s = parts[0].strip()
        end_s = parts[1].strip()
        # Some strings may include multiple pieces like '11AM–9:30PM' fine
        start_t = parse_time(start_s)
        end_t = parse_time(end_s)
        if end_t is None:
            continue
        if end_t > 18.0:
            open_after_6 = True
            break
    if not open_after_6:
        continue
    # get avg rating
    if gmap not in rev_map:
        continue
    avg = rev_map[gmap]
    results.append({
        'name': b.get('name'),
        'gmap_id': gmap,
        'hours': hours_field,
        'avg_rating': round(avg, 3)
    })

# Sort by avg_rating desc
results_sorted = sorted(results, key=lambda x: (-x['avg_rating'], x['name']))
# top 5
top5 = results_sorted[:5]

# Prepare printable JSON
out = json.dumps(top5, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NOBQcnmMHeyPDDcYXg1KoOv2': ['business_description'], 'var_call_PBzPUyXUc7SujFT4lVmAQrtc': 'file_storage/call_PBzPUyXUc7SujFT4lVmAQrtc.json', 'var_call_HqH2MGze2qRNOpoabHx9Aibs': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'num_reviews': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'num_reviews': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'num_reviews': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'num_reviews': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'num_reviews': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'num_reviews': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'num_reviews': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'num_reviews': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'num_reviews': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'num_reviews': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'num_reviews': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'num_reviews': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'num_reviews': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'num_reviews': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'num_reviews': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'num_reviews': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'num_reviews': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'num_reviews': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'num_reviews': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'num_reviews': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'num_reviews': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'num_reviews': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'num_reviews': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'num_reviews': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'num_reviews': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'num_reviews': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'num_reviews': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'num_reviews': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'num_reviews': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'num_reviews': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'num_reviews': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'num_reviews': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'num_reviews': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'num_reviews': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'num_reviews': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'num_reviews': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'num_reviews': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'num_reviews': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'num_reviews': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'num_reviews': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'num_reviews': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'num_reviews': '3'}]}

exec(code, env_args)
