code = """import json, re

pubs = json.load(open(var_call_1pUVsZq3mM75oW2rDXMZAczd,'r',encoding='utf-8'))
cpc_defs = json.load(open(var_call_0wDZJdeB5HNhIhfOGv0mW2RL,'r',encoding='utf-8'))

# Build symbol->titleFull map
title_map = {entry.get('symbol'): entry.get('titleFull') for entry in cpc_defs}

# month mapping
months = {
    'january':1,'jan':1,'february':2,'feb':2,'march':3,'mar':3,'april':4,'apr':4,
    'may':5,'june':6,'jun':6,'july':7,'jul':7,'august':8,'aug':8,'september':9,'sep':9,'sept':9,
    'october':10,'oct':10,'november':11,'nov':11,'december':12,'dec':12
}

alpha = 0.1

# Helper to extract year and month from natural-language date

def extract_year_month(date_str):
    if not date_str or '2019' not in date_str:
        return None, None
    s = date_str.lower()
    # find year
    yrs = re.findall(r"(19\d{2}|20\d{2})", date_str)
    year = int(yrs[-1]) if yrs else None
    # find month
    month = None
    for k,v in months.items():
        if k in s:
            month = v
            break
    return year, month

# Helper to detect Germany in Patents_info

def is_germany(pat_info):
    if not pat_info:
        return False
    s = pat_info
    # look for patterns like ' from DE', ' in DE', 'DE-' or ' DE,' or ' country code DE'
    if re.search(r'\bDE\b', s) or 'DE-' in s or ' from DE' in s or ' in DE' in s or 'country code DE' in s:
        return True
    return False

# Process publications: filter grant_date in H2 2019 and Germany
filtered = []
for rec in pubs:
    gd = rec.get('grant_date','')
    year, month = extract_year_month(gd)
    if year != 2019 or not month:
        continue
    if month < 7 or month > 12:
        continue
    if not is_germany(rec.get('Patents_info','')):
        continue
    filtered.append(rec)

# Aggregate counts by CPC group (level 4 -> first 3 chars) and filing year
counts = {}  # group -> {year: count}
for rec in filtered:
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpc_list = json.loads(cpc_field.replace("\n", "\\n"))
        except Exception:
            continue
    # filing year
    fd = rec.get('filing_date','')
    yrs = re.findall(r"(19\d{2}|20\d{2})", fd)
    if not yrs:
        continue
    filing_year = int(yrs[-1])
    for item in cpc_list:
        code = item.get('code') if isinstance(item, dict) else None
        if not code or len(code) < 3:
            continue
        group = code[:3]
        if not re.match(r'^[A-Z]\d{2}$', group):
            m = re.match(r'^([A-Z]\d{2})', code)
            if m:
                group = m.group(1)
            else:
                continue
        counts.setdefault(group, {})
        counts[group][filing_year] = counts[group].get(filing_year, 0) + 1

# For each group compute EMA across sorted years and find best year
results = []
for group, year_counts in counts.items():
    years_sorted = sorted(year_counts.keys())
    if not years_sorted:
        continue
    ema = None
    ema_by_year = {}
    for y in years_sorted:
        x = year_counts.get(y, 0)
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], -kv[0]))[0]
    max_ema = ema_by_year[best_year]
    results.append({
        'cpc_group_code': group,
        'titleFull': title_map.get(group),
        'best_year': best_year,
        'max_ema': round(max_ema, 4)
    })

# Sort results by max_ema descending
results_sorted = sorted(results, key=lambda x: x['max_ema'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_0wDZJdeB5HNhIhfOGv0mW2RL': 'file_storage/call_0wDZJdeB5HNhIhfOGv0mW2RL.json', 'var_call_V5af0m1qlI9kRcESlDZbtJdL': 'file_storage/call_V5af0m1qlI9kRcESlDZbtJdL.json', 'var_call_1pUVsZq3mM75oW2rDXMZAczd': 'file_storage/call_1pUVsZq3mM75oW2rDXMZAczd.json', 'var_call_J0g7Ap53kaVU0sAqFxGUrIJG': {'num_pubs': 4833, 'num_cpc_defs': 137}}

exec(code, env_args)
