code = """import json
import pandas as pd

# Load the counts data 
df_counts = pd.read_csv('/tmp/level5_counts.csv')
print('Loaded {} records'.format(len(df_counts)))

# Focus on relevant years (let's say 2015-2024 for practical computation)
relevant_years = list(range(2015, 2025))
df_relevant = df_counts[df_counts['year'].isin(relevant_years)].copy()

print('Records for 2015-2024: {}'.format(len(df_relevant)))
print('Year breakdown:')
for year in relevant_years:
    count = len(df_relevant[df_relevant['year'] == year])
    print('  {}: {}'.format(year, count))

# Get counts per (code, year)
pivot_df = df_relevant.pivot_table(
    index='level5_code', 
    columns='year', 
    values='count', 
    fill_value=0
)
print('Pivot shape: {}'.format(pivot_df.shape))

# Calculate EMA for alpha=0.2
alpha = 0.2

# Initialize with zeros for all years in range
all_years = sorted(relevant_years)
ema_data = []

for code in pivot_df.index:
    row = pivot_df.loc[code]
    ema = None
    code_emas = {'level5_code': code}
    
    for year in all_years:
        value = row[year] if year in row else 0
        if ema is None:
            ema = value
        else:
            ema = alpha * value + (1 - alpha) * ema
        code_emas[year] = float(ema)
    
    ema_data.append(code_emas)

ema_df = pd.DataFrame(ema_data)
print('EMA calculation complete for {} codes'.format(len(ema_df)))

# Find best year for each code
best_year_info = []
for idx, row in ema_df.iterrows():
    code = row['level5_code']
    # Get EMAs for all years
    year_emas = {year: row[year] for year in all_years}
    # Find best year (max EMA)
    best_year = max(year_emas.keys(), key=lambda y: year_emas[y])
    best_ema = year_emas[best_year]
    
    best_year_info.append({
        'level5_code': code,
        'best_year': int(best_year),
        'best_ema': best_ema
    })

# Filter for codes where best year is 2022
codes_best_2022 = [info for info in best_year_info if info['best_year'] == 2022]

print('Total codes with best year 2022: {}'.format(len(codes_best_2022)))

# Sort by EMA and get top 100
codes_best_2022_sorted = sorted(codes_best_2022, key=lambda x: x['best_ema'], reverse=True)[:100]

result = [info['level5_code'] for info in codes_best_2022_sorted]

# Save full data
with open('/tmp/best_2022_codes.json', 'w') as f:
    json.dump(codes_best_2022_sorted, f, indent=2)

print('Top 10 codes:')
for i, code in enumerate(result[:10]):
    ema = codes_best_2022_sorted[i]['best_ema']
    print('  {} - EMA: {}'.format(code, ema))

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'status': 'parsed', 'count': 2681388, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}]}, 'var_functions.execute_python:16': {'level5_records': 2533616, 'year_range': '1837-2024', 'unique_codes': 168648, 'combinations': 875100}}

exec(code, env_args)
