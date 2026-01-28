code = """import json
import re
from collections import defaultdict

# Load all level 5 CPC symbols
level5_file = locals()['var_functions.query_db:12']
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

level5_symbols = set()
for item in level5_data:
    if item and 'symbol' in item:
        symbol = item['symbol'].strip()
        if len(symbol) <= 5 and symbol:
            level5_symbols.add(symbol)

print(f"Total Level 5 CPC symbols: {len(level5_symbols)}")
print("Sample:", sorted(list(level5_symbols))[:10])

# Load patent data
patents_file = locals()['var_functions.query_db:8']
with open(patents_file, 'r') as f:
    patents_data = json.load(f)

print(f"Total patent records: {len(patents_data)}")

# Process filings per year for each Level 5 group
yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_pattern = re.compile(r'"code":\s*"([^"]+)"')
year_pattern = re.compile(r'(\d{4})')

processed = 0
for record in patents_data:
    processed += 1
    if processed % 50000 == 0:
        print(f"Processed: {processed}")
    
    cpc_str = record.get('cpc', '')
    if not cpc_str:
        continue
    
    # Extract all CPC codes from this record
    cpc_codes = cpc_pattern.findall(cpc_str)
    
    # Extract year
    pub_date = record.get('publication_date', '')
    year_match = year_pattern.search(pub_date)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # For each CPC code, determine its Level 5 group
    for cpc_code in cpc_codes:
        # Remove any extra whitespace
        cpc_code = cpc_code.strip()
        
        # Extract main group portion
        if '/' in cpc_code:
            main_part = cpc_code.split('/')[0]
        else:
            main_part = cpc_code
        
        # Try to map to a Level 5 symbol
        # Level 5 symbols are typically 3-5 characters like A01B, H01M, C01B
        group_symbol = None
        
        # Direct match
        if main_part in level5_symbols:
            group_symbol = main_part
        else:
            # Try progressively shorter prefixes
            # For H01M10, try H01M, then H01, etc.
            for i in range(len(main_part)-1, 2, -1):
                prefix = main_part[:i]
                if prefix in level5_symbols:
                    group_symbol = prefix
                    break
        
        if group_symbol:
            yearly_counts[group_symbol][year] += 1

print(f"Processing complete. Found {len(yearly_counts)} Level 5 groups with filings.")

# Calculate EMA (α=0.2) for each group
alpha = 0.2
results = []

for group_symbol, year_data in yearly_counts.items():
    years = sorted(year_data.items())
    
    if len(years) < 2:
        continue
    
    # Calculate EMA values
    ema_values = {}
    first_year, first_count = years[0]
    ema = first_count
    ema_values[first_year] = ema
    
    for year, count in years[1:]:
        ema = alpha * count + (1 - alpha) * ema
        ema_values[year] = ema
    
    # Find year with highest EMA
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
    
    if best_year == 2022:
        results.append({
            'cpc_code': group_symbol,
            'ema_2022': round(ema_values[2022], 2),
            'total_years': len(years)
        })

print(f"Found {len(results)} Level 5 groups with best year 2022")

# Sort by EMA (highest first)
results.sort(key=lambda x: x['ema_2022'], reverse=True)

# Extract just the CPC codes
final_codes = [r['cpc_code'] for r in results]

# Remove duplicates (shouldn't be any, but just in case)
seen = set()
unique_codes = []
for code in final_codes:
    if code not in seen:
        seen.add(code)
        unique_codes.append(code)

print(f"Final unique codes: {len(unique_codes)}")
print("Top 10:", unique_codes[:10])

response = json.dumps(unique_codes)
print('__RESULT__:')
print(response)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': ['A01N', 'A01N', 'A01N', 'A01N', 'A01N', 'A01K', 'A01K', 'A01N', 'A01K', 'A01G', 'A01N', 'A01K', 'A01N', 'A01K', 'A01K', 'A01K', 'A01D', 'A01N', 'A01K', 'A01N', 'A01N', 'A01K', 'A01K', 'A01K', 'A01G', 'A01K', 'A01N', 'A01K', 'A01N', 'A01G', 'A01K', 'A01K', 'A01K', 'A01N', 'A01D', 'A01G', 'A01K', 'A01N', 'A01K', 'A01K', 'A01D', 'A01G', 'A01N', 'A01K', 'A01N', 'A01K', 'A01D', 'A01K', 'A01N', 'A01K', 'A01N', 'A01D', 'A01K', 'A01N', 'A01D', 'A01K', 'A01F', 'A01K', 'A01D', 'A01K', 'A01K', 'A01K', 'A01K', 'A01G', 'A01N', 'A01K', 'A01D', 'A01G', 'A01C', 'A01G', 'A01K', 'A01D', 'A01D', 'A01D', 'A01D', 'A01D', 'A01N'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': ['A61K'], 'var_functions.query_db:16': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}, {'publication_date': '30th of August, 2022'}, {'publication_date': '2nd August 2022'}, {'publication_date': 'Feb 8th, 2022'}, {'publication_date': '8th November 2022'}, {'publication_date': '2022, November 1st'}], 'var_functions.execute_python:20': ['H01L', 'A61K', 'G06F', 'A61B', 'H04L', 'H04W', 'H04N', 'A61P', 'G01N', 'B29C', 'G02B', 'C04B', 'C02F', 'C07C', 'C22C', 'C08K', 'A61L', 'B65D', 'B23K', 'G11C', 'B60L', 'C09D', 'H01R', 'E21B', 'C08F', 'B60R', 'B01L', 'C12Q', 'G05B', 'H04R', 'C09J', 'B22F', 'H05B', 'H01Q', 'C21D', 'G03F', 'A61H', 'H01F', 'B65H', 'F17C', 'G06K', 'F25B', 'F16C', 'B01F', 'C01P', 'F16K', 'C10G', 'F04D', 'G01J', 'F04B', 'B05B', 'H01G', 'G03B', 'B60G', 'A47J', 'B60T', 'B64C', 'H01B', 'A01G', 'H03M', 'C12M', 'G01B', 'C12Y', 'B64D', 'F15B', 'E05B', 'A43B', 'G07C', 'E04B', 'F16B', 'B05D', 'F16F', 'A61C', 'C10L', 'B60H', 'D06M', 'F04C', 'B64U', 'A61G', 'B82Y', 'G01F', 'A47B', 'A45D', 'G09F', 'B60Q', 'A41D', 'B63B', 'B02C', 'F26B', 'G01L', 'C30B', 'F03D', 'G09B', 'A47C', 'G16B', 'G01D', 'C07H', 'E04H', 'B05C', 'Y04S', 'G02C', 'F16J', 'B60B', 'B67D', 'B66C', 'B25B', 'H04S', 'B62K', 'B62B', 'D01F', 'E01C', 'E04C', 'B07B', 'B62J', 'A01B', 'C09C', 'G21C', 'G01P', 'F24D', 'B61L', 'D01D', 'D07B', 'A45F', 'F21W', 'F23G', 'B07C', 'E21D', 'F01M', 'B30B', 'F01K', 'E02B', 'E03F', 'F02K', 'G01G', 'A47F', 'C05F', 'A23B', 'H03L', 'E01D', 'H02N', 'B21J', 'B06B', 'C21C', 'C01F', 'D02G', 'B64F', 'B28D', 'E01B', 'A41B', 'A42B', 'G07G', 'A44C', 'B43K', 'B66D', 'C01D', 'G21K', 'C25C', 'B24C', 'C23G', 'B25H', 'F41G', 'B31F', 'F01C', 'A41C', 'B21F', 'F04F', 'C05C', 'A61D', 'A43D', 'C06B', 'B43L', 'F24T', 'B61G', 'B61H', 'C01C', 'A41H', 'A21B', 'B64B', 'F28G', 'B44F', 'B27G', 'B61K', 'B02B', 'B27C', 'F24V', 'C07G', 'A01L', 'G21H', 'B31C', 'D06Q', 'B21L', 'C12L']}

exec(code, env_args)
