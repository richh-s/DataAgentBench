code = """import re, json, pandas as pd

funding = var_call_c2lY39Vj3HbrRMpr1zoQd4HV
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

path = var_call_rWA2SUqvcyRvyAWw5Yze1UYu
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = " ".join(doc.get("text", "") for doc in civic_docs)

pattern = r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|$)"
design_section_match = re.search(pattern, texts, re.S)
project_names = []
if design_section_match:
    section = design_section_match.group(1)
    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if re.match(r"^[0-9()\-]", line):
            continue
        if len(line.split()) < 2:
            continue
        if any(x in line for x in ["Updates", "Project Schedule", "Estimated Schedule", "Page", "Agenda Item"]):
            continue
        project_names.append(line)

project_names = sorted(set(project_names))

design_projects_df = funding_df[funding_df["Project_Name"].isin(project_names)]

count_design_capital_over_50k = int((design_projects_df["Amount"] > 50000).sum())

result = json.dumps({"count_design_capital_over_50000": count_design_capital_over_50k})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_c2lY39Vj3HbrRMpr1zoQd4HV': 'file_storage/call_c2lY39Vj3HbrRMpr1zoQd4HV.json', 'var_call_rWA2SUqvcyRvyAWw5Yze1UYu': 'file_storage/call_rWA2SUqvcyRvyAWw5Yze1UYu.json'}

exec(code, env_args)
