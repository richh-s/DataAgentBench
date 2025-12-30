code = """import re, json, pandas as pd, os

funding = var_call_7m3Yxswa6Ch4GIVd59WjlFjU
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

civic = var_call_96I0LBUSwxghHeCnq6rsVaiR
if isinstance(civic, str) and os.path.isfile(civic):
    with open(civic, 'r') as f:
        civic = json.load(f)

texts = [d['text'] for d in civic]
full_text = '\n'.join(texts)

pattern = r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)"
match = re.search(pattern, full_text, flags=re.S)
design_block = match.group(1) if match else ''

project_lines = []
for line in design_block.split('\n'):
    s = line.strip()
    if not s:
        continue
    if len(s) < 5 or len(s) > 120:
        continue
    if any(k in s for k in ['Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description']):
        continue
    words = s.split()
    caps = sum(1 for w in words if w[0].isupper())
    if caps >= 2:
        project_lines.append(s)

project_names = sorted(set(project_lines))

design_funding = funding_df[funding_df['Project_Name'].isin(project_names)]

count = int((design_funding['Amount'] > 50000).sum())

out = json.dumps(count)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7m3Yxswa6Ch4GIVd59WjlFjU': 'file_storage/call_7m3Yxswa6Ch4GIVd59WjlFjU.json', 'var_call_96I0LBUSwxghHeCnq6rsVaiR': 'file_storage/call_96I0LBUSwxghHeCnq6rsVaiR.json'}

exec(code, env_args)
