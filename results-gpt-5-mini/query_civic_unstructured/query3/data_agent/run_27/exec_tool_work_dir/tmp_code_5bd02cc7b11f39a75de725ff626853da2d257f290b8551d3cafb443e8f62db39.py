code = """import json, re

# Load the query_db result file path variable
path = var_call_bnz5n8E8p3dgBfZPrwv4WgyV

with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = []
seen = set()

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    current_section = None
    for i, line in enumerate(lines):
        s = line.strip()
        # update section
        low = s.lower()
        if 'capital improvement projects' in low and 'design' in low:
            current_section = 'design'
            continue
        if 'capital improvement projects' in low and 'construction' in low:
            current_section = 'completed'
            continue
        if 'capital improvement projects' in low and 'not started' in low:
            current_section = 'not started'
            continue
        if 'construction' in low and '(construction)' in s.lower():
            current_section = 'completed'
            continue
        if '(design)' in s.lower():
            current_section = 'design'
            continue
        if '(not started)' in s.lower() or 'not started' in low:
            current_section = 'not started'
            continue
        # identify potential project title lines
        if not s:
            continue
        if s.startswith('(cid'):
            continue
        if re.match(r'^(updates:|project schedule:|project description:)', s.lower()):
            continue
        # exclude header-like lines
        if len(s) > 200:
            continue
        # heuristic: title lines often start with uppercase letter or digit
        if not re.match(r'^[A-Z0-9]', s):
            continue
        # exclude lines that are clearly sentences (contain period and lowercase words)
        if re.search(r'[a-z]\.', s):
            pass
        # check nearby context for keywords
        # look ahead next 12 lines for keywords
        window = "\n".join(lines[i:i+12])
        if re.search(r'\b(fema|caloes|cal o es|cal o es|calo es|calo es|emergency|emergency warning|federal assistance|federal funding)\b', window, re.I):
            project_name = s
            # determine status: prefer current_section
            status = current_section
            # if not set, try infer from nearby window
            if not status:
                wlow = window.lower()
                if 'complete design' in wlow or 'final design' in wlow or 'finalize the design' in wlow or 'preliminary design' in wlow:
                    status = 'design'
                elif 'construction was completed' in wlow or 'complete construction' in wlow or 'completed' in wlow:
                    status = 'completed'
                elif 'advertise' in wlow or 'begin construction' in wlow or 'begin construction:' in wlow or 'begin construction' in wlow:
                    # ambiguous, mark as design
                    status = 'design'
                elif 'identified' in wlow and 'project' in wlow:
                    status = 'not started'
                else:
                    status = None
            if project_name not in seen:
                seen.add(project_name)
                found.append({'Project_Name': project_name, 'Status': status})

# Also scan for explicit mentions like "(FEMA Project)" anywhere and try to extract preceding project name
pattern = re.compile(r'([A-Za-z0-9 \-&\(\)\'\.,]{5,120}?)\s*\(FEMA Project\)', re.I)
for doc in docs:
    for m in pattern.finditer(doc.get('text','')):
        pname = m.group(1).strip()
        if pname and pname not in seen:
            seen.add(pname)
            found.append({'Project_Name': pname, 'Status': None})

# Output results
print("__RESULT__:")
print(json.dumps(found))"""

env_args = {'var_call_bnz5n8E8p3dgBfZPrwv4WgyV': 'file_storage/call_bnz5n8E8p3dgBfZPrwv4WgyV.json'}

exec(code, env_args)
