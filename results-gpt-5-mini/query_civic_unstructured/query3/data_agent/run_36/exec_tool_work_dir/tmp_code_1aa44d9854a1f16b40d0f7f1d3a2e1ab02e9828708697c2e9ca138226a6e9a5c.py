code = """import json
from pathlib import Path
p = var_call_7LlutmHMvkqnp8WSh8dx7180
if isinstance(p, str) and Path(p).exists():
    data = json.loads(Path(p).read_text())
else:
    data = p

keywords = ['project','repairs','improvements','repair','facility','study','plan','program','master plan','warning signs','recovery','retaining wall']
results = []
seen = set()

for doc in data:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if 'fema' in ln.lower() or 'emergency' in ln.lower():
            # look back up to 12 lines for a heading containing keywords
            heading = None
            for j in range(max(0, i-12), i+1):
                l = lines[j]
                if any(kw in l.lower() for kw in keywords):
                    heading = l
            if not heading:
                # fallback: previous non-empty line
                for j in range(max(0,i-6), i+1):
                    if lines[j]:
                        heading = lines[j]
                        break
            if heading:
                hn = ' '.join(heading.split())
                # filter out generic lines
                if len(hn) > 3 and not hn.lower().startswith('page') and 'agenda' not in hn.lower():
                    if hn not in seen:
                        seen.add(hn)
                        results.append({'Project_Name': hn, 'Status': ''})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_7LlutmHMvkqnp8WSh8dx7180': 'file_storage/call_7LlutmHMvkqnp8WSh8dx7180.json'}

exec(code, env_args)
