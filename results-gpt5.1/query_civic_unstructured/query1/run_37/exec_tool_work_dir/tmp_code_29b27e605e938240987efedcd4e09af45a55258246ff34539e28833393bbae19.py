code = """import re, json, pandas as pd
from pathlib import Path

# Load all funding records with Amount > 50000
funding_records = var_call_es2JfH1av83Dm8vwu3Z2edNu

# Load civic documents full result from file if needed
civic_path = Path(var_call_PRBwy7WQ7kZyF8nCugIkPOiD)
import json as _json
with civic_path.open() as f:
    civic_docs = _json.load(f)

texts = [d['text'] for d in civic_docs]

# Very simple heuristic: extract project names that appear in design sections.
# We'll look for sections labeled 'Capital Improvement Projects (Design)' and then
# take subsequent lines that look like project titles (non-empty, not starting with bullet/parenthesis) until a blank line or another section header.

design_projects = set()
for text in texts:
    # Normalize newlines
    lines = text.split('\n')
    in_design = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Detect start of design section
        if 'Capital Improvement Projects (Design)' in stripped:
            in_design = True
            continue
        # Detect start of another high-level section
        if in_design and ('Capital Improvement Projects (' in stripped and '(Design)' not in stripped):
            in_design = False
        if not in_design:
            continue
        # Skip obvious non-project lines
        if stripped.startswith('(') or stripped.startswith('Page '):
            continue
        if any(stripped.startswith(prefix) for prefix in ['Updates', 'Project Description', 'Project Schedule', 'Estimated Schedule']):
            continue
        # Heuristic: consider lines that have at least 2 words and no colon as project names
        if ':' in stripped:
            continue
        if len(stripped.split()) >= 2:
            design_projects.add(stripped)

# Also flag projects whose descriptions explicitly mention 'design phase' or 'design plans' etc.
for text in texts:
    for proj in list(design_projects):
        pass  # already captured

# Build DataFrame from funding
fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Join on exact project names where amount > 50000 and project is in design list
design_funded = fund_df[(fund_df['Amount'] > 50000) & (fund_df['Project_Name'].isin(design_projects))]

count = int(design_funded.shape[0])

import json as _j
result = _j.dumps({"count_design_capital_over_50000": count})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_es2JfH1av83Dm8vwu3Z2edNu': 'file_storage/call_es2JfH1av83Dm8vwu3Z2edNu.json', 'var_call_PRBwy7WQ7kZyF8nCugIkPOiD': 'file_storage/call_PRBwy7WQ7kZyF8nCugIkPOiD.json'}

exec(code, env_args)
