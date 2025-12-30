code = """import json, re
from pathlib import Path

path = Path(var_call_YTPEzhMd2WjR5w3u0aYD7BGH)
with path.open() as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if ('Project' in line) or ('Improvements' in line) or ('Repairs' in line) or ('Resurfacing' in line) or ('Warning Sirens' in line):
            name = line
            window = "\n".join(lines[i:i+5])
            if re.search(r'FEMA|CalOES|CalJPIA|Woolsey|Disaster', window, re.I):
                ptype = 'disaster'
            else:
                ptype = 'capital'
            m = re.search(r'Begin Construction[^0-9]*([A-Za-z]+\s*2022|2022[^\n]*)', window, re.I)
            st = m.group(1).strip() if m else ''
            projects.append({'Project_Name': name, 'type': ptype, 'st': st})

disaster_2022 = {p['Project_Name'] for p in projects if p['type']=='disaster' and '2022' in p['st']}

path2 = Path(var_call_pLjOH9kbzJkpMv2dh8n3GHrC)
with path2.open() as f:
    funding = json.load(f)

names_lower = {n.lower() for n in disaster_2022}

total = 0
for row in funding:
    if row['Project_Name'].lower() in names_lower:
        total += int(row['Amount'])

print('__RESULT__:')
print(json.dumps(total))"""

env_args = {'var_call_YTPEzhMd2WjR5w3u0aYD7BGH': 'file_storage/call_YTPEzhMd2WjR5w3u0aYD7BGH.json', 'var_call_pLjOH9kbzJkpMv2dh8n3GHrC': 'file_storage/call_pLjOH9kbzJkpMv2dh8n3GHrC.json'}

exec(code, env_args)
