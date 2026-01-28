code = """import json

# Paths to stored query results
civic_docs_path = var_call_NqKGPQpy84p6EB1c1MXSKsJ2
funding_path = var_call_6ZUClCFfSioPFdzfzW0O50dZ

# Load files
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding project name set (Amount > 50000 already filtered)
funding_project_names = set()
for r in funding_rows:
    name = r.get('Project_Name')
    if name:
        funding_project_names.add(name.strip())

# Function to get next non-empty line index
def next_nonempty_index(lines, start):
    i = start + 1
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    return i if i < len(lines) else None

design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    # find design section
    key = 'Capital Improvement Projects (Design)'
    idx = text.find(key)
    if idx == -1:
        # sometimes it's split across lines, try a looser search
        if 'Capital Improvement Projects' in text and 'Design' in text:
            # take first occurrence of 'Capital Improvement Projects' and search nearby for 'Design'
            idx = text.find('Capital Improvement Projects')
        else:
            continue
    # determine end of design block
    end_idx_candidates = []
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        m = text.find(marker, idx)
        if m != -1:
            end_idx_candidates.append(m)
    end_idx = min(end_idx_candidates) if end_idx_candidates else len(text)
    block = text[idx:end_idx]
    lines = block.splitlines()
    # iterate lines to detect project titles
    for i, line in enumerate(lines):
        l = line.strip()
        if not l:
            continue
        lower = l.lower()
        if lower.startswith('(') or lower.endswith(':') or lower.startswith('page'):
            continue
        # find next non-empty line
        ni = next_nonempty_index(lines, i)
        nextline = lines[ni].strip() if ni is not None else ''
        if any(k in nextline.lower() for k in ['updates', 'project schedule', 'project description', 'estimated schedule', 'project updates']) or nextline.startswith('(cid:'):
            design_projects.add(l)
            continue
        # fallback: if line contains keywords
        keywords = ['project', 'repair', 'improv', 'road', 'park', 'walkway', 'study', 'plan', 'facility', 'median', 'signal', 'culvert', 'drain', 'bridge']
        if any(k in lower for k in keywords) and len(l) < 200:
            design_projects.add(l)

# Now intersect with funding project names
matched_projects = sorted([p for p in design_projects if p in funding_project_names])
count = len(matched_projects)

result = {'count': count, 'projects': matched_projects}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6ZUClCFfSioPFdzfzW0O50dZ': 'file_storage/call_6ZUClCFfSioPFdzfzW0O50dZ.json', 'var_call_C2kUMvhtoqTKmVrjf8jRVdRK': ['civic_docs'], 'var_call_NqKGPQpy84p6EB1c1MXSKsJ2': 'file_storage/call_NqKGPQpy84p6EB1c1MXSKsJ2.json'}

exec(code, env_args)
