code = """import re, json, pandas as pd

# Load funding data
funding = var_call_c2lY39Vj3HbrRMpr1zoQd4HV
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract project names from civic docs that are capital & design
path = var_call_rWA2SUqvcyRvyAWw5Yze1UYu
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc.get('text', '') for doc in civic_docs)

# Very simple heuristic: sections headed 'Capital Improvement Projects (Design)' then list project names as separate lines until next heading
design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|$)', texts, re.S)
project_names = []
if design_section_match:
    section = design_section_match.group(1)
    # candidate lines: non-empty, not starting with bullet/parenthesis, reasonably short
    for line in section.splitlines():
        line = line.strip('\n\r \t')
        if not line:
            continue
        if re.match(r'^[•()*0-9]', line):
            continue
        if len(line.split()) < 2:
            continue
        # skip generic words
        if any(x in line for x in ['Updates', 'Project Schedule', 'Estimated Schedule']):
            continue
        project_names.append(line)

project_names = sorted(set(project_names))

# Join with funding on exact Project_Name
design_projects_df = funding_df[funding_df['Project_Name'].isin(project_names)]

count_design_capital_over_50k = int((design_projects_df['Amount'] > 50000).sum())

result = json.dumps({"count_design_capital_over_50000": count_design_capital_over_50k, "matched_project_names": project_names})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_c2lY39Vj3HbrRMpr1zoQd4HV': 'file_storage/call_c2lY39Vj3HbrRMpr1zoQd4HV.json', 'var_call_rWA2SUqvcyRvyAWw5Yze1UYu': 'file_storage/call_rWA2SUqvcyRvyAWw5Yze1UYu.json'}

exec(code, env_args)
