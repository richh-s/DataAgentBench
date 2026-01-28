code = """import json, re, pandas as pd

# Load data from storage-provided file paths
path_pub = var_call_tKIU0nLtYU8KUaqSCKbnTWcZ
path_cpc = var_call_e48glC3FbHk3HPXi2zUZCmMq

with open(path_pub, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(path_cpc, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from 3-char symbol to titleFull
cpc_map = {row['symbol']: row.get('titleFull','') for row in cpc_defs}

# Helpers
month_map = {
    'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
    'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12
}

def extract_year(date_str):
    if not date_str or not isinstance(date_str,str):
        return None
    m = re.search(r'(20\d{2})', date_str)
    if m:
        return int(m.group(1))
    return None

def extract_month(date_str):
    if not date_str or not isinstance(date_str,str):
        return None
    s = date_str.lower()
    for k,v in month_map.items():
        if k in s:
            return v
    # try numeric month
    m = re.search(r'on (\d{1,2})/(\d{1,2})/(20\d{2})', date_str)
    if m:
        return int(m.group(2))
    return None

def is_germany(pat_info):
    if not pat_info or not isinstance(pat_info,str):
        return False
    s = pat_info
    # look for ' from DE' or ' in DE' or ' DE,' or ' DE ' or a DE- application id
    if re.search(r'\bDE\b', s):
        return True
    if re.search(r'DE[-_]', s):
        return True
    return False

# Filter patents: granted in second half of 2019 (months 7-12) and Germany
filtered = []
for rec in pubs:
    gd = rec.get('grant_date','')
    if not gd or '2019' not in gd:
        continue
    month = extract_month(gd)
    # if month unknown, try to see if 'July-December' words
    if month is None:
        if any(x in gd.lower() for x in ['jul','aug','sep','oct','nov','dec']):
            month = 7
    if month is None:
        # skip if cannot determine month
        continue
    if month < 7 or month > 12:
        continue
    if not is_germany(rec.get('Patents_info','')):
        continue
    # parse filing year
    fy = extract_year(rec.get('filing_date','') or '')
    if fy is None:
        # try to extract from Patents_info
        fy = extract_year(rec.get('Patents_info','') or '')
    # parse cpc codes
    cpc_field = rec.get('cpc')
    codes = []
    if cpc_field and isinstance(cpc_field,str):
        try:
            arr = json.loads(cpc_field)
            for it in arr:
                code = it.get('code') if isinstance(it,dict) else None
                if code and len(code) >= 3:
                    codes.append(code)
        except Exception:
            # try to find codes via regex
            codes += re.findall(r'\b[A-H][0-9]{2}[A-Z]?', cpc_field)
    filtered.append({'family_id':rec.get('family_id'), 'filing_year':fy, 'cpc_codes':codes})

# Build counts per group (3-char symbol) per year
from collections import defaultdict, Counter
counts = defaultdict(Counter)
for rec in filtered:
    fy = rec['filing_year']
    if fy is None:
        continue
    for code in rec['cpc_codes']:
        grp = code[:3]
        counts[grp][fy] += 1

# For each group, compute EMA across years (ascending) with alpha=0.1
alpha = 0.1
results = []
for grp, counter in counts.items():
    years = sorted(counter.keys())
    if not years:
        continue
    ema_vals = {}
    ema = None
    for y in years:
        val = counter[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1-alpha) * ema
        ema_vals[y] = ema
    # find year with max ema
    best_year = max(ema_vals.items(), key=lambda x: (x[1], -x[0]))[0]
    best_ema = ema_vals[best_year]
    results.append({'code': grp, 'titleFull': cpc_map.get(grp,''), 'best_year': int(best_year), 'best_ema': float(best_ema)})

# Sort results by best_ema desc
results = sorted(results, key=lambda x: x['best_ema'], reverse=True)

# Output results
print("__RESULT__:")
print(json.dumps(results, ensure_ascii=False))"""

env_args = {'var_call_6HiLfyHpkEuMpxypBsxKvczR': ['publicationinfo'], 'var_call_06hRIQ0UUW40Tg63gfOIGRmg': ['cpc_definition'], 'var_call_gyo560Shj3kL0VAUTtkXbqY7': 'file_storage/call_gyo560Shj3kL0VAUTtkXbqY7.json', 'var_call_e48glC3FbHk3HPXi2zUZCmMq': 'file_storage/call_e48glC3FbHk3HPXi2zUZCmMq.json', 'var_call_tKIU0nLtYU8KUaqSCKbnTWcZ': 'file_storage/call_tKIU0nLtYU8KUaqSCKbnTWcZ.json'}

exec(code, env_args)
