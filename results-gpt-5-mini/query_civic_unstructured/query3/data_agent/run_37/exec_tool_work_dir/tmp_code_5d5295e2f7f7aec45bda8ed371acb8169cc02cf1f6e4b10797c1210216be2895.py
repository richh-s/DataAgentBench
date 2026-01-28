code = """import json, re

with open(var_call_qAIVVBQpLbB6atIJDbCLzuG1, 'r') as f:
    docs = json.load(f)

results = []
seen = set()

for doc in docs:
    text = doc.get('text', '')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if re.search(r'\b(FEMA|emergency)\b', ln, re.I):
            pn = None
            # look back for a line that likely is a project name
            for j in range(max(0, i-12), i+1):
                cand = lines[j]
                if not cand:
                    continue
                if re.search(r'\bProject\b', cand, re.I) or re.search(r'\bRepairs\b', cand, re.I) or re.search(r'\bImprovements\b', cand, re.I) or re.search(r'\bMaster Plan\b', cand, re.I) or re.search(r'\bFacility\b', cand, re.I):
                    pn = cand
                    break
            if not pn:
                for j in range(i-1, max(-1, i-12)-1, -1):
                    if lines[j]:
                        pn = lines[j]
                        break
            if not pn:
                continue
            pn = re.sub(r'\s+', ' ', pn).strip()
            # determine status by scanning forward
            status = 'unknown'
            for k in range(i, min(len(lines), i+13)):
                s = lines[k]
                if not s:
                    continue
                if re.search(r'under construction|Begin Construction|Begin construction', s, re.I):
                    status = 'under construction'
                    break
                if re.search(r'Construction was completed|Complete Construction|completed|Notice of completion', s, re.I):
                    status = 'completed'
                    break
                if re.search(r'Complete Design|Final Design|preliminary design|preliminary Design|design\b', s, re.I):
                    status = 'design'
                    break
                if re.search(r'Not Started|Not started|not started|Not Started', s, re.I):
                    status = 'not started'
                    break
            key = (pn.lower(), status)
            if key not in seen:
                seen.add(key)
                results.append({'Project_Name': pn, 'Status': status, 'Source_File': doc.get('filename')})

output = {'projects': results, 'project_names': [r['Project_Name'] for r in results]}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_qAIVVBQpLbB6atIJDbCLzuG1': 'file_storage/call_qAIVVBQpLbB6atIJDbCLzuG1.json'}

exec(code, env_args)
