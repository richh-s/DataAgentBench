code = """import re, json
from pathlib import Path

path = Path(var_call_V6M3AKnxaPZ2NomV2QZm3Dvv)
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

projects_2022 = set()
for match in re.finditer(r'\n([A-Z0-9][^\n]{5,80})\n[\s\S]{0,200}?2022', texts):
    name = match.group(1).strip()
    projects_2022.add(name)

for match in re.finditer(r'\n([^\n]{5,80}FEMA[^\n]{0,40})\n[\s\S]{0,200}?2022', texts):
    projects_2022.add(match.group(1).strip())

funding = var_call_fsnMnMGYuVlZlVb0U5IhMidD

disaster_funding_2022 = 0
projects_counted = []
for row in funding:
    name = row['Project_Name']
    if not (('(FEMA' in name) or ('(CalOES' in name) or ('(CalJPIA' in name) or ('Disaster' in name)):
        continue
    base_name = name.split('(')[0].strip()
    in_2022 = any(base_name in p for p in projects_2022)
    if not in_2022 and base_name:
        pattern = re.escape(base_name)
        if re.search(pattern + r'[\s\S]{0,200}?2022|2022[\s\S]{0,200}?' + pattern, texts):
            in_2022 = True
    if in_2022:
        disaster_funding_2022 += int(row['Amount'])
        projects_counted.append(name)

result = {"total_disaster_funding_started_2022": disaster_funding_2022, "projects_counted": projects_counted}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V6M3AKnxaPZ2NomV2QZm3Dvv': 'file_storage/call_V6M3AKnxaPZ2NomV2QZm3Dvv.json', 'var_call_fsnMnMGYuVlZlVb0U5IhMidD': 'file_storage/call_fsnMnMGYuVlZlVb0U5IhMidD.json'}

exec(code, env_args)
