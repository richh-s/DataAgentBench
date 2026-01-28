code = """import json, re
import pandas as pd
from datetime import datetime

# Load publication records (large file)
pub_src = var_call_PhA5KtVSST1r9jmANV5VZEeK
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

# Load CPC definitions level 4
cpc_defs_src = var_call_vJiriVHj3OogSDv2ZYp570e5
if isinstance(cpc_defs_src, str):
    with open(cpc_defs_src, 'r', encoding='utf-8') as f:
        cpc_defs = json.load(f)
else:
    cpc_defs = cpc_defs_src

def parse_country(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'\bfrom\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\bIn\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\bcountry_code\s*[:=]\s*([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    return None

MONTHS = {
    'jan':1,'january':1,
    'feb':2,'february':2,
    'mar':3,'march':3,
    'apr':4,'april':4,
    'may':5,
    'jun':6,'june':6,
    'jul':7,'july':7,
    'aug':8,'august':8,
    'sep':9,'sept':9,'september':9,
    'oct':10,'october':10,
    'nov':11,'november':11,
    'dec':12,'december':12,
}

def parse_nl_date(s: str):
    if not s:
        return None
    t = s.strip()
    # normalize commas
    t2 = re.sub(r'[,]', ' ', t)
    t2 = re.sub(r'\s+', ' ', t2).strip()
    # find year
    ym = re.search(r'(19\d{2}|20\d{2})', t2)
    if not ym:
        return None
    year = int(ym.group(1))
    # find month name/abbr
    ml = re.search(r'\b(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:t|tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\b', t2, flags=re.I)
    month = MONTHS[ml.group(1).lower()] if ml else 1
    # find day number near month if possible
    day = 1
    if ml:
        # look around month token for day numbers
        # pattern like '14th Mar 2019' or 'Mar 19th 2019'
        p1 = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+' + re.escape(ml.group(1)) + r'\b', t2, flags=re.I)
        p2 = re.search(re.escape(ml.group(1)) + r'\b\s+(\d{1,2})(?:st|nd|rd|th)?', t2, flags=re.I)
        if p1:
            day = int(p1.group(1))
        elif p2:
            day = int(p2.group(1))
        else:
            # any day number
            dm = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', t2)
            if dm:
                day = int(dm.group(1))
    else:
        dm = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', t2)
        if dm:
            day = int(dm.group(1))
    try:
        return datetime(year, month, day)
    except ValueError:
        # fallback safe
        return datetime(year, month, 1)

# Build dataframe and filter
rows = []
for r in pubs:
    country = parse_country(r.get('Patents_info'))
    if country != 'DE':
        continue
    gd = parse_nl_date(r.get('grant_date'))
    if gd is None:
        continue
    if not (gd.year == 2019 and gd.month >= 7):
        continue
    fd = parse_nl_date(r.get('filing_date'))
    if fd is None:
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        # CPC group at level 4: first 3 chars (e.g., A61, G06)
        grp = code.strip()[:3]
        rows.append({'grp': grp, 'filing_year': fd.year})

if not rows:
    out = []
else:
    df = pd.DataFrame(rows)
    # Count filings per year per group (count occurrences)
    counts = df.groupby(['grp','filing_year']).size().reset_index(name='n')

    alpha = 0.1
    results = []
    for grp, gdf in counts.groupby('grp'):
        gdf = gdf.sort_values('filing_year')
        ema = None
        best_year = None
        best_ema = None
        for _, row in gdf.iterrows():
            y = int(row['filing_year'])
            x = float(row['n'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            if best_ema is None or ema > best_ema or (ema == best_ema and y < best_year):
                best_ema = ema
                best_year = y
        results.append({'cpc_group_code': grp, 'best_year': best_year, 'best_ema': best_ema})

    resdf = pd.DataFrame(results).sort_values(['best_ema','cpc_group_code'], ascending=[False, True])

    # join titles
    defs_df = pd.DataFrame(cpc_defs)
    defs_df['symbol'] = defs_df['symbol'].astype(str)
    defs_df = defs_df[['symbol','titleFull']].rename(columns={'symbol':'cpc_group_code','titleFull':'full_title'})
    merged = resdf.merge(defs_df, on='cpc_group_code', how='left')

    # keep only those with title
    merged = merged.dropna(subset=['full_title'])

    # find max EMA and return all ties
    if merged.empty:
        out = []
    else:
        max_ema = merged['best_ema'].max()
        top = merged[merged['best_ema'] == max_ema].copy()
        top = top.sort_values('cpc_group_code')
        out = top[['full_title','cpc_group_code','best_year','best_ema']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_PhA5KtVSST1r9jmANV5VZEeK': 'file_storage/call_PhA5KtVSST1r9jmANV5VZEeK.json', 'var_call_vJiriVHj3OogSDv2ZYp570e5': 'file_storage/call_vJiriVHj3OogSDv2ZYp570e5.json'}

exec(code, env_args)
