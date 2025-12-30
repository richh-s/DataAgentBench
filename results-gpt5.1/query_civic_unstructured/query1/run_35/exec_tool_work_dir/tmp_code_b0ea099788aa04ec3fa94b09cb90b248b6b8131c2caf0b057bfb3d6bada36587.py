code = """import re, json, pandas as pd, os, json as json_lib

# Load funding data from storage (SQLite query)
funding_records = var_call_yuoy9hbfBjCrDt7ti3DdiGLc

# Load civic documents data from storage (MongoDB query)
civic_docs_data = var_call_GbNYPqDAV7wTvW9baLvNyqVZ
if isinstance(civic_docs_data, str) and os.path.isfile(civic_docs_data):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json_lib.load(f)

texts = [doc.get('text', '') for doc in civic_docs_data]
full_text = '\n'.join(texts)

projects = []

pattern = r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|$)"
match = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
if match:
    design_section = match.group(1)
    for raw_line in design_section.split('\n'):
        line = raw_line.strip('\r\n ')
        if not line:
            continue
        if any(kw in line for kw in ["Updates", "Project Schedule", "Estimated Schedule", "Agenda", "Page "]):
            continue
        if ':' in line:
            continue
        if len(line.split()) < 3:
            continue
        projects.append({"Project_Name": line, "type": "capital", "status": "design"})

projects_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')
funding_df = funding_df[funding_df['Amount'] > 50000]

merged = pd.merge(projects_df, funding_df, on='Project_Name', how='inner')
count = int(len(merged))

result = json.dumps({"count": count})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yuoy9hbfBjCrDt7ti3DdiGLc': 'file_storage/call_yuoy9hbfBjCrDt7ti3DdiGLc.json', 'var_call_GbNYPqDAV7wTvW9baLvNyqVZ': 'file_storage/call_GbNYPqDAV7wTvW9baLvNyqVZ.json'}

exec(code, env_args)
