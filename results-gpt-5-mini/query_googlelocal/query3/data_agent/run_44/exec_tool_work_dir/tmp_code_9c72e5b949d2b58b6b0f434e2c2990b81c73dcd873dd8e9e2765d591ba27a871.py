code = """import json
import pandas as pd
import re
import ast
import datetime

# Load data from previous tool results
rev = var_call_1hBiknLxJamdJbRoSBUqFjjM
business_file = var_call_qMcsIgf9EImB2HPrYAEY2jST
with open(business_file, 'r', encoding='utf-8') as f:
    biz = json.load(f)

# DataFrames
df_rev = pd.DataFrame(rev)
if not df_rev.empty:
    df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)

df_biz = pd.DataFrame(biz)

# Merge
df = pd.merge(df_biz, df_rev, on='gmap_id', how='inner')

weekdays = set(["Monday","Tuesday","Wednesday","Thursday","Friday"])

# helper functions

def try_parse_list(s):
    if s is None:
        return None
    if isinstance(s, list):
        return s
    # Some entries are the string "None"
    if isinstance(s, str) and s.strip().lower() == 'none':
        return None
    # Try json loads
    try:
        return json.loads(s)
    except Exception:
        try:
            return ast.literal_eval(s)
        except Exception:
            return None


def to_minutes(tstr):
    t = tstr.strip().upper().replace('.', '')
    # Normalize like '12' to '12'
    # Try formats
    for fmt in ('%I:%M%p', '%I%p'):
        try:
            dt = datetime.datetime.strptime(t, fmt)
            return dt.hour*60 + dt.minute
        except Exception:
            continue
    # If fails, try to extract numbers
    m = re.match(r"(\d{1,2})(?::(\d{2}))?\s*(AM|PM)?", t)
    if m:
        hour = int(m.group(1))
        minute = int(m.group(2) or 0)
        suffix = m.group(3)
        if suffix:
            suffix = suffix.upper()
            if suffix == 'AM' and hour == 12:
                hour = 0
            if suffix == 'PM' and hour != 12:
                hour += 12
        return hour*60 + minute
    return None


def closes_after_6pm(hours_field):
    lst = try_parse_list(hours_field)
    if lst is None:
        return False
    for entry in lst:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        time_str = entry[1]
        if day not in weekdays:
            continue
        if not isinstance(time_str, str):
            continue
        ts = time_str.strip()
        if ts.lower() == 'closed':
            continue
        if 'open 24' in ts.lower():
            return True
        # Replace unicode dashes with ascii
        parts = re.split(r'[–—-]', ts)
        if len(parts) != 2:
            # Some entries might be like '3–8PM' which splits fine; others unexpected
            continue
        left = parts[0].strip()
        right = parts[1].strip()
        # detect AM/PM in right
        m = re.search(r'(AM|PM)', right, re.I)
        right_suffix = m.group(1).upper() if m else None
        # If left lacks suffix but right has, append suffix to left
        if right_suffix and not re.search(r'(AM|PM)', left, re.I):
            left_mod = left + right_suffix
        else:
            left_mod = left
        # If right lacks suffix but left has, append left's suffix to right
        if not right_suffix and re.search(r'(AM|PM)', left, re.I):
            m2 = re.search(r'(AM|PM)', left, re.I)
            right_mod = right + m2.group(1).upper()
        else:
            right_mod = right
        # Now parse
        lmin = to_minutes(left_mod)
        rmin = to_minutes(right_mod)
        if lmin is None or rmin is None:
            continue
        # handle overnight: if rmin <= lmin, assume closes next day
        if rmin <= lmin:
            rmin += 24*60
        # check if close time strictly after 6:00 PM (18:00)
        if rmin > 18*60:
            return True
    return False

# Apply filter
candidates = []
for _, row in df.iterrows():
    hours_field = row.get('hours')
    if closes_after_6pm(hours_field):
        candidates.append({
            'gmap_id': row.get('gmap_id'),
            'name': row.get('name'),
            'hours': row.get('hours'),
            'avg_rating': float(row.get('avg_rating'))
        })

# Sort by avg_rating desc and take top 5
candidates_sorted = sorted(candidates, key=lambda x: (-x['avg_rating'], x['name']))[:5]

# Round ratings to 3 decimals for display
for c in candidates_sorted:
    c['avg_rating'] = round(c['avg_rating'], 3)

result = candidates_sorted

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_wOeAvnQ5HHmKbIE8RmuijwIe': ['review'], 'var_call_AHflkGgersTWKMTV7BOdnEfz': ['business_description'], 'var_call_1hBiknLxJamdJbRoSBUqFjjM': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'cnt_reviews': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'cnt_reviews': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'cnt_reviews': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'cnt_reviews': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'cnt_reviews': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'cnt_reviews': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'cnt_reviews': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'cnt_reviews': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'cnt_reviews': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'cnt_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'cnt_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'cnt_reviews': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'cnt_reviews': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'cnt_reviews': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'cnt_reviews': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'cnt_reviews': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'cnt_reviews': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'cnt_reviews': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'cnt_reviews': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'cnt_reviews': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'cnt_reviews': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'cnt_reviews': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'cnt_reviews': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'cnt_reviews': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'cnt_reviews': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'cnt_reviews': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'cnt_reviews': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'cnt_reviews': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'cnt_reviews': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'cnt_reviews': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'cnt_reviews': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'cnt_reviews': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'cnt_reviews': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'cnt_reviews': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'cnt_reviews': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'cnt_reviews': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'cnt_reviews': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'cnt_reviews': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'cnt_reviews': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'cnt_reviews': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'cnt_reviews': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'cnt_reviews': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'cnt_reviews': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'cnt_reviews': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'cnt_reviews': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'cnt_reviews': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'cnt_reviews': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'cnt_reviews': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'cnt_reviews': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'cnt_reviews': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'cnt_reviews': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'cnt_reviews': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'cnt_reviews': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'cnt_reviews': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'cnt_reviews': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'cnt_reviews': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'cnt_reviews': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'cnt_reviews': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'cnt_reviews': '3'}], 'var_call_qMcsIgf9EImB2HPrYAEY2jST': 'file_storage/call_qMcsIgf9EImB2HPrYAEY2jST.json'}

exec(code, env_args)
