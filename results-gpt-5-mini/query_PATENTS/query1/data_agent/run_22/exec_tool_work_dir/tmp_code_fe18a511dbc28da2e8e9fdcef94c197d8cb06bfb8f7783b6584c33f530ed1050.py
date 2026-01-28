code = """import json
import re
import pandas as pd

# Load the stored results (they may be either lists or file paths)
# Keys from previous calls:
# var_call_rNEMBCty03tcI6f7C4gQat9u -> level 5 symbols (possibly a file path)
# var_call_HpuCT0oiO1VIEQqAb6wNltjq -> publication cpc and filing_date (possibly a file path)

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to json
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

level5_raw = load_var(var_call_rNEMBCty03tcI6f7C4gQat9u)
pub_raw = load_var(var_call_HpuCT0oiO1VIEQqAb6wNltjq)

# Extract level-5 symbols into a set
level5_symbols = set()
for item in level5_raw:
    sym = item.get('symbol')
    if sym:
        level5_symbols.add(sym.strip())

# Function to extract year from filing_date
year_re = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None

# Function to parse cpc field and extract codes

def extract_group_codes(cpc_text):
    # cpc_text expected to be a JSON array string
    codes = []
    if not cpc_text or not isinstance(cpc_text, str):
        return codes
    try:
        arr = json.loads(cpc_text)
        if isinstance(arr, list):
            for obj in arr:
                if isinstance(obj, dict) and 'code' in obj:
                    code = obj['code']
                    if code and isinstance(code, str):
                        # clean code
                        code = code.strip()
                        # take leading part before slash
                        lead = code.split('/')[0]
                        # try regex for pattern like A01B
                        m = re.match(r'^([A-Z]\d{2}[A-Z])', lead)
                        if m:
                            codes.append(m.group(1))
                        else:
                            # fallback: take up to first 4 chars alnum
                            cleaned = re.sub(r'[^A-Z0-9]', '', lead)
                            codes.append(cleaned[:4])
        return codes
    except Exception:
        # fallback: try to find code-like tokens via regex
        tokens = re.findall(r'([A-Z]\d{2}[A-Z])', cpc_text)
        return tokens

# Build counts per (group, year)
from collections import defaultdict
counts = defaultdict(int)
years_set = set()

for rec in pub_raw:
    cpc_text = rec.get('cpc')
    filing = rec.get('filing_date')
    y = extract_year(filing)
    if y is None:
        continue
    years_set.add(y)
    groups = extract_group_codes(cpc_text)
    for g in groups:
        if g: 
            counts[(g, y)] += 1

if not years_set:
    result = []
else:
    min_year = min(years_set)
    max_year = max(years_set)
    # Ensure we include up to 2022
    max_year = max(max_year, 2022)
    years = list(range(min_year, max_year+1))

    alpha = 0.2
    groups = sorted({g for (g,y) in counts.keys()})

    # Only consider groups that are in level5_symbols
    groups = [g for g in groups if g in level5_symbols]

    best_year_by_group = {}

    for g in groups:
        # build series of counts for each year
        series = [counts.get((g, y), 0) for y in years]
        # compute EMA
        ema_vals = []
        if len(series) == 0:
            continue
        ema = series[0]
        ema_vals.append(ema)
        for x in series[1:]:
            ema = alpha * x + (1 - alpha) * ema
            ema_vals.append(ema)
        # find year of max EMA
        max_idx = int(pd.Series(ema_vals).idxmax())
        best_year = years[max_idx]
        best_year_by_group[g] = best_year

    # select groups whose best year is 2022
    result = sorted([g for g,y in best_year_by_group.items() if y == 2022])

# Print result in required format
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rNEMBCty03tcI6f7C4gQat9u': 'file_storage/call_rNEMBCty03tcI6f7C4gQat9u.json', 'var_call_HpuCT0oiO1VIEQqAb6wNltjq': 'file_storage/call_HpuCT0oiO1VIEQqAb6wNltjq.json', 'var_call_KeEnwUm5YO3S0yxf74ZaPbmq': 'file_storage/call_KeEnwUm5YO3S0yxf74ZaPbmq.json'}

exec(code, env_args)
