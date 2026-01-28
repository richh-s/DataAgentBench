code = """import json, re
# Load data from previous tool calls
data_path_cpc = var_call_YbY7DM7wImXuzhOIchcbO51h
data_path_pub = var_call_N0b91Hn5uZaQS2tLZuS3l9hW

# helper to load either list or file path
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cpc_defs = load_var(data_path_cpc)
pubs = load_var(data_path_pub)

# Build set and map for level-4 CPC symbols -> titleFull
level4_map = {rec['symbol']: rec.get('titleFull') for rec in cpc_defs}
level4_symbols = set(level4_map.keys())

# Month mapping for detection
months_h2 = set(['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december'])

# regex to find year
year_re = re.compile(r'(\d{4})')
# regex to find country code DE or word Germany
country_re = re.compile(r'\bDE\b|Germany', re.IGNORECASE)
# regex to find month names
month_names = ['jan','january','feb','february','mar','march','apr','april','may','jun','june','jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

# accumulate counts per group per filing year
from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    try:
        pat = rec.get('Patents_info','')
        gd = rec.get('grant_date','')
        fd = rec.get('filing_date','')
        # filter grant year 2019
        if '2019' not in gd:
            continue
        # check month in second half
        gd_l = gd.lower()
        month_found = None
        for m in month_names:
            if m in gd_l:
                month_found = m
                break
        if not month_found or month_found not in months_h2:
            continue
        # country filter Germany
        if not country_re.search(pat):
            continue
        # parse filing year
        m = year_re.search(fd or '')
        if not m:
            continue
        filing_year = int(m.group(1))
        # parse cpc codes (field is JSON-like string)
        cpc_field = rec.get('cpc','')
        try:
            cpcs = json.loads(cpc_field)
        except Exception:
            # sometimes already list
            cpcs = cpc_field if isinstance(cpc_field, list) else []
        for entry in cpcs:
            code = None
            if isinstance(entry, dict):
                code = entry.get('code')
            elif isinstance(entry, str):
                code = entry
            if not code or len(code) < 4:
                continue
            # normalize code
            code_clean = code.replace(' ', '')
            # extract level-4 group as first 4 chars
            group = code_clean[:4]
            # Only include if group exists in level4_symbols
            if group in level4_symbols:
                counts[group][filing_year] += 1
    except Exception:
        continue

# For each group compute EMA over sorted years with alpha=0.1
alpha = 0.1
results = []
for group, year_counts in counts.items():
    # build sorted years sequence
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema = None
    ema_by_year = {}
    for y in years:
        count = year_counts[y]
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max ema
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    title = level4_map.get(group)
    results.append({'cpc_group': group, 'titleFull': title, 'best_year': best_year})

# Sort results by cpc_group
results = sorted(results, key=lambda x: x['cpc_group'])

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_YbY7DM7wImXuzhOIchcbO51h': 'file_storage/call_YbY7DM7wImXuzhOIchcbO51h.json', 'var_call_N0b91Hn5uZaQS2tLZuS3l9hW': 'file_storage/call_N0b91Hn5uZaQS2tLZuS3l9hW.json'}

exec(code, env_args)
