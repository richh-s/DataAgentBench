code = """import re, json, pandas as pd

# Load funding results
funding_path = var_call_DoUb5wecv2lDAW4ilEVXX1Wc
with open(funding_path, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)

# Normalize amount to int
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load civic docs
civic_path = var_call_4gSFwPmqMIUxl3QzEbSkypiw
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

texts = ' \n '.join(doc['text'] for doc in civic_docs)

# Extract project names that are clearly in design status from the sample structure
# We look for sections like 'Capital Improvement Projects (Design)' and then grab subsequent capital project names.

design_projects = set()

# Simple heuristic: in lines after the 'Capital Improvement Projects (Design)' heading, treat non-empty lines
# that look like title case and not starting with '(' or 'Page' etc. as project names, until another major heading.

lines = texts.split('\n')

in_design_section = False
for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    if 'Capital Improvement Projects (Design)' in stripped:
        in_design_section = True
        continue
    if in_design_section and stripped.startswith('Capital Improvement Projects (Construction)'):
        in_design_section = False
    if not in_design_section:
        continue
    # Filter likely headings/project names
    if stripped.startswith('Agenda Item') or stripped.startswith('Page '):
        continue
    if any(stripped.startswith(prefix) for prefix in ['Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Project Updates']):
        continue
    # Stop if we hit another big heading not design
    if stripped.endswith('Projects (Construction)') or stripped.endswith('Projects (Not Started)'):
        in_design_section = False
        continue
    # Treat lines without periods and with multiple words as project names
    if '.' not in stripped and len(stripped.split()) >= 2 and not stripped.endswith(':'):
        design_projects.add(stripped)

# From preview we know some capital projects in design even if heuristic misses; ensure they are included explicitly
manual_add = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    'PCH Median Improvements Project',
    'Westward Beach Road Repair Project',
    'Westward Beach Road Drainage Improvements Project',
    'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Storm Drain Master Plan',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Civic Center Water Treatment Facility Phase 2',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Outdoor Warning Signs',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Playground',
    'Malibu Canyon Road Traffic Study'
]
for name in manual_add:
    design_projects.add(name)

# Now join with funding on Project_Name and filter amount > 50000
funding_design = funding_df[funding_df['Project_Name'].isin(design_projects)]
result_count = int((funding_design['Amount'] > 50000).sum())

import json as _json
out = _json.dumps(result_count)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_DoUb5wecv2lDAW4ilEVXX1Wc': 'file_storage/call_DoUb5wecv2lDAW4ilEVXX1Wc.json', 'var_call_4gSFwPmqMIUxl3QzEbSkypiw': 'file_storage/call_4gSFwPmqMIUxl3QzEbSkypiw.json'}

exec(code, env_args)
