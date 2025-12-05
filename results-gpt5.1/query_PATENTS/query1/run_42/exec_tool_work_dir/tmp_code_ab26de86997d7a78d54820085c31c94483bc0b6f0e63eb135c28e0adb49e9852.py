code = """import json, pandas as pd

# Stream/process publication records in chunks to avoid timeout
with open(var_call_O9FHJjNZP6Wqv82keo9sOKlj, 'r') as f:
    pub_records = json.load(f)

# Helper to parse year
def parse_year(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    parts = date_str.replace(',', '').split()
    if len(parts) < 3:
        return None
    try:
        return int(parts[-1])
    except:
        return None

# Build (symbol, year) counts incrementally using dict
from collections import defaultdict
counts = defaultdict(int)
for r in pub_records:
    y = parse_year(r.get('publication_date'))
    if not y:
        continue
    cpc_raw = r.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except:
        continue
    for c in cpc_list:
        code = c.get('code') if isinstance(c, dict) else None
        if code:
            counts[(code, y)] += 1

if not counts:
    result = json.dumps([])
else:
    # Convert counts dict to DataFrame
    data = [{'symbol': k[0], 'year': k[1], 'count': v} for k, v in counts.items()]
    df = pd.DataFrame(data)
    all_years = sorted(df['year'].unique())

    # Compute EMA symbol by symbol
    alpha = 0.2
    ema_records = []
    for sym, grp in df.groupby('symbol'):
        year_to_count = {row['year']: row['count'] for _, row in grp.iterrows()}
        ema_prev = None
        for y in all_years:
            x = year_to_count.get(y, 0)
            if ema_prev is None:
                ema = x
            else:
                ema = alpha * x + (1-alpha) * ema_prev
            ema_prev = ema
            ema_records.append({'symbol': sym, 'year': y, 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)

    # Best year per symbol
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # Filter to best year 2022
    best_2022 = best[best['year'] == 2022]

    # Load level 5 symbols
    with open(var_call_tLvSAiYMplzyc8PT5ueokZYP, 'r') as f:
        level5 = json.load(f)
    level5_syms = set(str(r['symbol']) for r in level5)

    best_2022_level5 = best_2022[best_2022['symbol'].isin(level5_syms)]
    symbols_2022 = sorted(best_2022_level5['symbol'].unique().tolist())
    result = json.dumps(symbols_2022)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_O9FHJjNZP6Wqv82keo9sOKlj': 'file_storage/call_O9FHJjNZP6Wqv82keo9sOKlj.json', 'var_call_tLvSAiYMplzyc8PT5ueokZYP': 'file_storage/call_tLvSAiYMplzyc8PT5ueokZYP.json'}

exec(code, env_args)
