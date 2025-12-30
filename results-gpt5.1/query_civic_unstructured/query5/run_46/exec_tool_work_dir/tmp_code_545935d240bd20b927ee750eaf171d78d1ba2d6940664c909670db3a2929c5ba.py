code = """import json, re
from pathlib import Path

path = Path(var_call_uc9M00Bcoal84raBdElG9Rjg)
with path.open() as f:
    civic_docs = json.load(f)

funding = var_call_1lFvlL93oufXi71u0Ul7F26O

projects = {}
for doc in civic_docs:
    text = doc.get('text','')
    sections = re.split(r'\n\s*\n', text)
    current_type = None
    for sec in sections:
        head = sec.strip().lower()
        if 'disaster recovery projects' in head:
            current_type = 'disaster'
        elif 'capital improvement projects' in head:
            current_type = 'capital'
        m = re.search(r'(20\d{2}[^\n]+)', sec)
        if m and current_type:
            name = m.group(1).strip()
            if not name[0].isdigit():
                continue
            st_match = re.search(r'(20\d{2}[^\n]*)', sec)
            st = st_match.group(1).strip() if st_match else ''
            proj = projects.setdefault(name, {'type': current_type, 'st': st})
            proj['type'] = current_type
            proj['st'] = st

def norm(n):
    return re.sub(r'\s+',' ', n.lower()).strip()

proj_year = {}
for name, info in projects.items():
    st = info.get('st','')
    y = None
    m = re.search(r'(20\d{2})', st)
    if m:
        y = m.group(1)
    proj_year[norm(name)] = {'year': y, 'type': info.get('type')}

total = 0
for row in funding:
    pname = row['Project_Name']
    key = norm(pname)
    info = proj_year.get(key)
    if info and info['year'] == '2022' and info['type'] == 'disaster':
        total += int(row['Amount'])

result = total

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uc9M00Bcoal84raBdElG9Rjg': 'file_storage/call_uc9M00Bcoal84raBdElG9Rjg.json', 'var_call_1lFvlL93oufXi71u0Ul7F26O': 'file_storage/call_1lFvlL93oufXi71u0Ul7F26O.json', 'var_call_NVN7R7ttV6KjBWTFK9mSy7jy': ['civic_docs'], 'var_call_W7ummdj6XnhQI6dgKx4ida1S': ['Funding']}

exec(code, env_args)
