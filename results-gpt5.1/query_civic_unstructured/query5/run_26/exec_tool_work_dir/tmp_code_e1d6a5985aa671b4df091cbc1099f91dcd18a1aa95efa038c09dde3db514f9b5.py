code = """import json, re, pandas as pd
from pathlib import Path

# Load full civic docs
path_civic = Path(var_call_FZ3bNgaF8x8kDcGY3xXsLOa9)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Load full funding
path_fund = Path(var_call_gvC8z1mkBnGcnJ2jbOoIsG9d)
with open(path_fund, 'r') as f:
    funding = json.load(f)

texts = "\n".join(d['text'] for d in civic_docs)

# Heuristic: capture lines that look like project titles followed by schedules/dates
lines = [l.strip() for l in texts.split('\n') if l.strip()]

projects = []
current = None
for line in lines:
    # project name heuristic: line that contains 'Project' or typical capital words and not too long
    if re.search(r'Project', line) and len(line) < 120:
        # commit previous
        if current:
            projects.append(current)
        current = {'Project_Name': line, 'context': ''}
    elif current:
        current['context'] += ' ' + line

if current:
    projects.append(current)

# Extract start date/year from context: look for 'Begin Construction:' or similar with a 4-digit year
for p in projects:
    ctx = p['context']
    m = re.search(r'(Begin Construction[^\d]*)(\d{4})', ctx)
    if not m:
        m = re.search(r'(Start[^\d]*)(\d{4})', ctx)
    p['start_year'] = m.group(2) if m else None

# Determine type: disaster if FEMA/CalOES mentioned or 'Disaster Recovery'
for p in projects:
    ctx = p['context']
    name = p['Project_Name']
    if re.search(r'FEMA|CalOES|Disaster', ctx+name, re.IGNORECASE):
        p['type'] = 'disaster'
    else:
        p['type'] = 'capital'

proj_df = pd.DataFrame(projects)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Join on project name: we need to match Funding.Project_Name to our extracted names.
# Use simple exact match first; also many disaster projects in funding have suffixes like '(FEMA Project)'.

# Build mapping of base names (without suffix parentheses) to start_year and type.
proj_df['base_name'] = proj_df['Project_Name'].str.replace(r'\s*\([^)]*\)', '', regex=True).str.strip()

fund_df['base_name'] = fund_df['Project_Name'].str.replace(r'\s*\([^)]*\)', '', regex=True).str.strip()

merged = pd.merge(fund_df, proj_df[['base_name','start_year','type']], on='base_name', how='left')

# Filter for disaster projects with start_year 2022
mask = (merged['type'] == 'disaster') & (merged['start_year'] == '2022')

total = int(merged.loc[mask, 'Amount'].sum())

result = {'total_disaster_funding_2022_start': total}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_FZ3bNgaF8x8kDcGY3xXsLOa9': 'file_storage/call_FZ3bNgaF8x8kDcGY3xXsLOa9.json', 'var_call_gvC8z1mkBnGcnJ2jbOoIsG9d': 'file_storage/call_gvC8z1mkBnGcnJ2jbOoIsG9d.json'}

exec(code, env_args)
