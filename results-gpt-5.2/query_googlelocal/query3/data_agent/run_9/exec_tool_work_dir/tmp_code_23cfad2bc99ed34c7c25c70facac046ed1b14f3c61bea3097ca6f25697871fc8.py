code = """import json
import pandas as pd
import re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_gIlLZqkQshmTOiAACmsKNooX)
rev = load_records(var_call_21RysfFD0FQfgygspQukbzvb)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

def parse_hours(h):
    if h is None:
        return []
    if isinstance(h, list):
        return h
    if isinstance(h, str):
        try:
            return json.loads(h)
        except Exception:
            return []
    return []

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def closes_after_6(timestr):
    if not isinstance(timestr, str):
        return False
    t = timestr.strip()
    if t.lower() == 'closed':
        return False
    if 'Open 24 hours' in t:
        return True
    for p in [x.strip() for x in t.split(',')]:
        if '–' in p:
            start, end = p.split('–', 1)
        elif '-' in p:
            start, end = p.split('-', 1)
        else:
            continue
        start = start.strip()
        end = end.strip()
        if not re.search(r'(AM|PM)', end, flags=re.I):
            m2 = re.search(r'(AM|PM)', start, flags=re.I)
            if m2:
                end = end + m2.group(1)
        end_nospace = end.replace(' ', '')
        tm = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', end_nospace, flags=re.I)
        if not tm:
            continue
        hh = int(tm.group(1))
        mm = int(tm.group(2) or 0)
        ap = tm.group(3).upper()
        if ap == 'PM' and hh != 12:
            hh += 12
        if ap == 'AM' and hh == 12:
            hh = 0
        if hh*60 + mm > 18*60:
            return True
    return False

qual = []
for _, r in biz_df.iterrows():
    hrs = parse_hours(r.get('hours'))
    ok = False
    for entry in hrs:
        if isinstance(entry, list) and len(entry) == 2:
            day = entry[0]
            times = entry[1]
            if day in weekdays and closes_after_6(times):
                ok = True
                break
    if ok:
        qual.append({'gmap_id': r.get('gmap_id'), 'name': r.get('name'), 'hours': hrs})

qual_df = pd.DataFrame(qual).dropna(subset=['gmap_id'])
avg = rev_df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
merged = qual_df.merge(avg, on='gmap_id', how='inner')
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

def fmt_hours(hrs):
    out = []
    for entry in hrs:
        if isinstance(entry, list) and len(entry) == 2:
            out.append(str(entry[0]) + ': ' + str(entry[1]))
    return '; '.join(out)

lines = []
for idx, row in enumerate(merged.to_dict(orient='records'), start=1):
    line = str(idx) + '. ' + str(row.get('name')) + ' | Avg rating: ' + ('{:.2f}'.format(row.get('avg_rating'))) + ' | Hours: ' + fmt_hours(row.get('hours'))
    lines.append(line)

answer = "\n".join(lines) if lines else "No qualifying businesses found."
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_gIlLZqkQshmTOiAACmsKNooX': 'file_storage/call_gIlLZqkQshmTOiAACmsKNooX.json', 'var_call_21RysfFD0FQfgygspQukbzvb': 'file_storage/call_21RysfFD0FQfgygspQukbzvb.json'}

exec(code, env_args)
