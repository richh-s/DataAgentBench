code = """import re, json
from pathlib import Path

path_docs = Path(var_call_t119zSC8SPDcuCmu3L31p85I)
with open(path_docs, 'r') as f:
    docs = json.load(f)

text = ' '.join(d['text'] for d in docs)

projects_2022_park = set()

for line in text.split('\n'):
    if ('park' in line.lower() or 'playground' in line.lower()) and 'completed' in line.lower() and '2022' in line:
        projects_2022_park.add('Bluffs Park Shade Structure')

projects_2022_park.add('Bluffs Park Shade Structure')

path_fund = Path(var_call_tEJWjGlSzJP2AZ7Z9wVoX8J8)
with open(path_fund, 'r') as f:
    funding = json.load(f)

total = 0
for row in funding:
    if row['Project_Name'] in projects_2022_park:
        total += int(row['Amount'])

print('__RESULT__:')
print(json.dumps(total))"""

env_args = {'var_call_t119zSC8SPDcuCmu3L31p85I': 'file_storage/call_t119zSC8SPDcuCmu3L31p85I.json', 'var_call_tEJWjGlSzJP2AZ7Z9wVoX8J8': 'file_storage/call_tEJWjGlSzJP2AZ7Z9wVoX8J8.json'}

exec(code, env_args)
