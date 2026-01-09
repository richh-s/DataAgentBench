code = """import json, pandas as pd, re
from datetime import datetime

reviews = pd.DataFrame(var_call_9momzWnHyghxROlPwcrfRXYA)
reviews['avg_rating'] = reviews['avg_rating'].astype(float)
reviews['review_count'] = reviews['review_count'].astype(int)

# load businesses (may be file path)
biz_raw = var_call_M9ZniHvhjHop50HF5nwfrFyv
if isinstance(biz_raw, str):
    with open(biz_raw, 'r') as f:
        biz_list = json.load(f)
else:
    biz_list = biz_raw
biz = pd.DataFrame(biz_list)

# parse hours field which is stored as stringified JSON list or None

def parse_hours(val):
    if val is None or val == 'None':
        return None
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        s = val.strip()
        try:
            return json.loads(s)
        except Exception:
            return None
    return None

biz['hours_parsed'] = biz['hours'].apply(parse_hours)

weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

# time parsing: accept 'Open 24 hours' as always open; accept ranges with en dash

def to_minutes(t):
    t=t.strip()
    # handle like '8:30AM' or '8AM'
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$', t, re.I)
    if not m:
        return None
    hh=int(m.group(1))
    mm=int(m.group(2) or 0)
    ap=m.group(3).upper()
    if ap=='AM':
        if hh==12:
            hh=0
    else:
        if hh!=12:
            hh+=12
    return hh*60+mm


def closes_after_6pm(hours_list):
    if not hours_list:
        return False
    for day, hrs in hours_list:
        if day not in weekdays:
            continue
        if hrs is None:
            continue
        if isinstance(hrs, str) and 'Open 24 hours' in hrs:
            return True
        if isinstance(hrs, str) and 'Closed' in hrs:
            continue
        # split multiple ranges if present
        if not isinstance(hrs, str):
            continue
        parts = [p.strip() for p in hrs.split(',')]
        for part in parts:
            # normalize dash
            part = part.replace('–','-').replace('—','-')
            if '-' not in part:
                continue
            start,end = [x.strip() for x in part.split('-',1)]
            end_min = to_minutes(end)
            if end_min is None:
                continue
            if end_min > 18*60:
                return True
    return False

biz['open_after_6_weekday'] = biz['hours_parsed'].apply(closes_after_6pm)

# join with reviews
merged = biz.merge(reviews, on='gmap_id', how='inner')
filtered = merged[merged['open_after_6_weekday']].copy()
filtered = filtered.sort_values(['avg_rating','review_count'], ascending=[False, False]).head(5)

# format operating hours back to readable lines

def format_hours(hours_list):
    if not hours_list:
        return 'Hours not available'
    return '; '.join([f"{d}: {h}" for d,h in hours_list])

filtered['operating_hours'] = filtered['hours_parsed'].apply(format_hours)

out = filtered[['name','operating_hours','avg_rating']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9momzWnHyghxROlPwcrfRXYA': [{'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}], 'var_call_M9ZniHvhjHop50HF5nwfrFyv': 'file_storage/call_M9ZniHvhjHop50HF5nwfrFyv.json'}

exec(code, env_args)
