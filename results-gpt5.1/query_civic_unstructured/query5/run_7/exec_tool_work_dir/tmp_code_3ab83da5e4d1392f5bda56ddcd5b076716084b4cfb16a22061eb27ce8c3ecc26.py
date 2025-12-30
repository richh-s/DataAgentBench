code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_civic = Path(var_call_6XnHRP3CC73pgbpZp1fYXrmQ)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Heuristic: disaster projects often have FEMA/CalOES etc in name; but type is not structured, so infer from name keywords
# Extract project blocks by splitting on two or more newlines followed by something that looks like a project title
texts = ' \n '.join(doc['text'] for doc in civic_docs)

# Find lines that look like project titles (start of line, some text, then newline, then bullet/Updates etc.)
lines = [l.strip() for l in texts.split('\n')]
projects = []
for i, line in enumerate(lines):
    if not line or len(line) > 120 or len(line) < 4:
        continue
    # Likely a project title if followed by 'Updates' or 'Project Description' within next 3 lines
    window = ' '.join(lines[i+1:i+4]).lower()
    if 'project description' in window or 'updates' in window or 'project schedule' in window:
        projects.append(line)

projects = list(dict.fromkeys(projects))

# Now we should detect which are disaster projects and started in 2022.
# For start year 2022, search in vicinity of project name in full text for '2022' near 'begin construction' or similar.

project_info = {}
for name in projects:
    # Disaster heuristic: FEMA/CalOES/CalJPIA or words like 'slope repair', 'drain', 'culvert', 'road repair' which are often disaster but not always.
    disaster = False
    if any(k in name for k in ['(FEMA', 'FEMA)', 'CalOES', 'CalJPIA']):
        disaster = True
    # search in text around name
    pattern = re.escape(name)
    for m in re.finditer(pattern, texts):
        start = max(0, m.start()-400)
        end = m.end()+400
        ctx = texts[start:end]
        if 'disaster' in ctx.lower() or 'woolsey' in ctx.lower() or 'recovery' in ctx.lower():
            disaster = True
        if '2022' in ctx:
            # check any date-like string with 2022 for start time
            # we don't have explicit st/et fields, use presence of 'Begin Construction' + 2022
            if 'begin construction' in ctx.lower() or 'construction was completed' in ctx.lower() or 'advertise' in ctx.lower():
                project_info.setdefault(name, {'disaster': disaster, 'start_2022': False})
                project_info[name]['start_2022'] = True
    if name not in project_info and disaster:
        project_info[name] = {'disaster': True, 'start_2022': False}

# Determine disaster projects that start in 2022
start_2022_disaster = {n for n, info in project_info.items() if info['disaster'] and info.get('start_2022')}

# Now load Funding table
path_funding = Path(var_call_JmkQBnhbp6M6C4LtFDGlpvsO)
with open(path_funding, 'r') as f:
    funding_records = json.load(f)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster projects in funding are those whose Project_Name contains FEMA/CalOES/CalJPIA or that match extracted names marked disaster
def is_disaster_name(name: str) -> bool:
    if any(k in name for k in ['(FEMA', 'FEMA)', 'CalOES', 'CalJPIA']):
        return True
    return name in start_2022_disaster

fund_df['is_disaster'] = fund_df['Project_Name'].apply(is_disaster_name)

# For start year 2022, rely on civic-derived set start_2022_disaster or names containing '2022 '
fund_df['start_2022'] = fund_df['Project_Name'].apply(lambda n: (n in start_2022_disaster) or ('2022 ' in n))

result_amount = int(fund_df[(fund_df['is_disaster']) & (fund_df['start_2022'])]['Amount'].sum())

import json as _json
out = _json.dumps(result_amount)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_6XnHRP3CC73pgbpZp1fYXrmQ': 'file_storage/call_6XnHRP3CC73pgbpZp1fYXrmQ.json', 'var_call_JmkQBnhbp6M6C4LtFDGlpvsO': 'file_storage/call_JmkQBnhbp6M6C4LtFDGlpvsO.json'}

exec(code, env_args)
