code = """import json, ast, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_JiovvVbgEuncGDCebkVsq7bS)
rev = load_records(var_call_tpDEeRdKDEtoGN5ye877eAfZ)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)
if rev_df.empty:
    out = []
else:
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def parse_hours(hours_val):
    if hours_val is None:
        return []
    if isinstance(hours_val, str):
        s = hours_val.strip()
        if s in ('None','', 'null', 'NULL'):
            return []
        try:
            return ast.literal_eval(s)
        except Exception:
            return []
    if isinstance(hours_val, list):
        return hours_val
    return []

def close_time_minutes(spec):
    if not isinstance(spec, str):
        return None
    spec = spec.strip()
    if spec.lower() in ('closed',):
        return None
    if 'Open 24 hours' in spec:
        return 24*60
    # handle cases like '8:30AM–5:30PM' or '8:30AM-5:30PM'
    parts = re.split(r'[–-]', spec)
    if len(parts) < 2:
        return None
    end = parts[-1].strip()
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', end, re.IGNORECASE)
    if not m:
        return None
    hh = int(m.group(1))
    mm = int(m.group(2) or 0)
    ap = m.group(3).upper()
    if ap == 'AM':
        if hh == 12:
            hh = 0
    else:
        if hh != 12:
            hh += 12
    return hh*60 + mm

def open_after_6_on_weekday(hours_val):
    hrs = parse_hours(hours_val)
    for item in hrs:
        if not (isinstance(item, (list, tuple)) and len(item) >= 2):
            continue
        day, spec = item[0], item[1]
        if day in weekday_set:
            ct = close_time_minutes(spec)
            if ct is not None and ct > 18*60:
                return True
    return False

biz_df = biz_df[biz_df['hours'].apply(open_after_6_on_weekday)].copy()

# average rating per gmap_id
avg_df = rev_df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
merged = biz_df.merge(avg_df, on='gmap_id', how='inner')
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# format operating hours as readable string

def hours_to_str(hours_val):
    hrs = parse_hours(hours_val)
    if not hrs:
        return None
    parts = []
    for day, spec in hrs:
        parts.append(f"{day}: {spec}")
    return "; ".join(parts)

merged['operating_hours'] = merged['hours'].apply(hours_to_str)
merged['avg_rating'] = merged['avg_rating'].round(3)

out = merged[['name','operating_hours','avg_rating']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_JiovvVbgEuncGDCebkVsq7bS': 'file_storage/call_JiovvVbgEuncGDCebkVsq7bS.json', 'var_call_tpDEeRdKDEtoGN5ye877eAfZ': 'file_storage/call_tpDEeRdKDEtoGN5ye877eAfZ.json'}

exec(code, env_args)
