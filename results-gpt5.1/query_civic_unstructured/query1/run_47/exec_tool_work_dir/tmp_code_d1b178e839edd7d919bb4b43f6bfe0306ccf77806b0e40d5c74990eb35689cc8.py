code = """import json, pandas as pd
from pathlib import Path

# Load full funding results
funding_path = var_call_wvAtgABRPoy0z6ODP1E3b4zu
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)

# Load civic docs
civic_path = var_call_5L7ZumM7C9EJeheJNPq6ySIJ
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

texts = ' '.join(rec['text'] for rec in civic_records)

# Naive extraction: consider any funding project whose name appears in a 'Capital Improvement Projects (Design)' section
# We'll split the big text around that heading and collect lines until the next 'Capital Improvement Projects (' or 'Disaster' section

sections = []
start_idx = texts.find('Capital Improvement Projects (Design)')
if start_idx != -1:
    sub = texts[start_idx:]
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster']
    end_idx_candidates = [sub.find(m) for m in end_markers if sub.find(m) != -1]
    end_idx = min(end_idx_candidates) if end_idx_candidates else len(sub)
    design_block = sub[:end_idx]
    sections.append(design_block)
else:
    design_block = ''

lines = [ln.strip() for ln in design_block.split('\n')]
project_lines = []
for ln in lines:
    if not ln:
        continue
    # Heuristic: project name lines are those without colon and not starting with bullets or parentheses
    if (':' not in ln) and (not ln.startswith('(')) and (not ln.startswith('Page ')) and (not ln.startswith('Agenda Item')) and (not ln.startswith('Capital Improvement Projects')):
        project_lines.append(ln)

design_project_names = list(dict.fromkeys(project_lines))

# Now match funding projects with these names
mask = funding_df['Project_Name'].isin(design_project_names)
matched_df = funding_df[mask]

count_design_capital_over_50k = int(len(matched_df))

result = {
    'design_project_names': design_project_names,
    'matched_funding_projects': matched_df.to_dict(orient='records'),
    'count_design_capital_over_50k': count_design_capital_over_50k
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wvAtgABRPoy0z6ODP1E3b4zu': 'file_storage/call_wvAtgABRPoy0z6ODP1E3b4zu.json', 'var_call_5L7ZumM7C9EJeheJNPq6ySIJ': 'file_storage/call_5L7ZumM7C9EJeheJNPq6ySIJ.json'}

exec(code, env_args)
