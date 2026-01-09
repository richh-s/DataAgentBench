code = """import json, re, pandas as pd

# Load big query results from JSON files if needed

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pubrecs = load_records(var_call_1nlJr1EkZjKrr8zvgTlgDy1W)
level5_syms = load_records(var_call_eIyMDTpRnMPcMfv9LVGJHThX)
level5_set = set(r['symbol'] for r in level5_syms if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    if not m:
        return None
    return int(m.group(0))

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for it in data:
            c = it.get('code') if isinstance(it, dict) else None
            if c:
                c = c.strip()
                codes.append(c)
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d[^\"]*)"', cpc_str)

rows = []
for r in pubrecs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count each CPC code once per publication record
    for c in set(codes):
        # keep only level-5 group codes (appear in level5_set)
        # normalize: remove spaces
        c2 = c.replace(' ', '')
        if c2 in level5_set:
            rows.append((c2, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().reset_index(name='filings')
    years_sorted = sorted(counts['year'].unique())

    alpha = 0.2
    # compute EMA per symbol over full year range, filling missing with 0
    result_rows = []
    for sym, g in counts.groupby('symbol'):
        s = g.set_index('year')['filings']
        ema = None
        for y in years_sorted:
            v = float(s.get(y, 0))
            ema = v if ema is None else (alpha * v + (1-alpha) * ema)
            result_rows.append((y, sym, ema))

    emadf = pd.DataFrame(result_rows, columns=['year','symbol','ema'])
    # find highest EMA symbol(s) per year
    max_by_year = emadf.groupby('year')['ema'].transform('max')
    top = emadf[emadf['ema'] == max_by_year].copy()
    # for each symbol, determine best year (year where ema max; tie -> latest year)
    best = (emadf.sort_values(['symbol','ema','year'])
                 .groupby('symbol')
                 .tail(1)[['symbol','year','ema']]
                 .rename(columns={'year':'best_year','ema':'best_ema'}))
    # filter symbols whose best year is 2022 and that are top in their best year
    top_2022_syms = set(top.loc[top['year']==2022,'symbol'])
    final_syms = sorted(best.loc[(best['best_year']==2022) & (best['symbol'].isin(top_2022_syms)),'symbol'].unique())
    out = final_syms

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1nlJr1EkZjKrr8zvgTlgDy1W': 'file_storage/call_1nlJr1EkZjKrr8zvgTlgDy1W.json', 'var_call_eIyMDTpRnMPcMfv9LVGJHThX': 'file_storage/call_eIyMDTpRnMPcMfv9LVGJHThX.json'}

exec(code, env_args)
