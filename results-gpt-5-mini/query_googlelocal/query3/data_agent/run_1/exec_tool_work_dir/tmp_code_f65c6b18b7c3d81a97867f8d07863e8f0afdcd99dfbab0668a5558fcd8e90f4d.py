code = """import json
import pandas as pd
import ast
import re

# Load data from storage variables
business_file = var_call_MzktguWuZn07shvUjpsSRpQw  # path to JSON file
with open(business_file, 'r', encoding='utf-8') as f:
    business_list = json.load(f)

reviews = var_call_SLQN0Tn4PUEnqy0Ff7QhQ02A

# DataFrames
df_b = pd.DataFrame(business_list)
df_r = pd.DataFrame(reviews)

# Convert avg_rating and review_count to numeric
df_r['avg_rating'] = df_r['avg_rating'].astype(float)
if 'review_count' in df_r.columns:
    df_r['review_count'] = df_r['review_count'].astype(int)

# Merge on gmap_id
df = pd.merge(df_b, df_r, on='gmap_id', how='inner')

# Helper to parse times
weekday_set = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def extract_ampm(t):
    m = re.search(r'(?i)(am|pm)', t)
    return m.group(1).upper() if m else None

def parse_time_to_minutes(t, default_ampm=None):
    t = t.strip()
    # match hour[:minute] and optional am/pm
    m = re.match(r'(?i)^(\d{1,2})(?::(\d{2}))?\s*(am|pm)?', t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2) or 0)
    ampm = m.group(3).upper() if m.group(3) else (default_ampm.upper() if default_ampm else None)
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    elif ampm == 'PM':
        if hour != 12:
            hour = hour + 12
    else:
        # no am/pm info: fall back to default if provided, else try heuristic
        if default_ampm:
            if default_ampm.upper() == 'AM':
                if hour == 12:
                    hour = 0
            else:
                if hour != 12:
                    hour = hour + 12
        else:
            # heuristic: if hour between 1 and 6, assume PM for closings in ranges like 3–8PM where start missing
            if hour <= 6:
                hour = hour + 12
            elif hour == 12:
                # ambiguous 12 -> assume PM
                hour = 12
            else:
                # assume as-is
                pass
    return hour * 60 + minute


def hours_have_close_after_6pm(hours_str):
    if not hours_str or not isinstance(hours_str, str):
        return False
    try:
        entries = ast.literal_eval(hours_str)
    except Exception:
        return False
    for day, times in entries:
        if day not in weekday_set:
            continue
        if not isinstance(times, str):
            continue
        t = times.strip()
        if t.lower().startswith('open 24'):
            return True
        if 'closed' in t.lower():
            continue
        # split range by dash variants
        parts = re.split(r'–|—|-', t)
        if len(parts) < 2:
            continue
        start = parts[0].strip()
        end = parts[1].strip()
        # find ampm info
        end_ampm = extract_ampm(end)
        start_ampm = extract_ampm(start)
        default_ampm = end_ampm or start_ampm
        end_minutes = parse_time_to_minutes(end, default_ampm)
        if end_minutes is None:
            continue
        if end_minutes > 18 * 60:
            return True
    return False

# Apply filter
df['open_after_6pm_weekday'] = df['hours'].apply(hours_have_close_after_6pm)

# Filter rows
df_filtered = df[df['open_after_6pm_weekday'] == True].copy()

# Sort by avg_rating desc, then by review_count desc
if 'review_count' in df_filtered.columns:
    df_filtered = df_filtered.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])
else:
    df_filtered = df_filtered.sort_values(by=['avg_rating'], ascending=False)

# Take top 5
top5 = df_filtered.head(5)

# Prepare output
result = []
for _, row in top5.iterrows():
    result.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'hours': row['hours'],
        'avg_rating': round(float(row['avg_rating']), 3),
        'review_count': int(row['review_count']) if 'review_count' in row and pd.notna(row['review_count']) else None
    })

output = json.dumps(result)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_MzktguWuZn07shvUjpsSRpQw': 'file_storage/call_MzktguWuZn07shvUjpsSRpQw.json', 'var_call_SLQN0Tn4PUEnqy0Ff7QhQ02A': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}]}

exec(code, env_args)
