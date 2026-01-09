code = """import json, ast, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

reviews = pd.DataFrame(load_records(var_call_Pjdi51nqNvZkzGr2GtsFar8W))
biz = pd.DataFrame(load_records(var_call_yzrvREjFEENZ93xSEt9tJcGA))

# prep
reviews['avg_rating'] = reviews['avg_rating'].astype(float)
reviews['review_count'] = reviews['review_count'].astype(int)

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

# parse hours string like [["Thursday", "11AM–9:30PM"], ...]

def parse_hours(hours_val):
    if hours_val is None:
        return None
    if isinstance(hours_val, (list, dict)):
        return hours_val
    s = str(hours_val)
    if s in ('None', 'null', ''):
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
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(am|pm)$', t, re.I)
    if not m:
        return None
    hh = int(m.group(1))
    mm = int(m.group(2) or 0)
    ap = m.group(3).lower()
    if ap == 'am':
        if hh == 12:
            hh = 0
    else:
        if hh != 12:
            hh += 12
    return hh*60 + mm


def closes_after_6pm_on_weekday(hours_list):
    if not isinstance(hours_list, list):
        return False
    for entry in hours_list:
        if not (isinstance(entry, list) and len(entry) >= 2):
            continue
        day = entry[0]
        hrs = entry[1]
        if day not in weekday_set:
            continue
        if not isinstance(hrs, str):
            continue
        h = hrs.strip()
        if h.lower() == 'closed':
            continue
        if 'Open 24 hours'.lower() in h.lower():
            return True
        # handle possible multiple intervals separated by commas
        parts = [p.strip() for p in re.split(r',\s*', h) if p.strip()]
        for p in parts:
            # normalize dash
            p2 = p.replace('–','-').replace('—','-')
            if '-' not in p2:
                continue
            start,end = [x.strip() for x in p2.split('-',1)]
            end_m = time_to_minutes(end)
            if end_m is None:
                continue
            if end_m > 18*60:
                return True
    return False

biz['hours_parsed'] = biz['hours'].apply(parse_hours)
biz['open_after_6_weekday'] = biz['hours_parsed'].apply(closes_after_6pm_on_weekday)

merged = reviews.merge(biz, on='gmap_id', how='inner')
filtered = merged[(merged['open_after_6_weekday']) & (merged['hours_parsed'].notna())]

# top 5 by avg_rating
out = filtered.sort_values(['avg_rating','review_count'], ascending=[False, False]).head(5)

# format hours as day: hours
hours_fmt = []
for hl in out['hours_parsed']:
    if isinstance(hl, list):
        hours_fmt.append('; '.join([f"{d}: {h}" for d,h in hl if isinstance(d,str)]) )
    else:
        hours_fmt.append(None)

result = []
for (idx,row), hf in zip(out.iterrows(), hours_fmt):
    result.append({
        'name': row['name'],
        'average_rating': round(float(row['avg_rating']), 3),
        'hours': hf
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Pjdi51nqNvZkzGr2GtsFar8W': [{'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}], 'var_call_yzrvREjFEENZ93xSEt9tJcGA': 'file_storage/call_yzrvREjFEENZ93xSEt9tJcGA.json'}

exec(code, env_args)
