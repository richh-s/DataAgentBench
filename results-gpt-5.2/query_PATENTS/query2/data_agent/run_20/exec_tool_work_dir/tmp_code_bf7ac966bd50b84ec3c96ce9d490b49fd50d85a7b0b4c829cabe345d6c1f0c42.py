code = """import json, re
import pandas as pd

# Load publication records
pub_src = var_call_5e6SLUSrAbce5Dn6F7B5Juax
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

# CPC definitions (level 4, active)
defs = var_call_SShxqWuc6efuodI9ai6X8P90

def parse_nl_date_to_ymd(s):
    if not s:
        return None
    s0 = s.strip().lower()
    # common patterns: 'dated 5th march 2019', '29th march 2019', '21st of september, 2021', 'march the 18th, 2019'
    month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}
    # remove commas
    s0 = s0.replace(',', ' ')
    # normalize 'of'
    s0 = re.sub(r'\bthe\b', ' ', s0)
    s0 = re.sub(r'\bdated\b', ' ', s0)
    s0 = re.sub(r'\bof\b', ' ', s0)
    s0 = re.sub(r'\s+', ' ', s0).strip()

    # try: day month year
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+([a-z]+)\s+(\d{4})', s0)
    if m:
        d = int(m.group(1))
        mon = month_map.get(m.group(2))
        y = int(m.group(3))
        if mon:
            return f"{y:04d}-{mon:02d}-{d:02d}"
    # try: month day year
    m = re.search(r'([a-z]+)\s+(\d{1,2})(?:st|nd|rd|th)?\s+(\d{4})', s0)
    if m:
        mon = month_map.get(m.group(1))
        d = int(m.group(2))
        y = int(m.group(3))
        if mon:
            return f"{y:04d}-{mon:02d}-{d:02d}"
    return None

def extract_country_code(patents_info):
    if not patents_info:
        return None
    # look for 'country_code' patterns or publication/application IDs like 'DE-'
    m = re.search(r'country_code\s*[:=]\s*([A-Z]{2})', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\b(ID|application no\.|application no|application number)\s+([A-Z]{2})-', patents_info)
    if m:
        return m.group(2)
    m = re.search(r'\bpublication number\s+([A-Z]{2})-', patents_info)
    if m:
        return m.group(1)
    # fallback any token like 'DE-'
    m = re.search(r'\b([A-Z]{2})-', patents_info)
    return m.group(1) if m else None

def cpc_to_level4(code):
    if not code:
        return None
    code = code.strip()
    # remove spaces
    code = code.replace(' ', '')
    # Expect format like 'H01M10/0565' => level4 group 'H01M10/00'
    if '/' not in code:
        return None
    pre, suf = code.split('/', 1)
    # keep first 2 digits of subgroup; if missing, return pre + '/00'
    digits = re.match(r'(\d+)', suf)
    if not digits:
        return pre + '/00'
    d = digits.group(1)
    if len(d) >= 2:
        return pre + '/' + d[:2] + '00'
    elif len(d) == 1:
        return pre + '/' + d + '000'
    else:
        return pre + '/00'

a = 0.1

rows = []
for r in pubs:
    cc = extract_country_code(r.get('Patents_info'))
    if cc != 'DE':
        continue
    gd = parse_nl_date_to_ymd(r.get('grant_date'))
    if not gd:
        continue
    # second half 2019: 2019-07-01 to 2019-12-31
    if not ('2019-07-01' <= gd <= '2019-12-31'):
        continue
    fd = parse_nl_date_to_ymd(r.get('filing_date'))
    if not fd:
        continue
    year = int(fd[:4])
    cpc_field = r.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lvl4 = cpc_to_level4(code)
        if lvl4:
            rows.append((lvl4, year))

if not rows:
    out = []
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

_df = pd.DataFrame(rows, columns=['cpc4','year'])
counts = _df.groupby(['cpc4','year']).size().reset_index(name='filings')

# compute EMA per cpc4 over years
res = []
for cpc4, g in counts.groupby('cpc4'):
    g2 = g.sort_values('year').reset_index(drop=True)
    ema = None
    for _, row in g2.iterrows():
        y = int(row['year'])
        x = float(row['filings'])
        ema = x if ema is None else (a * x + (1-a) * ema)
        res.append({'cpc4': cpc4, 'year': y, 'ema': ema, 'filings': int(x)})
res_df = pd.DataFrame(res)

# best year per CPC4 by highest EMA (tie -> latest year)
best = res_df.sort_values(['cpc4','ema','year'], ascending=[True,False,False]).groupby('cpc4').head(1)

# get highest EMA each year across CPC4 (using best year entries? question: "highest EMA ... each year" for patents granted in H2 2019)
# Interpret as: within the filtered patent set, compute EMA over filing years per CPC4; then for each year, find CPC4 with maximum EMA.
# We'll compute per year maximum across all CPC4-year EMA points.
yearly_top = res_df.sort_values(['year','ema'], ascending=[True,False]).groupby('year').head(1)

# Map titles for CPC4
if defs is None:
    defs = []
def_df = pd.DataFrame(defs)
if not def_df.empty:
    def_df['symbol'] = def_df['symbol'].astype(str)
    title_map = dict(zip(def_df['symbol'], def_df['titleFull']))
else:
    title_map = {}

# Build output: for each year, top CPC4 with title; also include best year for that CPC group
best_map = {row.cpc4: {'best_year': int(row.year), 'best_year_ema': float(row.ema)} for row in best.itertuples(index=False)}

out = []
for row in yearly_top.itertuples(index=False):
    cpc4 = row.cpc4
    out.append({
        'year': int(row.year),
        'cpc_group_code_level4': cpc4,
        'titleFull': title_map.get(cpc4),
        'ema': float(row.ema),
        'best_year_for_cpc4': best_map.get(cpc4, {}).get('best_year'),
        'best_year_ema_for_cpc4': best_map.get(cpc4, {}).get('best_year_ema')
    })

out = sorted(out, key=lambda d: d['year'])

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_5e6SLUSrAbce5Dn6F7B5Juax': 'file_storage/call_5e6SLUSrAbce5Dn6F7B5Juax.json', 'var_call_SShxqWuc6efuodI9ai6X8P90': []}

exec(code, env_args)
