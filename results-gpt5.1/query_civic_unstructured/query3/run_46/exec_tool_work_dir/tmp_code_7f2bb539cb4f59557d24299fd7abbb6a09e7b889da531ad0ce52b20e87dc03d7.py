code = """import re, json as _json
from pathlib import Path

path_civic = Path(var_call_YS1wJmRGQQ3tRC9qJ84RCvmr)
with open(path_civic, 'r') as f:
    civic_docs = _json.load(f)

path_fund = Path(var_call_dPoWP6fbPitIM2IRJYeGULMl)
with open(path_fund, 'r') as f:
    funding = _json.load(f)

fund_names = {row['Project_Name'] for row in funding}

related_projects = {}

for doc in civic_docs:
    text = doc['text']
    for para in re.split('\\n\\s*\\n', text):
        if re.search('(?i)emergency|FEMA', para):
            for name in fund_names:
                if name in para:
                    status = None
                    m = re.search('(?i)(design|completed|not started)', para)
                    if m:
                        status = m.group(1).lower()
                    if name not in related_projects:
                        related_projects[name] = status

results = []
for row in funding:
    name = row['Project_Name']
    if re.search('(?i)FEMA|emergency', name) or name in related_projects:
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': related_projects.get(name)
        })

print('__RESULT__:')
print(_json.dumps(results))"""

env_args = {'var_call_YS1wJmRGQQ3tRC9qJ84RCvmr': 'file_storage/call_YS1wJmRGQQ3tRC9qJ84RCvmr.json', 'var_call_dPoWP6fbPitIM2IRJYeGULMl': 'file_storage/call_dPoWP6fbPitIM2IRJYeGULMl.json'}

exec(code, env_args)
