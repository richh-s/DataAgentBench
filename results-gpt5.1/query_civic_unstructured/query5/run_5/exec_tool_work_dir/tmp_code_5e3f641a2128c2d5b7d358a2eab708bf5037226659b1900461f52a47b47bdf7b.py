code = """import re, json
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_HA3G875VP1SZt1QW81T7quiX)
with path_docs.open() as f:
    docs = json.load(f)

# Simple heuristic: disaster projects contain FEMA, CalOES, CalJPIA, or the word 'Disaster' and have a year in the line
projects = {}
for d in docs:
    text = d.get('text','')
    for line in text.split('\n'):
        if any(k in line for k in ['FEMA','CalOES','CalJPIA','Disaster']):
            m_year = re.search(r'(20\d{2})', line)
            if not m_year:
                continue
            year = m_year.group(1)
            name = line.strip()
            if not name:
                continue
            proj = projects.setdefault(name, {'years': set()})
            proj['years'].add(year)

# Flatten to mapping from project name keyword to whether it has 2022 start
keys_2022 = []
for name, info in projects.items():
    if '2022' in info['years']:
        keys_2022.append(name)

result = {'disaster_2022_names_sample': keys_2022[:50]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HA3G875VP1SZt1QW81T7quiX': 'file_storage/call_HA3G875VP1SZt1QW81T7quiX.json', 'var_call_IcBZilRVasxcAhdwzTJthD9M': 'file_storage/call_IcBZilRVasxcAhdwzTJthD9M.json'}

exec(code, env_args)
