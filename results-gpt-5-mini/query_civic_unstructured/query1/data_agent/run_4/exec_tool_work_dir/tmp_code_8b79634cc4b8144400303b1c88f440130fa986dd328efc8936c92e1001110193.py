code = """import json, re

# Load the large results from storage-provided file paths
with open(var_call_TikI7oWVmPcxlcuANPN1YxeC, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_jlurDQYW7JR6GJNfGZCmGkUs, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Extract design capital projects from civic_docs texts
design_projects = set()
section_header_pattern = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
end_section_patterns = [re.compile(r"Capital Improvement Projects\s*\(Construction\)", re.IGNORECASE),
                        re.compile(r"Capital Improvement Projects\s*\(Not Started\)", re.IGNORECASE),
                        re.compile(r"Capital Improvement Projects\s*\(Construction\)", re.IGNORECASE),
                        re.compile(r"Capital Improvement Projects\s*\(Not Started\)", re.IGNORECASE),
                        re.compile(r"Capital Improvement Projects \(Construction\)", re.IGNORECASE)]

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    m = section_header_pattern.search(text)
    if not m:
        continue
    start = m.end()
    # find the nearest end pattern after start
    end = None
    for p in end_section_patterns:
        mm = p.search(text, pos=start)
        if mm:
            if end is None or mm.start() < end:
                end = mm.start()
    if end is None:
        # fallback: limit to next two pages or next major header like "Capital Improvement Projects (" occurrences
        end = len(text)
    section_text = text[start:end]
    # Split into lines and filter
    lines = [ln.strip() for ln in section_text.splitlines()]
    for ln in lines:
        if not ln:
            continue
        # skip lines that look like markers or notes
        low = ln.lower()
        if low.startswith('(cid:') or low.startswith('updates') or 'updates:' in low or 'project schedule' in low or low.startswith('page') or low.startswith('agenda'):
            continue
        if ':' in ln and len(ln.split(':')[0].split()) < 5:
            # likely a label like "Project Schedule:"
            continue
        # skip short lines
        if len(ln) < 6:
            continue
        # remove trailing punctuation
        cleaned = ln.strip(' .\t')
        # ignore lines that are clearly headings like "Capital Improvement Projects (Design)" repeated
        if 'capital improvement' in cleaned.lower():
            continue
        # Heuristic: consider lines that contain letters and not just numbers
        if re.search('[A-Za-z]', cleaned):
            design_projects.add(cleaned)

# Normalize funding project names and select those with amount > 50000 (they already are from query)
funded_projects = set()
for rec in funding_records:
    name = rec.get('Project_Name')
    if name:
        funded_projects.add(name.strip())

# Now find intersection between design_projects and funded_projects
matched = sorted([p for p in design_projects if p in funded_projects])
count = len(matched)

# Prepare result
result = {"count": count, "projects": matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jlurDQYW7JR6GJNfGZCmGkUs': 'file_storage/call_jlurDQYW7JR6GJNfGZCmGkUs.json', 'var_call_TikI7oWVmPcxlcuANPN1YxeC': 'file_storage/call_TikI7oWVmPcxlcuANPN1YxeC.json'}

exec(code, env_args)
