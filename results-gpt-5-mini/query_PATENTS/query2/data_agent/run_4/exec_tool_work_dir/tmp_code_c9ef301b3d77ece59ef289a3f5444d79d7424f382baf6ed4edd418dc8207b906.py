code = """import json, re

pub_path = var_call_T6EVN0wa6vXygggLELsEzSqf
with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

cpc_path = var_call_m1Hpssfn6VXXHXhXmjgyXmHg
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

level4_map = {row['symbol']: row.get('titleFull','') for row in cpc_defs}
level4_set = set(level4_map.keys())

year_re = re.compile(r"\b(19|20)\d{2}\b")

def extract_year(text):
    if not text:
        return None
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None

from collections import defaultdict
counts = defaultdict(lambda: defaultdict(int))
years_set = set()

parsed = 0
for i, rec in enumerate(pubs[:200]):
    filing = rec.get('filing_date','')
    year = extract_year(filing)
    if not year:
        continue
    years_set.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    parsed += 1
    for entry in cpcs[:5]:
        code = entry.get('code')
        if code:
            group = code.replace(' ','')[:3]
            # collect example
            if group in level4_set:
                counts[group][year] += 1

# collect top groups
top_groups = sorted([(g, sum(counts[g].values())) for g in counts], key=lambda x: -x[1])[:10]

res = {
    'num_records_sampled': min(200, len(pubs)),
    'parsed_with_year_and_cpc': parsed,
    'years_found_sample': sorted(list(years_set))[:10],
    'num_level4_symbols': len(level4_set),
    'top_groups_sample': top_groups,
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_T6EVN0wa6vXygggLELsEzSqf': 'file_storage/call_T6EVN0wa6vXygggLELsEzSqf.json', 'var_call_m1Hpssfn6VXXHXhXmjgyXmHg': 'file_storage/call_m1Hpssfn6VXXHXhXmjgyXmHg.json', 'var_call_iCbx0nyULprDUxHZEIFTb9kJ': []}

exec(code, env_args)
