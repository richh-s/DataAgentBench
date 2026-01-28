code = """import json
import pandas as pd
import numpy as np
from collections import defaultdict

# Read the counts data
df_counts = pd.read_csv('/tmp/level5_counts.csv')
print('Loaded {} records'.format(len(df_counts)))
print('Year range: {}-{}'.format(df_counts['year'].min(), df_counts['year'].max()))
print('Sample data:')
print(df_counts.head())

# Get all years and sort
df_counts = df_counts.sort_values(['level5_code', 'year'])
all_years = sorted(df_counts['year'].unique())
print('Total years in dataset:', len(all_years))

# Pivot to get counts per code per year
counts_pivot = df_counts.pivot(index='level5_code', columns='year', values='count')
counts_pivot = counts_pivot.fillna(0)
print('Pivot shape:', counts_pivot.shape)
print('Sample pivot:')
print(counts_pivot.head())

# Calculate EMA for each CPC code
alpha = 0.2

# Create a copy for EMA values
ema_df = counts_pivot.copy()

# For each CPC code (row), calculate EMA over years
for idx, row in counts_pivot.iterrows():
    ema = None
    for year in all_years:
        value = row[year]
        if ema is None:
            # First value - initialize EMA
            ema = value
        else:
            # EMA formula
            ema = alpha * value + (1 - alpha) * ema
        ema_df.loc[idx, year] = ema

print('EMA calculation complete')
print('Sample EMA:')
print(ema_df.head())

# For each year, rank codes by EMA
yearly_rankings = {}
for year in all_years:
    if year in ema_df.columns:
        # Get EMA values for this year
        year_ema = ema_df[year].sort_values(ascending=False)
        # Filter out zero EMA values
        year_ema = year_ema[year_ema > 0]
        yearly_rankings[year] = year_ema

# Save EMA data
ema_df.to_csv('/tmp/ema_data.csv')

print('Rankings calculated for years:', len(yearly_rankings))
print('Sample ranking for 2022:')
if 2022 in yearly_rankings:
    print(yearly_rankings[2022].head())

print('__RESULT__:')
print(json.dumps({
    'status': 'ema_calculated', 
    'years_processed': len(yearly_rankings),
    'unique_codes': len(ema_df.index)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'status': 'parsed', 'count': 2681388, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}]}, 'var_functions.execute_python:16': {'level5_records': 2533616, 'year_range': '1837-2024', 'unique_codes': 168648, 'combinations': 875100}}

exec(code, env_args)
