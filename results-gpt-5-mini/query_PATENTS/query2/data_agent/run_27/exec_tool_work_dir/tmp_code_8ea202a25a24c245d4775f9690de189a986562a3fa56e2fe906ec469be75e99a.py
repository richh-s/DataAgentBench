code = """import json
import re
import pandas as pd

# Load query results from storage variables
# var_call_mHTyVW2HlbcqEDchYWk8t8x3 and var_call_DrkprdjlxoYirsccbEiFXs0h are provided by the previous query_db calls

with open(var_call_mHTyVW2HlbcqEDchYWk8t8x3, 'r') as f:
    pub_records = json.load(f)

with open(var_call_DrkprdjlxoYirsccbEiFXs0h, 'r') as f:
    cpc_defs = json.load(f)

# Build mapping for level-4 symbols to titleFull
cpc_map = {r['symbol']: r.get('titleFull') for r in cpc_defs}

# Helper to detect Germany in Patents_info
country_token_re = re.compile(r"\b(DE|DE-|-DE|Germany|GERMANY|Federal Republic of Germany|Deutschland)\b", re.IGNORECASE)

def is_germany(patent_info):
    if not patent_info:
        return False
    return bool(country_token_re.search(patent_info))

# Helper to extract filing year
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(date_str):
    if not date_str:
        return None
    m = year_re.search(date_str)
    if m:
        return int(m.group(0))
    return None

# Helper to parse cpc JSON-like field to extract codes

def extract_cpc_codes(cpc_field):
    if not cpc_field:
        return []
    try:
        codes = []
        parsed = json.loads(cpc_field)
        for entry in parsed:
            code = entry.get('code')
            if code:
                codes.append(code)
        return codes
    except Exception:
        # fallback: find patterns like A61B5/6824 etc
        return re.findall(r"[A-Z][0-9]{2}[A-Z]?\S*", cpc_field)

# Process German patents granted in H2 2019
records = []
for r in pub_records:
    info = r.get('Patents_info','')
    if not is_germany(info):
        continue
    # include only those already filtered by grant_date in the query, but double-check month belongs to Jul-Dec
    # (we assume input already filtered)
    filing_year = extract_year(r.get('filing_date',''))
    if filing_year is None:
        continue
    cpc_list = extract_cpc_codes(r.get('cpc',''))
    records.append({'filing_year': filing_year, 'cpc_codes': cpc_list})

# Aggregate counts per level-4 group per year
# Level-4 group extraction: use leading pattern [A-Z][0-9]{2} (e.g., A61)

group_year_counts = {}
for rec in records:
    y = rec['filing_year']
    for code in rec['cpc_codes']:
        m = re.match(r'([A-Z][0-9]{2})', code)
        if not m:
            continue
        grp = m.group(1)
        group_year_counts.setdefault(grp, {})
        group_year_counts[grp][y] = group_year_counts[grp].get(y, 0) + 1

# For each group, compute EMA over years (sorted ascending) with alpha=0.1
alpha = 0.1
results = []
for grp, year_counts in group_year_counts.items():
    # create full sorted year list
    years = sorted(year_counts.keys())
    if not years:
        continue
    emas = {}
    ema = None
    for y in years:
        val = year_counts.get(y, 0)
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        emas[y] = ema
    # find year with highest EMA
    best_year = max(emas.items(), key=lambda x: x[1])[0]
    results.append({'cpc_group': grp, 'titleFull': cpc_map.get(grp), 'best_year': best_year})

# Sort results by cpc_group
results = sorted(results, key=lambda x: x['cpc_group'])

# Print according to required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_mHTyVW2HlbcqEDchYWk8t8x3': 'file_storage/call_mHTyVW2HlbcqEDchYWk8t8x3.json', 'var_call_DrkprdjlxoYirsccbEiFXs0h': 'file_storage/call_DrkprdjlxoYirsccbEiFXs0h.json'}

exec(code, env_args)
