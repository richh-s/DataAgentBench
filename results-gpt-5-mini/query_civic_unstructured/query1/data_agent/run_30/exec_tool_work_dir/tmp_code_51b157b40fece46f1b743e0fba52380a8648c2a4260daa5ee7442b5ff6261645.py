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
# Patterns to identify the design section and possible section terminators
design_header_re = re.compile(r"capital improvement projects\s*\(\s*design\s*\)", flags=re.I)
end_section_re = re.compile(r"capital improvement projects\s*\(\s*(construction|not started)\s*\)|capital improvement projects \(|capital improvement projects\\n|capital improvement projects\s*\(construction\)|capital improvement projects\s*\(not started\)", flags=re.I)
# Simpler approach: find header position and stop at known next headers like 'Capital Improvement Projects (Construction)' or 'Capital Improvement Projects (Not Started)' or next major heading like 'Capital Improvement Projects (Construction)' or 'Capital Improvement Projects (Not Started)'
next_headers = [r"Capital Improvement Projects (Construction)", r"Capital Improvement Projects (Not Started)", r"Capital Improvement Projects (Construction)", r"Capital Improvement Projects (Not Started)", r"Capital Improvement Projects \(Construction\)", r"Capital Improvement Projects \(Not Started\)", r"Capital Improvement Projects (Construction)"]

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    m = design_header_re.search(text)
    if not m:
        continue
    start = m.end()
    # find earliest occurrence of any next header after start
    end = len(text)
    for hdr in next_headers:
        try:
            pos = text.lower().find(hdr.lower(), start)
        except Exception:
            pos = -1
        if pos != -1:
            end = min(end, pos)
    section = text[start:end]
    # Split the section into blocks by two or more newlines
    parts = re.split(r"\n{2,}", section)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Take the first line as candidate project name
        first_line = part.splitlines()[0].strip()
        # Filter out lines that are clearly not project names
        if len(first_line) < 3 or len(first_line) > 200:
            continue
        low = first_line.lower()
        if any(x in low for x in ['updates', 'project schedule', 'page', 'agenda', 'item', 'discussion']):
            continue
        if first_line.startswith('(') or first_line.endswith(':'):
            continue
        # Heuristic: must contain at least one letter
        if not re.search(r"[a-zA-Z]", first_line):
            continue
        cap_design_projects.add(first_line)

# Normalize project names from civic docs
norm_cap_projects = {normalize(p): p for p in cap_design_projects}

# Process funding records (these already have Amount > 50000 from the earlier query)
matched_projects = set()
for fr in funding_records:
    fund_name = fr.get('Project_Name') or fr.get('Project_Name'.lower())
    if fund_name is None:
        continue
    norm_f = normalize(fund_name)
    # Try to match by normalization: if any normalized civic project is substring of norm_f or vice versa
    for norm_p, orig_p in norm_cap_projects.items():
        if not norm_p:
            continue
        if norm_p in norm_f or norm_f in norm_p:
            matched_projects.add(orig_p)

result = {
    'count': len(matched_projects),
    'matched_projects': sorted(list(matched_projects))
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qZ6ppq6qovP7stGAd8tlr74A': 'file_storage/call_qZ6ppq6qovP7stGAd8tlr74A.json', 'var_call_cUogTAB1VycKJDABHElVQES8': 'file_storage/call_cUogTAB1VycKJDABHElVQES8.json'}

exec(code, env_args)
