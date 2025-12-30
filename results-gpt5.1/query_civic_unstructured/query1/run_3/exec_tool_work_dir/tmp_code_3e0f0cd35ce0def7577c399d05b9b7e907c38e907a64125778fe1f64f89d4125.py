code = """import re, json
from collections import defaultdict

path = var_call_Za4OrhmRj19K5mnGJFYgs5Df
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

projects_design = set()

m = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)', texts, re.S)
if m:
    section = m.group(1)
    for line in section.split('\n'):
        line = line.strip()
        if not line or 'Updates' in line or 'Schedule' in line or 'Project Description' in line:
            continue
        if ':' in line:
            continue
        if re.search(r'[A-Za-z]', line) and 5 <= len(line) <= 80:
            projects_design.add(line)

for m2 in re.finditer(r'\n([A-Z][A-Za-z0-9&,\- ]*Design[ A-Za-z0-9&\-]*)\n', texts):
    projects_design.add(m2.group(1).strip())

funding_data = var_call_TP5LAvTolLgpDs82Xp55lHv9

count = 0
for rec in funding_data:
    name = rec['Project_Name']
    base_name = re.sub(r' \([^)]*\)$', '', name)
    if base_name in projects_design:
        count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_TP5LAvTolLgpDs82Xp55lHv9': 'file_storage/call_TP5LAvTolLgpDs82Xp55lHv9.json', 'var_call_Za4OrhmRj19K5mnGJFYgs5Df': 'file_storage/call_Za4OrhmRj19K5mnGJFYgs5Df.json'}

exec(code, env_args)
