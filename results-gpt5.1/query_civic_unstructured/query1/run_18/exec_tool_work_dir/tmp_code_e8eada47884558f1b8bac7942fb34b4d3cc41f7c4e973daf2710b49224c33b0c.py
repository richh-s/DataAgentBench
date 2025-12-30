code = """import re, json, pandas as pd
from pathlib import Path

with open(var_call_aA2hJe2cPLZreN0Y95XgNSQ2, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_vKaEfoUhpwoTByl64pO29rbS
fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)
fund_df = fund_df[fund_df['Amount'] > 50000]

texts = [d['text'] for d in civic_docs]
text_full = '\n'.join(texts)

sections = re.split(r'Capital Improvement Projects \(Design\)', text_full, flags=re.IGNORECASE)
if len(sections) < 2:
    design_block = ''
else:
    after = sections[1]
    end_split = re.split(r'Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)', after, flags=re.IGNORECASE)
    design_block = end_split[0]

lines = [l.strip() for l in design_block.split('\n') if l.strip()]

projects = []
current = None
for line in lines:
    if re.match(r'^[A-Z0-9].+', line) and not line.startswith('(cid:') and 'Updates' not in line and 'Project Schedule' not in line and 'Estimated Schedule' not in line:
        current = line
        projects.append(current)

projects = list(dict.fromkeys(projects))

fund_names = set(fund_df['Project_Name'].unique())

matched = []
for p in projects:
    for name in fund_names:
        if p.lower() in name.lower() or name.lower() in p.lower():
            matched.append(name)

matched = sorted(set(matched))

capital_design_funded = fund_df[fund_df['Project_Name'].isin(matched)]
count = int(len(capital_design_funded))

result = json.dumps({"count_capital_design_over_50000": count})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_vKaEfoUhpwoTByl64pO29rbS': 'file_storage/call_vKaEfoUhpwoTByl64pO29rbS.json', 'var_call_aA2hJe2cPLZreN0Y95XgNSQ2': 'file_storage/call_aA2hJe2cPLZreN0Y95XgNSQ2.json'}

exec(code, env_args)
