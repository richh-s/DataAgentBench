code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_0vz4IgtWyMoqJbYorgVZLvdF
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Heuristic: find project lines that look like names, then check for park topic and completed 2022
lines = full_text.split('\n')
project_names = set()
for i, line in enumerate(lines):
    if 'Park' in line or 'park' in line:
        # look back a bit for a line with 'Project' or 'Park'
        context = '\n'.join(lines[max(0,i-2):i+3])
        # naive project name: line itself if it has 'Park'
        name = line.strip('\u202f ').strip()
        if len(name) > 5 and not name.lower().startswith('updates'):
            project_names.add(name)

# But we really just need those that are marked completed in 2022
completed_2022_parks = set()
for i, line in enumerate(lines):
    if 'Construction was completed' in line and '2022' in line:
        # search nearby for park-related words
        context_lines = lines[max(0,i-5):i+1]
        name = None
        for cl in context_lines:
            if 'Park' in cl or 'park' in cl:
                name = cl.strip()
        if name:
            completed_2022_parks.add(name)

# We saw in preview examples like 'Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs'
# From those, only park-related: 'Bluffs Park Shade Structure'
# Also maybe others in full text:

# normalize names for matching with Funding table (they should match exactly or closely)
completed_2022_parks_normalized = set()
for n in completed_2022_parks:
    completed_2022_parks_normalized.add(n)

# Load funding table
path_funding = var_call_m06es62LEaolyVLqkfG4b1Dl
with open(path_funding, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Find funding records whose Project_Name matches any of the discovered names (or is very close)
# We'll do simple contains matching for 'Park' and completed-known projects from preview
park_project_names = set()
for pname in fund_df['Project_Name']:
    if 'Park' in pname:
        park_project_names.add(pname)

# From civic text we know completed 2022 park projects include 'Bluffs Park Shade Structure'
completed_2022_parks_normalized.add('Bluffs Park Shade Structure')

matched_funding = fund_df[fund_df['Project_Name'].isin(completed_2022_parks_normalized)]

total_funding = int(matched_funding['Amount'].sum())

result = {"completed_2022_park_projects": list(completed_2022_parks_normalized), "total_funding": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0vz4IgtWyMoqJbYorgVZLvdF': 'file_storage/call_0vz4IgtWyMoqJbYorgVZLvdF.json', 'var_call_m06es62LEaolyVLqkfG4b1Dl': 'file_storage/call_m06es62LEaolyVLqkfG4b1Dl.json'}

exec(code, env_args)
