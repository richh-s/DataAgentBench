code = """import json
import re
from collections import defaultdict
import ast

# Load data from storage file paths
cpc_def_path = var_call_NZK8gMFRH4HXYS6XWz1H0NwT
pubs_path = var_call_TPDWK2Yf9jznugo6fm9cYgPB

with open(cpc_def_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)
with open(pubs_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

level5_symbols = set()
for r in cpc_defs:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Helper to extract year
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

# Counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pubs:
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None:
        continue
    all_years.add(year)
    if not cpc_field or not isinstance(cpc_field, str):
        continue
    # parse cpc json-like string
    cpcs = None
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            # Remove newlines and stray commas
            cleaned = cpc_field.replace('\n', ' ')
            cpcs = json.loads(cleaned)
        except Exception:
            try:
                cpcs = ast.literal_eval(cpc_field)
            except Exception:
                # try to locate all occurrences of "code": "..." via regex
                codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
                if codes:
                    cpcs = [{'code': c} for c in codes]
                else:
                    cpcs = []
    codes = set()
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        elif isinstance(entry, str):
            code = entry
        else:
            code = None
        if not code or not isinstance(code, str):
            continue
        sym = code[:4]
        codes.add(sym)
    for sym in codes:
        if sym in level5_symbols:
            counts[sym][year] += 1

result = []
if all_years:
    min_year = min(all_years)
    max_year = max(all_years)
    years_range = list(range(min_year, max_year+1))
    alpha = 0.2
    best_symbols = []
    for sym, year_counts in counts.items():
        series = [year_counts.get(y, 0) for y in years_range]
        if not series:
            continue
        emas = {}
        ema_prev = float(series[0])
        emas[years_range[0]] = ema_prev
        for i in range(1, len(series)):
            y = years_range[i]
            c = series[i]
            ema = alpha * c + (1 - alpha) * ema_prev
            emas[y] = float(ema)
            ema_prev = ema
        best_year = max(emas.items(), key=lambda kv: (kv[1], kv[0]))[0]
        if best_year == 2022:
            best_symbols.append(sym)
    result = sorted(best_symbols)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NZK8gMFRH4HXYS6XWz1H0NwT': 'file_storage/call_NZK8gMFRH4HXYS6XWz1H0NwT.json', 'var_call_TPDWK2Yf9jznugo6fm9cYgPB': 'file_storage/call_TPDWK2Yf9jznugo6fm9cYgPB.json'}

exec(code, env_args)
