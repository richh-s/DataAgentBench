code = """import json, re
import pandas as pd

# load publication records (possibly from file)
rec_src = var_call_igsbZ8Cf7piPHmiaVEBL2zuf
if isinstance(rec_src, str):
    with open(rec_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = rec_src

def parse_year(text):
    if not text: return None
    m = re.search(r'(19|20)\d{2}', text)
    return int(m.group(0)) if m else None

def grant_in_2h_2019(grant_text):
    # second half: Jul-Dec 2019
    if not grant_text: return False
    # quick check year
    if '2019' not in grant_text: 
        return False
    # normalize
    t = grant_text.strip().lower().replace(',', ' ')
    # month mapping
    months = {
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
        'dec':12,'december':12
    }
    # find month token
    mm = None
    for k,v in months.items():
        if re.search(r'\b'+re.escape(k)+r'\b', t):
            mm = v
            break
    if mm is None:
        # sometimes like "2019 on Jul 12th"; caught above; else can't parse
        return False
    return 7 <= mm <= 12

def is_germany(patents_info):
    if not patents_info: return False
    return bool(re.search(r'\bfrom\s+de\b', patents_info, flags=re.I) or re.search(r'\bIn\s+DE\b', patents_info, flags=re.I) or re.search(r'\bDE-\d', patents_info))

def extract_cpc_codes(cpc_text):
    if not cpc_text: return []
    try:
        arr = json.loads(cpc_text)
        codes = [x.get('code') for x in arr if isinstance(x, dict) and x.get('code')]
        return codes
    except Exception:
        # fallback regex
        return re.findall(r'"code"\s*:\s*"([A-Z]\d\d[A-Z]\d+\/\d+)"', cpc_text)

def to_level4(code):
    # CPC level 4 assumed like 'G06F' (section+class+subclass)
    if not code or len(code) < 4: return None
    return code[:4]

# filter to patents granted in 2H2019 and Germany
filt = []
for r in pubs:
    if not is_germany(r.get('Patents_info')):
        continue
    if not grant_in_2h_2019(r.get('grant_date')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    codes = extract_cpc_codes(r.get('cpc'))
    lvl4s = {to_level4(c) for c in codes}
    lvl4s.discard(None)
    for g in lvl4s:
        filt.append({'group4': g, 'filing_year': fy})

df = pd.DataFrame(filt)
if df.empty:
    out = []
else:
    counts = df.groupby(['group4','filing_year']).size().reset_index(name='n').sort_values(['group4','filing_year'])
    # compute EMA alpha=0.1 per group across years present, but should include missing years with 0 between min and max
    res_rows = []
    alpha = 0.1
    for g, sub in counts.groupby('group4'):
        sub = sub.sort_values('filing_year')
        ymin, ymax = int(sub['filing_year'].min()), int(sub['filing_year'].max())
        year_index = pd.DataFrame({'filing_year': list(range(ymin, ymax+1))})
        sub2 = year_index.merge(sub, on='filing_year', how='left').fillna({'n':0})
        ema = None
        for _, row in sub2.iterrows():
            x = float(row['n'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            res_rows.append({'group4': g, 'filing_year': int(row['filing_year']), 'ema': float(ema), 'n': int(row['n'])})
    ema_df = pd.DataFrame(res_rows)
    # best year per group by highest EMA; tie -> latest year
    ema_df = ema_df.sort_values(['group4','ema','filing_year'], ascending=[True, False, False])
    best = ema_df.groupby('group4').head(1).copy()
    # join titles from CPC definition query (it returned empty); so query directly by symbols for these groups
    need_syms = best['group4'].unique().tolist()
    out = {'need_symbols': need_syms, 'best_records': best[['group4','filing_year','ema']].to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_igsbZ8Cf7piPHmiaVEBL2zuf': 'file_storage/call_igsbZ8Cf7piPHmiaVEBL2zuf.json', 'var_call_d8I31cB7VhXtiGaEwdAYVrQ0': []}

exec(code, env_args)
