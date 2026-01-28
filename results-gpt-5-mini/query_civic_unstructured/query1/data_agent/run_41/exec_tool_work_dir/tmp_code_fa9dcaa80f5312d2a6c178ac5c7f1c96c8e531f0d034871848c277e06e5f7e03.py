code = """import json
from pathlib import Path

# Load data from stored file paths
civic_docs_path = var_call_NqKGPQpy84p6EB1c1MXSKsJ2
funding_path = var_call_6ZUClCFfSioPFdzfzW0O50dZ

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Extract funding project names (these rows already filtered for Amount > 50000)
funding_project_names = set()
for r in funding_rows:
    name = r.get('Project_Name')
    if name:
        funding_project_names.add(name.strip())

# Helper to find next non-empty line index

def next_nonempty(lines, start):
    i = start + 1
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    return i if i < len(lines) else None

# Extract project names under "Capital Improvement Projects (Design)"
design_projects = set()
stop_headings = [
    'Capital Improvement Projects (Construction)',
    'Capital Improvement Projects (Not Started)',
    'Capital Improvement Projects (Design)\n',
]

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    # normalize line endings
    lines = text.splitlines()
    # find all occurrences of design heading
    for idx, line in enumerate(lines):
        if 'Capital Improvement Projects' in line and 'Design' in line:
            # extract block from next line until a stop heading or until end
            start = idx + 1
            end = len(lines)
            for j in range(start, len(lines)):
                l = lines[j]
                if 'Capital Improvement Projects (Construction)' in l or 'Capital Improvement Projects (Not Started)' in l:
                    end = j
                    break
            block = lines[start:end]
            # Iterate block to find project title lines
            i = 0
            while i < len(block):
                l = block[i].strip()
                if l == '':
                    i += 1
                    continue
                # Skip lines that look like headings or metadata
                lower = l.lower()
                if lower.startswith('(') or lower.endswith(':') or lower.startswith('page') or 'agenda' in lower or 'discussion' in lower or 'recommended action' in lower:
                    i += 1
                    continue
                # Check next non-empty line to see if it indicates this is a project title
                ni = i + 1
                while ni < len(block) and block[ni].strip() == '':
                    ni += 1
                nextline = block[ni].strip() if ni < len(block) else ''
                if ('updates' in nextline.lower()) or ('project schedule' in nextline.lower()) or ('project description' in nextline.lower()) or ('estimated schedule' in nextline.lower()) or ('project updates' in nextline.lower()):
                    # treat l as project title
                    design_projects.add(l)
                    i = ni + 1
                    continue
                # Also sometimes titles are followed by a blank then a parenthesis marker
                if nextline.startswith('(cid:'):
                    design_projects.add(l)
                    i = ni + 1
                    continue
                # If line looks like a project (contains words like Project, Repair, Improvements, Road, Park, Walkway, Study, Plan)
                keywords = ['project', 'repair', 'improv', 'road', 'park', 'walkway', 'study', 'plan', 'facility', 'median', 'signal', 'culvert', 'drain']
                if any(k in lower for k in keywords):
                    # to avoid catching long paragraphs, ensure line isn't too long
                    if len(l) < 200:
                        design_projects.add(l)
                i += 1

# Now intersect with funding_project_names
matched_projects = sorted([p for p in design_projects if p in funding_project_names])
count = len(matched_projects)

# Prepare result
result = {
    'count': count,
    'projects': matched_projects,
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6ZUClCFfSioPFdzfzW0O50dZ': 'file_storage/call_6ZUClCFfSioPFdzfzW0O50dZ.json', 'var_call_C2kUMvhtoqTKmVrjf8jRVdRK': ['civic_docs'], 'var_call_NqKGPQpy84p6EB1c1MXSKsJ2': 'file_storage/call_NqKGPQpy84p6EB1c1MXSKsJ2.json'}

exec(code, env_args)
