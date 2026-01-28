code = """import json, re

# Load the funding records (file path provided in var_call_dbBUriyltPz1JNXhcXBHu9ui)
with open(var_call_dbBUriyltPz1JNXhcXBHu9ui, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Load the civic docs (file path provided in var_call_DBR6umzIuHikn6R9Jud4sxA3)
with open(var_call_DBR6umzIuHikn6R9Jud4sxA3, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build set of funding project names (already filtered for Amount > 50000 in the query)
funding_names = set()
for rec in funding:
    name = rec.get('Project_Name')
    if name:
        funding_names.add(name.strip())

# Helper: extract project names from 'Capital Improvement Projects (Design)' sections
heading = 'Capital Improvement Projects (Design)'
delimiters = [
    'Capital Improvement Projects (Construction)',
    'Capital Improvement Projects (Not Started)',
    'Capital Improvement Projects (Design)',
    'Capital Improvement Projects (Construction)',
    'Capital Improvement Projects (Not Started)'
]

def extract_design_projects_from_text(text):
    projects = []
    for m in re.finditer(re.escape(heading), text):
        start = m.end()
        substring = text[start:]
        # find nearest delimiter
        end_idx = len(substring)
        for d in delimiters:
            i = substring.find(d)
            if i != -1 and i < end_idx:
                end_idx = i
        section = substring[:end_idx]
        # split into lines and pick candidate title lines
        for i, line in enumerate(section.splitlines()):
            s = line.strip()
            if not s:
                continue
            # Exclude lines that are obvious non-titles
            if s.startswith('(cid:'):
                continue
            if s.startswith('Updates') or s.startswith('Project Schedule'):
                continue
            if s.startswith('Page') or s.startswith('Agenda') or s.startswith('Item'):
                continue
            if ':' in s:  # lines like 'RECOMMENDED ACTION:' or similar
                continue
            # Exclude lines that appear to be headings in ALL CAPS
            if s.isupper():
                continue
            # Exclude very long lines
            if len(s) > 200:
                continue
            # Heuristic: lines that contain words and letters are likely project titles
            # Exclude lines that are just years or dates
            if re.fullmatch(r'[0-9\-\s,()]+', s):
                continue
            projects.append(s)
    return projects

# Aggregate projects from all documents
design_projects = set()
for doc in docs:
    text = doc.get('text', '')
    extracted = extract_design_projects_from_text(text)
    for p in extracted:
        design_projects.add(p)

# Now find intersection with funding names
matched_projects = sorted([p for p in design_projects if p in funding_names])
count = len(matched_projects)

# Prepare result
result = {
    'count': count,
    'matched_projects': matched_projects,
    'total_design_projects_extracted': len(design_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dbBUriyltPz1JNXhcXBHu9ui': 'file_storage/call_dbBUriyltPz1JNXhcXBHu9ui.json', 'var_call_DBR6umzIuHikn6R9Jud4sxA3': 'file_storage/call_DBR6umzIuHikn6R9Jud4sxA3.json'}

exec(code, env_args)
