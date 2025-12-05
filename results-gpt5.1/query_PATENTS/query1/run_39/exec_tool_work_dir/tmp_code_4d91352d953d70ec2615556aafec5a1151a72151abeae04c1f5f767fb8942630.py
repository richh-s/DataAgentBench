code = """import json, pandas as pd, datetime
from datetime import datetime

# Load full publication data
file_path = var_call_BRtEvDUGwcsW5f4WeeQ2SNSz
with open(file_path, 'r') as f:
    pub_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
def parse_year(date_str):
    if not isinstance(date_str, str) or not date_str.strip():
        return None
    for fmt in ['%b %dth, %Y', '%B %dth, %Y', '%b %dst, %Y', '%B %dst, %Y', '%b %dnd, %Y', '%B %dnd, %Y', '%b %drd, %Y', '%B %drd, %Y']:
        try:
            return datetime.strptime(date_str, fmt).year
        except Exception:
            continue
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)

# Drop rows without year
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Expand CPC JSON-like lists
def extract_cpc_codes(cpc_str):
    if not isinstance(cpc_str, str) or not cpc_str.strip():
        return []
    try:
        data = json.loads(cpc_str)
        if isinstance(data, list):
            return [entry.get('code') for entry in data if isinstance(entry, dict) and entry.get('code')]
        return []
    except Exception:
        return []

pub_df['cpc_list'] = pub_df['cpc'].apply(extract_cpc_codes)

# Explode to one row per (year, cpc_code)
exploded = pub_df.explode('cpc_list').dropna(subset=['cpc_list'])
exploded = exploded.rename(columns={'cpc_list': 'symbol'})

# Load level-5 symbols data (already a list of dicts)
level5_list = var_call_WuaGZ78KOmcVSrbBK4zL6jre
level5_df = pd.DataFrame(level5_list)
level5_symbols = set(level5_df['symbol'].astype(str))

exploded = exploded[exploded['symbol'].isin(level5_symbols)]

if exploded.empty:
    result = []
else:
    # Count filings per year per symbol
    counts = exploded.groupby(['symbol','year']).size().reset_index(name='count')

    # Compute EMA per symbol over years (sorted) with alpha=0.2
    alpha = 0.2
    all_years = sorted(counts['year'].unique())

    ema_records = []
    for symbol, grp in counts.groupby('symbol'):
        grp = grp.set_index('year').reindex(all_years, fill_value=0).sort_index()
        ema = None
        for y in all_years:
            c = grp.loc[y, 'count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1-alpha) * ema
            ema_records.append({'symbol': symbol, 'year': int(y), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)

    # For each symbol, find year with highest EMA
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best_df = ema_df.loc[idx].reset_index(drop=True)

    # Filter to those whose best year is 2022
    best_2022 = best_df[best_df['year'] == 2022]

    result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_BRtEvDUGwcsW5f4WeeQ2SNSz': 'file_storage/call_BRtEvDUGwcsW5f4WeeQ2SNSz.json', 'var_call_WuaGZ78KOmcVSrbBK4zL6jre': 'file_storage/call_WuaGZ78KOmcVSrbBK4zL6jre.json', 'var_call_ZzSMWosIL71ZrCsbsTKt5Qki': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_call_TGHx9Ynwae7HVZJyYqynXUBk': ['publicationinfo']}

exec(code, env_args)
