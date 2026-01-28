code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import re
import os

# Read the CPC-year data
with open('/tmp/cpc_yearly_data.json', 'r') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)
print(f'Total CPC-year records: {len(df)}')
print(f'Date range: {df["year"].min()} to {df["year"].max()}')

# Count filings per CPC code per year
cpc_yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')
print(f'CPC-year combinations: {len(cpc_yearly_counts)}')

# Get all CPC codes and years
cpc_codes = cpc_yearly_counts['cpc_code'].unique()
years = sorted(cpc_yearly_counts['year'].unique())
print(f'Years: {years}')
print(f'CPC codes: {len(cpc_codes)}')

# Create complete matrix of CPC codes vs years
matrix = cpc_yearly_counts.pivot(index='cpc_code', columns='year', values='count')
matrix = matrix.fillna(0)

print(f'Matrix shape: {matrix.shape}')
print('Sample matrix:')
print(matrix.head())

# Calculate EMA for each CPC code
# EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
α = 0.2

ema_data = {}
for cpc_code in matrix.index:
    values = matrix.loc[cpc_code].values
    ema_values = []
    ema_prev = values[0]  # Initialize with first value
    
    for i, val in enumerate(values):
        if i == 0:
            ema_values.append(ema_prev)
        else:
            ema_current = α * val + (1-α) * ema_prev
            ema_values.append(ema_current)
            ema_prev = ema_current
    
    ema_data[cpc_code] = dict(zip(years, ema_values))

# Create EMA DataFrame
ema_df = pd.DataFrame.from_dict(ema_data, orient='index')
ema_df = ema_df[years]  # Ensure correct column order

print(f'EMA DataFrame shape: {ema_df.shape}')
print('Sample EMA values:')
print(ema_df.head())

# For each year, find CPC codes with highest EMA
# We'll identify top N for each year (let's use top 10% as threshold)
yearly_top_cpcs = {}
for year in years:
    # Get EMA values for this year
    year_ema = ema_df[year].sort_values(ascending=False)
    
    # Use top 10% or top 100, whichever is smaller
    top_n = min(100, max(1, int(len(year_ema) * 0.1)))
    top_cpcs = year_ema.head(top_n).index.tolist()
    yearly_top_cpcs[year] = set(top_cpcs)

print('Top CPCs per year:')
for year in years[-5:]:
    print(f'{year}: {len(yearly_top_cpcs[year])} CPCs')

# Save EMA data and top CPCs
with open('/tmp/ema_data.json', 'w') as f:
    json.dump(ema_data, f)

with open('/tmp/yearly_top_cpcs.json', 'w') as f:
    # Convert sets to lists for JSON serialization
    yearly_top_cpcs_serializable = {str(k): list(v) for k, v in yearly_top_cpcs.items()}
    json.dump(yearly_top_cpcs_serializable, f)

result = {
    'years': years,
    'cpc_codes': len(cpc_codes),
    'yearly_top_counts': {year: len(cpcs) for year, cpcs in yearly_top_cpcs.items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 277813, 'cpc_year_records': 2681388, 'unique_cpcs': 175852, 'sample_cpcs': ['Y10T29/23', 'B08B9/093', 'H03B5/30', 'F25B2313/0315', 'G05B9/02', 'A61C17/10', 'A23V2400/157', 'C02F11/06', 'G11C17/14', 'F23D2900/03081']}}

exec(code, env_args)
