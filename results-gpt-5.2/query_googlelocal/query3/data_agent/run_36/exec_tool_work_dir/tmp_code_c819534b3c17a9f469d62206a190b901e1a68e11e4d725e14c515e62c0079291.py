code = """import json, re
import pandas as pd

# Load business rows (may be in file)
biz_src = var_call_uw07kZ6oSA21WYe5US5iBvtp
if isinstance(biz_src, str) and biz_src.endswith('.json'):
    with open(biz_src, 'r', encoding='utf-8') as f:
        biz_rows = json.load(f)
else:
    biz_rows = biz_src

rev_rows = var_call_IclK8PuiHv3tDlyyP8mTkwLm

biz_df = pd.DataFrame(biz_rows)
rev_df = pd.DataFrame(rev_rows)
if rev_df.empty or biz_df.empty:
    out = []
else:
    rev_df['avg_rating'] = pd.to_numeric(rev_df['avg_rating'], errors='coerce')

WEEKDAYS = {'monday','tuesday','wednesday','thursday','friday'}

# Parse hours field which is stored as a stringified JSON list of [day, hours]
def parse_hours(val):
    if val is None:
        return []
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        s = val.strip()
        try:
            return json.loads(s)
        except Exception:
            # sometimes single quotes; attempt replacement
            try:
                return json.loads(s.replace("'","\""))
            except Exception:
                return []
    return []

def time_to_minutes(t):
    t = t.strip().lower()
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(am|pm)$', t)
    if not m:
        return None
    h = int(m.group(1))
    minute = int(m.group(2) or 0)
    ampm = m.group(3)
    if ampm == 'am':
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    return h*60 + minute

six_pm = 18*60

def open_after_6(hours_text):
    ht = hours_text.strip()
    if ht.lower() == 'closed':
        return False
    if ht.lower() == 'open 24 hours':
        return True
    # split ranges by comma if multiple
    parts = [p.strip() for p in ht.split(',') if p.strip()]
    for p in parts:
        if '–' in p:
            a,b = [x.strip() for x in p.split('–',1)]
        elif '-' in p:
            a,b = [x.strip() for x in p.split('-',1)]
        else:
            continue
        end_m = time_to_minutes(b)
        if end_m is None:
            continue
        if end_m > six_pm:
            return True
    return False

qual_gmap = []
hours_map = {}
for r in biz_rows:
    g = r.get('gmap_id')
    hlist = parse_hours(r.get('hours'))
    hours_map[g] = hlist
    qualifies = False
    for day, ht in hlist:
        if str(day).strip().lower() in WEEKDAYS and open_after_6(str(ht)):
            qualifies = True
            break
    if qualifies:
        qual_gmap.append(g)

qual_set = set(qual_gmap)
qual_biz_df = biz_df[biz_df['gmap_id'].isin(qual_set)][['gmap_id','name','hours']].copy()
merged = qual_biz_df.merge(rev_df, on='gmap_id', how='inner')
merged = merged.dropna(subset=['avg_rating'])
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# Prepare output records
out_records = []
for _, row in merged.iterrows():
    out_records.append({
        'name': row['name'],
        'operating_hours': row['hours'],
        'average_rating': float(row['avg_rating'])
    })

print('__RESULT__:')
print(json.dumps(out_records, ensure_ascii=False))"""

env_args = {'var_call_uw07kZ6oSA21WYe5US5iBvtp': 'file_storage/call_uw07kZ6oSA21WYe5US5iBvtp.json', 'var_call_IclK8PuiHv3tDlyyP8mTkwLm': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
