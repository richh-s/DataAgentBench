code = """import re, json, pandas as pd

funding_records = var_call_F7IPz5S2s4TofsGuRlXS5yZi
texts_info = var_call_nfijdFA3pO757Y71Y42fSlwX

# Load civic docs full result if it's a file path
if isinstance(texts_info, str):
    import pathlib, json as _json
    with open(texts_info, 'r') as f:
        civic_docs = _json.load(f)
else:
    civic_docs = texts_info

texts = [d.get('text', '') for d in civic_docs]
full_text = "\n".join(texts)

# Extract capital project blocks by rough headings and lines
projects = []
current_section_type = None
for line in full_text.splitlines():
    l = line.strip()
    if not l:
        continue
    if 'Capital Improvement Projects (Design)' in l:
        current_section_type = 'design'
        continue
    if 'Capital Improvement Projects (Construction)' in l:
        current_section_type = 'construction'
        continue
    if 'Capital Improvement Projects (Not Started)' in l:
        current_section_type = 'not started'
        continue
    # Stop when leaving CIP/disaster sections (very rough)
    if 'Agenda Item' in l and '4.B.' in l and 'Page' in l:
        current_section_type = None
        continue
    if current_section_type == 'design':
        # Heuristic: project name lines are those without bullets and not schedules
        if not l.startswith('(') and not l.startswith('cid:') and not l.startswith('Updates') and not l.endswith(':') and 'Project Schedule' not in l and 'Estimated Schedule' not in l and 'Project Description' not in l and 'Project Updates' not in l:
            # Avoid generic lines
            if len(l.split()) <= 2:
                continue
            projects.append({'Project_Name': l, 'status': 'design', 'type': 'capital'})

# Create DataFrame for funding > 50000
fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)
fund_df = fund_df[fund_df['Amount'] > 50000]

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

merged = proj_df.merge(fund_df, on='Project_Name', how='inner')

count_design_capital_over_50k = int(len(merged))

result = json.dumps({'count': count_design_capital_over_50k})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_F7IPz5S2s4TofsGuRlXS5yZi': 'file_storage/call_F7IPz5S2s4TofsGuRlXS5yZi.json', 'var_call_nfijdFA3pO757Y71Y42fSlwX': 'file_storage/call_nfijdFA3pO757Y71Y42fSlwX.json'}

exec(code, env_args)
