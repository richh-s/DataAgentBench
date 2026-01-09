code = """import json, pandas as pd, re

biz_src = var_call_vp3LdraNMWJtxtOWh93JMQk0
rev_src = var_call_pvSScyNQDNuoN7VGbrho6Wu2

def load_records(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

biz = pd.DataFrame(load_records(biz_src))
rev = pd.DataFrame(load_records(rev_src))

# parse hours field stored as string representation of list

def parse_hours(val):
    if val is None:
        return None
    if isinstance(val, (list, dict)):
        return val
    s = str(val)
    if s in ('None', 'null', 'NULL', ''):
        return None
    try:
        return json.loads(s)
    except Exception:
        return None

biz['hours_parsed'] = biz['hours'].apply(parse_hours)

weekdays = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

# time parsing for close time

def parse_time_to_minutes(t):
    t = t.strip()
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', t, re.I)
    if not m:
        return None
    h = int(m.group(1))
    mi = int(m.group(2) or 0)
    ap = m.group(3).upper()
    if ap == 'AM':
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    return h*60 + mi


def close_after_6pm(hours_list):
    if not hours_list:
        return False
    for day, hrs in hours_list:
        if day not in weekdays:
            continue
        if hrs is None:
            continue
        hs = str(hrs)
        if 'Open 24 hours' in hs:
            return True
        if 'Closed' in hs:
            continue
        # may contain multiple ranges separated by comma
        parts = [p.strip() for p in hs.split(',')]
        for part in parts:
            if '–' in part:
                start,end = [x.strip() for x in part.split('–',1)]
            elif '-' in part:
                start,end = [x.strip() for x in part.split('-',1)]
            else:
                continue
            end_min = parse_time_to_minutes(end)
            if end_min is None:
                continue
            if end_min > 18*60:
                return True
    return False

biz_f = biz[biz['hours_parsed'].apply(close_after_6pm)].copy()

# compute avg rating
rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')
avg = rev.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

merged = biz_f.merge(avg, on='gmap_id', how='inner')
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# format hours for output

def format_hours(hours_list):
    if not hours_list:
        return None
    return '; '.join([f"{d}: {h}" for d,h in hours_list])

out = []
for _,r in merged.iterrows():
    out.append({
        'name': r['name'],
        'operating_hours': format_hours(r['hours_parsed']),
        'average_rating': round(float(r['avg_rating']), 3)
    })

result = json.dumps(out, ensure_ascii=False)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_vp3LdraNMWJtxtOWh93JMQk0': 'file_storage/call_vp3LdraNMWJtxtOWh93JMQk0.json', 'var_call_pvSScyNQDNuoN7VGbrho6Wu2': 'file_storage/call_pvSScyNQDNuoN7VGbrho6Wu2.json'}

exec(code, env_args)
