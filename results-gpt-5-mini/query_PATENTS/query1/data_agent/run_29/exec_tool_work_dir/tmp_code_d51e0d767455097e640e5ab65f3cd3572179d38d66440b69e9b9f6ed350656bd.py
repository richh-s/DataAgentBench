code = """import json
import re
from collections import defaultdict

# Load query results from storage variables
data_path = var_call_Lj3Bve0KkBwHnrcj4EEc0gN5
level5_path = var_call_F5YLadWqPOGKj5sHcECkNpOZ

def load_var(v):
    if isinstance(v, str):
        # it's a file path to a JSON file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

pub_rows = load_var(data_path)
level5_rows = load_var(level5_path)

# Extract set of level-5 symbols
level5_symbols = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Build counts per group per year
counts = defaultdict(int)
years_set = set()

for row in pub_rows:
    filing = row.get('filing_date') or ''
    # extract year
    m = re.search(r"(20\d{2}|19\d{2})", filing)
    if not m:
        continue
    year = int(m.group(0))
    years_set.add(year)
    cpc_text = row.get('cpc') or ''
    # parse cpc field (JSON-like)
    cpc_list = []
    try:
        cpc_list = json.loads(cpc_text)
    except Exception:
        try:
            # fallback: evaluate safely
            import ast
            cpc_list = ast.literal_eval(cpc_text)
        except Exception:
            cpc_list = []
    groups = set()
    for entry in cpc_list:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code or not isinstance(code, str):
            continue
        code = code.strip()
        if len(code) >= 4:
            group = code[:4]
            groups.add(group)
    # increment count once per group per patent
    for g in groups:
        counts[(g, year)] += 1

if not years_set:
    result = []
else:
    years = sorted(years_set)
    alpha = 0.2
    best_year_for_group = {}

    # consider only groups that are in level5_symbols
    groups_in_data = set(g for (g, y) in counts.keys())
    candidate_groups = sorted(groups_in_data & level5_symbols)

    for g in candidate_groups:
        # build time series across all years
        xs = [counts.get((g, y), 0) for y in years]
        # compute EMA
        ema_vals = []
        if xs:
            ema = xs[0]
            ema_vals.append(ema)
            for x in xs[1:]:
                ema = alpha * x + (1 - alpha) * ema
                ema_vals.append(ema)
        # find year with max EMA; in tie pick the latest year
        max_ema = None
        max_year = None
        for y, e in zip(years, ema_vals):
            if (max_ema is None) or (e > max_ema) or (e == max_ema and y > max_year):
                max_ema = e
                max_year = y
        if max_year is not None:
            best_year_for_group[g] = max_year

    # collect groups whose best year is 2022
    result = [g for g, y in best_year_for_group.items() if y == 2022]
    result.sort()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Lj3Bve0KkBwHnrcj4EEc0gN5': 'file_storage/call_Lj3Bve0KkBwHnrcj4EEc0gN5.json', 'var_call_F5YLadWqPOGKj5sHcECkNpOZ': 'file_storage/call_F5YLadWqPOGKj5sHcECkNpOZ.json'}

exec(code, env_args)
