code = """import json, re

path = var_call_bnz5n8E8p3dgBfZPrwv4WgyV
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = []
seen = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if len(s) > 200:
            continue
        # candidate lines that mention 'Project' or end with 'Repairs' or 'Project Name'
        if 'project' in s.lower() or s.lower().endswith('repairs') or 'fema' in s.lower():
            if not re.match(r'^[A-Z0-9]', s):
                continue
            window = "\n".join(lines[max(0, i-6): i+7])
            if re.search(r"\b(fema|emergency|emergency warning|caloes|cal o es|federal|federal assistance|federal funding)\b", window, re.I):
                pname = re.sub(r"\s+", " ", s)
                # determine status from nearby window
                wlow = window.lower()
                status = None
                if 'complete' in wlow or 'completed' in wlow or 'complete construction' in wlow or 'construction was completed' in wlow:
                    status = 'completed'
                elif 'design' in wlow or 'final design' in wlow or 'finalize the design' in wlow or 'preliminary design' in wlow:
                    status = 'design'
                elif 'not started' in wlow or ('identified' in wlow and 'project' in wlow):
                    status = 'not started'
                # normalize name
                if pname not in seen:
                    seen.add(pname)
                    found.append({'Project_Name': pname, 'Status': status})

# also look for explicit '(FEMA Project)' mentions
for doc in docs:
    for m in re.finditer(r"([A-Za-z0-9 \-\&\(\)\'\.,]{5,120}?)\s*\(FEMA Project\)", doc.get('text',''), re.I):
        pname = m.group(1).strip()
        if pname and pname not in seen:
            seen.add(pname)
            # try to infer status by searching nearby
            idx = doc.get('text','').lower().find(m.group(0).lower())
            snippet = doc.get('text','')[max(0, idx-200): idx+200]
            s = snippet.lower()
            status = None
            if 'complete' in s or 'completed' in s:
                status = 'completed'
            elif 'design' in s or 'final design' in s:
                status = 'design'
            elif 'not started' in s:
                status = 'not started'
            found.append({'Project_Name': pname, 'Status': status})

print("__RESULT__:")
print(json.dumps(found))"""

env_args = {'var_call_bnz5n8E8p3dgBfZPrwv4WgyV': 'file_storage/call_bnz5n8E8p3dgBfZPrwv4WgyV.json'}

exec(code, env_args)
