code = """import json
import pandas as pd
import re

# Load the data from the file path stored in the variable
file_path = var_functions.query_db:2
print(f"Loading data from: {file_path}")

with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Filter for German patents (DE in Patents_info)
german_patents = []
for record in data:
    if 'DE-' in record['Patents_info']:
        german_patents.append(record)

print(f"German patents found: {len(german_patents)}")

# Filter for second half of 2019 (July-December)
h2_2019_patents = []
for record in german_patents:
    grant_date_str = record['grant_date']
    if '2019' in grant_date_str:
        # Check for second half months
        h2_months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if any(month in grant_date_str for month in h2_months):
            h2_2019_patents.append(record)

print(f"German patents granted in H2 2019: {len(h2_2019_patents)}")

# Extract CPC codes
patent_data = []
for idx, record in enumerate(h2_2019_patents):
    cpc_json = record['cpc']
    if cpc_json and cpc_json != '[]':
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code:
                    patent_data.append({
                        'patent_index': idx,
                        'cpc_code': code,
                        'patents_info': record['Patents_info'],
                        'grant_date': record['grant_date']
                    })
        except:
            # Fallback for malformed JSON
            if '[{"code":' in cpc_json:
                codes = re.findall(r'"code":\s*"([^"]+)"', cpc_json)
                for code in codes:
                    patent_data.append({
                        'patent_index': idx,
                        'cpc_code': code,
                        'patents_info': record['Patents_info'],
                        'grant_date': record['grant_date']
                    })

print(f"CPC code entries extracted: {len(patent_data)}")

# Group by CPC group code (level 4)
cpc_groups = {}
for item in patent_data:
    code = item['cpc_code']
    # Take the group code (first 4 characters of the main class)
    group_code = code.split('/')[0][:4]
    
    if group_code not in cpc_groups:
        cpc_groups[group_code] = []
    cpc_groups[group_code].append(item)

print(f"Number of CPC groups: {len(cpc_groups)}")
print("Top CPC groups by volume:")
sorted_groups = sorted(cpc_groups.items(), key=lambda x: len(x[1]), reverse=True)
for group, items in sorted_groups[:20]:
    print(f"  {group}: {len(items)} patents")

# Prepare detailed results
detailed_results = []
for group_code, items in sorted_groups[:20]:
    detailed_results.append({
        'cpc_group': group_code,
        'patent_count': len(items),
        'sample_patents': [item['patents_info'][:100] + '...' for item in items[:3]]
    })

result = {
    'german_patents_h2_2019': len(h2_2019_patents),
    'total_cpc_entries': len(patent_data),
    'cpc_groups_count': len(cpc_groups),
    'top_groups': detailed_results
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
