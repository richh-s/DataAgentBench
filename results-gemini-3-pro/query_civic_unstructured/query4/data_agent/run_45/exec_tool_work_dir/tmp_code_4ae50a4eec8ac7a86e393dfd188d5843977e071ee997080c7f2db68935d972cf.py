code = """import json
import pandas as pd
import re

# Use the keys for the file paths
path_docs = locals()['var_function-call-11755073423388004543']
path_funding = locals()['var_function-call-11755073423388006536']

with open(path_docs, 'r') as f:
    docs = json.load(f)
with open(path_funding, 'r') as f:
    funding = json.load(f)

df_funding = pd.DataFrame(funding)
valid_projects = set(df_funding['Project_Name'].unique())

found_projects = []

# Regex patterns
# We look for lines containing "Start" or "Begin Construction" AND ("Spring" or "March" or "April" or "May") AND "2022"
pat_start = re.compile(r'(Start|Begin Construction)', re.IGNORECASE)
pat_time = re.compile(r'(Spring|March|April|May)', re.IGNORECASE)

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    current_proj = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Exact match for project name
        if line in valid_projects:
            current_proj = line
            continue
            
        if current_proj:
            # Check for start date criteria
            # Must have "Start" or "Begin Construction"
            # Must have "2022"
            # Must have "Spring" or relevant months
            if pat_start.search(line) and '2022' in line and pat_time.search(line):
                found_projects.append(current_proj)

unique_projects = list(set(found_projects))

# Calculate total funding
# Note: Funding amounts are strings in the JSON, need to convert to int
funding_subset = df_funding[df_funding['Project_Name'].isin(unique_projects)]
total_amount = funding_subset['Amount'].astype(int).sum()

print('__RESULT__:')
print(json.dumps({
    'count': len(unique_projects),
    'total_funding': int(total_amount),
    'projects': unique_projects
}))"""

env_args = {'var_function-call-11755073423388006536': 'file_storage/function-call-11755073423388006536.json', 'var_function-call-11755073423388004543': 'file_storage/function-call-11755073423388004543.json'}

exec(code, env_args)
