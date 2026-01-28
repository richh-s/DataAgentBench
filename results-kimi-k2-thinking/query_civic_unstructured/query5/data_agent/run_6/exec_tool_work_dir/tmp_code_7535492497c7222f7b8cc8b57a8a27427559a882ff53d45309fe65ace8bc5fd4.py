code = """import json, pandas as pd, re

# Load funding data
with open('/var/lib/docker/volumes/809e893b8de3cf52e4b0a2b282f5e0ca08f0f0c16f9a5b0e0bed6b2e5c8a4bf5/_data.json', 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Find disaster projects (FEMA, CalOES, CalJPIA)
pattern = r'\(FEMA|FEMA\b|\(CalOES|\(CalJPIA'
disaster_projects = funding_df[funding_df['Project_Name'].str.contains(pattern, case=False, na=False)]

# Find projects with 2022 in their names
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Load civic documents
def load_civic_docs():
    try:
        with open('/var/lib/docker/volumes/df8cf2ea2fa0e5d8e6c61ad7e3fb1e92b1a3c5e21d7b0d95c1f2c0b7b5a9b0c4/_data.json', 'r') as f:
            civic_docs = json.load(f)
        return civic_docs
    except:
        return None

# Analyze civic documents for additional 2022 disaster projects
civic_docs = load_civic_docs()
if civic_docs:
    additional_projects = []
    for doc in civic_docs:
        text = doc.get('text', '')
        if '2022' in text and any(indicator in text.lower() for indicator in ['fema', 'caloes', 'caljpia']):
            # Look for project names
            for _, proj in disaster_projects.iterrows():
                proj_name_clean = proj['Project_Name'].split('(')[0].strip()
                if len(proj_name_clean) > 8 and proj_name_clean.lower() in text.lower():
                    additional_projects.append(proj.to_dict())
    
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
