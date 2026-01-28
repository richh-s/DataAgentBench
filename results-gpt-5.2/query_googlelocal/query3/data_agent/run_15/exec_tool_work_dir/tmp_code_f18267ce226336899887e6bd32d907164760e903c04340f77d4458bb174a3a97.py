code = """import json, ast, re
import pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        # assume it's a file path to json
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

biz = load_records(var_call_hmzumWjinL96gYjXgWOziMEW)
rev = load_records(var_call_XNXrGfXuHvWbHvKavbLLNyqu)

df_b = pd.DataFrame(biz)
df_r = pd.DataFrame(rev)
if df_r.empty:
    out = []
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

def parse_hours_cell(cell):
    if cell is None:
        return None
    if isinstance(cell, float) and pd.isna(cell):
        return None
    if isinstance(cell, (list, dict)):
        return cell
    s = str(cell)
    if s.strip().lower() in {'none','nan','null',''}:
        return None
    # try json then python literal
    try:
        return json.loads(s)
    except Exception:
        pass
    try:
        return ast.literal_eval(s)
    except Exception:
        return None


def time_to_minutes(t):
    t = t.strip()
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$', t, re.I)
    if not m:
        return None
    hh = int(m.group(1))
    mm = int(m.group(2) or '0')
    ampm = m.group(3).upper()
    if hh == 12:
        hh = 0
    if ampm == 'PM':
        hh += 12
    return hh*60 + mm


def closes_after_6pm_on_weekday(hours_obj):
    if not isinstance(hours_obj, list):
        return False
    for entry in hours_obj:
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            continue
        day = str(entry[0])
        if day not in weekday_set:
            continue
        hours_str = str(entry[1])
        hs = hours_str.strip()
        if hs.lower() == 'closed':
            continue
        if 'Open 24 hours' in hs:
            return True
        # handle multiple intervals separated by ','
        parts = [p.strip() for p in hs.split(',') if p.strip()]
        for part in parts:
            # normalize dash types
            part_norm = part.replace('–','-').replace('—','-')
            if '-' not in part_norm:
                continue
            start, end = [x.strip() for x in part_norm.split('-', 1)]
            end_min = time_to_minutes(end)
            if end_min is None:
                continue
            if end_min > 18*60:
                return True
    return False


df_b['hours_obj'] = df_b['hours'].apply(parse_hours_cell)
df_b['open_after_6_weekday'] = df_b['hours_obj'].apply(closes_after_6pm_on_weekday)

# average rating per gmap_id
avg = df_r.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

merged = df_b.merge(avg, on='gmap_id', how='inner')
filtered = merged[merged['open_after_6_weekday']].copy()
filtered = filtered.dropna(subset=['avg_rating'])
filtered = filtered.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# operating hours as readable string

def hours_to_string(hours_obj):
    if hours_obj is None:
        return None
    if isinstance(hours_obj, list):
        return '; '.join([f"{d}: {h}" for d,h in hours_obj if isinstance(d,str)])
    return str(hours_obj)

filtered['operating_hours'] = filtered['hours_obj'].apply(hours_to_string)
filtered['avg_rating'] = filtered['avg_rating'].round(3)

out = filtered[['name','operating_hours','avg_rating']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hmzumWjinL96gYjXgWOziMEW': 'file_storage/call_hmzumWjinL96gYjXgWOziMEW.json', 'var_call_XNXrGfXuHvWbHvKavbLLNyqu': 'file_storage/call_XNXrGfXuHvWbHvKavbLLNyqu.json'}

exec(code, env_args)
