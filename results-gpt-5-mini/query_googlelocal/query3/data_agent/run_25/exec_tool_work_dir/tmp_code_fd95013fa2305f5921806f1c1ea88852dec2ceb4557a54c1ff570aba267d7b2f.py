code = """import json
import pandas as pd
import re

# Load previous tool results
reviews = var_call_h3ZZZQWIhWd4kWKOz1CnyT4N
# var_call_oWUq... is a file path containing the large JSON result
with open(var_call_oWUq9SWfG2Wv9zcxhXfn7oZs, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Normalize reviews into DataFrame
df_reviews = pd.DataFrame(reviews)
if not df_reviews.empty:
    df_reviews['avg_rating'] = df_reviews['avg_rating'].astype(float)

# Normalize businesses into DataFrame
df_biz = pd.DataFrame(businesses)

# Function to parse time strings like '9:30AM', '11AM', etc. into minutes since midnight
def parse_time(t):
    t = t.strip().upper().replace('.', '')
    # Ensure there's a space before AM/PM for easier parsing
    t = re.sub(r'(?i)(AM|PM)$', lambda m: ' ' + m.group(1), t)
    parts = t.split()
    if len(parts) == 2:
        time_part, ampm = parts
    else:
        # If no AM/PM found, try to infer (assume AM if hour between 1-11 and PM for common closing times)
        time_part = parts[0]
        ampm = None
    if ':' in time_part:
        h, m = time_part.split(':')
    else:
        h, m = time_part, '0'
    h = int(h)
    m = int(m)
    if ampm is None:
        # ambiguous - default heuristic: hours 7-11 => AM, 12 => PM?, 1-6 => PM for closing times
        if 7 <= h <= 11:
            ampm = 'AM'
        elif h == 12:
            ampm = 'PM'
        else:
            # treat 1-6 as PM (for late times)
            ampm = 'PM'
    if ampm == 'AM':
        if h == 12:
            h24 = 0
        else:
            h24 = h
    else:
        # PM
        if h == 12:
            h24 = 12
        else:
            h24 = h + 12
    return h24 * 60 + m

# Function to determine if any weekday closes after 18:00
weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def closes_after_6pm(hours_str):
    if hours_str is None:
        return False
    if isinstance(hours_str, str) and hours_str.strip().lower() == 'none':
        return False
    # hours_str should be a JSON-like string representing list of [day, times]
    try:
        hours_list = json.loads(hours_str)
    except Exception:
        # If parsing fails, can't determine
        return False
    for day, times in hours_list:
        if day not in weekday_names:
            continue
        if not isinstance(times, str):
            continue
        if 'closed' in times.lower():
            continue
        # Find end time using regex capturing start and end
        # Replace unicode en-dash with hyphen
        times_clean = times.replace('\u2013', '-').replace('\u2014', '-').replace('\u2012', '-')
        # Some times may include multiple ranges; split on comma or '/'
        ranges = re.split(r'[,/]| and ', times_clean)
        for r in ranges:
            r = r.strip()
            m = re.search(r"(\d{1,2}(?::\d{2})?\s*[APMapm\.]*?)\s*[\u2013\-–—]\s*(\d{1,2}(?::\d{2})?\s*[APMapm\.]*)", r)
            if not m:
                # try simple split by hyphen
                if '-' in r:
                    parts = r.split('-')
                    if len(parts) >= 2:
                        start_s = parts[0].strip()
                        end_s = parts[1].strip()
                    else:
                        continue
                else:
                    continue
            else:
                start_s = m.group(1)
                end_s = m.group(2)
            try:
                end_min = parse_time(end_s)
            except Exception:
                continue
            if end_min > 18 * 60:
                return True
    return False

# Apply to businesses
df_biz['open_after_6pm_weekday'] = df_biz['hours'].apply(closes_after_6pm)

# Merge with ratings
df = pd.merge(df_biz, df_reviews[['gmap_id', 'avg_rating']], on='gmap_id', how='inner')

# Filter to those open after 6pm on at least one weekday
df_filtered = df[df['open_after_6pm_weekday'] == True].copy()

# Sort by avg_rating desc
df_filtered['avg_rating'] = df_filtered['avg_rating'].astype(float)
df_filtered = df_filtered.sort_values(by='avg_rating', ascending=False)

# Select top 5
top5 = df_filtered.head(5)

# Prepare output
output = []
for _, row in top5.iterrows():
    output.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'hours': row['hours'],
        'avg_rating': round(float(row['avg_rating']), 4)
    })

result_json = json.dumps(output)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_h3ZZZQWIhWd4kWKOz1CnyT4N': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}], 'var_call_oWUq9SWfG2Wv9zcxhXfn7oZs': 'file_storage/call_oWUq9SWfG2Wv9zcxhXfn7oZs.json'}

exec(code, env_args)
