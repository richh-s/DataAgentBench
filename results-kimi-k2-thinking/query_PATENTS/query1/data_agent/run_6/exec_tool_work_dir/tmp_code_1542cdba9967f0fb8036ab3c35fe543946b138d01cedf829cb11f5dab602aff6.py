code = """import json
import pandas as pd
import re
import os

# Access the file path from the storage variable
file_path = locals()['var_functions.query_db:5']
print('File path:', file_path)
print('File exists:', os.path.exists(file_path))

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

print('Total records loaded:', len(data))

# Parse CPC codes and extract years
parsed_data = []
for record in data:
    try:
        date_str = record['publication_date']
        year_match = re.search(r'(\d{4})', date_str)
        if year_match:
            year = int(year_match.group(1))
        else:
            continue
            
        cpc_str = record['cpc']
        if cpc_str and cpc_str != 'null' and cpc_str != '[]':
            try:
                cpc_list = json.loads(cpc_str)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code:
                        group_match = re.match(r'^([A-Z]\d{2}[A-Z])', code)
                        if group_match:
                            level5_group = group_match.group(1)
                            parsed_data.append({
                                'year': year,
                                'cpc_group': level5_group,
                                'full_code': code
                            })
            except json.JSONDecodeError:
                continue
    except Exception:
        continue

print('Parsed CPC records:', len(parsed_data))

# Process in DataFrame
df = pd.DataFrame(parsed_data)
result_summary = {}

if not df.empty:
    # Convert numpy types to Python types
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    print('Year range:', min_year, 'to', max_year)
    print('Unique CPC groups:', int(df['cpc_group'].nunique()))
    
    # Count per year-group
    yearly_counts = df.groupby(['year', 'cpc_group']).size().reset_index(name='count')
    
    # For each year, find group with max count
    for year in sorted(yearly_counts['year'].unique()):
        year_data = yearly_counts[yearly_counts['year'] == year]
        if not year_data.empty:
            max_idx = year_data['count'].idxmax()
            top_group = year_data.loc[max_idx]
            result_summary[int(year)] = {
                'cpc_group': str(top_group['cpc_group']),
                'count': int(top_group['count'])
            }

# Print in required format with proper type conversion
output = {
    'total_records': int(len(data)),
    'parsed_records': int(len(parsed_data)),
    'year_range': [min_year, max_year] if not df.empty else None,
    'top_groups_by_year': result_summary
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)
