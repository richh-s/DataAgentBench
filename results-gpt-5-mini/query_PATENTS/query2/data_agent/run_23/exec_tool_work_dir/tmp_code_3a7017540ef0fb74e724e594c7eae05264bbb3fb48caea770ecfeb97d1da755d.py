code = """import json, re
from collections import defaultdict

# Load large results from previous tool calls (file paths are stored in these variables)
with open(var_call_0lC1am3NJZ8EsQJn0BGEWOEL, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_fVK8SKf9SEDrsW892HcnLDfK, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping from level-4 symbol to titleFull
symbol_to_title = {item['symbol']: item.get('titleFull') for item in cpc_defs}

# Aggregate counts per level4 CPC group per filing year
counts = defaultdict(lambda: defaultdict(int))

for p in pubs:
    cpc_field = p.get('cpc') or '[]'
    # parse cpc field which is a JSON-string-like
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        import ast
        try:
            cpcs = ast.literal_eval(cpc_field)
        except Exception:
            cpcs = []
    # extract filing year (try filing_date, publication_date, grant_date)
    filing_date = p.get('filing_date') or p.get('publication_date') or p.get('grant_date') or ''
    m = re.search(r"(19|20)\d{2}", filing_date)
    if m:
        year = int(m.group(0))
    else:
        # fallback: try to find year in Patents_info
        m2 = re.search(r"(19|20)\d{2}", str(p.get('Patents_info','')))
        if m2:
            year = int(m2.group(0))
        else:
            continue
    # For each cpc code, map to level4 (letter + two digits)
    for entry in cpcs:
        code = None
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            # entry might be a string
            code = str(entry)
        if not code:
            continue
        code = code.strip().upper()
        m3 = re.match(r'^([A-Z]\d{2})', code)
        if m3:
            lvl4 = m3.group(1)
        else:
            # fallback to first 3 chars
            lvl4 = code[:3]
        counts[lvl4][year] += 1

# Compute EMA (alpha=0.1) across years for each lvl4 group and find best year (year with max EMA)
alpha = 0.1
results = []
for grp, year_counts in counts.items():
    # sort years
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    # initialize EMA with first year's count
    first_year = years[0]
    ema_prev = float(year_counts[first_year])
    ema_by_year[first_year] = ema_prev
    for y in years[1:]:
        c = float(year_counts[y])
        ema_curr = alpha * c + (1 - alpha) * ema_prev
        ema_by_year[y] = ema_curr
        ema_prev = ema_curr
    # find year with max EMA
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    max_ema = ema_by_year[best_year]
    results.append({
        'cpc_group': grp,
        'titleFull': symbol_to_title.get(grp),
        'best_year': int(best_year),
        'max_EMA': max_ema,
        'years_counted': {str(y): year_counts[y] for y in years}
    })

# Sort results by max_EMA descending
results_sorted = sorted(results, key=lambda x: x['max_EMA'], reverse=True)

# Output the results as JSON string
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_TTx4q0cnsQS5dfxTAjqT7zpu': ['publicationinfo'], 'var_call_Sm8x7BQnANlb143CVqlBRCSZ': ['cpc_definition'], 'var_call_fMmUmNi51YShZIgJXzeiae19': 'file_storage/call_fMmUmNi51YShZIgJXzeiae19.json', 'var_call_exqkfm1c0Qd52gEtxnBvzNC5': 'file_storage/call_exqkfm1c0Qd52gEtxnBvzNC5.json', 'var_call_0lC1am3NJZ8EsQJn0BGEWOEL': 'file_storage/call_0lC1am3NJZ8EsQJn0BGEWOEL.json', 'var_call_fVK8SKf9SEDrsW892HcnLDfK': 'file_storage/call_fVK8SKf9SEDrsW892HcnLDfK.json'}

exec(code, env_args)
