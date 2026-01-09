code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

pub = load_records(var_call_fPCO64Cy8m5Q3HQGPi4AZNM1)
levels = load_records(var_call_tCd29zo0lwBEAZgLY4BQsYw1)

lvl5 = set(r['symbol'] for r in levels if r.get('symbol') is not None)

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    return int(m.group(1)) if m else None

# Extract level-5 CPC group code as subclass (e.g., H01M) from detailed code (e.g., H01M10/0565)
code_re = re.compile(r'^([A-HY]\d{2}[A-Z])')

def extract_lvl5_from_code(code):
    if not code: return None
    code = code.strip()
    m = code_re.match(code)
    return m.group(1) if m else None

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    seen = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        g = extract_lvl5_from_code(code)
        if g and g in lvl5 and g not in seen:
            seen.add(g)
            rows.append((g, y))

if not rows:
    out = []
else:
    df = pd.DataFrame(rows, columns=['group5','year'])
    counts = df.groupby(['group5','year']).size().reset_index(name='filings')

    alpha = 0.2
    # compute EMA per group across years (fill missing years with 0 within global year range)
    min_year = int(counts['year'].min())
    max_year = int(counts['year'].max())
    all_years = list(range(min_year, max_year+1))

    best = []
    for g, sub in counts.groupby('group5'):
        s = sub.set_index('year')['filings'].reindex(all_years, fill_value=0).sort_index()
        ema = None
        for yr, x in s.items():
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            best.append((g, yr, float(ema)))

    best_df = pd.DataFrame(best, columns=['group5','year','ema'])
    # for each year find max EMA and groups achieving it
    max_by_year = best_df.groupby('year')['ema'].max().reset_index(name='max_ema')
    winners = best_df.merge(max_by_year, on='year')
    winners = winners[winners['ema'] == winners['max_ema']][['group5','year','ema']]

    # for each group, compute its best year (earliest if tie)
    gbest = best_df.sort_values(['group5','ema','year'], ascending=[True, False, True])
    gbest = gbest.groupby('group5').head(1)[['group5','year','ema']].rename(columns={'year':'best_year','ema':'best_ema'})

    # filter: groups that are winners in some year, and whose best year is 2022
    win_groups = set(winners['group5'].unique())
    gbest = gbest[gbest['group5'].isin(win_groups) & (gbest['best_year'] == 2022)]

    out = sorted(gbest['group5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fPCO64Cy8m5Q3HQGPi4AZNM1': 'file_storage/call_fPCO64Cy8m5Q3HQGPi4AZNM1.json', 'var_call_tCd29zo0lwBEAZgLY4BQsYw1': 'file_storage/call_tCd29zo0lwBEAZgLY4BQsYw1.json'}

exec(code, env_args)
