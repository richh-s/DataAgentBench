code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_xbChgbOFCiNcNgxWKItj6FpL
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Heuristic: project names are lines ending with 'Project' or 'Improvements' etc.;
# dates appear as 'Begin Construction: Spring 2022', 'Start: 2022-Spring', etc.

# First, split into lines
lines = [l.strip() for l in full_text.split('\n') if l.strip()]

projects = {}
current_project = None
for line in lines:
    # Detect potential project name by typical capitalized words and keywords
    if re.search(r'(Project|Improvements|Repairs|Maintenance|Facility|Study|Biofilter|Benches|Arbors|Shade Structure|Playground|Culvert|Bridge|Road|Drainage)', line) and not line.startswith('('):
        # treat as project heading when reasonably short
        if len(line.split()) <= 12:
            current_project = line.strip(':')
            projects.setdefault(current_project, {'st': None})
            continue
    if current_project:
        # Look for start/begin phrases with Spring 2022
        if re.search(r'(Begin Construction|Start|Construction Start)', line, re.I) and re.search(r'Spring\s*2022|2022-Spring', line, re.I):
            projects[current_project]['st'] = '2022-Spring'

# Filter projects that started in Spring 2022
spring_projects = [name for name, info in projects.items() if info['st'] == '2022-Spring']

# Load funding table
path_funding = var_call_gsIj5BMep4C2QSktQZh4208T
with open(path_funding, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Match on exact Project_Name
matched = fund_df[fund_df['Project_Name'].isin(spring_projects)]

result = {
    'projects_started_spring_2022': len(spring_projects),
    'projects_with_funding_started_spring_2022': int(matched['Project_Name'].nunique()),
    'total_funding_for_spring_2022_projects': int(matched['Amount'].sum()),
    'project_names_started_spring_2022': spring_projects,
    'funded_project_names_started_spring_2022': matched['Project_Name'].unique().tolist()
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_xbChgbOFCiNcNgxWKItj6FpL': 'file_storage/call_xbChgbOFCiNcNgxWKItj6FpL.json', 'var_call_gsIj5BMep4C2QSktQZh4208T': 'file_storage/call_gsIj5BMep4C2QSktQZh4208T.json'}

exec(code, env_args)
