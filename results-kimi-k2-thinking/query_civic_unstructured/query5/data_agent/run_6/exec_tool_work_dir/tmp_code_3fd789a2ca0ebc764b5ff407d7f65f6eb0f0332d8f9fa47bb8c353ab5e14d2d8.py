code = """import json
import pandas as pd

# Load funding data from the correct path
with open('/tmp/tmpf4d6q2f3.json', 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify disaster projects
disaster_projects = funding_df[funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)]

# Find projects with 2022 explicitly mentioned in their names
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Load civic documents to enhance analysis
with open('/tmp/tmp2v7m_6l3.json', 'r') as f:
    civic_docs = json.load(f)

# Check if any other disaster projects mention 2022 in documents
additional_2022_projects = []
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and any(indicator in text.lower() for indicator in ['fema', 'caloes', 'caljpia']):
        # Look for project names that match our disaster projects
        for _, proj in disaster_projects.iterrows():
            proj_name_clean = proj['Project_Name'].replace('(FEMA Project)', '').replace('(CalOES Project)', '').replace('(CalJPIA Project)', '').strip()
            if len(proj_name_clean) > 10 and proj_name_clean.lower() in text.lower():
                additional_2022_projects.append(proj)

# Combine and deduplicate
if additional_2022_projects:
    additional_df = pd.DataFrame(additional_2022_projects)
    all_2022 = pd.concat([projects_2022, additional_df]).drop_duplicates()
else:
    all_2022 = projects_2022

# Calculate final totals
total_funding = all_2022['Amount'].sum()
num_projects = len(all_2022)

# Prepare result
result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': all_2022[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs']}

exec(code, env_args)
