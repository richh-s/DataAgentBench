code = """import json, ast, re
import pandas as pd

reviews = pd.DataFrame(var_call_ZhdJuw59iYSzHBuI8AoLhEMO)
# load businesses from file if needed
biz_raw = var_call_hbh9fR3EARQe6buhPGeqo4a1
if isinstance(biz_raw, str):
    with open(biz_raw, 'r', encoding='utf-8') as f:
        biz_list = json.load(f)
else:
    biz_list = biz_raw
biz = pd.DataFrame(biz_list)

# parse hours field (stringified python list) into list of [day, hours]
def parse_hours(x):
    if x is None:
        return None
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        if x.strip().lower() == 'none' or x.strip()=='' :
            return None
        try:
            return ast.literal_eval(x)
        except Exception:
            return None
    return None

weekdays = {'monday','tuesday','wednesday','thursday','friday'}

def closes_after_6pm_on_weekday(hours_list):
    if not hours_list:
        return False
    for day, hrs in hours_list:
        if day is None or hrs is None:
            continue
        if str(day).strip().lower() not in weekdays:
            continue
        s = str(hrs)
        if 'Closed' in s:
            continue
        if 'Open 24 hours' in s:
            return True
        # take last close time after an en dash
        if '–' in s:
            close_part = s.split('–')[-1].strip()
        elif '-' in s:
            close_part = s.split('-')[-1].strip()
        else:
            continue
        m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', close_part, re.IGNORECASE)
        if not m:
            continue
        hh = int(m.group(1))
        mm = int(m.group(2) or 0)
        ampm = m.group(3).upper()
        if ampm == 'AM':
            close_minutes = (0 if hh==12 else hh)*60 + mm
        else:
            close_minutes = (12 if hh==12 else hh+12)*60 + mm
        if close_minutes > 18*60:
            return True
    return False

biz['hours_parsed'] = biz['hours'].apply(parse_hours)
biz['after6_weekday'] = biz['hours_parsed'].apply(closes_after_6pm_on_weekday)

# join and rank
reviews['avg_rating'] = reviews['avg_rating'].astype(float)
merged = reviews.merge(biz, on='gmap_id', how='inner')
filtered = merged[(merged['after6_weekday'])]

# top 5 by avg_rating, tie-breaker review_count desc
filtered['review_count'] = filtered['review_count'].astype(int)
filtered = filtered.sort_values(['avg_rating','review_count'], ascending=[False, False]).head(5)

out = []
for _, r in filtered.iterrows():
    hours_list = r['hours_parsed']
    # present operating hours as "Day: Hours" lines
    if hours_list:
        hours_text = '; '.join([f"{d}: {h}" for d,h in hours_list])
    else:
        hours_text = None
    out.append({
        'name': r['name'],
        'operating_hours': hours_text,
        'average_rating': round(float(r['avg_rating']), 4)
    })

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_ZhdJuw59iYSzHBuI8AoLhEMO': [{'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}], 'var_call_hbh9fR3EARQe6buhPGeqo4a1': 'file_storage/call_hbh9fR3EARQe6buhPGeqo4a1.json'}

exec(code, env_args)
