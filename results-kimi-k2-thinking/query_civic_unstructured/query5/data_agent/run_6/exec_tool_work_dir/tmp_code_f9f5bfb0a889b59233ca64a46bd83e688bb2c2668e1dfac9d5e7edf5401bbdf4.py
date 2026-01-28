code = """import json, pandas as pd, os

# Check available files
files = os.listdir('data')
print('Available files:', files)

# Load funding data
funding_file = [f for f in files if 'funding' in f.lower()][0]
with open('data/' + funding_file, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Find disaster projects
pattern = r'\(FEMA Project\)|\(CalOES Project\)|\(CalJPIA Project\)|\(FEMA/CalOES Project\)'
disaster = funding_df['Project_Name'].str.contains(pattern, case=False, na=False)
disaster_projects = funding_df[disaster]

# Filter for 2022
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Load civic documents to verify
civic_file = [f for f in files if '694' in f or 'civic' in f.lower()][0]
with open('data/' + civic_file, 'r') as f:
    civic_docs = json.load(f)

# Cross-check for additional 2022 disaster projects
additional = []
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and any(ind in text.lower() for ind in ['fema', 'caloes', 'caljpia']):
        for _, proj in disaster_projects.iterrows():
            name = proj['Project_Name'].split('(')[0].strip()
            if name.lower() in text.lower():
                additional.append(proj)

if additional:
    additional_df = pd.DataFrame(additional).drop_duplicates()
    projects_2022 = pd.concat([projects_2022, additional_df]).drop_duplicates()

# Calculate results
total_funding = projects_2022['Amount'].sum()
num_projects = len(projects_2022)

result = {'total_funding': int(total_funding), 'num_projects': int(num_projects), 'projects': projects_2022[['Project_Name', 'Amount']].to_dict('records')}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
