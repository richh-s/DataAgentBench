code = """import json, re
from collections import defaultdict

# Load files
with open(var_call_pkjPqSxvvQTVbYqH88xTnOJI, 'r', encoding='utf-8') as f:
    level5_list = json.load(f)
with open(var_call_Qu1OO1VzIP91iYj6XT11aFcf, 'r', encoding='utf-8') as f:
    pub_records = json.load(f)

level5_symbols = set()
for item in level5_list:
    s = item.get('symbol')
    if s:
        level5_symbols.add(s.strip().upper())

counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pub_records:
    cpc_str = rec.get('cpc')
    filing = rec.get('filing_date') or ''
    years = re.findall(r'[0-9]{4}', filing)
    if not years:
        continue
    year = None
    for y in years:
        if y.startswith('19') or y.startswith('20'):
            year = int(y)
            break
    if year is None:
        continue
    all_years.add(year)
    if not cpc_str:
        continue
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        try:
            cpcs = json.loads(cpc_str.replace('\n',''))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            code = None
        if not code or len(code) < 4:
            continue
        grp = code[:4].upper()
        if grp in level5_symbols:
            counts[grp][year] += 1

result = []
if all_years:
    years_sorted = sorted(all_years)
    alpha = 0.2
    for grp, year_counts in counts.items():
        ema = None
        ema_by_year = {}
        for y in years_sorted:
            cnt = year_counts.get(y, 0)
            if ema is None:
                ema = cnt
            else:
                ema = alpha * cnt + (1 - alpha) * ema
            ema_by_year[y] = ema
        # choose latest year in tie by using -year
        best_year = max(ema_by_year.items(), key=lambda x: (x[1], -x[0]))[0]
        if best_year == 2022:
            result.append(grp)
    result = sorted(result)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pkjPqSxvvQTVbYqH88xTnOJI': 'file_storage/call_pkjPqSxvvQTVbYqH88xTnOJI.json', 'var_call_Qu1OO1VzIP91iYj6XT11aFcf': 'file_storage/call_Qu1OO1VzIP91iYj6XT11aFcf.json'}

exec(code, env_args)
