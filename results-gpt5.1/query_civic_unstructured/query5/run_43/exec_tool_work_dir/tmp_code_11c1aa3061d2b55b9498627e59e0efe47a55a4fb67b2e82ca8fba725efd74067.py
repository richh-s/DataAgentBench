code = """import json, re
from pathlib import Path

# Load full civic docs
path = Path(var_call_YTPEzhMd2WjR5w3u0aYD7BGH)
with path.open() as f:
    civic_docs = json.load(f)

# Very rough heuristic extraction: project name lines followed by possible dates
projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line or 'Resurfacing' in line or 'Warning Sirens' in line:
            name = line
            window = '\n'.join(lines[i:i+5])
            # look for type keywords
            ptype = 'disaster' if re.search(r'FEMA|CalOES|CalJPIA|Woolsey|Disaster', window, re.I) else 'capital'
            # look for a start date containing 2022
            st_match = re.search(r'(Begin Construction|Start|st)[:\s]*(.*2022[^\n]*)', window, re.I)
            st = st_match.group(2).strip() if st_match else ''
            projects.append({'Project_Name': name, 'type': ptype, 'st': st})

# Filter disaster projects with start containing 2022
disaster_2022 = {p['Project_Name'] for p in projects if p['type']=='disaster' and '2022' in p['st']}

# Load funding table
path2 = Path(var_call_pLjOH9kbzJkpMv2dh8n3GHrC)
with path2.open() as f:
    funding = json.load(f)

# Match by project name (exact match) for now
names_lower = {n.lower() for n in disaster_2022}

total = 0
for row in funding:
    if row['Project_Name'].lower() in names_lower:
        total += int(row['Amount'])

result = total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YTPEzhMd2WjR5w3u0aYD7BGH': 'file_storage/call_YTPEzhMd2WjR5w3u0aYD7BGH.json', 'var_call_pLjOH9kbzJkpMv2dh8n3GHrC': 'file_storage/call_pLjOH9kbzJkpMv2dh8n3GHrC.json'}

exec(code, env_args)
