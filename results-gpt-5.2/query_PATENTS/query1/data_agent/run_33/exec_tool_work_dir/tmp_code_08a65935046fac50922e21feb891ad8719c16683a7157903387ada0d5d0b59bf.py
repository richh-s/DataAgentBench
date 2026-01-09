code = """import json, re
import pandas as pd

# Load publication rows (may be file path)
rows_src = var_call_iX6mlFAGBeGazZfzIDNBn3ad
if isinstance(rows_src, str):
    with open(rows_src, 'r', encoding='utf-8') as f:
        pub_rows = json.load(f)
else:
    pub_rows = rows_src

lvl5_src = var_call_ShrTPhMkj96kZbHCn5LsO4s9
if isinstance(lvl5_src, str):
    with open(lvl5_src, 'r', encoding='utf-8') as f:
        lvl5_rows = json.load(f)
else:
    lvl5_rows = lvl5_src

lvl5_set = set(r['symbol'] for r in lvl5_rows if r.get('symbol'))

# Helpers
month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19\d{2}|20\d{2})', s)
    return int(m.group(1)) if m else None

# parse CPC codes from JSON-like list; fallback regex
code_re = re.compile(r'"code"\s*:\s*"([A-Z]\d\d[A-Z]\d[^\"]*)"')

def parse_codes(cpc_str):
    if not cpc_str:
        return []
    # Try json
    try:
        data = json.loads(cpc_str)
        codes = []
        if isinstance(data, list):
            for it in data:
                if isinstance(it, dict) and 'code' in it and isinstance(it['code'], str):
                    codes.append(it['code'])
        return codes
    except Exception:
        return code_re.findall(cpc_str)

records = []
for r in pub_rows:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_codes(r.get('cpc'))
    if not codes:
        continue
    # unique per publication to avoid repeated codes within same record
    for c in set(codes):
        grp = c.split('/')[0]
        if grp in lvl5_set:
            records.append((grp, y))

df = pd.DataFrame(records, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='n')
    # complete years per symbol
    res = []
    alpha = 0.2
    for sym, g in counts.groupby('symbol'):
        g2 = g.sort_values('year')
        years = list(range(int(g2['year'].min()), int(g2['year'].max())+1))
        m = dict(zip(g2['year'], g2['n']))
        ema = None
        best_year = None
        best_ema = None
        for yr in years:
            x = float(m.get(yr, 0))
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            if (best_ema is None) or (ema > best_ema):
                best_ema = ema
                best_year = yr
        if best_year == 2022:
            res.append(sym)
    out = sorted(res)

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iX6mlFAGBeGazZfzIDNBn3ad': 'file_storage/call_iX6mlFAGBeGazZfzIDNBn3ad.json', 'var_call_ShrTPhMkj96kZbHCn5LsO4s9': 'file_storage/call_ShrTPhMkj96kZbHCn5LsO4s9.json'}

exec(code, env_args)
