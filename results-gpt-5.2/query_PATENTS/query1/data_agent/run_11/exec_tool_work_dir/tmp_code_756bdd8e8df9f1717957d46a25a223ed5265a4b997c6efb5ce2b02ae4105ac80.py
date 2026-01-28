code = """import json, re
import pandas as pd

# Load publication rows
path_pub = var_call_REpIUU5Q9ZjXVG7PraCmHz6q
with open(path_pub, 'r', encoding='utf-8') as f:
    pub_rows = json.load(f)

# Load level-5 CPC symbols (as provided; many are 4-char subclass symbols in this dataset)
path_lvl5 = var_call_ZBVZBFbjXz4WyZTQo7zUIwBP
with open(path_lvl5, 'r', encoding='utf-8') as f:
    lvl5_rows = json.load(f)

lvl5_set = set(r['symbol'] for r in lvl5_rows if r.get('symbol'))

month_map = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
    'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

def parse_year(s):
    if s is None:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if not m:
        return None
    return int(m.group(1))

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for item in data if isinstance(data, list) else []:
            code = item.get('code') if isinstance(item, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d[^\"]*)"', cpc_str)

def to_lvl5_symbol(full_code):
    # Map CPC full code to dataset's level-5 symbol style: subclass like H01M
    m = re.match(r'^([A-Z]\d{2}[A-Z])', full_code)
    if not m:
        return None
    subclass4 = m.group(1)  # e.g., H01M
    # Some rows have 4 chars exactly
    if subclass4 in lvl5_set:
        return subclass4
    return None

records = []
for r in pub_rows:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    syms = set(filter(None, (to_lvl5_symbol(c) for c in codes)))
    for sym in syms:
        records.append((sym, y))

df = pd.DataFrame(records, columns=['symbol','year'])
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
            x = float(s.get(y, 0))
            if ema is None:
                ema = x
            else:
                ema = alpha * x + (1-alpha) * ema
            result_rows.append((sym, y, x, ema))

    ema_df = pd.DataFrame(result_rows, columns=['symbol','year','filings','ema'])

    # highest EMA per year across symbols
    ema_df['rank_in_year'] = ema_df.groupby('year')['ema'].rank(method='min', ascending=False)
    top = ema_df[ema_df['rank_in_year'] == 1].copy()

    # for each symbol, find its best year (max EMA; tie -> latest year)
    best = (ema_df.sort_values(['symbol','ema','year'], ascending=[True,False,False])
            .groupby('symbol', as_index=False)
            .first()[['symbol','year','ema']]
            .rename(columns={'year':'best_year','ema':'best_ema'}))

    top = top.merge(best, on='symbol', how='left')
    out = sorted(top.loc[top['best_year'] == 2022, 'symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_REpIUU5Q9ZjXVG7PraCmHz6q': 'file_storage/call_REpIUU5Q9ZjXVG7PraCmHz6q.json', 'var_call_ZBVZBFbjXz4WyZTQo7zUIwBP': 'file_storage/call_ZBVZBFbjXz4WyZTQo7zUIwBP.json'}

exec(code, env_args)
