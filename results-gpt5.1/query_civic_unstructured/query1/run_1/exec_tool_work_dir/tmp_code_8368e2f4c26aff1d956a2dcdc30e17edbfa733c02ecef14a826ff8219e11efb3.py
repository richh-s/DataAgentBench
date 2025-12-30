code = """import re, json, pandas as pd

# Load funding records (>50k)
funding_records = var_call_e5rLLLPQEJkD7z4j3StbWZMk
if isinstance(funding_records, str) and funding_records.endswith('.json'):
    with open(funding_records, 'r') as f:
        funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)

# Normalize amount to int
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load civic docs texts
civic_docs = var_call_7t2NfPdYBCR8n3eAG3tsUNST
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Identify project names that appear in a "Capital Improvement Projects (Design)" section
# We will capture project lines between "Capital Improvement Projects (Design)" and the next section heading

capital_design_projects = set()

sections = re.split(r'Capital Improvement Projects \(Design\)', texts, flags=re.IGNORECASE)
for sec in sections[1:]:
    # Stop at next major heading like 'Capital Improvement Projects (Construction)' or 'Capital Improvement Projects (Not Started)' or 'Disaster Recovery'
    sec = re.split(r'Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects', sec, flags=re.IGNORECASE)[0]
    # Project names appear as standalone lines with typical capitalization; approximate by lines that are not too long and not empty
    for line in sec.split('\n'):
        line = line.strip('\r ')
        if not line:
            continue
        # Skip obvious non-project lines
        if any(keyword in line.lower() for keyword in ['updates', 'schedule', 'project description', 'agenda item', 'page ', 'meeting', 'subject', 'recommended action']):
            continue
        # Heuristic: project lines often have multiple words and capital letters, and not end with ':'
        if line.endswith(':'):
            continue
        if len(line.split()) >= 2:
            # Filter out lines that look like sentences
            if not line.endswith('.'):
                capital_design_projects.add(line)

# We also look specifically for known project names around that section using Funding project names as anchors

project_names = set(funding_df['Project_Name'].unique())
matched_design_projects = set()

for pname in project_names:
    # if project name appears near the word 'Design' and 'Capital Improvement' in the text, treat as capital design
    pattern = re.escape(pname)
    for m in re.finditer(pattern, texts):
        start = max(0, m.start() - 200)
        end = min(len(texts), m.end() + 200)
        window = texts[start:end].lower()
        if 'capital improvement' in window and 'design' in window:
            matched_design_projects.add(pname)
            break

# Combine heuristics: any funding project name that matches or is contained in capital_design_projects lines
for line in capital_design_projects:
    for pname in project_names:
        if pname.lower() in line.lower() or line.lower() in pname.lower():
            matched_design_projects.add(pname)

# Now we have a set of project names that are capital projects in design status

# Filter funding for those projects
design_funding_df = funding_df[funding_df['Project_Name'].isin(matched_design_projects) & (funding_df['Amount'] > 50000)]

count_design_projects = int(design_funding_df['Project_Name'].nunique())

import json as _json
result = _json.dumps({"count_capital_design_projects_over_50000": count_design_projects})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_e5rLLLPQEJkD7z4j3StbWZMk': 'file_storage/call_e5rLLLPQEJkD7z4j3StbWZMk.json', 'var_call_7t2NfPdYBCR8n3eAG3tsUNST': 'file_storage/call_7t2NfPdYBCR8n3eAG3tsUNST.json'}

exec(code, env_args)
