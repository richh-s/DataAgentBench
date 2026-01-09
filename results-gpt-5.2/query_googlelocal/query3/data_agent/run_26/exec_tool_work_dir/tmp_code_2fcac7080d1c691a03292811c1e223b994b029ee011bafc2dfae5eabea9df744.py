code = """import json, pandas as pd, re

# Load business records
biz_path = var_call_xpNxU9htIvsNNWLdPISIz6yP
with open(biz_path, 'r', encoding='utf-8') as f:
    biz = json.load(f)

# Load reviews
rev_path = var_call_dHvsOEpk3uGSh0xdKW0QoBPr
with open(rev_path, 'r', encoding='utf-8') as f:
    rev = json.load(f)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# parse hours JSON string to list of [day, hours]
def parse_hours(h):
    if h is None:
        return None
    if isinstance(h, list):
        return h
    if isinstance(h, str):
        try:
            return json.loads(h)
        except Exception:
            return None
    return None

biz_df['hours_parsed'] = biz_df['hours'].apply(parse_hours)

weekday_set = {'Monday','Tuesday','Wednesday','Thursday','Friday'}

# parse a closing time; return True if any weekday closes after 6pm or is open 24 hours

def to_minutes(t):
    t = t.strip()
    m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', t, re.I)
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
    return hh*60+mm


def closes_after_6pm(hours_list):
    if not isinstance(hours_list, list):
        return False
    for entry in hours_list:
        if not (isinstance(entry, list) and len(entry) >= 2):
            continue
        day, spec = entry[0], entry[1]
        if day not in weekday_set or spec is None:
            continue
        s = str(spec)
        if 'Open 24 hours' in s:
            return True
        if 'Closed' in s:
            continue
        # take last closing time after an en dash or hyphen
        parts = re.split(r'[–-]', s)
        if len(parts) < 2:
            continue
        close_part = parts[-1].strip()
        # sometimes close_part like '9PM' or '9:30PM'
        cm = to_minutes(close_part)
        if cm is None:
            continue
        if cm > 18*60:
            return True
    return False

biz_df = biz_df[biz_df['hours_parsed'].apply(closes_after_6pm)].copy()

# average rating per gmap_id
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
avg = rev_df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

merged = biz_df.merge(avg, on='gmap_id', how='inner')
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

# format operating hours into readable string

def format_hours(hours_list):
    if not isinstance(hours_list, list):
        return None
    return '; '.join([f"{d}: {h}" for d,h in hours_list if isinstance(d,str)])

out = []
for _, r in merged.iterrows():
    out.append({
        'name': r['name'],
        'operating_hours': format_hours(r['hours_parsed']),
        'average_rating': round(float(r['avg_rating']), 3)
    })

result = json.dumps(out, ensure_ascii=False)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_ziRNWuqiCpF3zCmLngppVlS3': [], 'var_call_dHvsOEpk3uGSh0xdKW0QoBPr': 'file_storage/call_dHvsOEpk3uGSh0xdKW0QoBPr.json', 'var_call_QujPM4IzJqcUl9nlhvvMW6tW': ['business_description'], 'var_call_wCWBfpWKQIqigJQlsgY2EQ8V': [{'n': '79', 'open_n': '0', 'hours_n': '66'}], 'var_call_Sz9kVoOTfvMCo0tz63j4mlZ8': [{'state': 'Open ⋅ Closes 5PM', 'n': '18'}, {'state': 'None', 'n': '9'}, {'state': 'Closed ⋅ Opens 10AM', 'n': '5'}, {'state': 'Open ⋅ Closes 9:30PM', 'n': '4'}, {'state': 'Open now', 'n': '4'}, {'state': 'Open ⋅ Closes 8PM', 'n': '3'}, {'state': 'Permanently closed', 'n': '3'}, {'state': 'Open ⋅ Closes 7PM', 'n': '3'}, {'state': 'Open ⋅ Closes 4PM', 'n': '3'}, {'state': 'Open ⋅ Closes 10PM', 'n': '3'}, {'state': 'Open ⋅ Closes 6PM', 'n': '3'}, {'state': 'Closed ⋅ Opens 9AM', 'n': '3'}, {'state': 'Open 24 hours', 'n': '2'}, {'state': 'Open ⋅ Closes 5:30PM', 'n': '2'}, {'state': 'Open ⋅ Closes 11AM ⋅ Reopens 4PM', 'n': '1'}, {'state': 'Open ⋅ Closes 3:30PM', 'n': '1'}, {'state': 'Open ⋅ Closes 9PM', 'n': '1'}, {'state': 'Closed ⋅ Opens 5PM Fri', 'n': '1'}, {'state': 'Open ⋅ Closes 11:30AM ⋅ Reopens 1PM', 'n': '1'}, {'state': 'Open ⋅ Closes 12PM ⋅ Reopens 1PM', 'n': '1'}, {'state': 'Opens soon ⋅ 10AM', 'n': '1'}, {'state': 'Open ⋅ Closes 4:30PM', 'n': '1'}, {'state': 'Closed ⋅ Opens 11AM', 'n': '1'}, {'state': 'Open ⋅ Closes 12PM ⋅ Reopens 12:30PM', 'n': '1'}, {'state': 'Closed ⋅ Opens 3PM', 'n': '1'}, {'state': 'Temporarily closed', 'n': '1'}, {'state': 'Closed ⋅ Opens 12PM', 'n': '1'}, {'state': 'Open ⋅ Closes 12AM', 'n': '1'}], 'var_call_xpNxU9htIvsNNWLdPISIz6yP': 'file_storage/call_xpNxU9htIvsNNWLdPISIz6yP.json'}

exec(code, env_args)
