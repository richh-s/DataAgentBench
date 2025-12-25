code = """import json
import re
import pandas as pd

# Load Level 5 symbols
with open(locals()['var_function-call-12401183994811719569'], 'r') as f:
    level5_data = json.load(f)

# Extract symbols into a set
level5_symbols = set(item['symbol'] for item in level5_data)

# Load Publication Info
with open(locals()['var_function-call-9876044052458878502'], 'r') as f:
    pub_data = json.load(f)

# Data structure to hold counts: {year: {code: count}}
counts = {}

# Regex for extracting year from filing_date
# "dated 5th March 2019", "March the 18th, 2019"
# Look for 4 digits at the end or near the end
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Regex for extracting code from cpc string
# "code": "C01B33/00"
code_pattern = re.compile(r'"code":\s*"([^"]+)"')

for entry in pub_data:
    f_date = entry.get('filing_date', '')
    cpc_str = entry.get('cpc', '')
    
    if not f_date or not cpc_str:
        continue
    
    # Extract year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract codes
    # We can use regex to find all codes in the string
    # Then truncate to 4 chars and check if in level5_symbols
    found_codes = code_pattern.findall(cpc_str)
    
    # Get unique level 5 codes for this patent
    unique_l5 = set()
    for c in found_codes:
        l5 = c[:4]
        if l5 in level5_symbols:
            unique_l5.add(l5)
    
    # Update counts
    if year not in counts:
        counts[year] = {}
    
    for code in unique_l5:
        counts[year][code] = counts[year].get(code, 0) + 1

# Convert to DataFrame
# Rows: Years, Columns: Codes
# Fill missing with 0
df = pd.DataFrame(counts).T.fillna(0).sort_index()

# Calculate EMA
# alpha = 0.2
# adjust = False (recursive)
ema_df = df.ewm(alpha=0.2, adjust=False).mean()

# Find best year for each code
best_years = ema_df.idxmax()

# Filter for codes where best year is 2022
target_codes = best_years[best_years == 2022].index.tolist()

print("__RESULT__:")
print(json.dumps(target_codes))"""

env_args = {'var_function-call-12401183994811719569': 'file_storage/function-call-12401183994811719569.json', 'var_function-call-12401183994811719334': [{'COUNT(*)': '277813'}], 'var_function-call-12401183994811719099': 'file_storage/function-call-12401183994811719099.json', 'var_function-call-3975511198914497484': [{'level': '2.0', 'cnt': '9', 'min_len': '1', 'max_len': '1', 'example': 'A'}, {'level': '4.0', 'cnt': '137', 'min_len': '3', 'max_len': '3', 'example': 'A01'}, {'level': '5.0', 'cnt': '677', 'min_len': '4', 'max_len': '4', 'example': 'A01B'}, {'level': '7.0', 'cnt': '9816', 'min_len': '8', 'max_len': '11', 'example': 'A01B1/00'}, {'level': '8.0', 'cnt': '48384', 'min_len': '8', 'max_len': '14', 'example': 'A01B1/02'}, {'level': '9.0', 'cnt': '70250', 'min_len': '8', 'max_len': '15', 'example': 'A01B1/022'}, {'level': '10.0', 'cnt': '62585', 'min_len': '8', 'max_len': '15', 'example': 'A01B1/225'}, {'level': '11.0', 'cnt': '35084', 'min_len': '8', 'max_len': '15', 'example': 'A01B3/421'}, {'level': '12.0', 'cnt': '17632', 'min_len': '8', 'max_len': '15', 'example': 'A01B3/4215'}, {'level': '13.0', 'cnt': '8015', 'min_len': '8', 'max_len': '15', 'example': 'A01D2034/6843'}, {'level': '14.0', 'cnt': '3649', 'min_len': '8', 'max_len': '15', 'example': 'A01D2034/6825'}, {'level': '15.0', 'cnt': '1521', 'min_len': '8', 'max_len': '14', 'example': 'A47J31/4446'}, {'level': '16.0', 'cnt': '1223', 'min_len': '9', 'max_len': '14', 'example': 'A61B17/7028'}, {'level': '17.0', 'cnt': '720', 'min_len': '10', 'max_len': '14', 'example': 'A61K47/6823'}, {'level': '18.0', 'cnt': '485', 'min_len': '10', 'max_len': '14', 'example': 'G01N2333/96444'}, {'level': '19.0', 'cnt': '621', 'min_len': '12', 'max_len': '14', 'example': 'H01L21/32137'}], 'var_function-call-9876044052458878502': 'file_storage/function-call-9876044052458878502.json'}

exec(code, env_args)
