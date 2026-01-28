code = """import re, json
from collections import defaultdict

# Load funding data
funding_records = var_call_ytm6ttfV16j822VrWLI0h2uY

# Load civic docs text
civic_docs = var_call_IlBpye4RpLRD2lb69CV4NLrt

# Very simple heuristic parser: find sections under 'Capital Improvement Projects (Design)' and list project lines until next blank line or header
project_status = {}

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    section = text.split('Capital Improvement Projects (Design)', 1)[1]
    # stop at next major header
    stop_tokens = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    for tok in stop_tokens:
        if tok in section:
            section = section.split(tok, 1)[0]
    # project name lines: assume lines that are not empty and not bullets and in title case-ish
    for line in section.split('\n'):
        s = line.strip()
        if not s:
            continue
        if 'Project Schedule' in s or 'Updates' in s or 'Estimated Schedule' in s or 'Project Description' in s:
            continue
        # Heuristic: consider lines with at least 3 words and starting with uppercase letter as project names
        if len(s.split()) >= 3 and s[0].isupper():
            # Clean weird characters
            name = re.sub(r'[^A-Za-z0-9&(),\- ]+', ' ', s).strip()
            project_status[name] = 'design'

# Build a set of capital projects: here we approximate that all in this design list are capital
capital_design_projects = set(project_status.keys())

# Now match with funding records by exact name match, counting those over 50000 (already filtered in SQL)
count = 0
for rec in funding_records:
    pname = rec['Project_Name']
    if pname in capital_design_projects:
        count += 1

result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_ytm6ttfV16j822VrWLI0h2uY': 'file_storage/call_ytm6ttfV16j822VrWLI0h2uY.json', 'var_call_IlBpye4RpLRD2lb69CV4NLrt': 'file_storage/call_IlBpye4RpLRD2lb69CV4NLrt.json'}

exec(code, env_args)
