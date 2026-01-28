code = """import json, re
# load data from previous query results stored in files
with open(var_call_sVFapy2HVnUUDPN1vSFJc7dk, 'r') as f:
    patents = json.load(f)
with open(var_call_tyvHmzSc4cejYDjBsfVyXt7g, 'r') as f:
    cpcs = json.load(f)

import pandas as pd

# Filter patents: granted in second half of 2019 (July 1 - Dec 31, 2019)
# grant_date is natural language; parse month and year
month_map = {"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"sept":9,"oct":10,"nov":11,"dec":12}

def parse_grant_year_month(gd):
    if not gd or not isinstance(gd, str):
        return None
    s = gd.lower()
    # find year
    m = re.search(r"(19|20)\d{2}", s)
    year = int(m.group(0)) if m else None
    # find month by name
    for k,v in month_map.items():
        if k in s:
            return (year, v)
    # try numeric month
    m2 = re.search(r"\b(0?[1-9]|1[0-2])\b", s)
    if m2:
        return (year, int(m2.group(0)))
    return (year, None)

rows = []
for p in patents:
    parsed = parse_grant_year_month(p.get('grant_date',''))
    if parsed and parsed[0]==2019 and parsed[1] and parsed[1]>=7 and parsed[1]<=12:
        # extract country code from Patents_info (e.g., 'from DE,' or 'In DE,')
        pi = p.get('Patents_info','')
        cc = None
        m = re.search(r"\bfrom ([A-Z]{2})\b", pi)
        if not m:
            m = re.search(r"\bIn ([A-Z]{2}),\b", pi)
        if m:
            cc = m.group(1)
        # Also look for 'DE,' inside parentheses like (no. DE-...)
        if not cc:
            m2 = re.search(r"\b([A-Z]{2})-\d", pi)
            if m2:
                cc = m2.group(1)
        rows.append({'rowid': p.get('rowid'), 'Patents_info': pi, 'cpc': p.get('cpc'), 'grant_year': parsed[0], 'grant_month': parsed[1], 'country': cc})

# expand CPC codes: cpc field is a JSON-like list; parse and extract codes
import ast

expanded = []
for r in rows:
    cpc_field = r['cpc']
    try:
        # sometimes it's proper JSON with double quotes; ast.literal_eval handles JSON-like
        cpc_list = ast.literal_eval(cpc_field)
    except Exception:
        # fallback: find all occurrences of "code": "..."
        codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
        cpc_list = [{'code': c} for c in codes]
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # normalize to CPC group level 4: first letter + two digits (section+class?) For CPC level 4 symbol in cpc_definition, symbols are like 'A01', i.e., letter + two digits
        m = re.match(r'^([A-Z])(\d{2})', code)
        if m:
            grp = m.group(1)+m.group(2)
        else:
            # some codes have different forms; take first 3 chars
            grp = code[:3]
        expanded.append({'rowid': r['rowid'], 'country': r['country'], 'grant_year': r['grant_year'], 'grant_month': r['grant_month'], 'cpc_code': code, 'cpc_group': grp})

# keep only Germany (DE)
df = pd.DataFrame(expanded)
if df.empty:
    result = {'error': 'no DE patents in H2 2019 found'}
else:
    df_de = df[df['country']=='DE'].copy()
    # count filings per year for each cpc_group. We will consider years based on filing_date? The user asked: EMA of patent filings each year for patents granted in H2 2019. Interpret as count of filings by year (filing_date) among those patents that were granted in H2 2019.
    # Need filing_date from original patents list
    filing_map = {p['rowid']: p.get('filing_date') for p in patents}
    df_de['filing_date'] = df_de['rowid'].map(filing_map)

    def parse_filing_year(fd):
        if not fd or not isinstance(fd, str):
            return None
        m = re.search(r"(19|20)\d{2}", fd)
        return int(m.group(0)) if m else None

    df_de['filing_year'] = df_de['filing_date'].apply(parse_filing_year)
    # drop rows without filing_year
    df_de = df_de.dropna(subset=['filing_year']).copy()

    # compute annual counts per cpc_group by filing_year
    counts = df_de.groupby(['cpc_group','filing_year']).size().reset_index(name='count')

    # compute EMA per cpc_group across years sorted ascending, smoothing factor alpha=0.1
    out = []
    for grp, gdf in counts.groupby('cpc_group'):
        g = gdf.sort_values('filing_year')
        ema = None
        years = []
        for _, row in g.iterrows():
            if ema is None:
                ema = row['count']
            else:
                ema = 0.1*row['count'] + 0.9*ema
            years.append({'year': int(row['filing_year']), 'count': int(row['count']), 'ema': float(ema)})
        # find year with highest EMA value for this group
        best = max(years, key=lambda x: x['ema'])
        out.append({'cpc_group': grp, 'best_year': best['year'], 'best_ema': best['ema']})

    # join with cpc definitions to get titleFull
    df_cpc = pd.DataFrame(cpcs)
    # cpc_definition symbols are like 'A01' etc; ensure symbol col is string
    df_cpc['symbol'] = df_cpc['symbol'].astype(str)
    merged = pd.DataFrame(out).merge(df_cpc, left_on='cpc_group', right_on='symbol', how='left')
    # prepare final list for top groups by best_ema
    merged['best_ema'] = merged['best_ema'].astype(float)
    merged_sorted = merged.sort_values('best_ema', ascending=False)
    final = merged_sorted[['cpc_group','titleFull','best_year','best_ema']].to_dict(orient='records')
    result = final

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_sVFapy2HVnUUDPN1vSFJc7dk': 'file_storage/call_sVFapy2HVnUUDPN1vSFJc7dk.json', 'var_call_tyvHmzSc4cejYDjBsfVyXt7g': 'file_storage/call_tyvHmzSc4cejYDjBsfVyXt7g.json'}

exec(code, env_args)
