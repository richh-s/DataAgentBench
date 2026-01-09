code = """import json, pandas as pd

# Load business rows (may be file path)
biz_src = var_call_raMlgDglXSnv1YbWZ2dHGk6x
if isinstance(biz_src, str):
    with open(biz_src, 'r', encoding='utf-8') as f:
        biz_rows = json.load(f)
else:
    biz_rows = biz_src

rev_rows = var_call_vxgTdtDH88zWyyMul5JBCIgg

biz = pd.DataFrame(biz_rows)
rev = pd.DataFrame(rev_rows)
if not rev.empty:
    rev['avg_rating'] = rev['avg_rating'].astype(float)

# parse hours stored as stringified JSON

def parse_hours(x):
    if x is None:
        return []
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        s = x.strip()
        try:
            return json.loads(s)
        except Exception:
            return []
    return []

weekday_names = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

# determine if any weekday closes after 6 PM or is open 24 hours

def to_minutes(t):
    t=t.strip().lower().replace(' ', '')
    # format like 9:30pm or 9pm
    import re
    m=re.match(r'^(\d{1,2})(?::(\d{2}))?(am|pm)$', t)
    if not m:
        return None
    h=int(m.group(1))%12
    mi=int(m.group(2) or 0)
    if m.group(3)=='pm':
        h+=12
    return h*60+mi


def open_after_6pm(hours_list):
    for day, rng in hours_list:
        if day not in weekday_names:
            continue
        if not isinstance(rng, str):
            continue
        r = rng.strip().lower()
        if 'open 24 hours' in r:
            return True
        if 'closed' in r:
            continue
        # split ranges by comma in case of multiple intervals
        parts=[p.strip() for p in r.split(',')]
        for p in parts:
            if '–' in p:
                a,b=[z.strip() for z in p.split('–',1)]
            elif '-' in p:
                a,b=[z.strip() for z in p.split('-',1)]
            else:
                continue
            end=to_minutes(b)
            if end is None:
                continue
            if end>18*60:
                return True
            # handle after midnight (e.g., 2am) which is < 6pm but logically late; treat as open after 6pm
            if end < 6*60:
                return True
    return False

biz['hours_parsed'] = biz['hours'].apply(parse_hours)
biz['open_after_6pm_weekday'] = biz['hours_parsed'].apply(open_after_6pm)

biz2 = biz[biz['open_after_6pm_weekday']].copy()

merged = biz2.merge(rev, on='gmap_id', how='left')
merged = merged.dropna(subset=['avg_rating'])

# rank top 5 by avg_rating desc, tie-breaker by name
top5 = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# format hours back to readable lines

def hours_to_str(hours_list):
    out=[]
    for day, rng in hours_list:
        out.append(f"{day}: {rng}")
    return " | ".join(out)

top5['operating_hours'] = top5['hours_parsed'].apply(hours_to_str)

result = top5[['name','operating_hours','avg_rating']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_raMlgDglXSnv1YbWZ2dHGk6x': 'file_storage/call_raMlgDglXSnv1YbWZ2dHGk6x.json', 'var_call_vxgTdtDH88zWyyMul5JBCIgg': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
