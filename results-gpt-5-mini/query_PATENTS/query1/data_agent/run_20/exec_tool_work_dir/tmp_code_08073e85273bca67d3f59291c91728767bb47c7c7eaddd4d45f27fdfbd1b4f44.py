code = """import json
import re
from collections import defaultdict

# Load data
with open(var_call_m4GCke2KQvO6V0csBgBCc96I, 'r') as f:
    defs = json.load(f)

# Build level-5 symbol sets
level5_symbols = [rec['symbol'] for rec in defs if rec.get('symbol')]
sym_set = set(level5_symbols)
# create sets for 4-char and 3-char prefixes
pref4 = set(s for s in sym_set if len(s) >= 4)
pref3 = set(s for s in sym_set if len(s) >= 3)

# Regex for year and codes
year_re = re.compile(r"(19|20)\d{2}")
code_re = re.compile(r'"code"\s*:\s*"([^"]+)"')

group_year_counts = defaultdict(lambda: defaultdict(int))

# To avoid loading entire publications JSON into memory in one go (could be large),
# read the file and parse incrementally by finding occurrences of filing_date and cpc pairs.
# The file is a JSON list of objects; we'll use a regex to find each object. This is a bit hacky
# but faster than full json.loads for each cpc string.

with open(var_call_fMlECO7TIQUsXsbKDAsNfIoa, 'r') as f:
    data = f.read()

# Find all objects: split on '}, {' occurrences inside list - approximate
# Add braces to make valid JSON objects
objs = re.split(r'\},\s*\{', data.strip()[1:-1])  # remove leading [ and trailing ]

for obj_text in objs:
    # ensure braces
    if not obj_text.startswith('{'):
        obj_text = '{' + obj_text
    if not obj_text.endswith('}'):
        obj_text = obj_text + '}'
    # extract filing_date value
    m_fd = re.search(r'"filing_date"\s*:\s*"([^"]+)"', obj_text)
    if not m_fd:
        continue
    fd = m_fd.group(1)
    y_m = year_re.search(fd)
    if not y_m:
        continue
    year = int(y_m.group(0))
    # extract all codes
    codes = code_re.findall(obj_text)
    if not codes:
        continue
    matched_groups = set()
    for code in codes:
        code_norm = re.sub(r'[^A-Za-z0-9]', '', code)
        if len(code_norm) >= 4:
            k4 = code_norm[:4]
            if k4 in pref4:
                matched_groups.add(k4)
                continue
        if len(code_norm) >= 3:
            k3 = code_norm[:3]
            if k3 in pref3:
                matched_groups.add(k3)
                continue
    for g in matched_groups:
        group_year_counts[g][year] += 1

# Compute EMA and find groups with best year 2022
alpha = 0.2
groups_best_2022 = []
for g, yc in group_year_counts.items():
    years = sorted(yc.keys())
    if not years:
        continue
    miny, maxy = years[0], years[-1]
    prev_ema = None
    best_year = None
    best_ema = -1
    for y in range(miny, maxy+1):
        count = yc.get(y, 0)
        if prev_ema is None:
            ema = float(count)
        else:
            ema = alpha * count + (1 - alpha) * prev_ema
        prev_ema = ema
        # tie-breaker: prefer later year if equal
        if ema > best_ema or (ema == best_ema and (best_year is None or y > best_year)):
            best_ema = ema
            best_year = y
    if best_year == 2022:
        groups_best_2022.append(g)

groups_best_2022_sorted = sorted(groups_best_2022)

import json as _json
print("__RESULT__:")
print(_json.dumps(groups_best_2022_sorted))"""

env_args = {'var_call_fMlECO7TIQUsXsbKDAsNfIoa': 'file_storage/call_fMlECO7TIQUsXsbKDAsNfIoa.json', 'var_call_m4GCke2KQvO6V0csBgBCc96I': 'file_storage/call_m4GCke2KQvO6V0csBgBCc96I.json'}

exec(code, env_args)
