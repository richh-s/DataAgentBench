code = """import json, re, pandas as pd

# Load full publication data from file
with open(var_call_eEEAZzukwKjShZbabuTbjdEo, 'r') as f:
    pubs = json.load(f)

pubs_df = pd.DataFrame(pubs)

# Filter to Germany using Patents_info containing 'country code DE'
pubs_df = pubs_df[pubs_df['Patents_info'].str.contains('country code DE', case=False, na=False)].copy()

# Parse grant_date natural language to datetime and filter to second half of 2019
from dateutil import parser

def parse_date(s):
    if not isinstance(s, str) or not s.strip():
        return pd.NaT
    s = re.sub(r'\b(\d+)(st|nd|rd|th)\b', r'\1', s)
    s = s.replace('dated ', '')
    s = s.replace('the ', '')
    try:
        return parser.parse(s, dayfirst=False, fuzzy=True)
    except Exception:
        try:
            return parser.parse(s, dayfirst=True, fuzzy=True)
        except Exception:
            return pd.NaT

pubs_df['grant_dt'] = pubs_df['grant_date'].apply(parse_date)

mask = (pubs_df['grant_dt'] >= pd.Timestamp('2019-07-01')) & (pubs_df['grant_dt'] <= pd.Timestamp('2019-12-31'))
pubs_df = pubs_df[mask].copy()

# Extract application year from grant_dt for EMA by year
pubs_df['year'] = pubs_df['grant_dt'].dt.year

# Parse CPC JSON-like string and extract codes; map to level-4 group (first 4 chars letters+digits)

def extract_cpc_codes(cpc_str):
    if not isinstance(cpc_str, str) or not cpc_str.strip():
        return []
    try:
        data = json.loads(cpc_str)
    except Exception:
        return []
    codes = []
    for entry in data:
        code = entry.get('code') if isinstance(entry, dict) else None
        if isinstance(code, str):
            m = re.match(r'^[A-Z]\d{2}', code)
            if m:
                codes.append(m.group(0))
    return list(set(codes))

pubs_df['cpc_groups'] = pubs_df['cpc'].apply(extract_cpc_codes)

rows = []
for _, r in pubs_df.iterrows():
    for g in r['cpc_groups']:
        rows.append({'cpc_group': g, 'year': r['year']})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Count filings per year and CPC group
    counts = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')
    # Compute EMA per group over years sorted
    records = []
    alpha = 0.1
    for g, sub in counts.groupby('cpc_group'):
        sub = sub.sort_values('year')
        ema = None
        best_ema = None
        best_year = None
        for _, row in sub.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            if (best_ema is None) or (ema > best_ema):
                best_ema = ema
                best_year = int(row['year'])
        records.append({'cpc_group': g, 'best_year': best_year, 'best_ema': float(best_ema)})
    res_df = pd.DataFrame(records)
    # Keep top groups by best_ema
    res_df = res_df.sort_values('best_ema', ascending=False)
    result = res_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eEEAZzukwKjShZbabuTbjdEo': 'file_storage/call_eEEAZzukwKjShZbabuTbjdEo.json', 'var_call_nu3TybwcAHcPWhDwF33RtlZj': 'file_storage/call_nu3TybwcAHcPWhDwF33RtlZj.json'}

exec(code, env_args)
