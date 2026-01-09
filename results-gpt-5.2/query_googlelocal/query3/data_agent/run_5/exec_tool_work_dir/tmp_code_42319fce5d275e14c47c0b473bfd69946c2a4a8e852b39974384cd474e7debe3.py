code = """import json, pandas as pd, re

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

biz = load(var_call_HYhdmm0bOV032M3YXFbJXGQQ)
rev = load(var_call_hkZKPPpDlZVnCBSOr5hOItTM)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def parse_time_to_minutes(t):
    t=t.strip()
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', t, re.I)
    if not m:
        return None
    h = int(m.group(1))
    mi = int(m.group(2) or 0)
    ap = m.group(3).upper()
    if h==12:
        h=0
    if ap=='PM':
        h += 12
    return h*60+mi

# hours stored as stringified JSON

def closes_after_6pm(hours_str):
    if hours_str is None:
        return False
    try:
        hrs = json.loads(hours_str)
    except Exception:
        return False
    for day, span in hrs:
        if day not in weekday_set:
            continue
        if not isinstance(span, str):
            continue
        s = span.strip()
        if s.lower().startswith('open 24'):
            return True
        if s.lower()=='closed':
            continue
        # take last closing time after dash/en dash
        parts = re.split(r'\s*[\u2013\-]\s*', s)
        if len(parts) >= 2:
            close = parts[-1]
            cm = parse_time_to_minutes(close)
            if cm is not None and cm > 18*60:
                return True
    return False

dfb['after6_weekday'] = dfb['hours'].apply(closes_after_6pm)
filtered = dfb[dfb['after6_weekday']].copy()

avg = dfr.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
merged = filtered.merge(avg, on='gmap_id', how='inner')
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

out_lines=[]
for i, row in enumerate(merged.itertuples(index=False), start=1):
    out_lines.append(f"{i}. {row.name} | Avg rating: {row.avg_rating:.2f} | Hours: {row.hours}")
answer = "\n".join(out_lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_HYhdmm0bOV032M3YXFbJXGQQ': 'file_storage/call_HYhdmm0bOV032M3YXFbJXGQQ.json', 'var_call_hkZKPPpDlZVnCBSOr5hOItTM': 'file_storage/call_hkZKPPpDlZVnCBSOr5hOItTM.json'}

exec(code, env_args)
