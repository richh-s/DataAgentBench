code = """import json
import re

level5_file_path = locals()['var_function-call-17141822990107305310']
patent_file_path = locals()['var_function-call-12961292587599410676']

with open(level5_file_path, 'r') as f:
    level5_data = json.load(f)
level5_codes = set()
for item in level5_data:
    if 'symbol' in item:
        level5_codes.add(item['symbol'])

with open(patent_file_path, 'r') as f:
    patent_data = json.load(f)

def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

years = set()
matched_codes_count = 0
sample_dates = []

for row in patent_data[:100]: # Check first 100
    f_date = row.get('filing_date')
    sample_dates.append((f_date, extract_year(f_date)))
    
for row in patent_data:
    y = extract_year(row.get('filing_date'))
    if y:
        years.add(y)
    
    cpc_json = row.get('cpc')
    if not cpc_json: continue
    try:
        cpc_list = json.loads(cpc_json)
        for entry in cpc_list:
            code = entry.get('code', '')
            if code[:4] in level5_codes: # simple check
                matched_codes_count += 1
    except:
        pass

print("__RESULT__:")
debug_info = {
    "min_year": min(years) if years else None,
    "max_year": max(years) if years else None,
    "matched_codes_sample_count": matched_codes_count,
    "sample_dates": sample_dates[:10],
    "level5_sample": list(level5_codes)[:5]
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16843621957294656966': 'file_storage/function-call-16843621957294656966.json', 'var_function-call-6909709033955517173': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-17141822990107305310': 'file_storage/function-call-17141822990107305310.json', 'var_function-call-12961292587599410676': 'file_storage/function-call-12961292587599410676.json', 'var_function-call-15227026791012080898': []}

exec(code, env_args)
