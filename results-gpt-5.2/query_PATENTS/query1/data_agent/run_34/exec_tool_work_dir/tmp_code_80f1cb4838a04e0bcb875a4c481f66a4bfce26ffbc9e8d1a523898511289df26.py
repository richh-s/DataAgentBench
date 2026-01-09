code = """import json, re
import pandas as pd

# Load publication rows
pub_src = var_call_HjftnbeyopHmA1raH1t4CwGk
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

# Load CPC level-5 symbols list
lvl5_src = var_call_lIBKpcxhT0OCMsAyFj0i1epF
if isinstance(lvl5_src, str):
    with open(lvl5_src, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl5_src

lvl5_set = set(r['symbol'] for r in lvl5 if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate([
    'January','February','March','April','May','June','July','August','September','October','November','December'
], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def extract_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for it in arr if isinstance(arr, list) else []:
            code = it.get('code') if isinstance(it, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z][0-9A-Z]{2,4}[^\"]*)"', cpc_str)

def to_lvl5_group(code):
    # level-5 group codes in this dataset correspond to CPC class/subclass/main group like H01M, G06F, etc.
    # Map full symbol to its leading part (letters+2 digits+optional letter) before any group slash.
    if not code:
        return None
    m = re.match(r'^([A-Z][0-9]{2}[A-Z]?)', code)
    return m.group(1) if m else None

rows = []
for r in pubs:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    groups = set()
    for c in codes:
        g = to_lvl5_group(c)
        if g and g in lvl5_set:
            groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['symbol','year']).size().reset_index(name='filings')
    years = sorted(counts['year'].unique())
    alpha = 0.2

    # Compute EMA per symbol across full year range (fill missing with 0)
    res = []
    for sym, g in counts.groupby('symbol'):
        series = g.set_index('year')['filings']
        ema = None
        for yr in years:
            x = float(series.get(yr, 0.0))
            if ema is None:
                ema = x  # initialize with first year value
            else:
                ema = alpha * x + (1-alpha) * ema
            res.append((sym, yr, x, ema))

    ema_df = pd.DataFrame(res, columns=['symbol','year','filings','ema'])

    # Find max EMA per year across symbols; then select those whose best year (argmax over years) is 2022
    idx = ema_df.groupby('year')['ema'].idxmax()
    top_per_year = ema_df.loc[idx, ['year','symbol','ema']].sort_values('year')

    # Determine each symbol's best year based on EMA
    best_idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[best_idx, ['symbol','year','ema']]
    syms_best_2022 = set(best.loc[best['year']==2022, 'symbol'])

    final = top_per_year[top_per_year['symbol'].isin(syms_best_2022)].copy()
    out = sorted(final['symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_HjftnbeyopHmA1raH1t4CwGk': 'file_storage/call_HjftnbeyopHmA1raH1t4CwGk.json', 'var_call_lIBKpcxhT0OCMsAyFj0i1epF': 'file_storage/call_lIBKpcxhT0OCMsAyFj0i1epF.json'}

exec(code, env_args)
