code = """import json
import re

# Load data from storage file paths
with open(var_call_JB6TQEL3z93YnYHK9rnGpkHo, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_qNKgQ52ocQxIOP8yjhn1GgPu, 'r') as f:
    funding_rows = json.load(f)

def normalize_name(name):
    if not isinstance(name, str):
        return ''
    # remove parenthetical content and extra whitespace, lowercase
    name = re.sub(r"\(.*?\)", "", name)
    name = re.sub(r"[^\w\s&-]", " ", name)  # remove punctuation except & and -
    name = re.sub(r"\s+", " ", name).strip().lower()
    return name

# Extract project names under 'Capital Improvement Projects (Design)'
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    low = text.lower()
    marker = 'capital improvement projects (design)'
    idx = low.find(marker)
    if idx == -1:
        # try alternative phrasing
        marker_alt = 'capital improvement projects - design'
        idx = low.find(marker_alt)
        if idx != -1:
            marker = marker_alt
    if idx == -1:
        continue
    start = idx + len(marker)
    # find next section markers
    stop_tokens = ['capital improvement projects (construction)',
                   'capital improvement projects (not started)',
                   'capital improvement projects (design)',
                   '\ncapital improvement projects (construction)',
                   '\ncapital improvement projects (not started)']
    end = len(text)
    for tok in stop_tokens:
        j = low.find(tok, start)
        if j != -1 and j < end:
            end = j
    section = text[start:end]
    # split into lines and filter
    lines = [ln.strip() for ln in section.splitlines()]
    for ln in lines:
        if not ln:
            continue
        lnl = ln.lower()
        # exclude common boilerplate and lines that are clearly not project names
        exclude_keywords = ['updates', 'project schedule', 'page', 'agenda', 'item', 'subject', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion', 'cid:', 'begin construction', 'complete design', 'advertise', 'estimated schedule', 'updates:', 'project description', 'project updates']
        if any(k in lnl for k in exclude_keywords):
            continue
        if lnl.endswith(':'):
            continue
        if ln.isupper():
            continue
        # avoid lines that are clearly sentences (contain verbs)
        if re.search(r'\b(is|are|was|will|has|have|working|submitted|expected|awaiting|plans)\b', lnl):
            continue
        # simple heuristic: lines that are short headings (<=10 words) and contain letters
        if len(ln.split()) > 0 and len(ln.split()) <= 12 and re.search('[A-Za-z]', ln):
            # further clean: remove leading bullets or numbering
            clean_ln = re.sub(r'^[\d\.-\)\s]+', '', ln).strip()
            # ignore lines that look like table headers
            if len(clean_ln) < 3:
                continue
            design_projects.append(clean_ln)

# Deduplicate while preserving
seen = set()
design_projects_unique = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        design_projects_unique.append(p)

# Normalize funding rows into a map
funding_map = {}
for r in funding_rows:
    pname = r.get('Project_Name', '')
    amt = r.get('Amount', 0)
    try:
        amt_int = int(str(amt))
    except:
        try:
            amt_int = int(float(amt))
        except:
            continue
    norm = normalize_name(pname)
    if norm not in funding_map:
        funding_map[norm] = []
    funding_map[norm].append({'original': pname, 'amount': amt_int})

# For each design project, check funding > 50000
matched = []
for p in design_projects_unique:
    normp = normalize_name(p)
    if normp in funding_map:
        # check if any funding amounts > 50000
        if any(entry['amount'] > 50000 for entry in funding_map[normp]):
            matched.append({'project_name': p, 'normalized_name': normp, 'funding_records': funding_map[normp]})

result = {
    'count': len(matched),
    'matched_projects': [m['project_name'] for m in matched]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qNKgQ52ocQxIOP8yjhn1GgPu': 'file_storage/call_qNKgQ52ocQxIOP8yjhn1GgPu.json', 'var_call_JB6TQEL3z93YnYHK9rnGpkHo': 'file_storage/call_JB6TQEL3z93YnYHK9rnGpkHo.json'}

exec(code, env_args)
