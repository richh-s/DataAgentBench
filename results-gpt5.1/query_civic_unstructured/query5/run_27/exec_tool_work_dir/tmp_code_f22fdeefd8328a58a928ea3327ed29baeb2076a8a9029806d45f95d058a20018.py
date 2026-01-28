code = """import re, json
from pathlib import Path

# Load full civic docs result
path = Path(var_call_HRI4PW8QV1GTGI4uWDKyXvYP)
with path.open() as f:
    civic_docs = json.load(f)

# Disaster-related project names with 2022 start
disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc.get('text','')
    # crude split on double newlines for project-like blocks
    blocks = re.split(r"\n\s*\n", text)
    for b in blocks:
        if 'disaster' not in b.lower() and 'fema' not in b.lower() and 'woolsey' not in b.lower():
            continue
        # find year-like patterns for 2022 in block
        if '2022' not in b:
            continue
        # look for lines that look like project titles
        lines = [ln.strip() for ln in b.split('\n') if ln.strip()]
        for i, ln in enumerate(lines):
            if re.search(r"project", ln, re.I):
                # require some cue that this is start or schedule mentioning 2022
                around = '\n'.join(lines[max(0,i-2):i+3])
                if 'Begin Construction' in around or 'Start' in around or 'Design' in around or 'Not Started' in around:
                    # assume line itself is the project name
                    name = re.sub(r"[\u200b\ufeff]", "", ln)
                    disaster_projects_2022.add(name)

# Also add any obviously disaster-suffixed projects mentioned with 2022
for doc in civic_docs:
    text = doc.get('text','')
    if '2022' not in text:
        continue
    for m in re.finditer(r"([A-Z0-9][A-Za-z0-9 &/.-]+?(?:\s*\((?:FEMA|CalOES|CalJPIA)[^)]*\)))", text):
        span = m.group(1)
        if 'project' in span.lower():
            disaster_projects_2022.add(span.strip())

result = sorted(disaster_projects_2022)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HRI4PW8QV1GTGI4uWDKyXvYP': 'file_storage/call_HRI4PW8QV1GTGI4uWDKyXvYP.json', 'var_call_P6B4Pp4mHIL5Skb0Zvflh20B': 'file_storage/call_P6B4Pp4mHIL5Skb0Zvflh20B.json'}

exec(code, env_args)
