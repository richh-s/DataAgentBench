code = """import json, re, pandas as pd

# Load results (may be a json file path)
raw = var_call_HEE0uTfggdQoTJPVL0IpCFKH
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = raw

def parse_year_from_nl_date(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def extract_country_code(info):
    if not info:
        return None
    m = re.search(r'\bfrom\s+([A-Z]{2})\b', info)
    if m:
        return m.group(1)
    m = re.search(r'\bThe\s+([A-Z]{2})\s+', info)
    if m:
        return m.group(1)
    m = re.search(r'\bcountry_code:\s*([A-Z]{2})\b', info)
    if m:
        return m.group(1)
    return None

def cpc_level4(code):
    if not code:
        return None
    code = code.strip()
    code = code.split(' ')[0]
    if '/' not in code:
        return code
    pre, post = code.split('/', 1)
    digits = ''.join(ch for ch in post if ch.isdigit())
    if len(digits) == 0:
        return pre
    lvl = digits[:4] if len(digits) >= 4 else digits
    return pre + '/' + lvl

rows=[]
for r in records:
    cc = extract_country_code(r.get('Patents_info'))
    if cc != 'DE':
        continue
    fy = parse_year_from_nl_date(r.get('filing_date'))
    if fy is None:
        continue
    try:
        cpcs = json.loads(r.get('cpc')) if r.get('cpc') else []
    except Exception:
        cpcs = []
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lvl4 = cpc_level4(code)
        if lvl4:
            rows.append({'lvl4': lvl4, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out = {'error':'No DE granted H2 2019 records with parsable filing_year/CPC.'}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

# count filings per year per lvl4
cnt = df.groupby(['lvl4','filing_year']).size().reset_index(name='filings').sort_values(['lvl4','filing_year'])

alpha = 0.1
# compute EMA per lvl4 over years
emas=[]
for lvl4, g in cnt.groupby('lvl4'):
    g = g.sort_values('filing_year')
    ema = None
    for _, row in g.iterrows():
        x = float(row['filings'])
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        emas.append({'lvl4': lvl4, 'filing_year': int(row['filing_year']), 'ema': float(ema), 'filings': int(row['filings'])})
ema_df = pd.DataFrame(emas)
# best year per lvl4 by max ema (tie -> earliest)
idx = ema_df.sort_values(['lvl4','ema','filing_year'], ascending=[True,False,True]).groupby('lvl4').head(1)
idx = idx.sort_values('ema', ascending=False)
# take highest areas (top 10)
top = idx.head(10).copy()
# output list and symbols for title lookup
out = {'top': top[['lvl4','filing_year','ema']].to_dict('records'), 'symbols': sorted(top['lvl4'].unique().tolist())}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KtpJrgGjCQAScV8aiuSnhhAo': ['publicationinfo'], 'var_call_PdaBkhXROFG7raA0T0FkaSFu': ['cpc_definition'], 'var_call_OWtkZbNyowygBowaTEKzrfvj': [], 'var_call_OlEoAyjMSjsS9CmUmq6pTKsO': 'file_storage/call_OlEoAyjMSjsS9CmUmq6pTKsO.json', 'var_call_HEE0uTfggdQoTJPVL0IpCFKH': 'file_storage/call_HEE0uTfggdQoTJPVL0IpCFKH.json'}

exec(code, env_args)
