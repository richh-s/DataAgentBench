code = """import json, re

# Load data from storage file paths
with open(var_call_zeywUXiQEdBYRViOUVw0qjTf, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_rWQJD3On75AA8hcLZTYlrM35, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Helper to clean names (remove parenthetical suffixes, extra whitespace, punctuation)
def clean_name(s):
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical content
    s = re.sub(r"[^0-9a-zA-Z\s&-]", " ", s)  # replace punctuation with space
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

# Extract project names from "Capital Improvement Projects (Design)" sections
design_projects = set()
end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"]
for doc in civic_docs:
    text = doc.get('text', '')
    start_idx = text.find('Capital Improvement Projects (Design)')
    if start_idx == -1:
        continue
    start_idx += len('Capital Improvement Projects (Design)')
    # find nearest end marker
    end_idx = None
    possible_ends = []
    for m in end_markers:
        i = text.find(m, start_idx)
        if i != -1:
            possible_ends.append(i)
    if possible_ends:
        end_idx = min(possible_ends)
    section = text[start_idx:end_idx] if end_idx else text[start_idx: start_idx+4000]
    # Split into lines and filter
    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # Skip lines that are clearly labels or content, not project titles
        low = line.lower()
        if low.startswith('(cid:'):
            continue
        if low.startswith('updates:') or low.startswith('project schedule') or low.startswith('estimated schedule') or low.startswith('page'):
            continue
        if ':' in line and len(line.split(':')[0].split()) < 6:
            # lines like "Complete Design: Summer 2023" etc. skip
            # but allow lines that look like titles with many words
            continue
        # Heuristic: project names usually have at least 2 words and contain letters
        if len(re.findall(r'[a-zA-Z]', line)) < 2:
            continue
        words = line.split()
        if len(words) < 2:
            continue
        # Avoid lines that are common headings
        if low.startswith('discussion') or low.startswith('recommended action') or low.startswith('agenda item'):
            continue
        # Finally, treat as a project name
        design_projects.add(line)

# Clean design project names
clean_design_projects = {p: clean_name(p) for p in design_projects}

# Prepare funding records (from query: amounts already > 50000)
# Convert amount to int
funding = []
for r in funding_records:
    try:
        amt = int(r.get('Amount') if isinstance(r.get('Amount'), (int, float)) else int(str(r.get('Amount')).replace(',', '')))
    except:
        continue
    funding.append({'Funding_ID': r.get('Funding_ID'), 'Project_Name': r.get('Project_Name'), 'Amount': amt})

# Match funding records to design capital projects using substring matching on cleaned names
matched_projects = {}
for proj_orig, proj_clean in clean_design_projects.items():
    for fr in funding:
        fr_clean = clean_name(fr['Project_Name'])
        if proj_clean and (proj_clean in fr_clean or fr_clean in proj_clean):
            matched_projects.setdefault(proj_orig, []).append({'Funding_Project_Name': fr['Project_Name'], 'Amount': fr['Amount'], 'Funding_ID': fr.get('Funding_ID')})

# Count unique design capital projects that have at least one funding record > 50000
count = len(matched_projects)

result = {'count': count, 'matched_projects': matched_projects}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4Qcts42BSdxsN6aGvrhXqhev': ['civic_docs'], 'var_call_04W7JozyaSAyqJxnMzzcOVLs': ['Funding'], 'var_call_zeywUXiQEdBYRViOUVw0qjTf': 'file_storage/call_zeywUXiQEdBYRViOUVw0qjTf.json', 'var_call_rWQJD3On75AA8hcLZTYlrM35': 'file_storage/call_rWQJD3On75AA8hcLZTYlrM35.json'}

exec(code, env_args)
