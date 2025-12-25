code = """import json, pandas as pd, re, datetime as dt

# Load full publication data
file_path = var_call_IR88Pe7p8TAKAffIix7ARFNT
with open(file_path, 'r') as f:
    pub_data = json.load(f)

# Helper to parse natural-language date like "Aug 3rd, 2021"
suffix_re = re.compile(r'(st|nd|rd|th)')

def parse_date(s):
    if not s:
        return None
    try:
        # remove ordinal suffix from day
        parts = s.split()
        if len(parts) == 3:
            # e.g., Aug 3rd, 2021
            month = parts[0]
            day = suffix_re.sub('', parts[1].replace(',', ''))
            year = parts[2].replace(',', '')
            cleaned = f"{month} {day} {year}"
            return dt.datetime.strptime(cleaned, '%b %d %Y')
        else:
            # fallback
            return dt.datetime.strptime(s, '%B %dth, %Y')
    except Exception:
        return None

records = []
for rec in pub_data:
    d = parse_date(rec.get('publication_date'))
    if not d:
        continue
    year = d.year
    # Only consider years up to 2022 as relevant for EMA
    if year > 2022:
        continue
    cpc_raw = rec.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        records.append({'year': year, 'code': code})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per (code, year)
    counts = df.groupby(['code','year']).size().reset_index(name='count')

    # For each code, compute yearly EMA with alpha=0.2, in chronological order
    alpha = 0.2
    ema_rows = []
    for code, sub in counts.groupby('code'):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            y = row['year']
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_rows.append({'code': code, 'year': int(y), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_rows)
    # For each code, find year with max EMA and the max EMA value
    idx = ema_df.groupby('code')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    # Keep only codes whose best year is 2022
    best_2022 = best[best['year'] == 2022]
    # We only need the codes
    result = sorted(best_2022['code'].unique().tolist())

import json as _json
out = _json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_hyWqSqLLOeAWPBJkYlhwZkrm': [], 'var_call_IR88Pe7p8TAKAffIix7ARFNT': 'file_storage/call_IR88Pe7p8TAKAffIix7ARFNT.json'}

exec(code, env_args)
