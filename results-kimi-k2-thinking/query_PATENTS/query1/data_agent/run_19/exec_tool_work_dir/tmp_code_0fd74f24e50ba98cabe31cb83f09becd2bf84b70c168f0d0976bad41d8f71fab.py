code = """import json
import pandas as pd
import numpy as np

# Load the counts data
df_counts = pd.read_csv('/tmp/level5_counts.csv')
print('Loaded {} records'.format(len(df_counts)))

# Let's see unique years
unique_years = sorted(df_counts['year'].unique())
print('Years from {} to {}'.format(min(unique_years), max(unique_years)))
print('Total years:', len(unique_years))

# Check for 2022 specifically
print('Records for 2022:', len(df_counts[df_counts['year'] == 2022]))

# Let's get top codes by count for each year and save for EMA calculation
# This is more memory efficient
yearly_top_codes = {}

for year in unique_years:
    year_data = df_counts[df_counts['year'] == year]
    if len(year_data) > 0:
        # Sort by count descending and get top codes (say top 5000 per year for efficiency)
        top_codes = year_data.nlargest(5000, 'count')[['level5_code', 'count']]
        yearly_top_codes[year] = top_codes
        print('Year {}: {} records, top code: {} ({})'.format(
            year, len(year_data), 
            top_codes.iloc[0]['level5_code'] if len(top_codes) > 0 else 'N/A',
            top_codes.iloc[0]['count'] if len(top_codes) > 0 else 'N/A'
        ))

# Save this more manageable dataset
with open('/tmp/yearly_top_codes.json', 'w') as f:
    # Convert to serializable format
    serializable = {}
    for year, df in yearly_top_codes.items():
        serializable[str(year)] = df.to_dict('records')
    json.dump(serializable, f)

print('__RESULT__:')
print(json.dumps({
    'status': 'processed_by_year',
    'years': len(unique_years),
    'min_year': min(unique_years),
    'max_year': max(unique_years)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'status': 'parsed', 'count': 2681388, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}]}, 'var_functions.execute_python:16': {'level5_records': 2533616, 'year_range': '1837-2024', 'unique_codes': 168648, 'combinations': 875100}}

exec(code, env_args)
