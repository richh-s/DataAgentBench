code = """import json
import pandas as pd
import re
from ast import literal_eval

# Load business data from file path stored in var_call_z8FbFgcR2MHzcmQOd1prQK00
business_file = var_call_z8FbFgcR2MHzcmQOd1prQK00
with open(business_file, 'r', encoding='utf-8') as f:
    business_data = json.load(f)

# Load review averages from var_call_0JQ3NtM3m45Pbi2GIVMJQzr8 (already a Python list)
review_avgs = var_call_0JQ3NtM3m45Pbi2GIVMJQzr8

# Create DataFrames
bdf = pd.DataFrame(business_data)
rdf = pd.DataFrame(review_avgs)
# Ensure avg_rating numeric
rdf['avg_rating'] = rdf['avg_rating'].astype(float)

# Merge
df = pd.merge(bdf, rdf, on='gmap_id', how='inner')

# Helper to parse time string to minutes since midnight
ampm_re = re.compile(r"^(\d{1,2})(?::(\d{2}))?\s*([APap][Mm])$")

def parse_ampm(t):
    t = t.strip()
    m = ampm_re.match(t)
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

# Split range like '9AM–5PM' into open, close minutes
range_sep_re = re.compile(r'[\u2013\u2014\-–—]')

def parse_range(range_str):
    parts = range_sep_re.split(range_str)
    if len(parts) != 2:
        return (None, None)
    open_s = parts[0].strip()
    close_s = parts[1].strip()
    if open_s.lower() == 'closed' or close_s.lower() == 'closed':
        return (None, None)
    o = parse_ampm(open_s)
    c = parse_ampm(close_s)
    return (o, c)

# Days considered weekdays
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

results = []
for _, row in df.iterrows():
    hours_raw = row.get('hours')
    if hours_raw is None:
        continue
    if isinstance(hours_raw, str) and hours_raw.strip().lower() == 'none':
        continue
    hours_list = None
    # Try JSON load
    try:
        hours_list = json.loads(hours_raw)
    except Exception:
        try:
            hours_list = literal_eval(hours_raw)
        except Exception:
            hours_list = None
    if not hours_list:
        continue
    # hours_list expected like [["Thursday","6:30AM–6PM"], ...]
    open_after_6 = False
    for entry in hours_list:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in weekdays:
            continue
        if not isinstance(times, str):
            continue
        # Some entries like 'Closed'
        if 'closed' in times.lower():
            continue
        o,c = parse_range(times)
        if c is None:
            continue
        if c > 18*60:
            open_after_6 = True
            break
    if open_after_6:
        results.append({
            'name': row.get('name'),
            'hours': hours_raw,
            'avg_rating': row.get('avg_rating')
        })

# Sort by avg_rating desc and take top 5
results_sorted = sorted(results, key=lambda x: float(x['avg_rating']), reverse=True)[:5]
# Convert avg_rating to float with 3 decimals
for r in results_sorted:
    r['avg_rating'] = round(float(r['avg_rating']), 3)

import json as _json
print("__RESULT__:")
print(_json.dumps(results_sorted))"""

env_args = {'var_call_z8FbFgcR2MHzcmQOd1prQK00': 'file_storage/call_z8FbFgcR2MHzcmQOd1prQK00.json', 'var_call_0JQ3NtM3m45Pbi2GIVMJQzr8': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
