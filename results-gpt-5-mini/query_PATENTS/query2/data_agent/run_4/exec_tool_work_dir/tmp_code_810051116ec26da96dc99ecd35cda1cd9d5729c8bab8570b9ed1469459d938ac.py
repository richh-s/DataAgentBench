code = """import json, re
from collections import defaultdict

path = var_call_93nbrQx7BQWZpY6lcR3aUu1W
with open(path, 'r', encoding='utf-8') as f:
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

# build counts by group (level4) per year using grant_date year
counts = defaultdict(lambda: defaultdict(int))
years_set = set()

for rec in pubs:
    grant = rec.get('grant_date','') or ''
    year = extract_year(grant)
    if not year:
        # fallback to filing_date
        year = extract_year(rec.get('filing_date','') or '')
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
    for entry in cpcs:
        code = entry.get('code')
        if not code:
            continue
        code_norm = code.replace(' ', '')
        group = code_norm[:3]
        if group in level4_set:
            counts[group][year] += 1

# compute EMA per group across years range
if not years_set:
    results = []
else:
    years = list(range(min(years_set), max(years_set)+1))
    alpha = 0.1
    results = []
    for group, yc in counts.items():
        series = [yc.get(y,0) for y in years]
        if not any(series):
            continue
        ema = series[0]
        ema_vals = [ema]
        for x in series[1:]:
            ema = alpha * x + (1 - alpha) * ema
            ema_vals.append(ema)
        max_idx = max(range(len(ema_vals)), key=lambda i: ema_vals[i])
        best_year = years[max_idx]
        results.append({'symbol': group, 'titleFull': level4_map.get(group,''), 'best_year': best_year, 'max_ema': round(ema_vals[max_idx],3)})

results = sorted(results, key=lambda r: -r['max_ema'])

print('__RESULT__:')
print(json.dumps({'num_records': len(pubs), 'years_covered': sorted(list(years_set)), 'results': results}))"""

env_args = {'var_call_T6EVN0wa6vXygggLELsEzSqf': 'file_storage/call_T6EVN0wa6vXygggLELsEzSqf.json', 'var_call_m1Hpssfn6VXXHXhXmjgyXmHg': 'file_storage/call_m1Hpssfn6VXXHXhXmjgyXmHg.json', 'var_call_iCbx0nyULprDUxHZEIFTb9kJ': [], 'var_call_ABeRRIOm5CmvsmZQcYRzkK9j': {'num_records_sampled': 74, 'parsed_with_year_and_cpc': 0, 'years_found_sample': [], 'num_level4_symbols': 137, 'top_groups_sample': []}, 'var_call_AaU6OyCxPJeTVcXNDrAcJQ7c': {'total_records_sampled': 74, 'found_examples': {'DE': ['GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.'], '/DE': [], 'Germany': [], 'country_code': [], 'DE-': ['In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.']}, 'word_counts_sample': {}}, 'var_call_9zQ9GwG4xZVECv3m35cXtlly': {'matched_records': 21, 'years_covered': [], 'results': []}, 'var_call_93nbrQx7BQWZpY6lcR3aUu1W': 'file_storage/call_93nbrQx7BQWZpY6lcR3aUu1W.json'}

exec(code, env_args)
