code = """import json, re

path = var_call_F7UDdQqOSp06hyXJN6tIfdKY
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
seen = set()

for doc in docs:
    text = doc.get('text','')
    # find candidate project-like phrases
    for m in re.finditer(r"([A-Z][A-Za-z0-9 &,'\-]{3,120}?(?:Project|Improvements|Repairs|Repair|Phase|Study|Plan|Park|Road|Bridge|Drainage|Walkway|Facility|Master Plan|Playground|Retaining Wall))", text):
        name = m.group(1).strip()
        key = name.lower()
        if key in seen:
            continue
        # ensure the document contains FEMA or emergency
        if re.search(r"\bFEMA\b|\bemergency\b", text, re.I):
            seen.add(key)
            projects.append({"Project_Name": name})

# fallback: if nothing found, also try lines containing 'FEMA' and grab neighboring words
if not projects:
    for doc in docs:
        text = doc.get('text','')
        lines = text.splitlines()
        for i,l in enumerate(lines):
            if re.search(r"\bFEMA\b|\bemergency\b", l, re.I):
                # take previous non-empty line
                for j in range(i-1, max(-1, i-6), -1):
                    if j<0: break
                    candidate = lines[j].strip()
                    if 5 < len(candidate) < 140:
                        key = candidate.lower()
                        if key not in seen:
                            seen.add(key)
                            projects.append({"Project_Name": candidate})
                        break

result = json.dumps(projects, ensure_ascii=False)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_F7UDdQqOSp06hyXJN6tIfdKY': 'file_storage/call_F7UDdQqOSp06hyXJN6tIfdKY.json'}

exec(code, env_args)
