code = """import json, re
from collections import defaultdict

# Load full funding result
with open(var_call_TOBEben6wKuNQVLE3xRB5Eea, 'r') as f:
    funding = json.load(f)

# Build set of project names with amount>50000
funding_names = {rec['Project_Name'] for rec in funding}

# Load civic docs
with open(var_call_sgtTIIAAuXdUS7RgpZGOd1zD, 'r') as f:
    docs = json.load(f)

text = '\n'.join(doc['text'] for doc in docs)

# Extract project sections under "Capital Improvement Projects and Disaster Recovery Projects Status Report"
# We'll classify by headings: (Design), (Construction), (Not Started)

projects = {}
current_status = None

for line in text.split('\n'):
    line = line.strip()
    if not line:
        continue
    if line.startswith('Capital Improvement Projects (Design)'):
        current_status = 'design'
        continue
    if line.startswith('Capital Improvement Projects (Construction)'):
        current_status = 'completed'
        continue
    if line.startswith('Capital Improvement Projects (Not Started)'):
        current_status = 'not started'
        continue
    # Heuristic: project name lines are non-indented, not "Updates"/"Project"/"Page"/"Agenda" etc and current_status is set
    if current_status and not line.startswith(('(', 'Page ', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Subject:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Project Description:', 'Project Updates:', 'Estimated Schedule', 'Project Schedule', 'Updates:')):
        # avoid obvious narrative sentences by requiring it not end with ':' and be relatively short
        if not line.endswith(':') and len(line) < 120:
            projects[line] = {'status': current_status, 'type': 'capital'}

# Now count projects that are capital, status=design, and have funding>50000
count = 0
matched = []
for name, info in projects.items():
    if info['status'] == 'design' and info['type'] == 'capital':
        # try exact match first
        if name in funding_names:
            count += 1
            matched.append(name)
        else:
            # try fuzzy: any funding project containing this name or vice versa
            for fname in funding_names:
                if name in fname or fname in name:
                    count += 1
                    matched.append(name + ' -> ' + fname)
                    break

result = {'count': count, 'matched': matched}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TOBEben6wKuNQVLE3xRB5Eea': 'file_storage/call_TOBEben6wKuNQVLE3xRB5Eea.json', 'var_call_sgtTIIAAuXdUS7RgpZGOd1zD': 'file_storage/call_sgtTIIAAuXdUS7RgpZGOd1zD.json'}

exec(code, env_args)
