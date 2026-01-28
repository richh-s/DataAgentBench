code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the full dataset
with open('var_functions.query_db:5', 'r') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")
print("Sample record:")
print(json.dumps(data[0], indent=2)[:500])

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

print(f"\nParsed {len(parsed_data)} CPC group entries")
if parsed_data:
    print("Sample parsed entries:")
    for i in range(min(3, len(parsed_data))):
        print(parsed_data[i])

# Create DataFrame
df = pd.DataFrame(parsed_data)
if not df.empty:
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Year range: {df['year'].min()} to {df['year'].max()}")
    print(f"Number of unique CPC groups: {df['cpc_group'].nunique()}")
    print("\nTop CPC groups:")
    print(df['cpc_group'].value_counts().head())

# Count filings per group per year
if not df.empty:
    yearly_counts = df.groupby(['year', 'cpc_group']).size().reset_index(name='count')
    print(f"\nYearly counts shape: {yearly_counts.shape}")
    print("Sample yearly counts:")
    print(yearly_counts.head(10))

    # Check if 2022 is in the data
    if 2022 in yearly_counts['year'].values:
        print(f"\n2022 data available: {yearly_counts[yearly_counts['year'] == 2022].shape[0]} groups")
    else:
        print("\n2022 data NOT FOUND in dataset")
        print(f"Available years: {sorted(yearly_counts['year'].unique())}")

# Save intermediate results
with open('parsed_data.json', 'w') as f:
    json.dump(parsed_data, f)

yearly_counts.to_csv('yearly_counts.csv', index=False)

print("\nData processing complete.")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)
