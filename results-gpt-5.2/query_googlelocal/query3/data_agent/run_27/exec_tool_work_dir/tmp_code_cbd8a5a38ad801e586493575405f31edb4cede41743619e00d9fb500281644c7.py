code = """import json, ast
import pandas as pd

reviews = pd.DataFrame(var_call_xcRO4pNeN8CyFdFHR11FNszn)
# load businesses (may be file path)
biz_src = var_call_di5EDmJR3S6ySaTA2XninUUu
if isinstance(biz_src, str):
    with open(biz_src, 'r', encoding='utf-8') as f:
        biz_records = json.load(f)
else:
    biz_records = biz_src
biz = pd.DataFrame(biz_records)

# normalize types
reviews['avg_rating'] = reviews['avg_rating'].astype(float)
reviews['review_count'] = reviews['review_count'].astype(int)

# parse hours (stored as string repr of list-of-lists or None)
def parse_hours(val):
    if val is None:
        return None
    if isinstance(val, (list, dict)):
        return val
    s = str(val)
    if s == 'None' or s.strip() == '':
        return None
    try:
        return json.loads(s)
    except Exception:
        try:
            return ast.literal_eval(s)
        except Exception:
            return None

biz['hours_parsed'] = biz['hours'].apply(parse_hours)

weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def closes_after_6pm(hours_parsed):
    if not isinstance(hours_parsed, list):
        return False
    for item in hours_parsed:
        if not (isinstance(item, (list, tuple)) and len(item) >= 2):
            continue
        day, hrs = item[0], item[1]
        if day not in weekdays:
            continue
        if not isinstance(hrs, str):
            continue
        h = hrs.strip()
        if h.lower() in {'closed'}:
            continue
        if 'Open 24 hours' in h or '24 hours' in h:
            return True
        if '–' in h:
            end = h.split('–',1)[1].strip()
        elif '-' in h:
            end = h.split('-',1)[1].strip()
        else:
            continue
        # parse end time
        try:
            t = pd.to_datetime(end, format='%I:%M%p', errors='coerce')
            if pd.isna(t):
                t = pd.to_datetime(end, format='%I%p', errors='coerce')
            if pd.isna(t):
                continue
            minutes = int(t.hour)*60 + int(t.minute)
            if minutes > 18*60:
                return True
        except Exception:
            continue
    return False

biz['open_after_6_weekday'] = biz['hours_parsed'].apply(closes_after_6pm)

merged = reviews.merge(biz[['gmap_id','name','hours','open_after_6_weekday']], on='gmap_id', how='inner')
filtered = merged[merged['open_after_6_weekday']].copy()
filtered = filtered.sort_values(['avg_rating','review_count'], ascending=[False, False]).head(5)

out = filtered[['name','hours','avg_rating']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_xcRO4pNeN8CyFdFHR11FNszn': [{'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}], 'var_call_di5EDmJR3S6ySaTA2XninUUu': 'file_storage/call_di5EDmJR3S6ySaTA2XninUUu.json'}

exec(code, env_args)
