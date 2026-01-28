code = """import json
import pandas as pd
import re

# Load the full dataset
with open('var_functions.query_db:5', 'r') as f:
    data = json.load(f)

print('Total records:', len(data))

# Parse CPC codes and extract years
parsed_data = []
for record in data:
    try:
        # Parse publication date
        date_str = record['publication_date']
        # Extract year using regex to handle formats like 'Aug 3rd, 2021'
        year_match = re.search(r'(\d{4})', date_str)
        if year_match:
            year = int(year_match.group(1))
        else:
            continue
            
        # Parse CPC codes (JSON string)
        cpc_str = record['cpc']
        if cpc_str and cpc_str != 'null' and cpc_str != '[]':
            try:
                cpc_list = json.loads(cpc_str)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code:
                        # Extract level 5 group (first part before / or .)
                        group_match = re.match(r'^([A-Z]\d{2}[A-Z])', code)
                        if group_match:
                            level5_group = group_match.group(1)
                            parsed_data.append({
                                'year': year,
                                'cpc_group': level5_group,
                                'full_code': code
                            })
            except json.JSONDecodeError:
                # Skip if CPC field is not valid JSON
                continue
    except Exception as e:
        continue

print('Parsed CPC group entries count:', len(parsed_data))

# Create DataFrame
df = pd.DataFrame(parsed_data)
if not df.empty:
    print('DataFrame shape:', df.shape)
    print('Year range:', df['year'].min(), 'to', df['year'].max())
    print('Number of unique CPC groups:', df['cpc_group'].nunique())
    print('Top CPC groups:')
    print(df['cpc_group'].value_counts().head())

# Count filings per group per year
if not df.empty:
    yearly_counts = df.groupby(['year', 'cpc_group']).size().reset_index(name='count')
    print('Yearly counts shape:', yearly_counts.shape)
    
    # Check year distribution
    year_dist = yearly_counts['year'].value_counts().sort_index()
    print('Year distribution:')
    print(year_dist.head(10))
    print('...')
    print(year_dist.tail(10))
    
    # Group by year and find top groups
    top_groups_by_year = {}
    for year in sorted(yearly_counts['year'].unique()):
        year_data = yearly_counts[yearly_counts['year'] == year]
        if not year_data.empty:
            top_group = year_data.loc[year_data['count'].idxmax()]
            top_groups_by_year[year] = {
                'cpc_group': top_group['cpc_group'],
                'count': int(top_group['count'])
            }
    
    print('Top groups by year:')
    for year in sorted(top_groups_by_year.keys()):
        print(year, ':', top_groups_by_year[year])

# Save data for further analysis
with open('parsed_data.json', 'w') as f:
    json.dump(parsed_data, f)

if not df.empty:
    yearly_counts.to_csv('yearly_counts.csv', index=False)

print('Data processing complete')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)
