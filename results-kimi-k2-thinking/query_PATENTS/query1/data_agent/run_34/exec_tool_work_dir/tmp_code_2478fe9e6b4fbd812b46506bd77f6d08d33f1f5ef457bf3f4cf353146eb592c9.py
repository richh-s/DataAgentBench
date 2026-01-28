code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_path = locals()['var_functions.query_db:66']
level5_path = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse and collect data
code_year_counts = {}
years_seen = set()
for row in cpc_data:
    pub_date = row.get('publication_date', '')
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
            years_seen.add(year)
        except:
            continue
    
    cpc_str = row.get('cpc', '')
    if cpc_str:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '')
                if code and len(code) >= 4:
                    level5_code = code[:4]
                    if level5_code in level5_symbols:
                        key = (level5_code, year)
                        code_year_counts[key] = code_year_counts.get(key, 0) + 1
        except:
            pass

print('Years in dataset:', sorted(years_seen))
print('Total year-code pairs:', len(code_year_counts))

# Count how many codes have data for each year
if code_year_counts:
    year_summary = {}
    for (code, year), count in code_year_counts.items():
        if year not in year_summary:
            year_summary[year] = {'codes': 0, 'total': 0}
        year_summary[year]['codes'] += 1
        year_summary[year]['total'] += count
    
    print('\nYear summary:')
    for year in sorted(year_summary.keys()):
        print(f"{year}: {year_summary[year]['codes']} codes, {year_summary[year]['total']} total filings")

# Check for 2022 specifically
has_2022 = any(year == 2022 for (_, year) in code_year_counts.keys())
print(f'\nData includes 2022: {has_2022}')

# Analyze codes that have data spanning multiple years
code_year_ranges = {}
for (code, year), count in code_year_counts.items():
    if code not in code_year_ranges:
        code_year_ranges[code] = []
    code_year_ranges[code].append(year)

multi_year_codes = {code: years for code, years in code_year_ranges.items() if len(set(years)) >= 3}
print(f'\nCodes with data spanning 3+ years: {len(multi_year_codes)}')

# Find codes with 2022 data
codes_with_2022 = [code for (code, year) in code_year_counts.keys() if year == 2022]
print(f'Codes with 2022 data: {len(set(codes_with_2022))}')

# Check if any codes peaked in 2022 using simple max (not EMA)
max_year_codes = []
for code in multi_year_codes.keys():
    code_counts_by_year = {}
    for (c, y), count in code_year_counts.items():
        if c == code:
            code_counts_by_year[y] = count
    
    if len(code_counts_by_year) >= 3:
        max_year = max(code_counts_by_year.items(), key=lambda x: x[1])[0]
        if max_year == 2022:
            max_year_codes.append(code)

print(f'Codes with peak in 2022 (simple max): {len(max_year_codes)}')
if max_year_codes:
    print('Sample codes:', max_year_codes[:10])

# Now do EMA analysis with debug info
ema_2022_codes = []
detailed_results = []

for code in multi_year_codes.keys():
    code_counts_by_year = {}
    for (c, y), count in code_year_counts.items():
        if c == code:
            code_counts_by_year[y] = count
    
    if len(code_counts_by_year) >= 3:
        years = sorted(code_counts_by_year.keys())
        counts = [code_counts_by_year[y] for y in years]
        
        # Calculate EMA
        ema = pd.Series(counts).ewm(alpha=0.2, adjust=False).mean()
        best_year = years[ema.idxmax()]
        best_ema_val = float(ema.iloc[ema.idxmax()])
        
        detailed_results.append({
            'code': code,
            'years': years,
            'counts': counts,
            'best_year': best_year,
            'best_ema': best_ema_val
        })
        
        if best_year == 2022:
            ema_2022_codes.append(code)

results_df = pd.DataFrame(detailed_results)
print(f'\nTotal codes with EMA calculation: {len(results_df)}')

if len(results_df) > 0:
    print('Best year distribution:')
    print(results_df['best_year'].value_counts().sort_index())
    
    print(f'\nCodes with EMA best year 2022: {len(ema_2022_codes)}')
    if ema_2022_codes:
        print('Sample codes:', ema_2022_codes[:10])
else:
    print('No codes met the criteria for EMA analysis')

# Final result
final_result = json.dumps(sorted(ema_2022_codes))
print('__RESULT__:' + final_result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': [], 'var_functions.execute_python:86': []}

exec(code, env_args)
