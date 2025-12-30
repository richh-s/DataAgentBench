code = """import json, pandas as pd
from pathlib import Path

funding_records = var_call_S9nDaeJwmRe3yqMkjKr8uDm0
funding_df = pd.DataFrame(funding_records)

civic_path = Path(var_call_ZBV6yHza1Le8jjYhL5GQwW93)
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

texts = [r['text'] for r in civic_records]
all_text = '\n'.join(texts)

parts = all_text.split('Capital Improvement Projects (Design)')
if len(parts) > 1:
    after_design = parts[1]
    design_section = after_design.split('Capital Improvement Projects (Construction)')[0]
else:
    design_section = ''

design_projects = []
for line in design_section.split('\n'):
    line = line.strip()
    if not line:
        continue
    if any(prefix in line for prefix in ['Updates', 'Project Schedule', 'Estimated Schedule', 'Page ', 'Agenda Item']):
        continue
    if any(ch.isalpha() for ch in line) and not line.startswith('('):
        if len(line.split()) < 2:
            continue
        # exclude very long narrative lines
        if len(line) > 120:
            continue
        design_projects.append(line)

funding_names = set(funding_df['Project_Name'].tolist())

matched_projects = []
for p in design_projects:
    for name in funding_names:
        if p.lower() in name.lower() or name.lower() in p.lower():
            matched_projects.append(name)

matched_projects = sorted(set(matched_projects))

count_design_funded = len(matched_projects)

result = json.dumps({"count_design_capital_projects_funding_gt_50000": count_design_funded, "matched_projects": matched_projects})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_S9nDaeJwmRe3yqMkjKr8uDm0': 'file_storage/call_S9nDaeJwmRe3yqMkjKr8uDm0.json', 'var_call_ZBV6yHza1Le8jjYhL5GQwW93': 'file_storage/call_ZBV6yHza1Le8jjYhL5GQwW93.json'}

exec(code, env_args)
