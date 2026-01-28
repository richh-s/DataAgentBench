code = """import re, json
from pathlib import Path

# Load full civic docs
path_civic = Path(var_call_YS1wJmRGQQ3tRC9qJ84RCvmr)
import json as _json
with open(path_civic, 'r') as f:
    civic_docs = _json.load(f)

# Load full funding table
path_fund = Path(var_call_dPoWP6fbPitIM2IRJYeGULMl)
with open(path_fund, 'r') as f:
    funding = _json.load(f)

# Extract project names from civic text that look like known funded projects
fund_names = {row['Project_Name'] for row in funding}

related_projects = {}

for doc in civic_docs:
    text = doc['text']
    # Only process paragraphs mentioning emergency or FEMA
    for para in re.split(r'\n\s*\n', text):
        if re.search(r'(?i)emergency|FEMA', para):
            for name in fund_names:
                if name in para:
                    # crude status extraction
                    status = None
                    m = re.search(r'(?i)(design|completed|not started)', para)
                    if m:
                        status = m.group(1).lower()
                    if name not in related_projects:
                        related_projects[name] = status

# Now collect funding info for projects whose name suggests FEMA or emergency OR found above
results = []
for row in funding:
    name = row['Project_Name']
    if re.search(r'(?i)FEMA|emergency', name) or name in related_projects:
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': related_projects.get(name)
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_YS1wJmRGQQ3tRC9qJ84RCvmr': 'file_storage/call_YS1wJmRGQQ3tRC9qJ84RCvmr.json', 'var_call_dPoWP6fbPitIM2IRJYeGULMl': 'file_storage/call_dPoWP6fbPitIM2IRJYeGULMl.json'}

exec(code, env_args)
