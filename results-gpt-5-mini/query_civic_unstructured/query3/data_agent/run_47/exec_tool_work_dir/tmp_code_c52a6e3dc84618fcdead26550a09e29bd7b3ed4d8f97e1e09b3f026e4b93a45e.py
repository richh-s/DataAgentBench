code = """import json, re

path = var_call_F7UDdQqOSp06hyXJN6tIfdKY
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
seen = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'\bFEMA\b', line, re.I) or re.search(r'\bemergency\b', line, re.I):
            title = None
            title_idx = None
            for j in range(max(0, i-8), i+1)[::-1]:
                l = lines[j].strip()
                if not l:
                    continue
                if re.search(r'Project\b|Improvements|Repair|Repairs|Phase|Study|Plan|Park|Road|Bridge|Drainage|Walkway|Facility|Master Plan|Playground|Retaining Wall', l, re.I):
                    title = l
                    title_idx = j
                    break
                if 5 < len(l) < 120 and l == l.title() and len(l.split()) <= 8:
                    title = l
                    title_idx = j
                    break
            if not title:
                for j in range(i, min(len(lines), i+6)):
                    l = lines[j].strip()
                    if not l:
                        continue
                    if re.search(r'Project\b|Improvements|Repair|Repairs|Phase|Study|Plan|Park|Road|Bridge|Drainage|Walkway|Facility|Master Plan|Playground|Retaining Wall', l, re.I):
                        title = l
                        title_idx = j
                        break
            if not title:
                title = line.strip()
                title_idx = i
            block = '\n'.join(lines[title_idx:title_idx+12])
            block_lower = block.lower()
            status = None
            if re.search(r'under construction|construction was|begin construction', block_lower):
                if 'complete construction' in block_lower or 'construction was completed' in block_lower:
                    status = 'completed'
                else:
                    if 'begin construction' in block_lower or 'begin construction:' in block_lower:
                        status = 'design'
                    else:
                        status = 'completed'
            if re.search(r'complete design|preliminary design|design phase|design is', block_lower):
                status = 'design'
            if re.search(r'construction was completed|notice of completion|complete construction:', block_lower):
                status = 'completed'
            if re.search(r'not started|not begun|identified but not begun', block_lower):
                status = 'not started'
            if re.search(r'awaiting final fema|awaiting fema|awaiting federal', block_lower):
                if not status:
                    status = 'design'
            project_name = re.sub(r'\s+', ' ', title).strip()
            if project_name and project_name.lower() not in seen:
                seen.add(project_name.lower())
                candidates.append({'Project_Name': project_name, 'Status': status, 'Context_Line': line.strip()})

result = json.dumps(candidates, ensure_ascii=False)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_F7UDdQqOSp06hyXJN6tIfdKY': 'file_storage/call_F7UDdQqOSp06hyXJN6tIfdKY.json'}

exec(code, env_args)
