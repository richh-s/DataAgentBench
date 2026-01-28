code = """import json
import pandas as pd
import ast
import re

# Load stored results
try:
    if isinstance(var_call_ENvHJNqhqjsCK9RfUlp1j2Iu, str):
        with open(var_call_ENvHJNqhqjsCK9RfUlp1j2Iu, 'r', encoding='utf-8') as f:
            business_data = json.load(f)
    else:
        business_data = var_call_ENvHJNqhqjsCK9RfUlp1j2Iu
except Exception:
    business_data = []

try:
    if isinstance(var_call_339SjRX2zZOOYj64qMKxLcX1, str):
        with open(var_call_339SjRX2zZOOYj64qMKxLcX1, 'r', encoding='utf-8') as f:
            reviews_data = json.load(f)
    else:
        reviews_data = var_call_339SjRX2zZOOYj64qMKxLcX1
except Exception:
    reviews_data = []

bd = pd.DataFrame(business_data)
rv = pd.DataFrame(reviews_data)

if not rv.empty:
    rv['rating'] = pd.to_numeric(rv['rating'], errors='coerce')

# helpers
WEEKDAYS = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def try_load_hours(val):
    if val is None:
        return None
    if isinstance(val, list):
        return val
    s = str(val).strip()
    if s.lower() in ('none','null',''):
        return None
    try:
        return json.loads(s)
    except Exception:
        pass
    try:
        return ast.literal_eval(s)
    except Exception:
        pass
    # regex fallback
    pairs = re.findall(r"\[\s*\'?(\w+)\'?\s*,\s*\'([^\']+)\'\s*\]", s)
    if pairs:
        return [[p[0], p[1]] for p in pairs]
    return None

def parse_time_token(tok):
    tok = tok.strip().upper()
    tok = tok.replace(' ', '')
    # standardize dash chars
    tok = tok.replace('\u2013','-').replace('\u2014','-')
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?(AM|PM)$', tok)
    if not m:
        return None
    h = int(m.group(1)); mnt = int(m.group(2)) if m.group(2) else 0; ampm = m.group(3)
    if ampm=='AM':
        if h==12: h=0
    else:
        if h!=12: h+=12
    return h*60+mnt

def closing_time_minutes(range_str):
    if not isinstance(range_str, str):
        return None
    s = range_str.replace('\u2013','-').replace('\u2014','-')
    s = s.strip()
    if s.lower()=='closed':
        return None
    parts = re.split(r'[-–—]|to', s)
    if len(parts)<2:
        return None
    close_part = parts[-1]
    m = re.search(r'(\d{1,2}(?::\d{2})?(?:AM|PM))', close_part, re.IGNORECASE)
    if not m:
        return None
    return parse_time_token(m.group(1))

def open_after_6pm(hours_field):
    parsed = try_load_hours(hours_field)
    if not parsed:
        return False
    for entry in parsed:
        if not isinstance(entry, (list,tuple)) or len(entry)<2:
            continue
        day = str(entry[0]).strip()
        if day not in WEEKDAYS:
            continue
        times = entry[1]
        if not isinstance(times, str):
            continue
        close_min = closing_time_minutes(times)
        if close_min and close_min>18*60:
            return True
    return False

# Apply
bd['open_after_6pm_weekday'] = bd['hours'].apply(lambda x: open_after_6pm(x) if pd.notna(x) else False)

if not rv.empty:
    avg = rv.groupby('gmap_id', as_index=False)['rating'].mean()
    avg.rename(columns={'rating':'avg_rating'}, inplace=True)
else:
    avg = pd.DataFrame(columns=['gmap_id','avg_rating'])

merged = bd.merge(avg, on='gmap_id', how='left')
filtered = merged[(merged['open_after_6pm_weekday']==True) & (~merged['avg_rating'].isna())]
res = filtered.sort_values(by=['avg_rating','name'], ascending=[False, True]).head(5)

out = []
for _,r in res.iterrows():
    out.append({'name': r.get('name'), 'hours': r.get('hours'), 'average_rating': round(float(r.get('avg_rating')),2)})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ENvHJNqhqjsCK9RfUlp1j2Iu': 'file_storage/call_ENvHJNqhqjsCK9RfUlp1j2Iu.json', 'var_call_339SjRX2zZOOYj64qMKxLcX1': 'file_storage/call_339SjRX2zZOOYj64qMKxLcX1.json'}

exec(code, env_args)
