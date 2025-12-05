code = """import json, re, pandas as pd
from datetime import datetime

with open(var_call_9ZMLU8ycLofgDjCOW1hmUTvQ, 'r') as f:
    pubs = json.load(f)

pubs_df = pd.DataFrame(pubs)

# Same processing but add guards
pat = re.compile(r'country code\s+([A-Z]{2})', re.IGNORECASE)

def get_country(info):
    if not isinstance(info, str):
        return None
    m = pat.search(info)
    return m.group(1).upper() if m else None

pubs_df['country'] = pubs_df['Patents_info'].apply(get_country)

months = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_natural_date(s):
    if not isinstance(s, str) or not s.strip():
        return None
    s = s.replace(',', ' ').replace('  ', ' ')
    s2 = re.sub(r'^(dated|on)\s+', '', s.strip(), flags=re.IGNORECASE)
    m = re.search(r'(\d{1,2})(st|nd|rd|th)?\s+(of\s+)?([A-Za-z]+)\s+(\d{4})', s2)
    if not m:
        m = re.search(r'([A-Za-z]+)\s+(\d{1,2})(st|nd|rd|th)?\s+(\d{4})', s2)
        if not m:
            return None
        month = m.group(1)
        day = int(m.group(2))
        year = int(m.group(4))
    else:
        day = int(m.group(1))
        month = m.group(4)
        year = int(m.group(5))
    month_num = months.get(month.capitalize())
    if not month_num:
        return None
    try:
        return datetime(year, month_num, day)
    except Exception:
        return None

pubs_df['grant_dt'] = pubs_df['grant_date'].apply(parse_natural_date)

start_2019_h2 = datetime(2019,7,1)
end_2019_h2 = datetime(2019,12,31)

filtered = pubs_df[(pubs_df['country'] == 'DE') & (pubs_df['grant_dt'] >= start_2019_h2) & (pubs_df['grant_dt'] <= end_2019_h2)].copy()

if filtered.empty:
    out = json.dumps([])
    print("__RESULT__:")
    print(out)
else:
    def extract_codes(cpc_str):
        if not isinstance(cpc_str, str) or not cpc_str.strip():
            return []
        try:
            data = json.loads(cpc_str)
            return [d.get('code') for d in data if isinstance(d, dict) and d.get('code')]
        except Exception:
            return re.findall(r'"code"\s*:\s*"([A-Z0-9/]+)"', cpc_str)

    filtered['cpc_codes'] = filtered['cpc'].apply(extract_codes)
    filtered = filtered.explode('cpc_codes').dropna(subset=['cpc_codes'])

    if filtered.empty:
        out = json.dumps([])
        print("__RESULT__:")
        print(out)
    else:
        filtered['cpc_group'] = filtered['cpc_codes'].str.slice(0,3)
        filtered['year'] = filtered['grant_dt'].dt.year
        counts = filtered.groupby(['cpc_group','year']).size().reset_index(name='filings')

        alpha = 0.1
        ema_rows = []
        for grp, sub in counts.groupby('cpc_group'):
            sub = sub.sort_values('year')
            ema = None
            for _, row in sub.iterrows():
                if ema is None:
                    ema = row['filings']
                else:
                    ema = alpha*row['filings'] + (1-alpha)*ema
                ema_rows.append({'cpc_group': grp, 'year': int(row['year']), 'ema_filings': float(ema)})

        ema_df = pd.DataFrame(ema_rows)
        if ema_df.empty:
            out = json.dumps([])
            print("__RESULT__:")
            print(out)
        else:
            idx = ema_df.groupby('cpc_group')['ema_filings'].idxmax()
            best = ema_df.loc[idx].reset_index(drop=True)

            with open(var_call_mOIWhZ82u82CIgq59CRn9m1r, 'r') as f:
                defs = json.load(f)
            defs_df = pd.DataFrame(defs)

            def to_int(x):
                try:
                    return int(float(x))
                except Exception:
                    return None

            defs_df['lvl'] = defs_df['level'].apply(to_int)
            level4 = defs_df[defs_df['lvl'] == 4]

            merged = best.merge(level4, left_on='cpc_group', right_on='symbol', how='left')
            merged = merged.sort_values('ema_filings', ascending=False).head(10)
            result = merged[['cpc_group','titleFull','year','ema_filings']].to_dict(orient='records')
            out = json.dumps(result)
            print("__RESULT__:")
            print(out)"""

env_args = {'var_call_9ZMLU8ycLofgDjCOW1hmUTvQ': 'file_storage/call_9ZMLU8ycLofgDjCOW1hmUTvQ.json', 'var_call_mOIWhZ82u82CIgq59CRn9m1r': 'file_storage/call_mOIWhZ82u82CIgq59CRn9m1r.json'}

exec(code, env_args)
