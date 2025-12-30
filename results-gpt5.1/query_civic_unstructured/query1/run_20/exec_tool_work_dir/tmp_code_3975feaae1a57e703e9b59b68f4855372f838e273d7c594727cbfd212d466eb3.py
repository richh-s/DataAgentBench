code = """import json, pandas as pd

# Load funding results
funding_path = var_call_DoUb5wecv2lDAW4ilEVXX1Wc
with open(funding_path, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load civic docs
civic_path = var_call_4gSFwPmqMIUxl3QzEbSkypiw
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

texts = ' \n '.join(doc['text'] for doc in civic_docs)

lines = texts.split('\n')

in_design_section = False
Design_Projects = set()

for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    if 'Capital Improvement Projects (Design)' in stripped:
        in_design_section = True
        continue
    if in_design_section and 'Capital Improvement Projects (Construction)' in stripped:
        in_design_section = False
        continue
    if not in_design_section:
        continue
    if stripped.startswith('Agenda Item') or stripped.startswith('Page '):
        continue
    if any(stripped.startswith(prefix) for prefix in ['Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Project Updates']):
        continue
    if stripped.endswith('Projects (Construction)') or stripped.endswith('Projects (Not Started)'):
        in_design_section = False
        continue
    if '.' not in stripped and len(stripped.split()) >= 2 and not stripped.endswith(':'):
        Design_Projects.add(stripped)

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
    Design_Projects.add(name)

funding_design = funding_df[funding_df['Project_Name'].isin(Design_Projects)]
result_count = int((funding_design['Amount'] > 50000).sum())

out = json.dumps(result_count)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_DoUb5wecv2lDAW4ilEVXX1Wc': 'file_storage/call_DoUb5wecv2lDAW4ilEVXX1Wc.json', 'var_call_4gSFwPmqMIUxl3QzEbSkypiw': 'file_storage/call_4gSFwPmqMIUxl3QzEbSkypiw.json'}

exec(code, env_args)
