code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-10032448971430008742'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Convert Amount to int
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Create a set of valid project names
valid_projects = set(df_funding['Project_Name'].unique())

# Load civic docs
with open(locals()['var_function-call-17801199440429665660'], 'r') as f:
    civic_docs = json.load(f)

disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey', 'Disaster']

matched_projects = set()

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_section = 'Unknown'
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        if 'Capital Improvement Projects' in line_clean:
            current_section = 'Capital'
            current_project = None
            continue
        if 'Disaster Recovery Projects' in line_clean:
            current_section = 'Disaster'
            current_project = None
            continue
            
        # Check if line is a project name
        if line_clean in valid_projects:
            current_project = line_clean
            continue
        
        if current_project:
            # Check for start date
            lower_line = line_clean.lower()
            if 'begin construction' in lower_line or 'start date' in lower_line or 'st:' in lower_line:
                if '2022' in lower_line:
                    # Check for disaster
                    is_disaster = False
                    # Check keywords in name
                    if any(k in current_project for k in disaster_keywords):
                        is_disaster = True
                    # Check section
                    elif current_section == 'Disaster':
                        is_disaster = True
                    
                    if is_disaster:
                        matched_projects.add(current_project)
                        current_project = None

matched_names = list(matched_projects)

# Sum funding
total_funding = df_funding[df_funding['Project_Name'].isin(matched_names)]['Amount'].sum()

print('__RESULT__:')
print(json.dumps({
    'matched_projects': matched_names,
    'total_funding': int(total_funding)
}))"""

env_args = {'var_function-call-10032448971430008742': 'file_storage/function-call-10032448971430008742.json', 'var_function-call-17801199440429665660': 'file_storage/function-call-17801199440429665660.json'}

exec(code, env_args)
