code = """import json
import pandas as pd
import re

# Load data from storage variables
business_file = var_call_EIvTonFtVFZOvX1TYImM1jmx
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
reviews_avg = var_call_Dj53ezTh2cTkkSU1fgnGdMRF

# DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews_avg)
# convert avg_rating to float
df_r['avg_rating'] = df_r['avg_rating'].astype(float)

# merge
df = pd.merge(df_b, df_r, on='gmap_id', how='left')

# helper to parse time strings
time_re = re.compile(r"^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$", re.IGNORECASE)

def parse_time(t):
    t = t.strip().upper()
    m = time_re.match(t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3)
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return hour * 60 + minute

# function to check if any weekday closes after 6:00 PM
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])
def closes_after_6pm(hours_field):
    if not hours_field or hours_field == 'None':
        return False
    # hours_field is a string representation of a list
    try:
        hrs = json.loads(hours_field)
    except Exception:
        # fallback to literal eval
        try:
            import ast
            hrs = ast.literal_eval(hours_field)
        except Exception:
            return False
    # hrs expected like [["Thursday","6:30AM–6PM"], ...]
    for entry in hrs:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = entry[0]
        times = entry[1]
        if day not in weekdays:
            continue
        if not times or times.lower() == 'closed':
            continue
        # split on en-dash, em-dash, hyphen
        parts = re.split(r'[\u2013\u2014\-\u2212]', times)
        if len(parts) < 2:
            # sometimes use ASCII minus surrounded by special spaces; attempt splitting on non alphanum
            parts = re.split(r'\s+to\s+|\s*-\s*', times)
        if len(parts) < 2:
            continue
        close_str = parts[1].strip()
        # remove any trailing annotation like "(next day)"
        close_str = re.sub(r"\(.*\)", "", close_str).strip()
        # some strings like '6PM' or '9:30PM'
        close_min = parse_time(close_str)
        if close_min is None:
            continue
        if close_min > 18*60:
            return True
    return False

# Apply filter
df['open_after_6pm_weekday'] = df['hours'].apply(closes_after_6pm)
filtered = df[df['open_after_6pm_weekday'] & df['avg_rating'].notna()].copy()

# sort by avg_rating desc and take top 5
filtered['avg_rating'] = filtered['avg_rating'].astype(float)
top5 = filtered.sort_values('avg_rating', ascending=False).head(5)

# prepare output
result = []
for _, row in top5.iterrows():
    result.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'hours': row['hours'],
        'average_rating': round(float(row['avg_rating']), 3)
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rbRqIqXpOGn0pnFLsM5pUd4Q': ['review'], 'var_call_XkPo0dlLb1zUFnJjHImyrkE2': ['business_description'], 'var_call_EIvTonFtVFZOvX1TYImM1jmx': 'file_storage/call_EIvTonFtVFZOvX1TYImM1jmx.json', 'var_call_Dj53ezTh2cTkkSU1fgnGdMRF': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
