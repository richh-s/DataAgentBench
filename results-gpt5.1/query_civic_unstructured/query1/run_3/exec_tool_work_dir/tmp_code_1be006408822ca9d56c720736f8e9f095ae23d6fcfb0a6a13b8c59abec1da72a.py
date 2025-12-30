code = """import re, json
from collections import defaultdict

# Load civic docs full result
path = var_call_Za4OrhmRj19K5mnGJFYgs5Df
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Very simple heuristic: extract project names under 'Capital Improvement Projects (Design)' section until next section header
projects_design = set()

# Split on that header
m = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)', texts, re.S)
if m:
    section = m.group(1)
    # project names: lines with title case not too long
    for line in section.split('\n'):
        line = line.strip()
        if not line or 'Updates' in line or 'Schedule' in line or 'Project Description' in line:
            continue
        # heuristic: line with letters and spaces, no colon, length between 5 and 80
        if ':' in line:
            continue
        if re.search(r'[A-Za-z]', line) and 5 <= len(line) <= 80:
            projects_design.add(line)

# Manually also search for keyword 'Design' projects that look like names
for m2 in re.finditer(r'\n([A-Z][A-Za-z0-9& ,\-]+Design[ A-Za-z0-9&\-]*)\n', texts):
    projects_design.add(m2.group(1).strip())

# Known from preview some design capital projects list; but rely on extraction

# Now, from funding DB result preview already loaded as var_call_TP5LAvTolLgpDs82Xp55lHv9 or path
funding_data = var_call_TP5LAvTolLgpDs82Xp55lHv9

# Count projects that are capital (assume all in this doc are capital) and in design status (our set), with amount>50000 (already filtered)
count = 0
for rec in funding_data:
    name = rec['Project_Name']
    # Match ignoring parenthetical suffixes
    base_name = re.sub(r' \([^)]*\)$', '', name)
    if base_name in projects_design:
        count += 1

result = count

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TP5LAvTolLgpDs82Xp55lHv9': 'file_storage/call_TP5LAvTolLgpDs82Xp55lHv9.json', 'var_call_Za4OrhmRj19K5mnGJFYgs5Df': 'file_storage/call_Za4OrhmRj19K5mnGJFYgs5Df.json'}

exec(code, env_args)
