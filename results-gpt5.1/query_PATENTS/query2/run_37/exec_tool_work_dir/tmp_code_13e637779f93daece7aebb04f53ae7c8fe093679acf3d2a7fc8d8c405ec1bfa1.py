code = """import json, re, pandas as pd

# Load full results from file paths
with open(var_call_H6gxBWrBgnKevCWiCcEtltqt, 'r') as f:
    grants = json.load(f)
with open(var_call_ttws7A7gi5PSQDtF9xZEcic8, 'r') as f:
    cpc_defs = json.load(f)

grants_df = pd.DataFrame(grants)

# Filter to Germany using Patents_info country code "DE " or " DE" or " DE-" patterns
def is_german(info):
    if not isinstance(info, str):
        return False
    return bool(re.search(r'\bDE\b', info)) or ' DE-' in info or 'DE patent' in info

grants_df = grants_df[grants_df['Patents_info'].apply(is_german)].copy()

# Parse grant year from natural-language grant_date
month_map = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(date_str):
    if not isinstance(date_str, str):
        return None
    m = re.search(r'(19|20)\d{2}', date_str)
    return int(m.group(0)) if m else None

# keep only rows with a valid year
grants_df['year'] = grants_df['grant_date'].apply(parse_year)

# extract country again to be safe

# Parse CPC list
codes = []
for _, row in grants_df.iterrows():
    cpc_raw = row.get('cpc')
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        # derive level-4 group code: take leading letter+2 digits, e.g., A01, H04, etc.
        m = re.match(r'^[A-Z]\d{2}', code)
        if not m:
            continue
        group4 = m.group(0)
        codes.append({'group4': group4, 'year': row['year']})

codes_df = pd.DataFrame(codes)

if codes_df.empty:
    result = []
else:
    # count filings per group per year
    counts = codes_df.groupby(['group4','year']).size().reset_index(name='count')

    # compute EMA by year per group with alpha=0.1, sorted by year
    alpha = 0.1
    ema_records = []
    for grp, sub in counts.groupby('group4'):
        sub = sub.sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_records.append({'group4': grp, 'year': int(r['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)

    # For patents granted in second half of 2019 we already filtered grant_date; EMA is over all available years, but since we only have 2019H2 data here, EMA reduces to that year.
    # Find best year (max EMA) per group4
    idx = ema_df.groupby('group4')['ema'].idxmax()
    best_df = ema_df.loc[idx].reset_index(drop=True)

    # Join with CPC definitions for titles
    cpc_defs_df = pd.DataFrame(cpc_defs)
    cpc_defs_df = cpc_defs_df[['symbol','titleFull']].rename(columns={'symbol':'group4','titleFull':'title'})

    merged = best_df.merge(cpc_defs_df, on='group4', how='left')

    # Sort by EMA descending
    merged = merged.sort_values('ema', ascending=False)

    # prepare output records
    result = []
    for _, r in merged.iterrows():
        result.append({
            'CPC_group_code': r['group4'],
            'titleFull': r.get('title'),
            'best_year': int(r['year']),
            'EMA_filings': r['ema']
        })

out = json.dumps(result[:50])
print("__RESULT__:")
print(out)"""

env_args = {'var_call_H6gxBWrBgnKevCWiCcEtltqt': 'file_storage/call_H6gxBWrBgnKevCWiCcEtltqt.json', 'var_call_ttws7A7gi5PSQDtF9xZEcic8': 'file_storage/call_ttws7A7gi5PSQDtF9xZEcic8.json'}

exec(code, env_args)
