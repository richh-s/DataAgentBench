code = """import json, re, pandas as pd

# Load variables from storage
pub_path = var_call_MDlcivTJXFIfR2vKR26j59aM
cpcdef_path = var_call_5Gw88oI4JpttA2mAkVduidzd

# Helper to load either list or filepath
def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

publications = load_var(pub_path)
cpc_defs = load_var(cpcdef_path)

# Build set of level-5 symbols from cpc_defs
level5_symbols = set()
for r in cpc_defs:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Parse publications: extract year and cpc codes
year_code_counts = {}
all_years = set()

year_re = re.compile(r"(19|20)\\d{2}")
for rec in publications:
    filing = rec.get('filing_date')
    cpc_field = rec.get('cpc')
    if not filing or not cpc_field:
        continue
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    all_years.add(year)
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("\n", "").replace("\t", ""))
        except Exception:
            continue
    groups = set()
    for entry in cpcs:
        code = entry.get('code')
        if not code or len(code) < 4:
            continue
        grp = code[:4]
        groups.add(grp)
    if not groups:
        continue
    year_counts = year_code_counts.setdefault(year, {})
    for g in groups:
        year_counts[g] = year_counts.get(g, 0) + 1

if not year_code_counts:
    result = []
else:
    min_year = min(all_years)
    max_year = max(all_years)
    years = list(range(min_year, max_year+1))

    groups = set()
    for yc in year_code_counts.values():
        groups.update(yc.keys())
    groups = sorted([g for g in groups if g in level5_symbols])

    counts = {g: [] for g in groups}
    for y in years:
        yc = year_code_counts.get(y, {})
        for g in groups:
            counts[g].append(int(yc.get(g, 0)))

    alpha = 0.2
    best_year_by_group = {}
    for g in groups:
        series = counts[g]
        if not series:
            continue
        ema_values = []
        ema = series[0]
        ema_values.append(ema)
        for val in series[1:]:
            ema = alpha * val + (1 - alpha) * ema
            ema_values.append(ema)
        max_idx = max(range(len(ema_values)), key=lambda i: ema_values[i])
        best_year = years[max_idx]
        best_year_by_group[g] = best_year

    result = [g for g, y in best_year_by_group.items() if y == 2022]

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MDlcivTJXFIfR2vKR26j59aM': 'file_storage/call_MDlcivTJXFIfR2vKR26j59aM.json', 'var_call_5Gw88oI4JpttA2mAkVduidzd': 'file_storage/call_5Gw88oI4JpttA2mAkVduidzd.json'}

exec(code, env_args)
