code = """import json, pandas as pd
from pathlib import Path

funding_path = var_call_wvAtgABRPoy0z6ODP1E3b4zu
with open(funding_path, 'r') as f:
    funding_records = json.load(f)
funding_df = pd.DataFrame(funding_records)

civic_path = var_call_5L7ZumM7C9EJeheJNPq6ySIJ
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

texts = ' '.join(rec['text'] for rec in civic_records)

start_idx = texts.find('Capital Improvement Projects (Design)')
if start_idx != -1:
    sub = texts[start_idx:]
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster']
    end_positions = []
    for m in end_markers:
        pos = sub.find(m)
        if pos != -1:
            end_positions.append(pos)
    end_idx = min(end_positions) if end_positions else len(sub)
    design_block = sub[:end_idx]
else:
    design_block = ''

lines = [ln.strip() for ln in design_block.split('\n')]
project_lines = []
for ln in lines:
    if not ln:
        continue
    if (':' not in ln) and (not ln.startswith('(')) and (not ln.startswith('Page ')) and (not ln.startswith('Agenda Item')) and (not ln.startswith('Capital Improvement Projects')):
        project_lines.append(ln)

design_project_names = list(dict.fromkeys(project_lines))

mask = funding_df['Project_Name'].isin(design_project_names)
matched_df = funding_df[mask]

count_design_capital_over_50k = int(len(matched_df))

out = json.dumps(count_design_capital_over_50k)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wvAtgABRPoy0z6ODP1E3b4zu': 'file_storage/call_wvAtgABRPoy0z6ODP1E3b4zu.json', 'var_call_5L7ZumM7C9EJeheJNPq6ySIJ': 'file_storage/call_5L7ZumM7C9EJeheJNPq6ySIJ.json'}

exec(code, env_args)
