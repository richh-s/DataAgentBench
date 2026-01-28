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
    name = re.sub(r"\([^)]*\)", "", name)
    # Lowercase
    name = name.lower()
    # Remove non-alphanumeric characters
    name = re.sub(r"[^a-z0-9]", " ", name)
    # Collapse spaces
    name = re.sub(r"\s+", " ", name).strip()
    return name

cap_design_projects = set()
# Pattern to identify the design section
design_header_re = re.compile(r"capital improvement projects\s*\(\s*design\s*\)", flags=re.I)

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    m = design_header_re.search(text)
    if not m:
        continue
    start = m.end()
    # find earliest occurrence of next section headers
    end_candidates = []
    for hdr in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', '\n\nCapital Improvement Projects (Construction)', '\n\nCapital Improvement Projects (Not Started)']:
        pos = text.lower().find(hdr.lower(), start)
        if pos != -1:
            end_candidates.append(pos)
    end = min(end_candidates) if end_candidates else len(text)
    section = text[start:end]
    # Split the section into lines and extract potential project names by detecting lines that look like titles
    lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    # Heuristic: project names are lines that are Title Case or contain keywords; also longer than short words
    for i, line in enumerate(lines):
        # Skip lines that appear to be headers like 'Updates:' or 'Project Schedule:'
        low = line.lower()
        if any(x in low for x in ['updates', 'project schedule', 'advertise', 'begin construction', 'page', 'agenda', 'item', 'discussion', 'updates:', 'project description']):
            continue
        # Filter out lines that are too long or too short
        if len(line) < 4 or len(line) > 200:
            continue
        # If line ends with 'Project' or contains keywords like 'road', 'park', 'storm drain', 'walkway', treat as project
        if re.search(r"\b(project|road|park|drain|walkway|street|signal|water|playground|curb|retaining wall|slope|biofilter|skate|skate park)\b", low):
            cap_design_projects.add(line)
        else:
            # Also consider lines that are Title Case (heuristic)
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
