code = """import json

# Load data from storage-provided file paths
with open(var_call_OmRNX83dyGJw6pDYgfkBbK3G, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_pbbgtafowuKchytUxWpyKUzq, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from CPC symbol to titleFull
cpc_map = {}
for rec in cpc_defs:
    sym = rec.get('symbol')
    if sym:
        cpc_map[sym] = rec.get('titleFull')

# Define second-half month keywords
months_second_half = ["Jul","July","Aug","August","Sep","Sept","September","Oct","October","Nov","November","Dec","December"]

# Helper to detect Germany in Patents_info
def is_germany(info):
    if not info:
        return False
    info_up = info.upper()
    if " FROM DE" in info_up or " FROM DE," in info_up:
        return True
    if "DE-" in info_up:
        return True
    # tokens
    tokens = info_up.replace('(', ' ').replace(')', ' ').replace(',', ' ').split()
    if 'DE' in tokens:
        return True
    return False

# Helper to extract year from a date-like string by finding first 4-digit number starting with 19 or 20
def extract_year(s):
    if not s:
        return None
    for i in range(len(s)-3):
        sub = s[i:i+4]
        if (sub.startswith('19') or sub.startswith('20')) and sub.isdigit():
            return int(sub)
    return None

# Aggregate counts per CPC level-4 group by filing year
counts = {}
for rec in pubs:
    grant = rec.get('grant_date') or ''
    if '2019' not in grant:
        continue
    # check second half months
    gl = grant.lower()
    if not any(m.lower() in gl for m in months_second_half):
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

    # parse cpc field
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace('\n','').replace('\t',''))
        except Exception:
            cpcs = []

    groups = set()
    for ce in cpcs:
        code = ''
        if isinstance(ce, dict):
            code = (ce.get('code') or '').upper()
        else:
            code = str(ce).upper()
        # extract letter + two digits
        if len(code) >= 3 and code[0].isalpha() and code[1:3].isdigit():
            groups.add(code[0:3])
        elif len(code) >= 2 and code[0].isalpha():
            groups.add(code[0:2])

    for g in groups:
        counts.setdefault(g, {})
        counts[g][filing_year] = counts[g].get(filing_year, 0) + 1

# Compute EMA with alpha=0.1 and find best year per group
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

# Sort and take top 10
results_sorted = sorted(results, key=lambda r: r['max_ema'], reverse=True)
output = results_sorted[:10]

print("__RESULT__:")
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_call_pbbgtafowuKchytUxWpyKUzq': 'file_storage/call_pbbgtafowuKchytUxWpyKUzq.json', 'var_call_OmRNX83dyGJw6pDYgfkBbK3G': 'file_storage/call_OmRNX83dyGJw6pDYgfkBbK3G.json'}

exec(code, env_args)
