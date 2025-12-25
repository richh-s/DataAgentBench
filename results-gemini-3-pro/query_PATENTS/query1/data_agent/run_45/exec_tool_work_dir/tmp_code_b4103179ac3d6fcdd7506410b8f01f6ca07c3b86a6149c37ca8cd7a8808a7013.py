code = """import json
import re

# Load level 5 symbols
with open(locals()['var_function-call-554775488917991620'], 'r') as f:
    cpc_def_data = json.load(f)
    
valid_level5 = set()
for item in cpc_def_data:
    if 'symbol' in item:
        valid_level5.add(item['symbol'])

# Load patent data
with open(locals()['var_function-call-4578472368250917218'], 'r') as f:
    patents = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Aggregation
counts = {}
all_years = set()
patents_processed = 0
patents_with_year = 0

for p in patents:
    patents_processed += 1
    # Extract Year
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    patents_with_year += 1
    
    # Extract CPC
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        candidate = code[:4]
        if candidate in valid_level5:
            patent_codes.add(candidate)
            
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

debug_info = {
    "patents_processed": patents_processed,
    "patents_with_year": patents_with_year,
    "min_year": min(all_years) if all_years else None,
    "max_year": max(all_years) if all_years else None,
    "total_codes_found": len(counts),
    "sample_counts": {k: counts[k] for k in list(counts.keys())[:2]} if counts else {}
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5429124950122687575': 'file_storage/function-call-5429124950122687575.json', 'var_function-call-5429124950122687372': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-2491700961690963414': [{'symbol': 'A01B59/00', 'level': '7.0'}, {'symbol': 'A01B19/00', 'level': '7.0'}, {'symbol': 'A01B35/00', 'level': '7.0'}, {'symbol': 'A01B13/00', 'level': '7.0'}, {'symbol': 'A01B67/00', 'level': '7.0'}, {'symbol': 'A01B76/00', 'level': '7.0'}, {'symbol': 'A01B37/00', 'level': '7.0'}, {'symbol': 'A01B47/00', 'level': '7.0'}, {'symbol': 'A01B79/00', 'level': '7.0'}, {'symbol': 'A01B23/00', 'level': '7.0'}], 'var_function-call-2505457230602989857': [{'level': '2.0', 'sample_symbol': 'A'}, {'level': '4.0', 'sample_symbol': 'A01'}, {'level': '5.0', 'sample_symbol': 'A01B'}, {'level': '7.0', 'sample_symbol': 'A01B1/00'}, {'level': '8.0', 'sample_symbol': 'A01B1/02'}, {'level': '9.0', 'sample_symbol': 'A01B1/022'}, {'level': '10.0', 'sample_symbol': 'A01B1/225'}, {'level': '11.0', 'sample_symbol': 'A01B3/421'}, {'level': '12.0', 'sample_symbol': 'A01B3/4215'}, {'level': '13.0', 'sample_symbol': 'A01D2034/6843'}, {'level': '14.0', 'sample_symbol': 'A01D2034/6825'}, {'level': '15.0', 'sample_symbol': 'A47J31/4446'}, {'level': '16.0', 'sample_symbol': 'A61B17/7028'}, {'level': '17.0', 'sample_symbol': 'A61K47/6823'}, {'level': '18.0', 'sample_symbol': 'G01N2333/96444'}, {'level': '19.0', 'sample_symbol': 'H01L21/32137'}], 'var_function-call-850820474688023751': [{'COUNT(*)': '277813'}], 'var_function-call-554775488917991620': 'file_storage/function-call-554775488917991620.json', 'var_function-call-4578472368250917218': 'file_storage/function-call-4578472368250917218.json', 'var_function-call-2135760982504745027': []}

exec(code, env_args)
