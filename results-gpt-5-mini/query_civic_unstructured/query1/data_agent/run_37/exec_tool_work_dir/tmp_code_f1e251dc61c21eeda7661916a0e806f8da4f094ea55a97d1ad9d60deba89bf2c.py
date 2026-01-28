code = """import json, unicodedata

# Load data
with open(var_call_1M7sMqR2IpdPIJ3evyKp9uWW, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_Itip1R3wzAsvEId1gYMLkyOS, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Find design projects by simple line-based parsing
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    start_pos = text.find('Capital Improvement Projects (Design)')
    if start_pos == -1:
        continue
    # determine end of section
    end_pos = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        p = text.find(marker, start_pos+1)
        if p != -1:
            end_pos = min(end_pos, p)
    section = text[start_pos:end_pos]
    lines = section.splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # check next two lines exist and pattern matches: blank line then a line starting with '(cid:' or 'Updates:' or '(cid)'
        if i+2 < n:
            if lines[i+1].strip() == '' and lines[i+2].strip().startswith('(cid:'):
                name = line_stripped
                low = name.lower()
                if len(name) < 4:
                    continue
                if any(x in low for x in ['agenda', 'item', 'page', 'updates', 'project schedule', 'recommended action', 'discussion', 'meeting date']):
                    continue
                design_projects.add(name)

# normalize helper
import re

def normalize(s):
    s = s or ''
    s = s.lower()
    s = unicodedata.normalize('NFKD', s)
    s = re.sub('[^a-z0-9]+', ' ', s)
    return s.strip()

# build funded names with amount > 50000
funded = []
for r in funding_records:
    amt = 0
    try:
        amt = int(r.get('Amount', 0))
    except:
        try:
            amt = int(str(r.get('Amount','0')).replace(',', ''))
        except:
            amt = 0
    if amt > 50000:
        funded.append(r.get('Project_Name','').strip())

funded_norms = {fn: normalize(fn) for fn in funded}

# match design projects to funded projects
matched = []
for dp in sorted(design_projects):
    dpn = normalize(dp)
    for fn, fnn in funded_norms.items():
        if dpn == fnn or dpn in fnn or fnn in dpn:
            matched.append(dp)
            break

result = {'count': len(matched), 'matched_projects': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FnYNtZP9uJz9tYMvaWsgr5mp': ['civic_docs'], 'var_call_zcwXW7ppv08WDgDZpxMecKLl': ['Funding'], 'var_call_1M7sMqR2IpdPIJ3evyKp9uWW': 'file_storage/call_1M7sMqR2IpdPIJ3evyKp9uWW.json', 'var_call_Itip1R3wzAsvEId1gYMLkyOS': 'file_storage/call_Itip1R3wzAsvEId1gYMLkyOS.json'}

exec(code, env_args)
