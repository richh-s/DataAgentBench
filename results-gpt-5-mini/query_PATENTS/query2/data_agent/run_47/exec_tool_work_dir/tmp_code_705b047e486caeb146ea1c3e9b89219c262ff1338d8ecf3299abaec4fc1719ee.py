code = """import json, re
from collections import defaultdict

# Load the large query results from storage paths
with open(var_call_BEtHMiSCnZgFvMAc6kD4Z97T, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_JUgaMWaczdflMQid6h7euVxI, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from level-4 symbol to titleFull
symbol_to_title = {rec['symbol']: rec.get('titleFull', '') for rec in cpc_defs}

# Function to extract year from natural-language date
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        return int(m.group(0))
    return None

# Parse CPC codes and accumulate counts per level-4 group by filing year
counts = defaultdict(lambda: defaultdict(int))  # counts[group][year] = count

for rec in pubs:
    pat_info = rec.get('Patents_info','') or ''
    # ensure it's Germany - the query already filtered Patents_info LIKE '%DE%'
    filing_date = rec.get('filing_date') or rec.get('filingDate') or ''
    year = extract_year(filing_date)
    # if no filing year, skip
    if year is None:
        continue
    cpc_field = rec.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            cpc_list = []
    # For each cpc entry, extract code and level-4 group (first 3 chars: letter + two digits)
    seen_groups = set()
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        # remove leading/trailing whitespace
        code = code.strip()
        # level-4 symbol typically is first letter + two digits, e.g., 'A61', 'B30'
        # Extract letters+digits at start
        m = re.match(r'^([A-HJ-Z]\d{2})', code)
        if not m:
            # fallback: take first 3 chars
            group = code[:3]
        else:
            group = m.group(1)
        if group in seen_groups:
            continue
        seen_groups.add(group)
        counts[group][year] += 1

# Compute EMA per group across years and find best year (year with highest EMA value)
alpha = 0.1
results = []
for group, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        c = year_counts[y]
        if ema is None:
            ema = float(c)
        else:
            ema = alpha * float(c) + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda x: x[1])[0]
    peak_ema = ema_by_year[best_year]
    title = symbol_to_title.get(group, '')
    results.append({
        'cpc_group': group,
        'titleFull': title,
        'best_year': best_year,
        'peak_ema': peak_ema,
        'years_analyzed': years,
        'year_counts': {str(y): year_counts[y] for y in years}
    })

# Sort results by peak_ema descending
results_sorted = sorted(results, key=lambda x: x['peak_ema'], reverse=True)

# Prepare JSON-serializable output: limit to top 50 to keep output reasonable
out = results_sorted[:50]

print("__RESULT__:")
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_7AdAmwyKADwnLHil6uygTFOX': ['publicationinfo'], 'var_call_fYmm2RMw63KHR8rYi3dDVRMl': ['cpc_definition'], 'var_call_2KvNQuXF3rVNly2aS1mpAS0z': 'file_storage/call_2KvNQuXF3rVNly2aS1mpAS0z.json', 'var_call_JUgaMWaczdflMQid6h7euVxI': 'file_storage/call_JUgaMWaczdflMQid6h7euVxI.json', 'var_call_BEtHMiSCnZgFvMAc6kD4Z97T': 'file_storage/call_BEtHMiSCnZgFvMAc6kD4Z97T.json'}

exec(code, env_args)
