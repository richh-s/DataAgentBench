code = """import json, re

pubs = json.load(open(var_call_rwPqIipt5dPkyMdOjurEqPw6, 'r', encoding='utf-8'))
cpc_defs = json.load(open(var_call_0wDZJdeB5HNhIhfOGv0mW2RL, 'r', encoding='utf-8'))

# map CPC group title
title_map = {e.get('symbol'): e.get('titleFull') for e in cpc_defs}

months = ['january','february','march','april','may','june','july','august','september','october','november','december']
month_nums = {m: i+1 for i,m in enumerate(months)}
alpha = 0.1

def extract_year_month(date_str):
    if not date_str:
        return None, None
    s = date_str.lower()
    # year
    m = re.search('(19[0-9]{2}|20[0-9]{2})', date_str)
    year = int(m.group(0)) if m else None
    month = None
    for name, num in month_nums.items():
        if name in s:
            month = num
            break
    return year, month

def is_germany(pat_info):
    if not pat_info:
        return False
    s = pat_info
    sl = s.lower()
    if ' de ' in sl or ' from de' in sl or ' in de' in sl or 'country code de' in sl:
        return True
    if 'de-' in s or 'DE-' in s:
        return True
    if re.search('\bDE\b', s):
        return True
    return False

# filter pubs: grant in H2 2019 and germany
filtered = []
for rec in pubs:
    gd = rec.get('grant_date', '')
    y,m = extract_year_month(gd)
    if y != 2019 or not m or m < 7 or m > 12:
        continue
    if not is_germany(rec.get('Patents_info','')):
        continue
    filtered.append(rec)

# aggregate counts by level-4 group (letter + two digits) and filing year
counts = {}
for rec in filtered:
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace('\n','\\n'))
        except Exception:
            continue
    fd = rec.get('filing_date','')
    m = re.search('(19[0-9]{2}|20[0-9]{2})', fd)
    if not m:
        continue
    filing_year = int(m.group(0))
    for item in cpcs:
        code = item.get('code') if isinstance(item, dict) else None
        if not code:
            continue
        mm = re.match('([A-Z][0-9]{2})', code)
        if not mm:
            continue
        group = mm.group(1)
        counts.setdefault(group, {})
        counts[group][filing_year] = counts[group].get(filing_year, 0) + 1

results = []
for group, yc in counts.items():
    years_sorted = sorted(yc.keys())
    if not years_sorted:
        continue
    ema = None
    ema_by_year = {}
    for yr in years_sorted:
        x = yc.get(yr, 0)
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1 - alpha) * ema
        ema_by_year[yr] = ema
    # best year: highest EMA, tiebreaker latest year
    best_year = max(ema_by_year.items(), key=lambda kv: (kv[1], kv[0]))[0]
    results.append({
        'cpc_group_code': group,
        'titleFull': title_map.get(group),
        'best_year': best_year,
        'max_ema': round(ema_by_year[best_year], 4)
    })

results_sorted = sorted(results, key=lambda x: x['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_0wDZJdeB5HNhIhfOGv0mW2RL': 'file_storage/call_0wDZJdeB5HNhIhfOGv0mW2RL.json', 'var_call_V5af0m1qlI9kRcESlDZbtJdL': 'file_storage/call_V5af0m1qlI9kRcESlDZbtJdL.json', 'var_call_1pUVsZq3mM75oW2rDXMZAczd': 'file_storage/call_1pUVsZq3mM75oW2rDXMZAczd.json', 'var_call_J0g7Ap53kaVU0sAqFxGUrIJG': {'num_pubs': 4833, 'num_cpc_defs': 137}, 'var_call_rwPqIipt5dPkyMdOjurEqPw6': 'file_storage/call_rwPqIipt5dPkyMdOjurEqPw6.json'}

exec(code, env_args)
