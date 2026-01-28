code = """import json
import pandas as pd
import re

# Load data from storage variables
business_file = var_call_DsoAR22TE1ll4QFNUNBedCpr
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
reviews = var_call_iWrg5B97fAnFTHMzVtehUwTy

# Create DataFrames
df_bus = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Convert types
if 'avg_rating' in df_rev.columns:
    df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)

# Merge on gmap_id
df = pd.merge(df_bus, df_rev, on='gmap_id', how='inner')

# Helper to parse times
weekday_set = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def parse_time_str(t):
    t = t.strip()
    # Normalize dot characters and spaces
    t = t.replace('.', '').upper()
    # Regex to capture hour, minute, am/pm
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)?$', t)
    if not m:
        # try 24-hour like 17:30
        m2 = re.match(r'^(\d{1,2}):(\d{2})$', t)
        if m2:
            h = int(m2.group(1)); mnt = int(m2.group(2));
            return h + mnt/60.0
        return None
    h = int(m.group(1))
    mnt = int(m.group(2)) if m.group(2) else 0
    period = m.group(3)
    if period == 'AM':
        if h == 12:
            h = 0
    elif period == 'PM':
        if h != 12:
            h += 12
    # if no period, assume 24h
    return h + mnt/60.0

# Determine if business open after 18:00 on at least one weekday
results = []
for _, row in df.iterrows():
    hours_raw = row.get('hours')
    if hours_raw is None:
        continue
    if isinstance(hours_raw, str) and hours_raw.strip().lower() == 'none':
        continue
    # Try to load as JSON; clean some unicode dashes
    hours_list = None
    if isinstance(hours_raw, str):
        s = hours_raw
        # replace en-dash and em-dash with hyphen for splits, but keep for json
        s_clean = s.replace('\u2013', '-')
        s_clean = s_clean.replace('\u2014', '-')
        # sometimes the string already contains actual en-dash char
        s_clean = s_clean.replace('\u2013', '-')
        s_clean = s_clean.replace('\u2014', '-')
        # also replace special unicode en-dash and em-dash characters
        s_clean = s_clean.replace('\u2013', '-')
        s_clean = s_clean.replace('–', '-')
        s_clean = s_clean.replace('—', '-')
        try:
            hours_list = json.loads(s_clean)
        except Exception:
            # Try eval as fallback (safe-ish for this controlled data)
            try:
                hours_list = eval(s_clean)
            except Exception:
                hours_list = None
    else:
        hours_list = hours_raw
    if not hours_list:
        continue
    open_after_6 = False
    for entry in hours_list:
        try:
            day = entry[0]
            times = entry[1]
        except Exception:
            continue
        if day not in weekday_set:
            continue
        if not isinstance(times, str):
            continue
        if times.strip().lower() == 'closed':
            continue
        # split on hyphen
        parts = re.split(r"[-–—]", times)
        if len(parts) < 2:
            continue
        start = parts[0].strip()
        end = parts[1].strip()
        # remove whitespace between number and am/pm if any
        start = re.sub(r'\s+', '', start)
        end = re.sub(r'\s+', '', end)
        end_time = parse_time_str(end)
        if end_time is None:
            continue
        if end_time > 18.0:
            open_after_6 = True
            break
    if open_after_6:
        results.append({
            'name': row.get('name'),
            'gmap_id': row.get('gmap_id'),
            'hours': row.get('hours'),
            'avg_rating': row.get('avg_rating')
        })

# Sort by avg_rating desc and take top 5
results_sorted = sorted(results, key=lambda x: float(x['avg_rating']), reverse=True)
top5 = results_sorted[:5]

# Prepare JSON serializable output
for r in top5:
    # ensure avg_rating is float
    r['avg_rating'] = float(r['avg_rating'])

output = json.dumps(top5)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_DsoAR22TE1ll4QFNUNBedCpr': 'file_storage/call_DsoAR22TE1ll4QFNUNBedCpr.json', 'var_call_iWrg5B97fAnFTHMzVtehUwTy': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}]}

exec(code, env_args)
