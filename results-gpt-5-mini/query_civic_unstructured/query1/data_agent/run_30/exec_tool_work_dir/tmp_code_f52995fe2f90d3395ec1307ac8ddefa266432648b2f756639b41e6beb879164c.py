code = """import json
import re

# Load the previous tool results from storage variables
with open(var_call_qZ6ppq6qovP7stGAd8tlr74A, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_cUogTAB1VycKJDABHElVQES8, 'r') as f:
    funding_records = json.load(f)

# Helper to normalize names
def normalize(name):
    if name is None:
        return ""
    # Remove parenthetical contents
    name = re.sub("\\([^)]*\\)", "", name)
    name = name.lower()
    name = re.sub("[^a-z0-9]", " ", name)
    name = re.sub("\\s+", " ", name).strip()
    return name

cap_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lower = text.lower()
    key = 'capital improvement projects (design)'
    idx = lower.find(key)
    if idx == -1:
        continue
    start = idx + len(key)
    # find next headers
    candidates = []
    for hdr in ['capital improvement projects (construction)', 'capital improvement projects (not started)']:
        p = lower.find(hdr, start)
        if p != -1:
            candidates.append(p)
    end = min(candidates) if candidates else len(text)
    section = text[start:end]
    lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    for line in lines:
        low = line.lower()
        if any(x in low for x in ['updates', 'project schedule', 'advertise', 'begin construction', 'page', 'agenda', 'item', 'discussion', 'project description']):
            continue
        if len(line) < 4 or len(line) > 200:
            continue
        keywords = ['project', 'road', 'park', 'drain', 'walkway', 'street', 'signal', 'water', 'playground', 'curb', 'retaining wall', 'slope', 'biofilter', 'skate', 'skate park', 'median']
        if any(k in low for k in keywords) or line.endswith('Project') or line.endswith('project'):
            cap_design_projects.add(line)
        else:
            # title case heuristic
            if re.match(r"^[A-Z][A-Za-z0-9 &,-.:']+$", line):
                cap_design_projects.add(line)

# Normalize project names from civic docs
norm_cap_projects = {normalize(p): p for p in cap_design_projects if p}

# Process funding records (these were filtered to Amount > 50000 already)
matched_projects = set()
for fr in funding_records:
    fund_name = fr.get('Project_Name')
    if fund_name is None:
        continue
    norm_f = normalize(fund_name)
    for norm_p, orig_p in norm_cap_projects.items():
        if not norm_p:
            continue
        if norm_p in norm_f or norm_f in norm_p:
            matched_projects.add(orig_p)

result = {
    'count': len(matched_projects),
    'matched_projects': sorted(list(matched_projects))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qZ6ppq6qovP7stGAd8tlr74A': 'file_storage/call_qZ6ppq6qovP7stGAd8tlr74A.json', 'var_call_cUogTAB1VycKJDABHElVQES8': 'file_storage/call_cUogTAB1VycKJDABHElVQES8.json'}

exec(code, env_args)
