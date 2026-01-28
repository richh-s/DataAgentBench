code = """import json
import pandas as pd
import re
from datetime import datetime
import os

# Read the previous results to understand the data scope
file_path = locals()['var_functions.query_db:12']
print('Loading full German patent data from:', file_path)

with open(file_path, 'r') as f:
    full_data = json.load(f)

print(f'Total German patent records: {len(full_data)}')

# Parse all German patents with grant dates
patent_records = []
for idx, record in enumerate(full_data):
    grant_date_str = record.get('grant_date', '')
    if not grant_date_str or grant_date_str == 'null':
        continue
    
    # Extract year from grant date
    year_match = re.search(r'(\d{4})', grant_date_str)
    if year_match:
        year = int(year_match.group(1))
        patent_records.append({
            'index': idx,
            'year': year,
            'grant_date': grant_date_str,
            'patents_info': record['Patents_info'],
            'cpc_json': record['cpc']
        })

print(f'Patents with valid grant dates: {len(patent_records)}')

# Extract CPC codes and count by year and group
cpc_year_data = []
year_range = {}

for record in patent_records:
    year = record['year']
    cpc_json = record['cpc_json']
    
    if cpc_json and cpc_json != '[]' and cpc_json != 'null':
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code and len(code) >= 4:
                    # Extract 4-character group code (CPC level 4)
                    group_code = code.split('/')[0][:4]
                    cpc_year_data.append({
                        'year': year,
                        'cpc_group': group_code,
                        'full_code': code
                    })
        except:
            # Fallback for malformed JSON
            if '[{"code":' in cpc_json:
                codes = re.findall(r'"code":\s*"([^"]+)"', cpc_json)
                for code in codes:
                    if len(code) >= 4:
                        group_code = code.split('/')[0][:4]
                        cpc_year_data.append({
                            'year': year,
                            'cpc_group': group_code,
                            'full_code': code
                        })

# Create DataFrame
df = pd.DataFrame(cpc_year_data)
print(f'Total CPC entries: {len(df)}')
print(f'Year range: {df["year"].min()} - {df["year"].max()}')
print(f'Unique CPC groups: {df["cpc_group"].nunique()}')

# Count patents by year and CPC group
cpc_counts = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')
print(f'Group-year combinations: {len(cpc_counts)}')

# Get top CPC groups by total volume
top_groups = df['cpc_group'].value_counts().head(20)
print('Top 20 CPC groups by total patents:')
for group, count in top_groups.items():
    print(f'  {group}: {count}')

# Calculate exponential moving average for each CPC group
smoothing_factor = 0.1
def calculate_ema(series, alpha=0.1):
    return series.ewm(alpha=alpha, adjust=False).mean()

# Process each CPC group
ema_results = []
yearly_data = {}

for cpc_group in top_groups.index:
    # Get data for this group
    group_data = cpc_counts[cpc_counts['cpc_group'] == cpc_group].copy()
    group_data = group_data.sort_values('year')
    
    # Calculate EMA
    if len(group_data) > 1:
        group_data['ema'] = calculate_ema(group_data['count'], smoothing_factor)
        
        # Find year with highest EMA
        max_ema_idx = group_data['ema'].idxmax()
        best_year = group_data.loc[max_ema_idx, 'year']
        max_ema_value = group_data.loc[max_ema_idx, 'ema']
        max_ema_count = group_data.loc[max_ema_idx, 'count']
        
        ema_results.append({
            'cpc_group': cpc_group,
            'total_patents': top_groups[cpc_group],
            'best_year': int(best_year),
            'best_year_count': int(max_ema_count),
            'best_year_ema': float(max_ema_value),
            'years_active': len(group_data)
        })
        
        # Store yearly data for detailed analysis
        yearly_data[cpc_group] = group_data.to_dict('records')

# Sort by EMA value
ema_results = sorted(ema_results, key=lambda x: x['best_year_ema'], reverse=True)

print(f'CPC groups with EMA calculated: {len(ema_results)}')

# Get CPC definitions for the top groups
cpc_groups_for_definitions = [result['cpc_group'] for result in ema_results[:20]]

result_summary = {
    'total_german_patents': len(patent_records),
    'total_cpc_entries': len(df),
    'unique_cpc_groups': df['cpc_group'].nunique(),
    'year_range': {'min': int(df['year'].min()), 'max': int(df['year'].max())},
    'top_groups_by_ema': ema_results[:20],
    'cpc_groups_needing_definitions': cpc_groups_for_definitions
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'german_patents_h2_2019': 34, 'total_cpc_entries': 313, 'cpc_groups_count': 62, 'top_50_cpc_groups': ['C04B', 'H04W', 'G02B', 'B29C', 'F02D', 'H04L', 'F02M', 'H01J', 'F02N', 'E02F', 'A61F', 'F23L', 'H01R', 'H01L', 'H02J', 'H03L', 'A43B', 'A61B', 'F16H', 'Y02T', 'F23B', 'G01M', 'H01F', 'F02P', 'H01H', 'G01L', 'B41F', 'F16C', 'F24B', 'B60K', 'F16D', 'B60N', 'F04B', 'Y02D', 'F05D', 'F01D', 'B62D', 'C09K', 'G01N', 'A61L', 'Y10T', 'G07C', 'G01F', 'F42B', 'F41H', 'G08B', 'G01D', 'B23K', 'B63B', 'B66C']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
