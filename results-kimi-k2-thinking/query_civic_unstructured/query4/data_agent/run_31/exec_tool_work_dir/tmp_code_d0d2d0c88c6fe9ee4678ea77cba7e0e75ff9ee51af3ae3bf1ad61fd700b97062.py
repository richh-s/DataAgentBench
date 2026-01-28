code = """import json
import pandas as pd
import re

# Load the data
funding_data = var_functions.query_db_14
all_docs = var_functions.query_db_2
filtered_docs = var_functions.query_db_16

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

spring_2022_projects = []

# Search for spring 2022 projects
for doc in filtered_docs:
    text = doc.get('text', '')
    
    # Find Spring 2022 mentions
    for match in re.finditer(r'Spring[^\n]{0,100}2022', text, re.IGNORECASE):
        context = text[max(0, match.start()-500):match.end()+200]
        
        # Check each funding project
        for _, row in funding_df.iterrows():
            proj_name = row['Project_Name']
            if proj_name[:50] in context:
                spring_2022_projects.append({
                    'name': proj_name,
                    'amount': row['Amount']
                })

# Remove duplicates
unique = {}
for proj in spring_2022_projects:
    if proj['name'] not in unique:
        unique[proj['name']] = proj

final = list(unique.values())
total_funding = sum(p['amount'] for p in final)

result = {
    'count': len(final),
    'funding': int(total_funding),
    'projects': final
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
