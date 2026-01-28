code = """import re, json, pandas as pd

path_docs = var_call_BDw70ni8117NDNAZ51i2exyr
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_4XPsRAW1Xzg8SR3hwSWqljjt)
funding['Amount'] = funding['Amount'].astype(int)

park_keywords = ['park', 'playground']

project_pattern = re.compile('^(?P<name>.+?)(?:\\n\\(cid:190\\)|\\n\\u2022|- )', re.MULTILINE)

completed_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text or 'completed' not in text.lower():
        continue
    if not any(kw in text.lower() for kw in park_keywords):
        continue
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'construction was completed' in line.lower() and '2022' in line:
            start = max(0, i-3)
            context = '\n'.join(lines[start:i+1])
            m = project_pattern.search(context)
            if m:
                name = m.group('name').strip()
                if any(kw in name.lower() for kw in park_keywords) or any(kw in context.lower() for kw in park_keywords):
                    completed_2022_projects.add(name)

funding_2022_park = funding[funding['Project_Name'].isin(completed_2022_projects)]

total_funding = int(funding_2022_park['Amount'].sum())

result = {
    'completed_2022_park_projects': sorted(list(completed_2022_projects)),
    'total_funding': total_funding
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_BDw70ni8117NDNAZ51i2exyr': 'file_storage/call_BDw70ni8117NDNAZ51i2exyr.json', 'var_call_4XPsRAW1Xzg8SR3hwSWqljjt': 'file_storage/call_4XPsRAW1Xzg8SR3hwSWqljjt.json'}

exec(code, env_args)
