code = """import json

# Load data from storage-provided file paths
with open(var_call_OmRNX83dyGJw6pDYgfkBbK3G, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_pbbgtafowuKchytUxWpyKUzq, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping
cpc_map = {}
for rec in cpc_defs:
    sym = rec.get('symbol')
    if sym:
        cpc_map[sym] = rec.get('titleFull')

months_second_half = ['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

def is_germany(info):
    if not info:
        return False
    up = info.upper()
    if ' FROM DE' in up or ' DE,' in up or ' DE ' in up:
        return True
    if 'DE-' in up:
        return True
    toks = up.replace('(', ' ').replace(')', ' ').replace(',', ' ').split()
    if 'DE' in toks:
        return True
    return False

def extract_year(s):
    if not s:
        return None
    s = str(s)
    n = len(s)
    for i in range(n-3):
        sub = s[i:i+4]
        if sub.isdigit() and (sub.startswith('19') or sub.startswith('20')):
            return int(sub)
    return None

counts = {}
for rec in pubs:
    grant = rec.get('grant_date') or ''
    if '2019' not in str(grant):
        continue
    gl = str(grant).lower()
    if not any(m in gl for m in months_second_half):
        continue
    info = rec.get('Patents_info') or ''
    if not is_germany(info):
        continue
    filing = rec.get('filing_date') or ''
    filing_year = extract_year(filing)
    if filing_year is None:
        filing_year = extract_year(grant)
    if filing_year is None:
        continue
    cpc_field = rec.get('cpc') or '[]'
    cpcs = []
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cleaned = cpc_field.replace(chr(10), '').replace(chr(9), '')
            cpcs = json.loads(cleaned)
        except Exception:
            cpcs = []
    groups = set()
    for ce in cpcs:
        code = ''
        if isinstance(ce, dict):
            code = (ce.get('code') or '').upper()
        else:
            code = str(ce).upper()
        if len(code) >= 3 and code[0].isalpha() and code[1].isdigit() and code[2].isdigit():
            groups.add(code[0:3])
        elif len(code) >= 2 and code[0].isalpha():
            groups.add(code[0:2])
    for g in groups:
        counts.setdefault(g, {})
        counts[g][filing_year] = counts[g].get(filing_year, 0) + 1

# EMA
alpha = 0.1
results = []
for g, yc in counts.items():
    years = sorted(yc.keys())
    ema = None
    emas = {}
    for y in years:
        x = float(yc[y])
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1 - alpha) * ema
        emas[y] = ema
    if not emas:
        continue
    best_year = max(emas.items(), key=lambda kv: kv[1])[0]
    max_ema = emas[best_year]
    results.append({'cpc_group': g, 'titleFull': cpc_map.get(g, ''), 'best_year': int(best_year), 'max_ema': round(float(max_ema),4)})

results_sorted = sorted(results, key=lambda r: r['max_ema'], reverse=True)
output = results_sorted[:10]

print('__RESULT__:')
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_call_pbbgtafowuKchytUxWpyKUzq': 'file_storage/call_pbbgtafowuKchytUxWpyKUzq.json', 'var_call_OmRNX83dyGJw6pDYgfkBbK3G': 'file_storage/call_OmRNX83dyGJw6pDYgfkBbK3G.json', 'var_call_iCnKIL1O8gjM4A04H9k1tjMD': 'ok'}

exec(code, env_args)
