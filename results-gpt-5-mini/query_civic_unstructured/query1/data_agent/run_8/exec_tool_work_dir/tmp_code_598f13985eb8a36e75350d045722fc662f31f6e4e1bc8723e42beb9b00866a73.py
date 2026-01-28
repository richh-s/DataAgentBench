code = """import json, re

docs_path = var_call_AvuBLWcpqQ0SJshtO6YsIDvN
fund_path = var_call_s1fX0ebjWAdtFmejFM65oemZ

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(fund_path, 'r', encoding='utf-8') as f:
    funds = json.load(f)

# Helper normalize
import string

def normalize(s):
    if s is None:
        return ""
    s = s.lower()
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Extract design capital project names from docs
design_projects = set()
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # find indices of section headers
    section_indices = {}
    for i,l in enumerate(lines):
        low = l.lower()
        if '(design)' in low or 'capital improvement projects (design)' in low:
            section_indices.setdefault('design',[]).append(i)
        if '(construction)' in low or 'capital improvement projects (construction)' in low:
            section_indices.setdefault('construction',[]).append(i)
        if '(not started)' in low or 'capital improvement projects (not started)' in low or 'not started' in low:
            section_indices.setdefault('not_started',[]).append(i)
    # find lines that indicate updates -> project names are typically immediately above
    for j,l in enumerate(lines):
        if 'updates' in l.lower():
            # find previous non-empty line that is not a heading
            k = j-1
            while k>=0 and (not lines[k].strip() or lines[k].strip().lower().startswith('page') or 'agenda' in lines[k].lower()):
                k -= 1
            if k>=0:
                candidate = lines[k].strip()
                # ignore short generic lines
                if len(candidate) < 3:
                    continue
                # determine nearest section header before k
                last_section = None
                last_idx = -1
                for sec, idxs in section_indices.items():
                    for idx in idxs:
                        if idx < k and idx > last_idx:
                            last_idx = idx
                            last_section = sec
                if last_section == 'design':
                    # clean candidate
                    # remove leading bullets or numbering
                    cand = re.sub(r'^[\-\u2022\*\d\.\)\s]+','', candidate)
                    design_projects.add(cand)

# fallback: also look for lines under a heading 'Capital Improvement Projects (Design)' until next blank line or next major heading
for doc in docs:
    text = doc.get('text','')
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Capital Improvement Projects\s*\(Construction\)|$)', text, flags=re.S|re.I)
    if m:
        block = m.group(1)
        # split into paragraphs by double newlines
        parts = re.split(r'\n\s*\n', block)
        for p in parts:
            p = p.strip()
            if not p:
                continue
            # project name likely first line
            first_line = p.splitlines()[0].strip()
            # avoid lines that start with (cid or Updates or Project Schedule
            if first_line and not re.search(r'updates|project schedule|\(', first_line, flags=re.I):
                # if it's long (has sentences), maybe first line is project name
                # ensure it's not a heading
                if len(first_line) > 2:
                    design_projects.add(first_line)

# Normalize design project names list
design_projects = sorted(list(design_projects))

# Prepare funding lookup
fund_records = funds  # list of dicts with Amount as string

# For each design project, check if any funding record matches with Amount > 50000
matching_projects = []
for proj in design_projects:
    nproj = normalize(proj)
    matched = False
    for rec in fund_records:
        fpn = rec.get('Project_Name','')
        if fpn is None:
            continue
        nfpn = normalize(fpn)
        if not nfpn:
            continue
        # consider a match if proj is contained in funding name or vice versa
        if nproj and (nproj in nfpn or nfpn in nproj):
            try:
                amt = int(str(rec.get('Amount','0')).replace(',',''))
            except:
                try:
                    amt = int(float(rec.get('Amount',0)))
                except:
                    amt = 0
            if amt > 50000:
                matched = True
                break
    if matched:
        matching_projects.append(proj)

# deduplicate
matching_projects = sorted(list(set(matching_projects)))
count = len(matching_projects)

import json
out = {'count': count, 'projects': matching_projects}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_AvuBLWcpqQ0SJshtO6YsIDvN': 'file_storage/call_AvuBLWcpqQ0SJshtO6YsIDvN.json', 'var_call_s1fX0ebjWAdtFmejFM65oemZ': 'file_storage/call_s1fX0ebjWAdtFmejFM65oemZ.json'}

exec(code, env_args)
