code = """import json
import re
from collections import Counter

# Load the query result - access via locals()
result_key = 'var_functions.query_db:2'
if result_key in locals():
    result_file = locals()[result_key]
    with open(result_file, 'r') as f:
        patents_data = json.load(f)
else:
    patents_data = []

print('Total patents loaded:', len(patents_data))

# Filter for Germany patents in H2 2019
german_patents = []
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc_data = patent.get('cpc', '')
    
    # Check for Germany patents
    if not patents_info or 'DE-' not in patents_info:
        continue
    
    # Parse grant date for month/year
    month = None
    year = None
    grant_date_lower = grant_date.lower()
    
    # Extract month and year
    for month_name, month_num in month_map.items():
        if month_name in grant_date_lower:
            month = month_num
            break
    
    if '2019' in grant_date:
        year = 2019
    
    # Check if second half of 2019
    if not (month and year == 2019 and month >= 7):
        continue
    
    # Parse CPC codes
    if not cpc_data or not cpc_data.strip():
        continue
    
    try:
        cpc_list = json.loads(cpc_data)
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code and '/' in code:
                main_class = code.split('/')[0]
                if len(main_class) >= 4:
                    group_4 = main_class[:4]
                    german_patents.append({
                        'patent_info': patents_info,
                        'cpc_code': code,
                        'cpc_group_4': group_4,
                        'grant_date': grant_date,
                        'month': month,
                        'year': year
                    })
    except:
        continue

print('German H2 2019 patents found:', len(german_patents))

# Count filings by CPC group (level 4)
group_counts = Counter([p['cpc_group_4'] for p in german_patents])
print('CPC groups (level 4) found:', len(group_counts))

# Get top groups
top_groups = group_counts.most_common(10)
print('Top 10 CPC groups:')
for group, count in top_groups:
    print(' ', group, ':', count)

# Prepare result
result = {
    'total_patents': len(german_patents),
    'total_groups': len(group_counts),
    'top_groups': [(g, c) for g, c in top_groups],
    'all_data': german_patents
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
