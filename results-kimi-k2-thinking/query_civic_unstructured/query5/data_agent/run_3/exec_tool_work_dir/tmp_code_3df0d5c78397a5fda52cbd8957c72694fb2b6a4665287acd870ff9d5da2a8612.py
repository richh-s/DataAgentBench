code = """import json
import pandas as pd
import re

# Load the data
civic_docs_data = locals()['var_functions.query_db:0']
funding_data = locals()['var_functions.query_db:2']

# Load from files if they're strings
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)
        
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert to DataFrames
df_civic = pd.DataFrame(civic_docs_data)
df_funding = pd.DataFrame(funding_data)

print('Documents:', len(df_civic))
print('Funding records:', len(df_funding))

# Simple extraction - look for disaster-related project names in the text
# First, let's see what disaster projects we have in funding
funding_disaster = df_funding[df_funding['Project_Name'].str.contains('(FEMA|CalOES|CalJPIA|Fire)', case=False, regex=True)]
print('\nDisaster-related funding records found:', len(funding_disaster))

# Create a list of unique disaster project names from funding
disaster_project_names = funding_disaster['Project_Name'].unique()
print('Sample disaster project names:', disaster_project_names[:10])

# Now let's check the civic documents for project mentions and dates
all_mentions = []

for _, doc in df_civic.iterrows():
    text = doc['text']
    
    # For each disaster project name, see if it appears in the document
    for proj_name in disaster_project_names:
        if proj_name in text:
            # Look for date mentions around the project
            # Search for year patterns (2020-2029) in the surrounding text
            nearby_text = text[max(0, text.find(proj_name)-200):min(len(text), text.find(proj_name)+200)]
            year_matches = re.findall(r'202[0-9]', nearby_text)
            
            all_mentions.append({
                'Project_Name': proj_name,
                'Years_Found': year_matches,
                'Doc_Filename': doc['filename']
            })

df_mentions = pd.DataFrame(all_mentions)

# Filter for projects with 2022
projects_2022 = df_mentions[df_mentions['Years_Found'].apply(lambda x: '2022' in x)]

print('\nProjects with 2022 mentions:', len(projects_2022))
unique_projects_2022 = projects_2022['Project_Name'].unique()
print('Unique disaster projects with 2022 mentions:', len(unique_projects_2022))

# Get funding for these projects
total_funding = 0
funded_projects = []

for proj in unique_projects_2022:
    proj_funding = funding_disaster[funding_disaster['Project_Name'] == proj]
    if not proj_funding.empty:
        amount = proj_funding['Amount'].astype(int).sum()
        total_funding += amount
        funded_projects.append({
            'Project_Name': proj,
            'Funding': amount
        })

print('\nTotal funding for disaster projects with 2022 mentions: $', total_funding)
print('Number of funded projects:', len(funded_projects))

result = {
    'total_funding': total_funding,
    'funded_projects': len(funded_projects),
    'disaster_projects_2022': len(unique_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'civic_docs_shape': [5, 3], 'funding_shape': [500, 4], 'civic_docs_columns': ['_id', 'filename', 'text'], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
