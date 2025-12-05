code = """import json, pandas as pd, re

# Load a subset of CPC publication data incrementally to avoid timeout
file_path = var_call_nHf6L2YMvTOSPHGA95ZHbNbd
with open(file_path, 'r') as f:
    pub_rows = json.load(f)

pub_df = pd.DataFrame(pub_rows)[['cpc', 'publication_date']]

month_map = {m: i for i, m in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], start=1)}

def parse_year(date_str):
    if not isinstance(date_str, str) or not date_str.strip():
        return None
    try:
        parts = date_str.replace(',', '').split()
        year = int(parts[-1])
        return year
    except Exception:
        m = re.search(r'(19|20)\d{2}', date_str)
        if m:
            return int(m.group(0))
        return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)
pub_df = pub_df[pub_df['year'] <= 2022]

# Expand CPC codes but only keep symbol-year counts directly (to reduce memory)
from collections import defaultdict
symbol_year_counts = defaultdict(int)

for _, row in pub_df.iterrows():
    year = row['year']
    cpc_str = row['cpc']
    if not isinstance(cpc_str, str) or not cpc_str.strip():
        continue
    try:
        codes = json.loads(cpc_str)
    except Exception:
        continue
    for entry in codes:
        code = entry.get('code')
        if not code:
            continue
        symbol_year_counts[(code, year)] += 1

# Load level-5 symbols
file_path2 = var_call_BKYPqxAJW74yvZQFukMXgQQV
with open(file_path2, 'r') as f:
    level5_rows = json.load(f)
level5_df = pd.DataFrame(level5_rows)
level5_symbols = set(level5_df['symbol'].astype(str).unique())
level5_sorted = sorted(level5_symbols, key=len, reverse=True)

# Map each code-year to nearest level-5 symbol prefix
from collections import defaultdict
lvl5_year_counts = defaultdict(int)

for (code, year), cnt in symbol_year_counts.items():
    match = None
    for sym in level5_sorted:
        if code.startswith(sym):
            match = sym
            break
    if match is not None:
        lvl5_year_counts[(match, year)] += cnt

# Compute EMA
alpha = 0.2
ema = {}
ema_best = {}  # symbol -> (best_year, best_ema)

# Get sorted years
years = sorted({year for (_, year) in lvl5_year_counts.keys()})

symbols = sorted({sym for (sym, _) in lvl5_year_counts.keys()})

for sym in symbols:
    prev_ema = None
    for year in years:
        f = lvl5_year_counts.get((sym, year), 0)
        if prev_ema is None:
            prev_ema = f
        else:
            prev_ema = alpha * f + (1 - alpha) * prev_ema
        key = (sym, year)
        ema[key] = prev_ema
        best_year, best_val = ema_best.get(sym, (None, float('-inf')))
        if prev_ema > best_val:
            ema_best[sym] = (year, prev_ema)

# Filter symbols whose best year is 2022
result_symbols = sorted([sym for sym, (year, _) in ema_best.items() if year == 2022])

import json as _json
out = _json.dumps(result_symbols)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nHf6L2YMvTOSPHGA95ZHbNbd': 'file_storage/call_nHf6L2YMvTOSPHGA95ZHbNbd.json', 'var_call_BKYPqxAJW74yvZQFukMXgQQV': 'file_storage/call_BKYPqxAJW74yvZQFukMXgQQV.json'}

exec(code, env_args)
