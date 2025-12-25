code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-9876044052458878502'], 'r') as f:
    pub_data = json.load(f)

# Load Level 5 symbols
with open(locals()['var_function-call-12401183994811719569'], 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

counts = {}
year_pattern = re.compile(r'(19|20)\d{2}')
code_pattern = re.compile(r'"code":\s*"([^"]+)"')

debug_matches = 0

for entry in pub_data:
    f_date = str(entry.get('filing_date', ''))
    cpc_str = entry.get('cpc', '')
    
    # Find all year candidates
    matches = year_pattern.findall(f_date)
    # matches will be list of tuples if groups are used in regex?
    # r'(19|20)\d{2}' has a capturing group. findall returns the group.
    # So it returns ['20', '20'] for 2019? No.
    # regex r'(?:19|20)\d{2}' is non-capturing group.
    # Or just r'[12]\d{3}' and check range.
    
    # Let's use a simpler regex
    years_found = re.findall(r'\d{4}', f_date)
    valid_year = None
    for y in years_found:
        yi = int(y)
        if 1900 <= yi <= 2024:
            valid_year = yi
            break
            
    if valid_year is None:
        continue
        
    debug_matches += 1
    
    # Process CPC
    found_codes = code_pattern.findall(cpc_str)
    unique_l5 = set()
    for c in found_codes:
        l5 = c[:4]
        if l5 in level5_symbols:
            unique_l5.add(l5)
            
    if valid_year not in counts:
        counts[valid_year] = {}
        
    for code in unique_l5:
        counts[valid_year][code] = counts[valid_year].get(code, 0) + 1

print(f"DEBUG: Processed {debug_matches} rows with valid years.")

if not counts:
    print("__RESULT__:")
    print("[]")
else:
    df = pd.DataFrame(counts).T.fillna(0).sort_index()
    ema_df = df.ewm(alpha=0.2, adjust=False).mean()
    best_years = ema_df.idxmax()
    target_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-12401183994811719569': 'file_storage/function-call-12401183994811719569.json', 'var_function-call-12401183994811719334': [{'COUNT(*)': '277813'}], 'var_function-call-12401183994811719099': 'file_storage/function-call-12401183994811719099.json', 'var_function-call-3975511198914497484': [{'level': '2.0', 'cnt': '9', 'min_len': '1', 'max_len': '1', 'example': 'A'}, {'level': '4.0', 'cnt': '137', 'min_len': '3', 'max_len': '3', 'example': 'A01'}, {'level': '5.0', 'cnt': '677', 'min_len': '4', 'max_len': '4', 'example': 'A01B'}, {'level': '7.0', 'cnt': '9816', 'min_len': '8', 'max_len': '11', 'example': 'A01B1/00'}, {'level': '8.0', 'cnt': '48384', 'min_len': '8', 'max_len': '14', 'example': 'A01B1/02'}, {'level': '9.0', 'cnt': '70250', 'min_len': '8', 'max_len': '15', 'example': 'A01B1/022'}, {'level': '10.0', 'cnt': '62585', 'min_len': '8', 'max_len': '15', 'example': 'A01B1/225'}, {'level': '11.0', 'cnt': '35084', 'min_len': '8', 'max_len': '15', 'example': 'A01B3/421'}, {'level': '12.0', 'cnt': '17632', 'min_len': '8', 'max_len': '15', 'example': 'A01B3/4215'}, {'level': '13.0', 'cnt': '8015', 'min_len': '8', 'max_len': '15', 'example': 'A01D2034/6843'}, {'level': '14.0', 'cnt': '3649', 'min_len': '8', 'max_len': '15', 'example': 'A01D2034/6825'}, {'level': '15.0', 'cnt': '1521', 'min_len': '8', 'max_len': '14', 'example': 'A47J31/4446'}, {'level': '16.0', 'cnt': '1223', 'min_len': '9', 'max_len': '14', 'example': 'A61B17/7028'}, {'level': '17.0', 'cnt': '720', 'min_len': '10', 'max_len': '14', 'example': 'A61K47/6823'}, {'level': '18.0', 'cnt': '485', 'min_len': '10', 'max_len': '14', 'example': 'G01N2333/96444'}, {'level': '19.0', 'cnt': '621', 'min_len': '12', 'max_len': '14', 'example': 'H01L21/32137'}], 'var_function-call-9876044052458878502': 'file_storage/function-call-9876044052458878502.json', 'var_function-call-8898429705340347951': [], 'var_function-call-14045330639905495782': {'total_rows': 277813, 'dates_with_year_found': 0, 'min_year': None, 'max_year': None, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th'], 'unique_years': []}}

exec(code, env_args)
