code = """import json
import re
import pandas as pd

# Load data from files
funding_result = locals()['var_functions.query_db:22']
civic_result = locals()['var_functions.query_db:20']

# Load funding data
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

# Load civic documents
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Create funding DataFrame
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract capital projects with design status from civic docs
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find Capital Improvement Projects (Design) section
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|$)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    
    if match:
        section_text = match.group(1)
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) < 5:
                continue
            
            # Skip markers and non-project lines
            if line[0] in '(-•▪' or 'cid:' in line or line.isupper():
                continue
            if 'PROJECTS' in line.upper() or line.lower().startswith('page'):
                continue
            
            # Skip schedule and update lines
            lower = line.lower()
            if any(x in lower for x in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'project description:', 'estimated schedule:', 'complete construction', 'project updates']):
                continue
            
            # Skip common words and headers
            if lower in ['design', 'construction', 'not started']:
                continue
            if any(phrase in lower for phrase in ['public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by', 'approved by', 'subject']):
                continue
            
            # Skip short numeric lines (dates)
            if any(c.isdigit() for c in line) and len(line) < 15:
                continue
            
            # Clean project name
            project_name = line
            for prefix in ['·', '•', '-', '▪']:
                if project_name.startswith(prefix):
                    project_name = project_name[1:].strip()
            
            design_capital_projects.append({
                'Project_Name': project_name,
                'status': 'design',
                'type': 'capital'
            })

# Remove duplicates
projects_df = pd.DataFrame(design_capital_projects).drop_duplicates(subset=['Project_Name'])

print('Capital design projects found:', len(projects_df))

# Merge with funding data
merged = projects_df.merge(
    funding_df[['Project_Name', 'Amount']],
    on='Project_Name',
    how='inner'
)

print('Projects with funding data:', len(merged))

# Filter for amount > 50000
filtered = merged[merged['Amount'] > 50000]

print('\nCapital design projects with funding > $50,000:', len(filtered))
for _, row in filtered.iterrows():
    print('  -', row['Project_Name'], ': $' + str(row['Amount']))

# Prepare result
result = json.dumps({'count': len(filtered), 'projects': filtered.to_dict('records')})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:18': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
