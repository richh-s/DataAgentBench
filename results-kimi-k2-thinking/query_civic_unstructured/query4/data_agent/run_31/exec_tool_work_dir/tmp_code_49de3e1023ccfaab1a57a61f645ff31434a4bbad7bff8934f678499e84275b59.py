code = """import json, pandas as pd

# Load the data
funding_data = var_functions.query_db_14
projects_2022 = var_functions.query_db_36

# Create DataFrame for funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Simple matching approach:
# Look for "Spring" and "2022" in the same document
# Then match project names that appear in that document

spring_2022_doc_projects = []

for doc in projects_2022:
    text = doc.get('text', '')
    
    # Check if this document mentions Spring and 2022
    if 'Spring' in text and '2022' in text:
        # For each funding project, check if its name appears in this document
        for _, row in funding_df.iterrows():
            proj_name = row['Project_Name']
            # Use a simple substring check on the project name
            if proj_name in text:
                spring_2022_doc_projects.append({
                    'name': proj_name,
                    'amount': row['Amount']
                })

# Remove duplicates
unique_projects = {}
for proj in spring_2022_doc_projects:
    unique_projects[proj['name']] = proj

final_projects = list(unique_projects.values())
total_count = len(final_projects)
total_funding = sum(p['amount'] for p in final_projects)

# Prepare result
result = {
    'project_count': total_count,
    'total_funding': int(total_funding),
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
