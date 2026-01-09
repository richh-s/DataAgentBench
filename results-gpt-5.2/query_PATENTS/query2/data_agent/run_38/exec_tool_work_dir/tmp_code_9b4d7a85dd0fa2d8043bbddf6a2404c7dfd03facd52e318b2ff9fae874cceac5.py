code = """import json, re
from datetime import datetime
import pandas as pd

# Load records (may be a filepath)
rec_source = var_call_T0yC7d9YpNuYksYj2b8qmIpM
if isinstance(rec_source, str):
    with open(rec_source, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = rec_source

month_map = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def is_h2_2019(grant):
    if not grant: return False
    y = parse_year(grant)
    if y != 2019: return False
    for mon in ['July','August','September','October','November','December']:
        if mon in grant:
            return True
    return False

def is_de(patents_info):
    if not patents_info: return False
    # look for explicit country_code DE or application starting with DE-
    if re.search(r'country_code\s*[:=]\s*DE', patents_info):
        return True
    if re.search(r'\bDE-\d', patents_info):
        return True
    return False

def extract_cpc4(cpc_str):
    if not cpc_str: return []
    try:
        arr = json.loads(cpc_str)
    except Exception:
        return []
    out=set()
    for o in arr if isinstance(arr,list) else []:
        code = o.get('code') if isinstance(o,dict) else None
        if not code or not isinstance(code,str):
            continue
        # remove spaces
        code = code.strip()
        # CPC level 4 approximated as subclass + main group (before '/') e.g., A61M1
        m = re.match(r'^([A-HY]\d{2}[A-Z]\d+)\s*/', code)
        if m:
            out.add(m.group(1))
    return sorted(out)

rows=[]
for r in records:
    if not (is_h2_2019(r.get('grant_date')) and is_de(r.get('Patents_info'))):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    for cpc4 in extract_cpc4(r.get('cpc')):
        rows.append({'cpc4': cpc4, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    result = []
    print('__RESULT__:')
    print(json.dumps(result))
    raise SystemExit

counts = df.groupby(['cpc4','filing_year']).size().reset_index(name='n').sort_values(['cpc4','filing_year'])

alpha=0.1
best_rows=[]
for cpc4, g in counts.groupby('cpc4'):
    g = g.sort_values('filing_year')
    ema=None
    best_year=None
    best_ema=None
    for _, row in g.iterrows():
        x = float(row['n'])
        if ema is None:
            ema = x
        else:
            ema = alpha*x + (1-alpha)*ema
        if (best_ema is None) or (ema > best_ema):
            best_ema = ema
            best_year = int(row['filing_year'])
    best_rows.append({'cpc4': cpc4, 'best_year': best_year, 'best_ema': best_ema})

best_df = pd.DataFrame(best_rows).sort_values(['best_ema','cpc4'], ascending=[False, True])
# take highest EMA groups (could be multiple). We'll return all tied for top EMA.
max_ema = best_df['best_ema'].max()
leaders = best_df[best_df['best_ema'] == max_ema].copy()

print('__RESULT__:')
print(json.dumps({'leaders': leaders.to_dict(orient='records'), 'max_ema': max_ema}))"""

env_args = {'var_call_3S22UBj8QVDMCsiJ3H4RzMVA': ['publicationinfo'], 'var_call_ZVYCqeilFQcAbaahWQpuOFk6': ['cpc_definition'], 'var_call_5UGm7dGNTbCHMbmHdcWLAO2S': [], 'var_call_T0yC7d9YpNuYksYj2b8qmIpM': 'file_storage/call_T0yC7d9YpNuYksYj2b8qmIpM.json'}

exec(code, env_args)
