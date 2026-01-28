code = """import json, re

# Load the large results from the provided storage file paths
with open(var_call_fLVR6B5bNi7wNkWewRGgMiKZ, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_c1QvQ3Pv8VW1Hpz3BmfCzQ6l, 'r') as f:
    funding = json.load(f)

# Helper normalization
def normalize(name):
    # remove parenthetical suffixes, lowercase, remove non-alphanum, collapse spaces
    name = re.sub(r"\(.*?\)", "", name)
    name = name.lower()
    name = re.sub(r"[^a-z0-9 ]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name

months_pattern = re.compile(r"spring|mar(ch)?|apr(il)?|may", re.I)

found_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    stripped = [ln.strip() for ln in lines]
    for i, ln in enumerate(stripped):
        if re.search(r'begin construction', ln, re.I):
            # try capture date on same line
            m = re.search(r'begin construction[:\s-]*([A-Za-z0-9 ,/\-]+)', ln, re.I)
            date_segment = m.group(1) if m else ''
            context = ' '.join(stripped[max(0,i-2):i+3])
            # Check for 2022 in date or nearby context and spring/months
            if ('2022' in date_segment) or ('2022' in context):
                if months_pattern.search(date_segment) or months_pattern.search(context):
                    # find project title by scanning backwards
                    j = i-1
                    proj_name = None
                    while j >= 0:
                        cand = stripped[j]
                        if cand and not re.search(r'updates|project schedule|project description|agenda item|page \d+|item|approved by|prepared by|subject|recommended action|discussion|\(|cid:', cand, re.I):
                            if len(cand) > 3:
                                proj_name = lines[j].strip()
                                break
                        j -= 1
                    if proj_name:
                        found_projects.append({'project': proj_name, 'date_context': date_segment or context})

# Deduplicate project names while preserving original
unique_projects = {}
for p in found_projects:
    n = normalize(p['project'])
    if n not in unique_projects:
        unique_projects[n] = p['project']

extracted_project_names = list(unique_projects.values())

# Prepare funding matching
# Normalize funding project names too
fund_rows = []
for row in funding:
    # ensure keys exist
    pname = row.get('Project_Name') or ''
    amt = row.get('Amount') or 0
    try:
        amt = int(amt)
    except:
        try:
            amt = int(float(amt))
        except:
            amt = 0
    fund_rows.append({'orig_name': pname, 'norm_name': normalize(pname), 'amount': amt})

# Match funding rows to extracted projects (substring match either way)
matched_funding_total = 0
matched_rows = []
matched_projects = {n:0 for n in unique_projects.keys()}
for fr in fund_rows:
    for n in unique_projects.keys():
        if n and (n in fr['norm_name'] or fr['norm_name'] in n):
            matched_funding_total += fr['amount']
            matched_rows.append({'funding_project': fr['orig_name'], 'amount': fr['amount'], 'matched_to': unique_projects[n]})
            matched_projects[n] += fr['amount']

# For clarity, prepare funding by project list
funding_by_project = []
for n, orig in unique_projects.items():
    funding_by_project.append({'project': orig, 'normalized': n, 'funding': matched_projects.get(n, 0)})

result = {
    'projects_count': len(unique_projects),
    'total_funding': matched_funding_total,
    'projects': funding_by_project,
    'matched_funding_rows_count': len(matched_rows)
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8oDcCsPeyX5huGLAIkGU9n3Z': ['civic_docs'], 'var_call_LYw8DGhO1vn5NserQXChPtHm': ['Funding'], 'var_call_fLVR6B5bNi7wNkWewRGgMiKZ': 'file_storage/call_fLVR6B5bNi7wNkWewRGgMiKZ.json', 'var_call_c1QvQ3Pv8VW1Hpz3BmfCzQ6l': 'file_storage/call_c1QvQ3Pv8VW1Hpz3BmfCzQ6l.json'}

exec(code, env_args)
