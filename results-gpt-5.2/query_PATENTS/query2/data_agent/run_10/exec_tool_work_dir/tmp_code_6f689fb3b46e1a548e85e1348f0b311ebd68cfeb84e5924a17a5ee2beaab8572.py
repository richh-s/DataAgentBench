code = """import json, re
import pandas as pd
from datetime import datetime

# Load publication records (large file)
path_pub = var_call_jjtQBT3Y7R4oBATuyGZHFkyH
with open(path_pub, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

def parse_country(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'\bIn\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\bcountry_code\s*[:=]\s*([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\b([A-Z]{2})\s+patent\b', patents_info)
    if m:
        return m.group(1)
    return None

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_nl_date(s: str):
    if not s:
        return None
    s0 = s.strip()
    # remove leading words
    s0 = re.sub(r'^(dated\s+|on\s+|the\s+|Date\s*[:=]\s*)', '', s0, flags=re.I)
    s0 = s0.replace(',', ' ')
    s0 = re.sub(r'\b(st|nd|rd|th)\b', '', s0, flags=re.I)
    s0 = re.sub(r'\s+', ' ', s0).strip()
    # patterns: "3 August 2021" or "August 3 2021" or "21 of September 2021"
    s0 = re.sub(r'\bof\b', ' ', s0, flags=re.I)
    parts = s0.split(' ')
    # try day month year
    try:
        if len(parts)>=3 and parts[0].isdigit() and parts[1].lower() in month_map and parts[2].isdigit():
            return datetime(int(parts[2]), month_map[parts[1].lower()], int(parts[0])).date()
        if len(parts)>=3 and parts[0].lower() in month_map and parts[1].isdigit() and parts[2].isdigit():
            return datetime(int(parts[2]), month_map[parts[0].lower()], int(parts[1])).date()
    except Exception:
        pass
    # fallback: datetime parser limited
    for fmt in ['%B %d %Y','%d %B %Y','%b %d %Y','%d %b %Y','%Y-%m-%d']:
        try:
            return datetime.strptime(s0, fmt).date()
        except Exception:
            continue
    return None

def extract_cpc_codes(cpc_field: str):
    if not cpc_field:
        return []
    try:
        arr = json.loads(cpc_field)
        codes = []
        for it in arr if isinstance(arr, list) else []:
            code = it.get('code') if isinstance(it, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        # regex fallback
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+\/\d+)"', cpc_field)

def cpc_level4(code: str):
    # level-4 as CPC subclass + main group (before '/')
    # e.g., H01M10/0565 -> H01M10; B29C70/48 -> B29C70
    if not code or '/' not in code:
        return None
    return code.split('/')[0]

rows = []
for r in pubs:
    cc = parse_country(r.get('Patents_info'))
    if cc != 'DE':
        continue
    gdate = parse_nl_date(r.get('grant_date'))
    if not gdate:
        continue
    if not (datetime(2019,7,1).date() <= gdate <= datetime(2019,12,31).date()):
        continue
    fdate = parse_nl_date(r.get('filing_date'))
    if not fdate:
        continue
    year = fdate.year
    codes = extract_cpc_codes(r.get('cpc'))
    lvl4s = {cpc_level4(c) for c in codes}
    lvl4s.discard(None)
    for g in lvl4s:
        rows.append((g, year))

df = pd.DataFrame(rows, columns=['cpc4','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['cpc4','year']).reset_index(name='filings')
    # build full year range per cpc4
    result_rows = []
    alpha = 0.1
    for cpc4, sub in counts.groupby('cpc4'):
        sub = sub.sort_values('year')
        years = list(range(int(sub['year'].min()), int(sub['year'].max())+1))
        m = sub.set_index('year')['filings'].to_dict()
        ema = None
        best_year = None
        best_ema = None
        for y in years:
            x = float(m.get(y, 0))
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = y
        result_rows.append({'cpc4': cpc4, 'best_year': int(best_year), 'best_ema': float(best_ema)})
    res = pd.DataFrame(result_rows).sort_values(['best_ema','cpc4'], ascending=[False, True])

    # load cpc definitions mapping
    path_def = var_call_5aEisBYPQ6yDsb6qphu1gI8Y
    with open(path_def, 'r', encoding='utf-8') as f:
        defs = json.load(f)
    defmap = {}
    for d in defs:
        sym = d.get('symbol')
        if sym and sym not in defmap:
            defmap[sym] = d.get('titleFull')

    res['titleFull'] = res['cpc4'].map(defmap)
    # keep highest EMA per year? question: "technology areas ... with the highest EMA of filings each year".
    # We'll identify for each best_year, the cpc4 with highest best_ema among those whose best_year==year.
    top_by_year = res.sort_values(['best_year','best_ema'], ascending=[True, False]).groupby('best_year').head(1)
    out = top_by_year[['best_year','cpc4','titleFull','best_ema']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_jjtQBT3Y7R4oBATuyGZHFkyH': 'file_storage/call_jjtQBT3Y7R4oBATuyGZHFkyH.json', 'var_call_5aEisBYPQ6yDsb6qphu1gI8Y': 'file_storage/call_5aEisBYPQ6yDsb6qphu1gI8Y.json'}

exec(code, env_args)
