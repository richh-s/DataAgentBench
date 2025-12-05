code = """import json, pandas as pd
from datetime import datetime

# Load full publication data
with open(var_call_O9FHJjNZP6Wqv82keo9sOKlj, 'r') as f:
    pub_records = json.load(f)

# Parse year from natural-language publication_date
months = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    parts = date_str.replace(',', '').split()
    if len(parts) < 3:
        return None
    try:
        year = int(parts[-1])
        return year
    except:
        return None

rows = []
for r in pub_records:
    y = parse_year(r.get('publication_date'))
    if not y:
        continue
    try:
        cpc_list = json.loads(r.get('cpc') or '[]')
    except:
        continue
    for c in cpc_list:
        code = c.get('code')
        if code:
            rows.append({'year': y, 'symbol': code})

if not rows:
    result = json.dumps([])
else:
    df = pd.DataFrame(rows)
    # Count filings per year per symbol
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')

    # Build complete year range
    all_years = sorted(counts['year'].unique())

    # Compute EMA per symbol over years (alpha=0.2), in ascending year order
    alpha = 0.2
    ema_records = []
    for sym, grp in counts.groupby('symbol'):
        grp = grp.set_index('year').reindex(all_years, fill_value=0)
        ema_prev = None
        for y in all_years:
            x = grp.loc[y, 'count']
            if ema_prev is None:
                ema = x
            else:
                ema = alpha * x + (1-alpha) * ema_prev
            ema_prev = ema
            ema_records.append({'symbol': sym, 'year': y, 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)

    # For each symbol, find year with max EMA and its value
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)

    # Keep only best year 2022
    best_2022 = best[best['year'] == 2022]

    # Load level-5 symbols
    with open(var_call_tLvSAiYMplzyc8PT5ueokZYP, 'r') as f:
        level5 = json.load(f)
    level5_syms = set(str(r['symbol']) for r in level5)

    # Filter to level 5 symbols
    best_2022_level5 = best_2022[best_2022['symbol'].isin(level5_syms)].copy()

    # We only need CPC group codes at level 5; return unique symbols
    symbols_2022 = sorted(best_2022_level5['symbol'].unique().tolist())
    result = json.dumps(symbols_2022)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_O9FHJjNZP6Wqv82keo9sOKlj': 'file_storage/call_O9FHJjNZP6Wqv82keo9sOKlj.json', 'var_call_tLvSAiYMplzyc8PT5ueokZYP': 'file_storage/call_tLvSAiYMplzyc8PT5ueokZYP.json'}

exec(code, env_args)
