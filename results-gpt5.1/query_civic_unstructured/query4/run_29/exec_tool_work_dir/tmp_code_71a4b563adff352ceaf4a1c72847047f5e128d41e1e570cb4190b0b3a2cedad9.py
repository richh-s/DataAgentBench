code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_f2P0DgxHMFOZ5MgGHBAYVzOC, 'r') as f:
    civic_docs = json.load(f)

# Simple heuristic: project lines often end with 'Project' or contain 'Improvements', 'Repairs', etc.
projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        # find lines that look like project titles
        if re.search(r'(Project|Improvements|Repairs|Resurfacing|Playground|Park|Study|Biofilter)', line) and len(line.split())<=12:
            name = line.strip('\u202f ').strip()
            # search nearby lines for date-like tokens
            window = '\n'.join(lines[max(0,i-5):i+10])
            m = re.search(r'(\d{4}[-/ ]?(Spring|Summer|Fall|Winter)|Spring\s*2022|March\s*2022|April\s*2022|May\s*2022|2022-0[3-5])', window, re.IGNORECASE)
            st = m.group(0) if m else ''
            projects.append({'Project_Name': name, 'st': st})

# deduplicate by name keeping any st containing '2022'
proj_df = pd.DataFrame(projects)
if not proj_df.empty:
    proj_df = proj_df.sort_values('Project_Name')
    proj_df = proj_df.drop_duplicates('Project_Name', keep='first')
    # tag spring 2022
    def is_spring_2022(s):
        s = s.lower()
        if 'spring 2022' in s or '2022-spring' in s:
            return True
        if '2022-03' in s or '2022-04' in s or '2022-05' in s:
            return True
        if 'march 2022' in s or 'april 2022' in s or 'may 2022' in s:
            return True
        return False
    proj_df['is_spring_2022'] = proj_df['st'].astype(str).apply(is_spring_2022)
    spring_projects = proj_df[proj_df['is_spring_2022']]
    spring_names = spring_projects['Project_Name'].unique().tolist()
else:
    spring_names = []

# Load funding table
with open(var_call_NW8fSPGSZXaIKBx4vJkgvUBZ, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Join on exact project names
mask = fund_df['Project_Name'].isin(spring_names)
matched = fund_df[mask]

result = {
    'spring_2022_project_count': int(mask.sum()),
    'total_funding': int(matched['Amount'].sum()),
    'matched_projects': matched[['Project_Name','Amount']].to_dict(orient='records')
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_f2P0DgxHMFOZ5MgGHBAYVzOC': 'file_storage/call_f2P0DgxHMFOZ5MgGHBAYVzOC.json', 'var_call_NW8fSPGSZXaIKBx4vJkgvUBZ': 'file_storage/call_NW8fSPGSZXaIKBx4vJkgvUBZ.json'}

exec(code, env_args)
