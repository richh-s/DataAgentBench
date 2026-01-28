code = """import re, json
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_t119zSC8SPDcuCmu3L31p85I)
with open(path_docs, 'r') as f:
    docs = json.load(f)

text = ' '.join(d['text'] for d in docs)

# Heuristic extraction of park-related projects completed in 2022
projects_2022_park = set()

# Look for lines containing 'Park' and 'completed' and '2022'
for line in text.split('\n'):
    if ('park' in line.lower() or 'playground' in line.lower()) and 'completed' in line.lower() and '2022' in line:
        # project name heuristically: up to 8 words before 'completed'
        m = re.search(r'([A-Z][A-Za-z0-9 &/\'-]{3,100})[^\n]*completed[^\n]*2022', line)
        if m:
            name = m.group(1).strip()
            projects_2022_park.add(name)

# Manually add clearly park-related 2022 completions seen in preview
# From preview we saw: 'Bluffs Park Shade Structure' completed November 2022
projects_2022_park.add('Bluffs Park Shade Structure')

# Load funding table
path_fund = Path(var_call_tEJWjGlSzJP2AZ7Z9wVoX8J8)
with open(path_fund, 'r') as f:
    funding = json.load(f)

total = 0
matched_projects = []
for row in funding:
    if row['Project_Name'] in projects_2022_park:
        amt = int(row['Amount'])
        total += amt
        matched_projects.append({'Project_Name': row['Project_Name'], 'Amount': amt})

result = {'total_funding_2022_park_completed': total, 'projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_t119zSC8SPDcuCmu3L31p85I': 'file_storage/call_t119zSC8SPDcuCmu3L31p85I.json', 'var_call_tEJWjGlSzJP2AZ7Z9wVoX8J8': 'file_storage/call_tEJWjGlSzJP2AZ7Z9wVoX8J8.json'}

exec(code, env_args)
