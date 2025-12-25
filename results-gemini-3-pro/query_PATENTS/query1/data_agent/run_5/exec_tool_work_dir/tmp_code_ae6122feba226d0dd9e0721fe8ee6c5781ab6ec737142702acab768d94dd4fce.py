code = """import json
import pandas as pd
import re

# Load level 5 symbols
with open(locals()['var_function-call-5220002852052879670'], 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

# Load publication info
with open(locals()['var_function-call-3342335174744796923'], 'r') as f:
    pub_data = json.load(f)

print("Total records:", len(pub_data))
print("Sample level 5 symbols:", list(level5_symbols)[:5])

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

years = []
matched_codes_count = 0
records_with_code = 0

for i, entry in enumerate(pub_data[:1000]): # Check first 1000
    date_str = entry.get('filing_date')
    cpc_str = entry.get('cpc')
    
    y = extract_year(date_str)
    if y:
        years.append(y)
    
    if cpc_str:
        try:
            cpc_list = json.loads(cpc_str)
            found = False
            for item in cpc_list:
                code = item.get('code', '')
                if len(code) >= 4:
                    subclass = code[:4]
                    if subclass in level5_symbols:
                        matched_codes_count += 1
                        found = True
            if found:
                records_with_code += 1
        except:
            pass

print("Sample years extracted:", years[:20])
print("Matched codes count in first 1000:", matched_codes_count)
print("Records with at least one match in first 1000:", records_with_code)

# Check max year in full dataset
all_years = []
for entry in pub_data:
    y = extract_year(entry.get('filing_date'))
    if y:
        all_years.append(y)

if all_years:
    print("Min year:", min(all_years))
    print("Max year:", max(all_years))
else:
    print("No years extracted.")

print("__RESULT__:")
print("DEBUG_DONE")"""

env_args = {'var_function-call-6966994197956776721': 'file_storage/function-call-6966994197956776721.json', 'var_function-call-6966994197956777598': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-7852690627219261662': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-14140994627699433809': [{'count(*)': '277813'}], 'var_function-call-5220002852052879670': 'file_storage/function-call-5220002852052879670.json', 'var_function-call-3342335174744796923': 'file_storage/function-call-3342335174744796923.json', 'var_function-call-7004644481195674653': []}

exec(code, env_args)
