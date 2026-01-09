code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_recs = load_records(var_call_4mA0UTp9dwV62J0V0EMQOlRP)
level5_recs = load_records(var_call_4svyWDOkDqjWCU6Wz1aF8Ulm)

level5_set = set(r['symbol'] for r in level5_recs if r.get('symbol'))

# parse year from natural language filing_date
months = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,
    'july':7,'august':8,'september':9,'october':10,'november':11,'december':12
}

year_re = re.compile(r'(19\d{2}|20\d{2})')

def extract_year(s):
    if not s:
        return None
    m = year_re.search(s)
    if m:
        y = int(m.group(1))
        if 1900 <= y <= 2100:
            return y
    return None

# extract CPC codes from JSON-like string

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for e in data:
            c = e.get('code') if isinstance(e, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex for code-like tokens
        return re.findall(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d+(?:/\d+)?)"', cpc_str)

rows = []
for r in pub_recs:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count each publication once per group per year
    groups = set()
    for c in codes:
        # group at level 5 corresponds to first 4 chars like H01M
        g = c[:4]
        if g in level5_set:
            groups.add(g)
    for g in groups:
        rows.append((g,y))

df = pd.DataFrame(rows, columns=['group','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['group','year']).reset_index(name='filings')
    # compute EMA per group over years
    alpha = 0.2
    res = []
    for g, sub in counts.sort_values(['group','year']).groupby('group', sort=False):
        sub = sub.sort_values('year')
        ema = None
        for _, row in sub.iterrows():
            x = float(row['filings'])
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            res.append({'group': g, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(res)
    # for each year find max ema among groups
    idx = ema_df.groupby('year')['ema'].idxmax()
    winners = ema_df.loc[idx, ['year','group','ema']].sort_values('year')
    # keep only those whose best year (winner year) is 2022
    out = sorted(winners[winners['year']==2022]['group'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4mA0UTp9dwV62J0V0EMQOlRP': 'file_storage/call_4mA0UTp9dwV62J0V0EMQOlRP.json', 'var_call_4svyWDOkDqjWCU6Wz1aF8Ulm': 'file_storage/call_4svyWDOkDqjWCU6Wz1aF8Ulm.json'}

exec(code, env_args)
