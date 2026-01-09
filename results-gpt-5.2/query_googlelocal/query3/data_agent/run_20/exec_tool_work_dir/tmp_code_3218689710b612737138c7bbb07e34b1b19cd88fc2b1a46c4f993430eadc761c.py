code = """import json, pandas as pd, re

# Load business records (may be file path)
biz_raw = var_call_kgKJrIq9zxDIWy55BZf1k8XP
if isinstance(biz_raw, str):
    with open(biz_raw, 'r', encoding='utf-8') as f:
        biz = json.load(f)
else:
    biz = biz_raw

rev = var_call_7p4kJ4JDLeooaFJ1XqBU9Y1n

df_b = pd.DataFrame(biz)
df_r = pd.DataFrame(rev)

# Parse hours strings to list of [day, hours]
def parse_hours(s):
    if s is None:
        return None
    if isinstance(s, list):
        return s
    if isinstance(s, str):
        if s.strip().lower() in ('none','null',''):
            return None
        try:
            return json.loads(s)
        except Exception:
            return None
    return None

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def parse_close_time_to_minutes(hours_str):
    if not hours_str or not isinstance(hours_str, str):
        return None
    hs = hours_str.strip()
    if hs.lower() == 'open 24 hours':
        return 24*60
    if hs.lower() == 'closed':
        return None
    # handle multiple ranges separated by ','
    parts = [p.strip() for p in hs.split(',')]
    closes = []
    for p in parts:
        # expect like '9AM–7PM' or '3–8PM'
        if '–' not in p:
            continue
        start, end = [x.strip() for x in p.split('–', 1)]
        end_m = re.match(r'^(?P<h>\d{1,2})(?::(?P<m>\d{2}))?\s*(?P<ap>AM|PM)$', end, re.I)
        if not end_m:
            continue
        h = int(end_m.group('h'))
        m = int(end_m.group('m') or 0)
        ap = end_m.group('ap').upper()
        if ap == 'AM':
            if h == 12:
                h = 0
        else:
            if h != 12:
                h += 12
        closes.append(h*60 + m)
    return max(closes) if closes else None

rows = []
for rec in biz:
    hours_list = parse_hours(rec.get('hours'))
    if not hours_list:
        continue
    open_after_6 = False
    for day, hrs in hours_list:
        if day in weekday_set:
            close_min = parse_close_time_to_minutes(hrs)
            if close_min is not None and close_min > 18*60:
                open_after_6 = True
                break
    if open_after_6:
        rows.append({'gmap_id': rec.get('gmap_id'), 'name': rec.get('name'), 'hours': hours_list})

df_open = pd.DataFrame(rows)

df = df_open.merge(df_r, on='gmap_id', how='inner')
df['avg_rating'] = df['avg_rating'].astype(float)

df = df.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

out = []
for _, r in df.iterrows():
    hours_list = r['hours']
    # keep as dict day->hours for readability
    hours_dict = {d: h for d, h in hours_list}
    out.append({
        'name': r['name'],
        'average_rating': round(float(r['avg_rating']), 4),
        'operating_hours': hours_dict
    })

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_pXtnMCklDpk38x9l2KdhmnAE': [], 'var_call_7p4kJ4JDLeooaFJ1XqBU9Y1n': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}], 'var_call_eD1B5ImoWnksjeUSRXsPFcxk': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_call_kgKJrIq9zxDIWy55BZf1k8XP': 'file_storage/call_kgKJrIq9zxDIWy55BZf1k8XP.json'}

exec(code, env_args)
