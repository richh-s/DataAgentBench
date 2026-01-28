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
# month names
month_names = ['jan','january','feb','february','mar','march','apr','april','may','jun','june','jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    try:
        pat = rec.get('Patents_info','')
        gd = rec.get('grant_date','') or ''
        fd = rec.get('filing_date','') or ''
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
        m = year_re.search(fd)
        if not m:
            continue
        filing_year = int(m.group(1))
        # parse cpc codes (field is JSON-like string)
        cpc_field = rec.get('cpc','')
        try:
            cpcs = json.loads(cpc_field)
        except Exception:
            cpcs = cpc_field if isinstance(cpc_field, list) else []
        for entry in cpcs:
            code = None
            if isinstance(entry, dict):
                code = entry.get('code')
            elif isinstance(entry, str):
                code = entry
            if not code or len(code) < 3:
                continue
            code_clean = code.replace(' ', '')
            # extract level-4 group as first 3 characters (letter+2 digits)
            group = code_clean[:3]
            # ensure group matches pattern Letter + 2 digits
            if not re.match(r'^[A-Z]\d{2}$', group):
                # try alternative: first letter + two digits maybe with leading char
                # find first occurrence of letter+2digits
                m2 = re.search(r'[A-Z]\d{2}', code_clean)
                if m2:
                    group = m2.group(0)
                else:
                    continue
            if group in level4_symbols:
                counts[group][filing_year] += 1
    except Exception:
        continue

# For each group compute EMA over sorted years with alpha=0.1
alpha = 0.1
results = []
for group, year_counts in counts.items():
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
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    title = level4_map.get(group)
    results.append({'cpc_group': group, 'titleFull': title, 'best_year': best_year, 'year_counts': dict(year_counts)})

# Sort results by descending max EMA value
# compute max ema for sorting
sorted_results = []
for r in results:
    # recompute EMA to get max value
    years = sorted(r['year_counts'].keys())
    ema = None
    max_ema = -1
    for y in years:
        c = r['year_counts'][y]
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        if ema > max_ema:
            max_ema = ema
    r['max_ema'] = max_ema
    sorted_results.append(r)
sorted_results = sorted(sorted_results, key=lambda x: (-x['max_ema'], x['cpc_group']))

# Keep only requested fields
final = [{'cpc_group': r['cpc_group'], 'titleFull': r['titleFull'], 'best_year': r['best_year']} for r in sorted_results]

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_YbY7DM7wImXuzhOIchcbO51h': 'file_storage/call_YbY7DM7wImXuzhOIchcbO51h.json', 'var_call_N0b91Hn5uZaQS2tLZuS3l9hW': 'file_storage/call_N0b91Hn5uZaQS2tLZuS3l9hW.json', 'var_call_OSp9CHdVJaPAAwHzrsm7Aejv': [], 'var_call_JddkCUE50101O1nwLqegyxf9': {'counts_by_length': {'3': 137}, 'sample_symbols': ['B23', 'B30', 'B99', 'B29', 'B33', 'F28', 'A45', 'A24', 'A61', 'A63', 'A22', 'A42', 'A99', 'A43', 'A01', 'A62', 'A23', 'A47', 'A46', 'A44', 'A21', 'A41', 'B27', 'B68', 'B31', 'B26', 'B66', 'B02', 'B65', 'B61', 'B24', 'B06', 'B43', 'B62', 'B64', 'B22', 'B28', 'B09', 'B01', 'B63', 'B60', 'B44', 'B07', 'B08', 'B82', 'B42', 'B32', 'B81', 'B05', 'B41', 'B03', 'B67', 'C23', 'C06', 'C02', 'C07', 'C25', 'C30', 'C12', 'C99', 'C05', 'C40', 'C11', 'C08', 'C10', 'C21', 'C04', 'C09', 'C03', 'C13', 'C14', 'C01', 'D02', 'D21', 'D04', 'D07', 'D01', 'D10', 'D06', 'D03', 'D05', 'E05', 'E21', 'E04', 'E99', 'E06', 'E02', 'E01', 'E03', 'F41', 'F01', 'F22', 'F26', 'F04', 'F16', 'F05', 'F42', 'F03', 'F02', 'F23']}}

exec(code, env_args)
