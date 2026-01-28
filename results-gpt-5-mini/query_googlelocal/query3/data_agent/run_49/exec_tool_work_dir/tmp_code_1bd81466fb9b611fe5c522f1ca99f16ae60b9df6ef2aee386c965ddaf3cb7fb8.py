code = """import json
import pandas as pd
import re

# load data from storage-provided file paths
with open(var_call_3lnKVJvdm1DbPWa3S61ySIUT, 'r') as f:
    biz = json.load(f)
with open(var_call_hX3jqNAGPgfeV8NWzJw1qApd, 'r') as f:
    rev = json.load(f)

df_biz = pd.DataFrame(biz)
df_rev = pd.DataFrame(rev)

# normalize ratings
if not df_rev.empty:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
else:
    df_rev['rating'] = pd.Series(dtype=float)

# average rating per business
df_avg = df_rev.groupby('gmap_id', dropna=False)['rating'].mean().reset_index()

# merge
df = df_biz.merge(df_avg, on='gmap_id', how='left')

# helper to parse time like '9:30AM' or '10PM'
time_re = re.compile(r"^(\d{1,2})(?::(\d{2}))?\s*([AP]M)$", re.IGNORECASE)

def parse_time(t):
    if not isinstance(t, str):
        return None
    t = t.strip().upper()
    m = time_re.match(t)
    if not m:
        return None
    hour = int(m.group(1))
    minute = int(m.group(2) or 0)
    ampm = m.group(3).upper()
    if ampm == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return hour * 60 + minute

weekdays = set(['Monday','Tuesday','Wednesday','Thursday','Friday'])

def open_after_6pm(hours_str):
    # hours_str is a string representation of a list like [["Thursday", "9AM–5PM"], ...]
    try:
        sched = json.loads(hours_str)
    except Exception:
        return False
    for entry in sched:
        if not (isinstance(entry, list) and len(entry) >= 2):
            continue
        day = entry[0]
        time_range = entry[1]
        if day not in weekdays:
            continue
        if not isinstance(time_range, str):
            continue
        if time_range.strip().lower() == 'closed':
            continue
        # split on en-dash, em-dash, or hyphen
        parts = re.split(r"\s*[\u2013\u2014-]\s*", time_range)
        if len(parts) < 2:
            continue
        open_t = parts[0]
        close_t = parts[1]
        close_mins = parse_time(close_t)
        if close_mins is None:
            continue
        if close_mins > 18 * 60:
            return True
    return False

# compute flag
if 'hours' not in df.columns:
    df['hours'] = None

df['open_after_6pm_weekday'] = df['hours'].apply(lambda x: open_after_6pm(x) if pd.notna(x) else False)

# filter businesses open after 6pm on at least one weekday and having average rating
df_filtered = df[df['open_after_6pm_weekday'] & df['rating'].notna()].copy()

# sort by avg rating desc
df_filtered['avg_rating'] = df_filtered['rating'].round(2)

df_sorted = df_filtered.sort_values(by=['avg_rating','name'], ascending=[False, True])

top5 = df_sorted.head(5)

result = []
for _, row in top5.iterrows():
    result.append({'name': row.get('name'), 'hours': row.get('hours'), 'average_rating': float(row.get('avg_rating'))})

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_3lnKVJvdm1DbPWa3S61ySIUT': 'file_storage/call_3lnKVJvdm1DbPWa3S61ySIUT.json', 'var_call_hX3jqNAGPgfeV8NWzJw1qApd': 'file_storage/call_hX3jqNAGPgfeV8NWzJw1qApd.json'}

exec(code, env_args)
