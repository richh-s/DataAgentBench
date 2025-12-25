code = """import json, pandas as pd
from datetime import datetime

# Load full results from files
with open(var_call_Cmc3AB6UtXhSUS1qKWLKTAnC, 'r') as f:
    cpc_defs = json.load(f)
with open(var_call_ozNe7AkERDt3kCok5FRQQ4MD, 'r') as f:
    pubs = json.load(f)

# CPC level-5 symbols set
level5 = {r['symbol'] for r in cpc_defs}

# Helper to parse natural-language dates to year
months = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(d):
    if not d:
        return None
    try:
        parts = d.replace(',', '').split()
        if len(parts) < 3:
            return None
        mon = parts[0][:3]
        day = parts[1].rstrip('stndrh').rstrip('th')
        year = parts[2]
        dt = datetime(int(year), months.get(mon, 1), int(day))
        return dt.year
    except Exception:
        return None

# Collect counts per symbol, per year
counts = {}
for row in pubs:
    year = parse_year(row.get('publication_date'))
    if year is None:
        continue
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # Map to level-5 group code: take main group like 'H01M10/0565' -> 'H01M'
        # Level-5 symbols file appears like section+class+subclass (e.g., 'H01M')
        grp = code.split('/')[0][:4]
        if grp in level5:
            counts.setdefault(grp, {})[year] = counts.setdefault(grp, {}).get(year, 0) + 1

# Compute EMA per symbol over years
alpha = 0.2
results = []
for sym, year_counts in counts.items():
    years = sorted(year_counts)
    ema = None
    best_year = None
    best_ema = None
    for y in years:
        x = year_counts[y]
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1-alpha) * ema
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_year = y
    results.append({'symbol': sym, 'best_year': best_year, 'best_ema': best_ema})

# Filter where best_year is 2022
final_syms = [r['symbol'] for r in results if r['best_year'] == 2022]

out = json.dumps(final_syms)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Cmc3AB6UtXhSUS1qKWLKTAnC': 'file_storage/call_Cmc3AB6UtXhSUS1qKWLKTAnC.json', 'var_call_ozNe7AkERDt3kCok5FRQQ4MD': 'file_storage/call_ozNe7AkERDt3kCok5FRQQ4MD.json', 'var_call_raN5G2diC0r4YWFnVN8Xlunu': [{'?column?': '1'}]}

exec(code, env_args)
