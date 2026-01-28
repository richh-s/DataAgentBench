code = """import json, re
with open(var_call_sVFapy2HVnUUDPN1vSFJc7dk, 'r') as f:
    patents = json.load(f)
with open(var_call_tyvHmzSc4cejYDjBsfVyXt7g, 'r') as f:
    cpcs = json.load(f)

import pandas as pd
month_map = {"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"sept":9,"oct":10,"nov":11,"dec":12}

def parse_grant_year_month(gd):
    if not gd or not isinstance(gd, str):
        return None
    s = gd.lower()
    m = re.search(r"(19|20)\d{2}", s)
    year = int(m.group(0)) if m else None
    for k,v in month_map.items():
        if k in s:
            return (year, v)
    m2 = re.search(r"\b(0?[1-9]|1[0-2])\b", s)
    if m2:
        return (year, int(m2.group(0)))
    return (year, None)

rows = []
for p in patents:
    parsed = parse_grant_year_month(p.get('grant_date',''))
    if parsed and parsed[0]==2019 and parsed[1] and 7 <= parsed[1] <= 12:
        pi = p.get('Patents_info','')
        cc = None
        # patterns
        m = re.search(r"\bfrom ([A-Z]{2})\b", pi)
        if not m:
            m = re.search(r"\bIn ([A-Z]{2}),", pi)
        if not m:
            m = re.search(r"\(([A-Z]{2})-\d", pi)
        if not m:
            m = re.search(r"publication number ([A-Z]{2})-", pi)
        if m:
            cc = m.group(1)
        rows.append({'rowid': p.get('rowid'), 'Patents_info': pi, 'cpc': p.get('cpc'), 'filing_date': p.get('filing_date'), 'grant_year': parsed[0], 'grant_month': parsed[1], 'country': cc})

# parse CPCs and expand
import ast
expanded = []
for r in rows:
    cpc_field = r['cpc']
    try:
        cpc_list = ast.literal_eval(cpc_field)
    except Exception:
        codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
        cpc_list = [{'code': c} for c in codes]
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        m = re.match(r'^([A-Z])(\d{2})', code)
        if m:
            grp = m.group(1)+m.group(2)
        else:
            grp = code[:3]
        expanded.append({'rowid': r['rowid'], 'country': r['country'], 'grant_year': r['grant_year'], 'grant_month': r['grant_month'], 'filing_date': r.get('filing_date'), 'cpc_code': code, 'cpc_group': grp})

# create df
df = pd.DataFrame(expanded)
# prepare result structure
if df.empty:
    result = {'error': 'No patents granted in H2 2019 matched or none with CPC codes.'}
else:
    # filter to DE only
    df_de = df[df['country']=='DE'].copy()
    if df_de.empty:
        # try alternative country detection: look for 'DE' anywhere in Patents_info
        # reopen rows and check
        alt = []
        for r in rows:
            pi = r['Patents_info']
            if ' DE,' in pi or ' DE ' in pi or '-DE-' in pi or 'DE-' in pi:
                # expand cpcs for this r
                try:
                    cpc_list = ast.literal_eval(r['cpc'])
                except Exception:
                    codes = re.findall(r'"code"\s*:\s*"([^"]+)"', r['cpc'])
                    cpc_list = [{'code': c} for c in codes]
                for c in cpc_list:
                    code = c.get('code')
                    if not code:
                        continue
                    m = re.match(r'^([A-Z])(\d{2})', code)
                    if m:
                        grp = m.group(1)+m.group(2)
                    else:
                        grp = code[:3]
                    alt.append({'rowid': r['rowid'], 'country': 'DE', 'grant_year': r['grant_year'], 'grant_month': r['grant_month'], 'filing_date': r.get('filing_date'), 'cpc_code': code, 'cpc_group': grp})
        df_de = pd.DataFrame(alt)
    if df_de.empty:
        result = {'error': 'No Germany patents found in H2 2019.'}
    else:
        # parse filing_year
        def parse_filing_year(fd):
            if not fd or not isinstance(fd, str):
                return None
            m = re.search(r"(19|20)\d{2}", fd)
            return int(m.group(0)) if m else None
        df_de['filing_year'] = df_de['filing_date'].apply(parse_filing_year)
        df_de = df_de.dropna(subset=['filing_year']).copy()
        if df_de.empty:
            result = {'error': 'No filing years parsed for DE patents.'}
        else:
            counts = df_de.groupby(['cpc_group','filing_year']).size().reset_index(name='count')
            out = []
            for grp, gdf in counts.groupby('cpc_group'):
                g = gdf.sort_values('filing_year')
                ema = None
                years = []
                for _, row in g.iterrows():
                    if ema is None:
                        ema = float(row['count'])
                    else:
                        ema = 0.1*float(row['count']) + 0.9*ema
                    years.append({'year': int(row['filing_year']), 'count': int(row['count']), 'ema': ema})
                best = max(years, key=lambda x: x['ema'])
                out.append({'cpc_group': grp, 'best_year': best['year'], 'best_ema': best['ema']})
            df_cpc = pd.DataFrame(cpcs)
            df_cpc['symbol'] = df_cpc['symbol'].astype(str)
            merged = pd.DataFrame(out).merge(df_cpc, left_on='cpc_group', right_on='symbol', how='left')
            merged['best_ema'] = merged['best_ema'].astype(float)
            merged_sorted = merged.sort_values('best_ema', ascending=False)
            final = merged_sorted[['cpc_group','titleFull','best_year','best_ema']].to_dict(orient='records')
            result = final

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_sVFapy2HVnUUDPN1vSFJc7dk': 'file_storage/call_sVFapy2HVnUUDPN1vSFJc7dk.json', 'var_call_tyvHmzSc4cejYDjBsfVyXt7g': 'file_storage/call_tyvHmzSc4cejYDjBsfVyXt7g.json'}

exec(code, env_args)
