code = """import json, re

# Load the civic documents and funding results from the provided storage file paths
with open(var_call_1M7sMqR2IpdPIJ3evyKp9uWW, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_Itip1R3wzAsvEId1gYMLkyOS, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Extract the text for each document and find project names under the "Capital Improvement Projects (Design)" section
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    start_idx = text.find('Capital Improvement Projects (Design)')
    if start_idx == -1:
        continue
    # find plausible end markers
    end_markers = ['Capital Improvement Projects (Construction)',
                   'Capital Improvement Projects (Not Started)',
                   'Capital Improvement Projects (Construction)',
                   'Capital Improvement Projects (Not Started)']
    end_idx = len(text)
    for m in end_markers:
        i = text.find(m, start_idx+1)
        if i != -1:
            end_idx = min(end_idx, i)
    section = text[start_idx:end_idx]
    # find lines that appear to be project titles followed by blank line and a '(cid:' update marker
    matches = re.findall(r"([^\n]+?)\n\s*\n\s*\(cid:", section)
    for m in matches:
        name = m.strip()
        # filter out lines that are unlikely to be project names
        if len(name) < 4:
            continue
        low = name.lower()
        if any(x in low for x in ['agenda', 'item', 'page', 'updates', 'project schedule', 'recommended action', 'discussion', 'meeting date']):
            continue
        design_projects.add(name)

# Normalize function for fuzzy matching with funding table
import unicodedata

def normalize(s):
    s = s.lower()
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    s = s.strip()
    return s

# Build set of funding project names with Amount > 50000
funded_names = []
for r in funding_records:
    try:
        amt = int(r.get('Amount', 0))
    except:
        try:
            amt = int(str(r.get('Amount','0')).replace(',', ''))
        except:
            amt = 0
    if amt > 50000:
        funded_names.append(r.get('Project_Name','').strip())

funded_set = set(funded_names)

# Precompute normalized funded names
funded_norms = {fn: normalize(fn) for fn in funded_set}

# Match design projects to funded projects using normalized substring matching
matched_design_projects = []
for dp in sorted(design_projects):
    dpn = normalize(dp)
    matched = False
    for fn, fn_norm in funded_norms.items():
        if dpn == fn_norm or dpn in fn_norm or fn_norm in dpn:
            matched = True
            break
    if matched:
        matched_design_projects.append(dp)

count = len(matched_design_projects)

result = {'count': count, 'matched_projects': matched_design_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FnYNtZP9uJz9tYMvaWsgr5mp': ['civic_docs'], 'var_call_zcwXW7ppv08WDgDZpxMecKLl': ['Funding'], 'var_call_1M7sMqR2IpdPIJ3evyKp9uWW': 'file_storage/call_1M7sMqR2IpdPIJ3evyKp9uWW.json', 'var_call_Itip1R3wzAsvEId1gYMLkyOS': 'file_storage/call_Itip1R3wzAsvEId1gYMLkyOS.json'}

exec(code, env_args)
