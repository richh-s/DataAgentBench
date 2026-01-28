code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_bMqqCsihKKsbVjwoYswoSk86, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_s5ETIbMwPzOsj4vNdNR6ym5z, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

def extract_design_projects_from_text(text):
    projects = []
    # Find the Capital Improvement Projects (Design) section
    m = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects|Capital Improvement Projects \(|Capital Improvement Projects \(|$)", text, re.DOTALL|re.IGNORECASE)
    if not m:
        return projects
    section = m.group(1)
    # Find all occurrences where a project name precedes a '(cid:' marker
    # We'll search for patterns like '\n\n<project_name>\n\n(cid:'
    for match in re.finditer(r"\n{2}(.+?)\n{2}\(cid:", section, re.DOTALL):
        name = match.group(1).strip()
        # Clean up whitespace and newlines within name
        name = re.sub(r"\s+", " ", name)
        # Remove any trailing words like 'Project' duplicated maybe
        projects.append(name)
    # As a fallback, also consider lines in the section that look like headings (not starting with '(')
    if not projects:
        lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
        # heuristics: take lines that are not 'Updates:' and not starting with '(cid' and not uppercase headings
        for i, ln in enumerate(lines):
            if ln.lower().startswith('updates:') or ln.lower().startswith('project schedule'):
                continue
            if ln.startswith('(cid:') or ln.startswith('Page '):
                continue
            # consider it a project if next non-empty line starts with '(cid:' or 'Updates:'
            next_ln = None
            for j in range(i+1, min(i+3, len(lines))):
                if lines[j].startswith('(cid:') or lines[j].lower().startswith('updates:'):
                    next_ln = lines[j]
                    break
            if next_ln:
                projects.append(re.sub(r"\s+"," ", ln))
    # Deduplicate preserving order
    seen = set()
    unique_projects = []
    for p in projects:
        if p not in seen:
            seen.add(p)
            unique_projects.append(p)
    return unique_projects

# Aggregate design projects from all documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    extracted = extract_design_projects_from_text(text)
    for p in extracted:
        if p not in design_projects:
            design_projects.append(p)

# Normalize funding records: amounts as ints
for rec in funding_records:
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        try:
            rec['Amount'] = int(float(rec['Amount']))
        except:
            rec['Amount'] = 0

# Filter funding records for Amount > 50000 (though query already did), and match project names
funded_project_names = set([rec['Project_Name'].strip() for rec in funding_records if rec['Amount'] > 50000])

# Find intersection between design projects and funded_project_names
matched_projects = [p for p in design_projects if p in funded_project_names]

result = {'count': len(matched_projects), 'projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_s5ETIbMwPzOsj4vNdNR6ym5z': 'file_storage/call_s5ETIbMwPzOsj4vNdNR6ym5z.json', 'var_call_zcIxW1P7GMljFyE6rFsrF9DA': ['civic_docs'], 'var_call_bMqqCsihKKsbVjwoYswoSk86': 'file_storage/call_bMqqCsihKKsbVjwoYswoSk86.json'}

exec(code, env_args)
