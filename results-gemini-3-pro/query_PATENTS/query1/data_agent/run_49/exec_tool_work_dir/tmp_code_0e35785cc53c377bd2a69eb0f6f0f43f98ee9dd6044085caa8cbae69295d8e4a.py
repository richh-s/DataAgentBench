code = """import json
import re
import pandas as pd

# Get file paths
l5_file = locals()['var_function-call-5635872423012651359']
patents_file = locals()['var_function-call-3527882799012816558']

with open(l5_file, 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

with open(patents_file, 'r') as f:
    patents = json.load(f)

# Debug
years = []
matched_codes = 0
total_patents = len(patents)
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

sample_dates = []

for i, p in enumerate(patents):
    f_date = p.get('filing_date', '')
    if i < 10:
        sample_dates.append(f_date)
        
    match = year_pattern.search(f_date)
    if match:
        year = int(match.group(0))
        years.append(year)
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4 and code[:4] in level5_codes:
                matched_codes += 1
                break # count patent once
    except:
        pass

df_years = pd.DataFrame(years, columns=['year'])
print("__RESULT__:")
debug_info = {
    "total_patents": total_patents,
    "parsed_years_count": len(years),
    "min_year": int(df_years['year'].min()) if not df_years.empty else None,
    "max_year": int(df_years['year'].max()) if not df_years.empty else None,
    "patents_with_level5_match": matched_codes,
    "sample_dates": sample_dates
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-11333700863713924145': 'file_storage/function-call-11333700863713924145.json', 'var_function-call-11333700863713924824': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-5635872423012651359': 'file_storage/function-call-5635872423012651359.json', 'var_function-call-4292733715298409796': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-18005061453345551091': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'A41D', 'level': '5.0', 'titleFull': 'OUTERWEAR; PROTECTIVE GARMENTS; ACCESSORIES'}], 'var_function-call-5617066391461986581': [], 'var_function-call-2737902941994605580': [{'count(*)': '277813'}], 'var_function-call-3527882799012816558': 'file_storage/function-call-3527882799012816558.json', 'var_function-call-17578414695543921447': []}

exec(code, env_args)
