code = """import json, pandas as pd, re

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

# Parse hours which are stored as a JSON string of list pairs

def parse_hours(h):
    if h is None:
        return []
    if isinstance(h, list):
        return h
    if isinstance(h, str):
        s = h.strip()
        try:
            return json.loads(s)
        except Exception:
            return []
    return []

weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

# Determine if open after 6PM on at least one weekday

def closes_after_6(timestr):
    if not isinstance(timestr, str):
        return False
    t = timestr.strip()
    if t.lower() == 'closed':
        return False
    if 'Open 24 hours' in t:
        return True
    # can have multiple intervals like '9AM–12PM, 1–6PM'
    parts = [p.strip() for p in t.split(',')]
    for p in parts:
        # find end time after dash/en-dash
        if '–' in p:
            end = p.split('–',1)[1].strip()
        elif '-' in p:
            end = p.split('-',1)[1].strip()
        else:
            continue
        # normalize end time with am/pm if missing
        # if end has no AM/PM, assume same meridiem as start if present
        m = re.search(r'(AM|PM)', end, flags=re.I)
        if not m:
            m2 = re.search(r'(AM|PM)', p.split('–',1)[0] if '–' in p else p.split('-',1)[0], flags=re.I)
            if m2:
                end = end + m2.group(1)
        # parse
        end = end.replace(' ', '')
        tm = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', end, flags=re.I)
        if not tm:
            continue
        hh = int(tm.group(1))
        mm = int(tm.group(2) or 0)
        ap = tm.group(3).upper()
        if ap == 'PM' and hh != 12:
            hh += 12
        if ap == 'AM' and hh == 12:
            hh = 0
        minutes = hh*60 + mm
        if minutes > 18*60:  # strictly after 6:00 PM
            return True
    return False

qual_rows = []
for _, r in biz_df.iterrows():
    hrs = parse_hours(r.get('hours'))
    ok = False
    for entry in hrs:
        if not (isinstance(entry, list) and len(entry)==2):
            continue
        day, times = entry[0], entry[1]
        if day in weekdays and closes_after_6(times):
            ok = True
            break
    if ok:
        qual_rows.append({'gmap_id': r.get('gmap_id'), 'name': r.get('name'), 'hours': hrs})

qual_df = pd.DataFrame(qual_rows).dropna(subset=['gmap_id'])

avg = rev_df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
merged = qual_df.merge(avg, on='gmap_id', how='inner')
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# format operating hours nicely

def fmt_hours(hrs):
    out=[]
    for entry in hrs:
        if isinstance(entry, list) and len(entry)==2:
            out.append(f"{entry[0]}: {entry[1]}")
    return '; '.join(out)

result_lines=[]
for i, row in enumerate(merged.to_dict(orient='records'), start=1):
    result_lines.append(f"{i}. {row['name']} | Avg rating: {row['avg_rating']:.2f} | Hours: {fmt_hours(row['hours'])}")

answer='\n'.join(result_lines) if result_lines else 'No qualifying businesses found.'
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_gIlLZqkQshmTOiAACmsKNooX': 'file_storage/call_gIlLZqkQshmTOiAACmsKNooX.json', 'var_call_21RysfFD0FQfgygspQukbzvb': 'file_storage/call_21RysfFD0FQfgygspQukbzvb.json'}

exec(code, env_args)
