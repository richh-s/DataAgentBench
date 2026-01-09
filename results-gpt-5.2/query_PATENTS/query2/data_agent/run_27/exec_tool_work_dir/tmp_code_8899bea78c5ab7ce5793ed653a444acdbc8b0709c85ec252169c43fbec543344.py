code = """import json, re, pandas as pd
from datetime import datetime

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

pub = load_records(var_call_qBBRnniB5PI8yE8ugWQT6KVX)
defs = load_records(var_call_dbBYBxKfVDod891JPW5JTsVk)

def parse_country(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'\bIn\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\bcountry_code\"\s*:\s*\"([A-Z]{2})\"', patents_info)
    if m:
        return m.group(1)
    # try publication number prefix like DE-
    m = re.search(r'\b([A-Z]{2})-\d', patents_info)
    if m:
        return m.group(1)
    return None

months = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_nat_date(s):
    if not s:
        return None
    s2 = s.strip()
    # Extract day month year patterns
    # e.g., '3rd August 2021', '21st of September, 2021', 'dated 6th October 2020', 'March the 18th, 2019', '29th March 2019'
    s2 = s2.replace(',', ' ')
    s2 = re.sub(r'\bdated\b', ' ', s2, flags=re.I)
    s2 = re.sub(r'\bthe\b', ' ', s2, flags=re.I)
    s2 = re.sub(r'\bof\b', ' ', s2, flags=re.I)
    s2 = re.sub(r'\s+', ' ', s2).strip()
    # month name first
    m = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b\s*(\d{1,2})(?:st|nd|rd|th)?\s*(\d{4})', s2, flags=re.I)
    if m:
        mon = months[m.group(1).lower()]
        day = int(m.group(2))
        year = int(m.group(3))
        return datetime(year, mon, day).date()
    # day first
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s*(\d{4})', s2, flags=re.I)
    if m:
        day = int(m.group(1))
        mon = months[m.group(2).lower()]
        year = int(m.group(3))
        return datetime(year, mon, day).date()
    # year only
    m = re.search(r'\b(\d{4})\b', s2)
    if m:
        return datetime(int(m.group(1)), 1, 1).date()
    return None

# filter patents granted in second half 2019 and country Germany
rows=[]
for r in pub:
    ctry = parse_country(r.get('Patents_info'))
    if ctry != 'DE':
        continue
    gd = parse_nat_date(r.get('grant_date'))
    if not gd:
        continue
    if not (gd.year==2019 and gd.month>=7 and gd.month<=12):
        continue
    fd = parse_nat_date(r.get('filing_date'))
    if not fd:
        continue
    # parse cpc list
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    for ent in cpcs:
        code = ent.get('code')
        if not code:
            continue
        # level 4: first 3 chars like H01, A61
        grp = code.replace(' ', '')[:3]
        if len(grp)==3 and grp[0].isalpha() and grp[1:].isdigit():
            rows.append({'grp4': grp, 'filing_year': fd.year})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    # count filings per year per grp4
    counts = df.groupby(['grp4','filing_year']).size().reset_index(name='filings')
    # build complete year range per group
    results=[]
    alpha=0.1
    for grp, sub in counts.groupby('grp4'):
        sub = sub.sort_values('filing_year')
        years = list(range(int(sub['filing_year'].min()), int(sub['filing_year'].max())+1))
        m = {int(y): int(f) for y,f in zip(sub['filing_year'], sub['filings'])}
        ema=None
        best_year=None
        best_ema=None
        for y in years:
            x = m.get(y, 0)
            if ema is None:
                ema = x
            else:
                ema = alpha*x + (1-alpha)*ema
            if best_ema is None or ema>best_ema:
                best_ema=ema
                best_year=y
        results.append({'cpc_group_code': grp, 'best_year': best_year, 'max_ema_filings': float(best_ema)})
    resdf = pd.DataFrame(results).sort_values(['max_ema_filings','cpc_group_code'], ascending=[False, True])
    # attach title
    defmap = {d['symbol']: d.get('titleFull') for d in defs if d.get('symbol')}
    resdf['titleFull'] = resdf['cpc_group_code'].map(defmap)
    out = resdf.to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qBBRnniB5PI8yE8ugWQT6KVX': 'file_storage/call_qBBRnniB5PI8yE8ugWQT6KVX.json', 'var_call_dbBYBxKfVDod891JPW5JTsVk': 'file_storage/call_dbBYBxKfVDod891JPW5JTsVk.json'}

exec(code, env_args)
