code = """import json, pandas as pd, re

# Stream and process publication data in chunks to avoid timeout

def parse_year(date_str):
    if not isinstance(date_str, str):
        return None
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}[^,]*,?\s*(\d{4})', date_str)
    if not m:
        m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}\w*,?\s*(\d{4})', date_str)
    if m:
        return int(m.group(2))
    m = re.search(r'(\d{4})', date_str)
    if m:
        return int(m.group(1))
    return None

# Load cpc level 5 symbols
with open(var_call_fPJM9bvSQ2hCsURVJ49wpMmI, 'r') as f:
    cpc5_data = json.load(f)
import pandas as pd
cpc5_df = pd.DataFrame(cpc5_data)
cpc5_symbols = set(cpc5_df['symbol'].astype(str))

# Read publication data file in memory (it's a JSON list)
with open(var_call_jA0ONeP22wVdv6r8PI2bC5RN, 'r') as f:
    pub_data = json.load(f)

counts = {}

for row in pub_data:
    year = parse_year(row.get('publication_date'))
    if year is None or year < 2000 or year > 2024:
        continue
    cpc_raw = row.get('cpc')
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        # we'll compute EMA later, keep full counts
        counts.setdefault(code, {}).setdefault(year, 0)
        counts[code][year] += 1

alpha = 0.2
ema_best_year = {}

for code, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    ema = None
    best_ema = None
    best_year = None
    for y in years:
        val = year_counts[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1-alpha) * ema
        if (best_ema is None) or (ema > best_ema):
            best_ema = ema
            best_year = y
    ema_best_year[code] = best_year

# Filter codes whose best year is 2022 and which are level 5
codes_2022_lvl5 = sorted([code for code, by in ema_best_year.items() if by == 2022 and code in cpc5_symbols])

import json as _json
print("__RESULT__:")
print(_json.dumps(codes_2022_lvl5))"""

env_args = {'var_call_jA0ONeP22wVdv6r8PI2bC5RN': 'file_storage/call_jA0ONeP22wVdv6r8PI2bC5RN.json', 'var_call_fPJM9bvSQ2hCsURVJ49wpMmI': 'file_storage/call_fPJM9bvSQ2hCsURVJ49wpMmI.json'}

exec(code, env_args)
