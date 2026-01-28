code = """import json
from collections import defaultdict, OrderedDict
import re

# Load data from previous tool results
# var_call_RSU4k7DwsveGieL7PeDPw9Zd and var_call_5WfuGLBdT3JLiVH2UuJ4VsqY are available

with open(var_call_RSU4k7DwsveGieL7PeDPw9Zd, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_5WfuGLBdT3JLiVH2UuJ4VsqY, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping for level-4 CPC symbols to titleFull
cpc_title = {entry.get('symbol'): entry.get('titleFull') for entry in cpc_defs}

# Helper to extract year from natural language date
year_re = re.compile(r"(19|20)\d{2}")
month_names = {
    'january':1,'jan':1,'february':2,'feb':2,'march':3,'mar':3,'april':4,'apr':4,'may':5,'june':6,'jun':6,
    'july':7,'jul':7,'august':8,'aug':8,'september':9,'sep':9,'october':10,'oct':10,'november':11,'nov':11,'december':12,'dec':12
}


def extract_year(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    m = year_re.search(date_str)
    if m:
        return int(m.group(0))
    return None


def extract_month(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    s = date_str.lower()
    for name, num in month_names.items():
        if name in s:
            return num
    # try numeric month like '2019-09-24' or '09/24/2019'
    m = re.search(r"\b(0?[1-9]|1[0-2])\b", s)
    if m:
        return int(m.group(0))
    return None


# Filter publications: Patents_info already filtered by SQL, but ensure grant_date in H2 2019
h2_pubs = []
for rec in pubs:
    gd = rec.get('grant_date')
    y = extract_year(gd)
    m = extract_month(gd)
    if y == 2019 and m is not None and 7 <= m <= 12:
        h2_pubs.append(rec)

# For each publication, parse cpc field (JSON string) and get codes
# Aggregate counts by level4 group (first 3 chars) and filing year
counts = defaultdict(lambda: defaultdict(int))  # group -> year -> count

for rec in h2_pubs:
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    filing_date = rec.get('filing_date')
    fyear = extract_year(filing_date)
    if fyear is None:
        # skip if no filing year
        continue
    for item in cpc_list:
        code = item.get('code')
        if not code or len(code) < 3:
            continue
        group = code[:3]
        counts[group][fyear] += 1

# For each group, compute EMA across years sorted
alpha = 0.1
results = []
for group, year_counts in counts.items():
    # convert to ordered years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        cnt = year_counts.get(y, 0)
        if ema is None:
            ema = cnt
        else:
            ema = alpha * cnt + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], -x[0]))[0]
    best_ema = ema_by_year[best_year]
    results.append({
        'cpc_group': group,
        'titleFull': cpc_title.get(group),
        'best_year': int(best_year),
        'best_year_ema': float(best_ema)
    })

# Sort results by best_year_ema descending
results_sorted = sorted(results, key=lambda x: x['best_year_ema'], reverse=True)

# Output only required fields: full title, CPC group code, and best year
final_output = [{
    'cpc_group': r['cpc_group'],
    'titleFull': r['titleFull'],
    'best_year': r['best_year']
} for r in results_sorted]

import json as _json
print("__RESULT__:")
print(_json.dumps(final_output))"""

env_args = {'var_call_5WfuGLBdT3JLiVH2UuJ4VsqY': 'file_storage/call_5WfuGLBdT3JLiVH2UuJ4VsqY.json', 'var_call_zsEpQCrJFdP8Bd3zRLCsXZNE': 'file_storage/call_zsEpQCrJFdP8Bd3zRLCsXZNE.json', 'var_call_RSU4k7DwsveGieL7PeDPw9Zd': 'file_storage/call_RSU4k7DwsveGieL7PeDPw9Zd.json'}

exec(code, env_args)
