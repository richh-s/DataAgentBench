code = """import json, pandas as pd

# Load funding data from the storage variable
funding_data = var_functions.query_db_36
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Find disaster projects (FEMA, CalOES, or CalJPIA in name)
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)
disaster_projects = funding_df[disaster_mask]

# Filter for projects with 2022 in their name
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Load civic documents to verify
civic_docs = var_functions.query_db_34

# Cross-reference for additional 2022 disaster projects
additional_projects = []
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and any(ind in text.lower() for ind in ['fema', 'caloes', 'caljpia']):
        # Look for matching project names
        for _, proj in disaster_projects.iterrows():
            clean_name = proj['Project_Name'].split('(')[0].strip()
            if len(clean_name) > 5 and clean_name.lower() in text.lower():
                additional_projects.append(proj.to_dict())

# Add any found projects and remove duplicates
if additional_projects:
    additional_df = pd.DataFrame(additional_projects).drop_duplicates()
    projects_2022 = pd.concat([projects_2022, additional_df]).drop_duplicates()

# Calculate totals
total_funding = projects_2022['Amount'].sum()
num_projects = len(projects_2022)

result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': projects_2022[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
