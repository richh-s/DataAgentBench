code = """import json, pandas as pd, re
from pathlib import Path

funding_records = var_call_es2JfH1av83Dm8vwu3Z2edNu

civic_path = Path(var_call_PRBwy7WQ7kZyF8nCugIkPOiD)
with civic_path.open() as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

design_projects = set()
for text in texts:
    lines = text.split('\n')
    in_design = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if 'Capital Improvement Projects (Design)' in stripped:
            in_design = True
            continue
        if in_design and ('Capital Improvement Projects (' in stripped and '(Design)' not in stripped):
            in_design = False
        if not in_design:
            continue
        if stripped.startswith('(') or stripped.startswith('Page '):
            continue
        if stripped.startswith('Updates') or stripped.startswith('Project Description') or stripped.startswith('Project Schedule') or stripped.startswith('Estimated Schedule'):
            continue
        if ':' in stripped:
            continue
        if len(stripped.split()) >= 2:
            design_projects.add(stripped)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

design_funded = fund_df[(fund_df['Amount'] > 50000) & (fund_df['Project_Name'].isin(design_projects))]

count = int(design_funded.shape[0])

result = json.dumps({"count_design_capital_over_50000": count})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_es2JfH1av83Dm8vwu3Z2edNu': 'file_storage/call_es2JfH1av83Dm8vwu3Z2edNu.json', 'var_call_PRBwy7WQ7kZyF8nCugIkPOiD': 'file_storage/call_PRBwy7WQ7kZyF8nCugIkPOiD.json'}

exec(code, env_args)
