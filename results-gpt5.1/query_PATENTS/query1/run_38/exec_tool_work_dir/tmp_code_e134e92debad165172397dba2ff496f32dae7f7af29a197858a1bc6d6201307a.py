code = """import json, pandas as pd, os, re, datetime as dt

# Load full CPC publication data
file_path = var_call_nHf6L2YMvTOSPHGA95ZHbNbd
with open(file_path, 'r') as f:
    pub_rows = json.load(f)

pub_df = pd.DataFrame(pub_rows)

# Parse year from natural-language publication_date
month_map = {m: i for i, m in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], start=1)}

def parse_year(date_str):
    if not isinstance(date_str, str) or not date_str.strip():
        return None
    # Expect formats like "Aug 3rd, 2021" or similar
    try:
        parts = date_str.replace(',', '').split()
        # last part should be year
        year = int(parts[-1])
        return year
    except Exception:
        # fallback: search 4-digit year
        m = re.search(r'(19|20)\d{2}', date_str)
        if m:
            return int(m.group(0))
        return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Keep years up to 2022 only
pub_df = pub_df[pub_df['year'] <= 2022]

# Expand CPC JSON-like list to rows
records = []
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
        # Use full code as given (group level granularity is inherent in CPC symbol)
        records.append({'symbol': code, 'year': year})

cpc_year_df = pd.DataFrame(records)

# Load list of level-5 CPC symbols
file_path2 = var_call_BKYPqxAJW74yvZQFukMXgQQV
with open(file_path2, 'r') as f:
    level5_rows = json.load(f)
level5_df = pd.DataFrame(level5_rows)
level5_symbols = set(level5_df['symbol'].astype(str).unique())

# Filter to level-5 symbols only (match exact code prefix equal to symbol)
# Many publication CPC codes are more specific (e.g., H01M10/0565) while level5 may be at group level like H01M10/05.
# We'll map each publication code to the longest level-5 symbol that is a prefix of it.

level5_sorted = sorted(level5_symbols, key=len, reverse=True)

mapped_records = []
for _, row in cpc_year_df.iterrows():
    code = row['symbol']
    year = row['year']
    # find matching prefix
    match = None
    for sym in level5_sorted:
        if code.startswith(sym):
            match = sym
            break
    if match is not None:
        mapped_records.append({'symbol': match, 'year': year})

if not mapped_records:
    result = []
else:
    mapped_df = pd.DataFrame(mapped_records)

    # Count filings per symbol per year
    counts = mapped_df.groupby(['symbol', 'year']).size().reset_index(name='filings')

    # Compute EMA per symbol across years (sorted by year); alpha = 0.2
    alpha = 0.2
    ema_rows = []
    for sym, grp in counts.groupby('symbol'):
        grp = grp.sort_values('year')
        ema = None
        for _, r in grp.iterrows():
            y = r['year']
            f = r['filings']
            if ema is None:
                ema = f
            else:
                ema = alpha * f + (1 - alpha) * ema
            ema_rows.append({'symbol': sym, 'year': int(y), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_rows)

    # For each symbol, find year with highest EMA (best year)
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best_df = ema_df.loc[idx].copy()

    # Keep only symbols whose best year is 2022
    best_2022 = best_df[best_df['year'] == 2022]

    # Return just the CPC group codes (symbols) at level 5
    result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nHf6L2YMvTOSPHGA95ZHbNbd': 'file_storage/call_nHf6L2YMvTOSPHGA95ZHbNbd.json', 'var_call_BKYPqxAJW74yvZQFukMXgQQV': 'file_storage/call_BKYPqxAJW74yvZQFukMXgQQV.json'}

exec(code, env_args)
