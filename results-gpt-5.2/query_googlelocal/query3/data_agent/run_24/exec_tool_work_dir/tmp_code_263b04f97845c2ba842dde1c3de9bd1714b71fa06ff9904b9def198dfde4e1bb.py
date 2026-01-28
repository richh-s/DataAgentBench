code = """import json, pandas as pd, re

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

biz = load_records(var_call_AgtLDDWky7aypsGcmRfUnkJ6)
rev = load_records(var_call_6mqurSxk4SZBUqiO93BgW5dj)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# parse hours stored as JSON-ish string
biz_df['hours_parsed'] = biz_df['hours'].apply(lambda x: json.loads(x) if isinstance(x, str) else x)

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def to_minutes(t):
    t = t.strip().upper().replace(' ', '')
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', t)
    if not m:
        return None
    hh = int(m.group(1))
    mm = int(m.group(2) or '0')
    ap = m.group(3)
    if ap == 'AM':
        if hh == 12:
            hh = 0
    else:
        if hh != 12:
            hh += 12
    return hh*60 + mm

def closes_after_6pm(hours_list):
    if not isinstance(hours_list, list):
        return False
    for item in hours_list:
        if not (isinstance(item, list) and len(item) >= 2):
            continue
        day, val = item[0], item[1]
        if day not in weekday_set:
            continue
        if not isinstance(val, str):
            continue
        v = val.strip()
        if v.lower() == 'closed':
            continue
        if 'open 24 hours' in v.lower():
            return True
        # handle possible multiple intervals separated by ','
        parts = [p.strip() for p in v.split(',')]
        for p in parts:
            # sometimes format like '9AM–5PM' with en dash
            if '–' in p:
                segs = [s.strip() for s in p.split('–')]
            elif '-' in p:
                segs = [s.strip() for s in p.split('-')]
            else:
                continue
            if len(segs) != 2:
                continue
            end = segs[1]
            end_min = to_minutes(end)
            if end_min is None:
                continue
            if end_min > 18*60:
                return True
    return False

biz_df = biz_df[biz_df['hours_parsed'].apply(closes_after_6pm)].copy()

avg = rev_df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
res = biz_df.merge(avg, on='gmap_id', how='inner')
res = res.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# format hours for display

def fmt_hours(hours_list):
    if not isinstance(hours_list, list):
        return ''
    return '; '.join([f"{d}: {h}" for d,h in hours_list if isinstance(d,str)])

out = []
for _, r in res.iterrows():
    out.append({
        'name': r['name'],
        'operating_hours': fmt_hours(r['hours_parsed']),
        'average_rating': round(float(r['avg_rating']), 3)
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AgtLDDWky7aypsGcmRfUnkJ6': 'file_storage/call_AgtLDDWky7aypsGcmRfUnkJ6.json', 'var_call_6mqurSxk4SZBUqiO93BgW5dj': 'file_storage/call_6mqurSxk4SZBUqiO93BgW5dj.json'}

exec(code, env_args)
