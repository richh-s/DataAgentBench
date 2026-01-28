code = """import json, re
from pathlib import Path
# load the Mongo query result from the stored file path variable
p = var_call_7LlutmHMvkqnp8WSh8dx7180
if isinstance(p, str) and Path(p).exists():
    data = json.loads(Path(p).read_text())
else:
    data = p

results = []

heading_re = re.compile(r"(?i)^(.*?(Project|Repairs|Improvements|Repair|Facility|Study|Plan|Program|Master Plan|Water Treatment|Warning Signs|Recovery).*)$")

for doc in data:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'(?i)\b(FEMA|emergency)\b', ln):
            # search backward for a heading within previous 10 lines
            heading = None
            for j in range(max(0,i-12), i+1):
                m = heading_re.match(lines[j])
                if m:
                    heading = lines[j]
            # if not found, also try to find a nearby line that ends with 'Project' or contains 'Project'
            if not heading:
                for j in range(max(0,i-12), i+1):
                    if 'Project' in lines[j] or 'project' in lines[j] or lines[j].endswith(':'):
                        heading = lines[j]
            if not heading:
                # fallback: take previous non-empty line
                for j in range(max(0,i-6), i+1):
                    if lines[j]:
                        heading = lines[j]
                        break
            # get status by scanning forward for 'Updates' or status-like phrases
            status = None
            for k in range(i, min(len(lines), i+12)):
                ln2 = lines[k]
                if re.search(r'(?i)Updates?:', ln2):
                    # collect following 3 non-empty lines
                    s_lines = []
                    for kk in range(k+1, min(len(lines), k+6)):
                        if lines[kk]:
                            s_lines.append(lines[kk])
                        else:
                            break
                    if s_lines:
                        status = ' '.join(s_lines)
                        break
                # look for direct status phrases
                if re.search(r'(?i)Project is currently under construction|Construction was completed|Complete Construction|completed|Complete Design|Awaiting|Awaiting final FEMA|Awaiting final FEMA|submitted|delayed|design', ln2):
                    status = ln2
                    break
            # normalize heading
            if heading:
                hn = re.sub(r'\s+', ' ', heading).strip(' :\n')
                results.append({'Project_Name': hn, 'Status': status if status else ''})

# deduplicate by project name
seen = set()
unique = []
for r in results:
    name = r['Project_Name']
    if name not in seen:
        seen.add(name)
        unique.append(r)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_7LlutmHMvkqnp8WSh8dx7180': 'file_storage/call_7LlutmHMvkqnp8WSh8dx7180.json'}

exec(code, env_args)
