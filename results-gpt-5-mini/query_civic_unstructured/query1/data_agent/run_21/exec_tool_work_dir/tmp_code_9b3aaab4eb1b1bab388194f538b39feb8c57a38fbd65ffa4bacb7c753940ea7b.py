code = """import json

# Load data from storage-provided file paths
with open(var_call_bMqqCsihKKsbVjwoYswoSk86, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_s5ETIbMwPzOsj4vNdNR6ym5z, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

def extract_design_projects_from_text(text):
    projects = []
    start_token = "Capital Improvement Projects (Design)"
    if start_token.lower() not in text.lower():
        return projects
    # Find start (case-insensitive)
    lower = text.lower()
    si = lower.find(start_token.lower())
    if si == -1:
        return projects
    # Determine end by looking for common next headings
    possible_ends = ["Capital Improvement Projects (Construction)",
                     "Capital Improvement Projects (Not Started)",
                     "Capital Improvement Projects (Design)",
                     "Capital Improvement Projects (Construction)",
                     "Page "]
    ei = len(text)
    for end in possible_ends:
        idx = lower.find(end.lower(), si + 1)
        if idx != -1 and idx < ei:
            ei = idx
    section = text[si:ei]
    # Split into lines and look for project headings
    lines = [ln.strip() for ln in section.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        # skip obvious non-project lines
        if low.startswith('updates:') or low.startswith('page ') or low.startswith('agenda'):
            continue
        if ln.startswith('(') or ln.endswith(':'):
            continue
        # Heuristic: if next few lines contain '(cid:' or 'updates' or 'project schedule' or 'project description', treat ln as project name
        next_block = " ".join(lines[i+1:i+4]).lower()
        if '(cid:' in next_block or 'updates:' in next_block or 'project schedule' in next_block or 'project description' in next_block:
            # Clean name
            name = ' '.join(ln.split())
            # Exclude lines that are generic headings
            if name.lower().startswith('capital improvement') or name.lower().startswith('page'):
                continue
            projects.append(name)
    # Dedupe preserving order
    seen = set()
    uniq = []
    for p in projects:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq

# Aggregate design projects from all documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    extracted = extract_design_projects_from_text(text)
    for p in extracted:
        if p not in design_projects:
            design_projects.append(p)

# Normalize funding records: amounts as ints and set of project names with amount > 50000
funded_project_names = set()
for rec in funding_records:
    name = rec.get('Project_Name', '').strip()
    amt = rec.get('Amount', 0)
    try:
        amt = int(amt)
    except:
        try:
            amt = int(float(amt))
        except:
            amt = 0
    if amt > 50000:
        funded_project_names.add(name)

# Find intersection
matched_projects = [p for p in design_projects if p in funded_project_names]

result = {'count': len(matched_projects), 'projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_s5ETIbMwPzOsj4vNdNR6ym5z': 'file_storage/call_s5ETIbMwPzOsj4vNdNR6ym5z.json', 'var_call_zcIxW1P7GMljFyE6rFsrF9DA': ['civic_docs'], 'var_call_bMqqCsihKKsbVjwoYswoSk86': 'file_storage/call_bMqqCsihKKsbVjwoYswoSk86.json'}

exec(code, env_args)
