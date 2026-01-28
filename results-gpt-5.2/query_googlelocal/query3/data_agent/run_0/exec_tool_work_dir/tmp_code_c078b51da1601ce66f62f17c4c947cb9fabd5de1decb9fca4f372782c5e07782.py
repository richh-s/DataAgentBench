code = """import json, ast, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str):
        # assume it's a json file path
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

reviews = pd.DataFrame(load_records(var_call_OSImIZf3cW8WCg2P32ZeYdVW))
biz = pd.DataFrame(load_records(var_call_pcz6cQpc0aZfi9vewo1AFZ51))

# normalize types
reviews['avg_rating'] = reviews['avg_rating'].astype(float)
reviews['review_count'] = reviews['review_count'].astype(int)

# parse hours field
WEEKDAYS = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def parse_hours_str(s):
    if s is None or s == 'None':
        return None
    if isinstance(s, list):
        return s
    if not isinstance(s, str):
        return None
    try:
        return json.loads(s)
    except Exception:
        try:
            return ast.literal_eval(s)
        except Exception:
            return None

def time_to_minutes(t):
    t = t.strip()
    if t.lower() == 'noon':
        return 12*60
    if t.lower() == 'midnight':
        return 0
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', t, re.I)
    if not m:
        return None
    hh = int(m.group(1))
    mm = int(m.group(2) or 0)
    ap = m.group(3).upper()
    if hh == 12:
        hh = 0
    minutes = hh*60 + mm
    if ap == 'PM':
        minutes += 12*60
    return minutes

def latest_close_minutes(hours_list):
    if not hours_list:
        return None
    latest = None
    for day, span in hours_list:
        if day not in WEEKDAYS:
            continue
        if not isinstance(span, str):
            continue
        sp = span.strip()
        if sp.lower() == 'closed':
            continue
        if sp.lower() == 'open 24 hours':
            close_m = 24*60
            latest = close_m if latest is None else max(latest, close_m)
            continue
        # handle possible multiple intervals separated by comma
        parts = [p.strip() for p in sp.split(',') if p.strip()]
        for part in parts:
            # formats like '9AM–5PM' using en dash
            if '–' in part:
                a,b = [x.strip() for x in part.split('–', 1)]
            elif '-' in part:
                a,b = [x.strip() for x in part.split('-', 1)]
            else:
                continue
            close_m = time_to_minutes(b)
            if close_m is None:
                continue
            latest = close_m if latest is None else max(latest, close_m)
    return latest

biz['hours_parsed'] = biz['hours'].apply(parse_hours_str)
biz['latest_weekday_close_m'] = biz['hours_parsed'].apply(latest_close_minutes)

# open after 6pm => close time strictly > 18:00
eligible_biz = biz[(biz['latest_weekday_close_m'].notna()) & (biz['latest_weekday_close_m'] > 18*60)].copy()

merged = eligible_biz.merge(reviews, on='gmap_id', how='inner')

# rank by avg rating desc
merged = merged.sort_values(['avg_rating','review_count'], ascending=[False, False])

top5 = merged.head(5)[['name','hours','avg_rating']]

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_OSImIZf3cW8WCg2P32ZeYdVW': [{'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}], 'var_call_pcz6cQpc0aZfi9vewo1AFZ51': 'file_storage/call_pcz6cQpc0aZfi9vewo1AFZ51.json'}

exec(code, env_args)
