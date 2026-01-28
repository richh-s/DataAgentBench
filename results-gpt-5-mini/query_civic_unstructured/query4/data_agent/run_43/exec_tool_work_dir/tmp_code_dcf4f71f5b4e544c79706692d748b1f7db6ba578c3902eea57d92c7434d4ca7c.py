code = """import json
import re

# Load the civic docs query result from storage
with open(var_call_cfHyLt4fnl8FkJTA47kfy1vu, 'r') as f:
    docs = json.load(f)

found_projects = []
month_keywords = ['Spring', 'March', 'April', 'May']
skip_tokens = ['updates', 'project schedule', 'project description', 'agenda', 'page', 'item', 'recommend', 'discussion', 'to:', 'prepared by', 'approved by', 'date prepared']

for doc in docs:
    text = doc.get('text', '')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, line in enumerate(lines):
        if '2022' in line and any(mk in line for mk in month_keywords):
            proj_name = None
            for j in range(i-1, max(i-9, -1), -1):
                l = lines[j]
                if not l:
                    continue
                l_low = l.lower()
                if any(tok in l_low for tok in skip_tokens):
                    continue
                if ':' in l and len(l) < 60:
                    continue
                if l.startswith('(cid') or l.startswith('('):
                    continue
                if 3 < len(l) < 200:
                    proj_name = l
                    break
            if proj_name and proj_name not in found_projects:
                found_projects.append(proj_name)

# Additional pattern: look for lines like 'Advertise: Spring 2022' and grab prior non-empty line
for doc in docs:
    text = doc.get('text', '')
    for m in re.finditer(r"(Advertise:|Begin Construction:|Complete Design:|Complete Construction:).{0,40}2022", text, flags=re.IGNORECASE):
        start = m.start()
        prev_text = text[:start]
        prev_lines = [ln.strip() for ln in prev_text.splitlines() if ln.strip()]
        if prev_lines:
            candidate = prev_lines[-1]
            if 3 < len(candidate) < 200 and candidate not in found_projects:
                found_projects.append(candidate)

result = {'projects': found_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cfHyLt4fnl8FkJTA47kfy1vu': 'file_storage/call_cfHyLt4fnl8FkJTA47kfy1vu.json'}

exec(code, env_args)
