code = """import json
import re
import pandas as pd

# Get the file path
file_path = locals()['var_functions.query_db:5']

# Read the publication data
with open(file_path, 'r') as f:
    pub_data = json.load(f)

# Parse CPC codes and extract years
records = []
for item in pub_data:
    cpc_json = item['cpc']
    pub_date = item['publication_date']
    
    # Extract year
    year_match = re.search(r'(\d{4})', pub_date)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    # Parse CPC codes - try multiple approaches
    try:
        # Clean and parse JSON
        clean_json = cpc_json.replace('\n', ' ').replace('\r', ' ')
        cpc_list = json.loads(clean_json)
        for cpc in cpc_list:
            if isinstance(cpc, dict) and 'code' in cpc:
                records.append({
                    'cpc_code': cpc['code'],
                    'year': year
                })
    except:
        # Regex fallback
        try:
            codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_json)
            for code in codes:
                records.append({
                    'cpc_code': code,
                    'year': year
                })
        except:
            continue

# Create DataFrame
df = pd.DataFrame(records)

# Group by CPC and year to get counts
yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')

# Save for later
yearly_counts_path = '/tmp/yearly_counts.json'
yearly_counts.to_json(yearly_counts_path, orient='records')

result = {
    'total_parsed_records': len(records),
    'unique_cpc_codes': int(df['cpc_code'].nunique()),
    'year_range': {
        'min': int(df['year'].min()),
        'max': int(df['year'].max())
    },
    'sample_counts': yearly_counts.head(10).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 'Successfully loaded 277813 records'}

exec(code, env_args)
