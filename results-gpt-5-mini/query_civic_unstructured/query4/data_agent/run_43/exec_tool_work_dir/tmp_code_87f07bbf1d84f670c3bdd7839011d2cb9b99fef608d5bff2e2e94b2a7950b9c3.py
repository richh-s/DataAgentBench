code = """import json
import re

# Load the civic docs query result from storage
with open(var_call_cfHyLt4fnl8FkJTA47kfy1vu, 'r') as f:
    docs = json.load(f)

found_projects = []

month_keywords = ['Spring', 'March', 'April', 'May']

for doc in docs:
    text = doc.get('text', '')
    # Normalize some unicode and parentheses markers
    text = text.replace('\r', '\n')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, line in enumerate(lines):
        if '2022' in line and any(mk in line for mk in month_keywords):
            # found a schedule line mentioning spring 2022 or months in spring
            # search upward for a project title within previous 8 lines
            proj_name = None
            for j in range(i-1, max(i-9, -1), -1):
                l = lines[j]
                if not l:
                    continue
                l_low = l.lower()
                # Skip lines that are clearly not project titles
                skip_tokens = ['updates', 'project schedule', 'project description', 'agenda', 'page', 'item', 'recommend', 'discussion', 'to:', 'prepared by', 'approved by', 'date prepared']
                if any(tok in l_low for tok in skip_tokens):
                    continue
                # Skip lines that contain colons heavily (likely labels) or start with parentheses markers
                if ':' in l and len(l) < 60:
                    # could still be a short title with colon, but skip to be safe
                    continue
                if l.startswith('(cid') or l.startswith('('):
                    continue
                # heuristics: project names often have mixed-case and words, not very long
                if len(l) > 3 and len(l) < 200:
                    proj_name = l
                    break
            if proj_name:
                # clean project name
                proj_name = re.sub(r'\s+', ' ', proj_name).strip()
                if proj_name not in found_projects:
                    found_projects.append(proj_name)

# As fallback, also search for lines that explicitly contain 'Advertise: Spring 2022' etc.
for doc in docs:
    text = doc.get('text', '')
    for match in re.finditer(r"(.{0,120})(Advertise:|Begin Construction:|Complete Design:|Complete Construction:|Advertise)[:\s].{0,80}2022", text, flags=re.IGNORECASE):
        context = match.group(0)
        # find preceding line in the doc
        # get position
        start = match.start()
        # take substring before start and splitlines
        prev_text = text[:start]
        prev_lines = [ln.strip() for ln in prev_text.splitlines() if ln.strip()]
        if prev_lines:
            candidate = prev_lines[-1]
            candidate = re.sub(r'\s+', ' ', candidate).strip()
            if len(candidate) > 3 and candidate not in found_projects:
                found_projects.append(candidate)

result = {"projects": found_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cfHyLt4fnl8FkJTA47kfy1vu': 'file_storage/call_cfHyLt4fnl8FkJTA47kfy1vu.json'}

exec(code, env_args)
