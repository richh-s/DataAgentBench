code = """import json
import pandas as pd
from datetime import datetime
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in cpc_level5_data)

# Load full publication data
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    full_publication_data = json.load(f)

print('Processing', len(full_publication_data), 'publication records')

# Function to extract year from natural language date
def extract_year(date_str):
    if not date_str or date_str == '':
        return None
    # Extract year from various formats like "March 5th, 2019" or "2019-03-05"
    year_match = re.search(r'(\d{4})', str(date_str))
    if year_match:
        return int(year_match.group(1))
    return None

# Parse CPC codes and extract filing years
cpc_year_list = []
for record in full_publication_data:
    filing_year = extract_year(record['filing_date'])
    if not filing_year:
        continue
    
    # Parse CPC JSON field
    try:
        cpc_entries = json.loads(record['cpc'])
    except:
        # Try to parse as is - appears to be a string representation of JSON
        cpc_str = record['cpc']
        if cpc_str and cpc_str.strip():
            # Try to extract codes using regex
            codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
            for code in codes:
                # Extract CPC group (first part before / or spaces)
                group = code.split('/')[0].split()[0]
                # Check if this group is at exactly level 5
                if group in level5_symbols:
                    cpc_year_list.append({
                        'cpc_group': group,
                        'year': filing_year
                    })
    else:
        # Successfully parsed JSON
        for entry in cpc_entries:
            code = entry.get('code', '')
            if code:
                group = code.split('/')[0].split()[0]
                if group in level5_symbols:
                    cpc_year_list.append({
                        'cpc_group': group,
                        'year': filing_year
                    })

print('Found', len(cpc_year_list), 'CPC group-year records')

# Create DataFrame
df = pd.DataFrame(cpc_year_list)

# Group by CPC group and year, count filings
yearly_counts = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')

print('Yearly counts sample:')
print(yearly_counts.head())

# Get all years in data
all_years = sorted(yearly_counts['year'].unique())
print('Year range:', min(all_years), 'to', max(all_years))

print('__RESULT__:')
print(json.dumps({
    'total_records': len(cpc_year_list),
    'cpc_groups': len(yearly_counts['cpc_group'].unique()),
    'years_range': f'{min(all_years)}-{max(all_years)}' if all_years else 'N/A'
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}}

exec(code, env_args)
