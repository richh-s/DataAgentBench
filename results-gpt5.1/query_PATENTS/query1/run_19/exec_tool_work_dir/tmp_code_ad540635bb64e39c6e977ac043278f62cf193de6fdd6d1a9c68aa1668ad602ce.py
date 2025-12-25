code = """import json, pandas as pd, datetime

# Load full publication data
with open(var_call_YOFW3apAvL3zruPMbGs3Qe3L, 'r') as f:
    pub_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
import dateutil.parser

def get_year(s):
    try:
        return dateutil.parser.parse(s).year
    except Exception:
        return None

pub_df['year'] = pub_df['publication_date'].apply(get_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Extract CPC codes per publication

def extract_codes(cpc_str):
    try:
        arr = json.loads(cpc_str)
        return [e.get('code') for e in arr if isinstance(e, dict) and e.get('code')]
    except Exception:
        return []

pub_df['codes'] = pub_df['cpc'].apply(extract_codes)

# Explode codes
pub_exp = pub_df.explode('codes').dropna(subset=['codes'])

# Count filings per year per CPC code
counts = pub_exp.groupby(['codes','year']).size().reset_index(name='count')

# Get list of years
years = sorted(counts['year'].unique())

alpha = 0.2

# Compute EMA for each code over years
ema_records = []
for code, grp in counts.groupby('codes'):
    year_to_count = {row['year']: row['count'] for _, row in grp.iterrows()}
    ema_prev = None
    for y in years:
        c = year_to_count.get(y, 0)
        if ema_prev is None:
            ema = c
        else:
            ema = alpha * c + (1-alpha) * ema_prev
        ema_prev = ema
        ema_records.append({'code': code, 'year': y, 'ema': ema})

ema_df = pd.DataFrame(ema_records)

# For each code, find year with max EMA
idx = ema_df.groupby('code')['ema'].idxmax()
best_df = ema_df.loc[idx].reset_index(drop=True)

# Keep only best year 2022
best_2022 = best_df[best_df['year'] == 2022]

# Load CPC level-5 symbols
with open(var_call_yyXQsWFYE4haL79sfwXApbEq, 'r') as f:
    cpc_defs = json.load(f)

cpc5 = {row['symbol'] for row in cpc_defs}

# Filter codes to those in level-5 definitions
best_2022_lvl5 = best_2022[best_2022['code'].isin(cpc5)]

# Return just the CPC group codes (unique)
result_codes = sorted(best_2022_lvl5['code'].unique().tolist())

out = json.dumps(result_codes)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_YOFW3apAvL3zruPMbGs3Qe3L': 'file_storage/call_YOFW3apAvL3zruPMbGs3Qe3L.json', 'var_call_yyXQsWFYE4haL79sfwXApbEq': 'file_storage/call_yyXQsWFYE4haL79sfwXApbEq.json'}

exec(code, env_args)
