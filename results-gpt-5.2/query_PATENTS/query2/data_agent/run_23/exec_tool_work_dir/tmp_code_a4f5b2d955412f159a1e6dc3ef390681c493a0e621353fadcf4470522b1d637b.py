code = """import json, re
import pandas as pd

# load records
path = var_call_vcOVAgHoyxakz68g1MceCiu1
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def is_de(patents_info):
    return bool(patents_info) and (' DE ' in (' ' + patents_info + ' ') or patents_info.strip().startswith('The DE ') or ' from DE' in patents_info or ', from DE' in patents_info)

def cpc_level4(code):
    if not code: return None
    code = code.strip()
    # remove spaces
    code = code.replace(' ', '')
    # take first 4 chars (section+class+subclass) and group digits before '/'
    m = re.match(r'^([A-HY]\d\d[A-Z])(\d+)?(?:/.*)?$', code)
    if not m: 
        return None
    prefix = m.group(1)
    grp = m.group(2) or ''
    return prefix + grp

rows=[]
for r in recs:
    if not is_de(r.get('Patents_info','')):
        continue
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    try:
        cpcs = json.loads(r.get('cpc') or '[]')
    except Exception:
        continue
    for e in cpcs:
        lv4 = cpc_level4(e.get('code'))
        if lv4:
            rows.append({'cpc4': lv4, 'year': y, 'rowid': r.get('rowid')})

df = pd.DataFrame(rows)
if df.empty:
    out = {'symbols': []}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

# count filings per year per cpc4 (unique rowid to avoid duplicates)
df = df.drop_duplicates(['cpc4','year','rowid'])
counts = df.groupby(['cpc4','year']).size().reset_index(name='n')

alpha = 0.1
best = []
for sym, g in counts.groupby('cpc4'):
    g = g.sort_values('year')
    ema = None
    best_year = None
    best_ema = None
    for _, row in g.iterrows():
        n = float(row['n'])
        year = int(row['year'])
        ema = n if ema is None else alpha*n + (1-alpha)*ema
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_year = year
    best.append({'symbol': sym, 'best_year': best_year, 'best_ema': best_ema})

best_df = pd.DataFrame(best).sort_values(['best_ema','symbol'], ascending=[False, True])
# keep those with highest ema; interpret as top (could be multiple ties)
max_ema = best_df['best_ema'].max()
leaders = best_df[best_df['best_ema'] == max_ema].copy()

out = {'max_ema': float(max_ema), 'leaders': leaders.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LGNwoYwFNT3vbRKKf6jzBG90': ['publicationinfo'], 'var_call_PaD7spDALVHLONxPexljNovY': ['cpc_definition'], 'var_call_vcOVAgHoyxakz68g1MceCiu1': 'file_storage/call_vcOVAgHoyxakz68g1MceCiu1.json'}

exec(code, env_args)
