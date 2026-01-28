code = """import json, ast, re
import pandas as pd

# load data from previous tool results
businesss = json.load(open(var_call_YNSKhWWKM6kLhAkH33wX8mXo))
ratings = var_call_C1VKTzXaQdH2rvLtZCKTQfvx

df_b = pd.DataFrame(businesss)
df_r = pd.DataFrame(ratings)

# convert avg_rating to float
if 'avg_rating' in df_r.columns:
    df_r['avg_rating'] = df_r['avg_rating'].astype(float)
    df_r['review_count'] = df_r['review_count'].astype(int)

# merge
df = pd.merge(df_b, df_r, on='gmap_id', how='inner')

# function to check if open after 6pm on any weekday
weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def parse_time_to_minutes(t):
    if t is None:
        return None
    t = t.strip().upper()
    # handle formats like '11AM' or '9:30PM'
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$", t)
    if m:
        h = int(m.group(1))
        minute = int(m.group(2) or 0)
        period = m.group(3)
        if period == 'AM':
            if h == 12:
                h = 0
        else:
            if h != 12:
                h += 12
        return h*60 + minute
    # try without AM/PM
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?$", t)
    if m:
        h = int(m.group(1))
        minute = int(m.group(2) or 0)
        # ambiguous; assume 24-hour style if hour>=13 else leave as is
        if h < 24:
            return h*60 + minute
    return None


def hours_string_qualifies(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    s = hours_str
    # normalize dash
    s = s.replace('\u2013', '-').replace('\u2014','-')
    try:
        entries = ast.literal_eval(s)
    except Exception:
        return False
    for day, time_range in entries:
        if day not in weekdays:
            continue
        if not time_range or 'Closed' in time_range:
            continue
        tr = time_range.strip()
        if 'Open 24' in tr or '24 hours' in tr or '24-hour' in tr:
            return True
        # split by '-'
        if '-' in tr:
            parts = tr.split('-', 1)
            close_part = parts[1].strip()
            # sometimes close part may include day indicators; just parse time
            # ensure AM/PM appended; if missing, try to infer from open_part
            close_minutes = parse_time_to_minutes(close_part.upper())
            if close_minutes is None:
                # try to extract trailing AM/PM and add to close
                m = re.search(r"(AM|PM)$", parts[0].strip().upper())
                if m:
                    close_minutes = parse_time_to_minutes(close_part.upper() + m.group(1))
            if close_minutes is not None and close_minutes > 18*60:
                return True
    return False

# apply
df['open_after_6_on_weekday'] = df['hours'].apply(hours_string_qualifies)

df_filtered = df[df['open_after_6_on_weekday']]

# sort by avg_rating desc and take top 5
if df_filtered.empty:
    result = []
else:
    df_filtered = df_filtered.sort_values(by='avg_rating', ascending=False)
    top5 = df_filtered.head(5)
    result = []
    for _, row in top5.iterrows():
        result.append({'name': row['name'], 'gmap_id': row['gmap_id'], 'hours': row['hours'], 'avg_rating': round(float(row['avg_rating']), 3)})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NcHHaefoKLwraqzt8jXA8WlS': ['business_description'], 'var_call_YNSKhWWKM6kLhAkH33wX8mXo': 'file_storage/call_YNSKhWWKM6kLhAkH33wX8mXo.json', 'var_call_C1VKTzXaQdH2rvLtZCKTQfvx': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}]}

exec(code, env_args)
