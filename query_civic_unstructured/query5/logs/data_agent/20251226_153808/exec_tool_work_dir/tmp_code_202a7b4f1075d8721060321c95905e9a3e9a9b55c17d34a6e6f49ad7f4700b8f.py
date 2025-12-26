code = """import json, re

# Load civic docs
civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding table
funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Helper functions
suffix_pattern = re.compile("\\s*\\((?:FEMA(?:/[A-Za-z]+)?|CalOES|CalJPIA)(?:[^)]*)\\)\\s*$", re.IGNORECASE)

def base_name(name):
    n = suffix_pattern.sub("", name).strip()
    n = re.sub("\\s+", " ", n)
    return n

def is_disaster_name(name):
    return bool(re.search("FEMA|CalOES|CalJPIA", name, re.IGNORECASE))

projects = []

for doc in civic_docs:
    text = (doc.get('text') or '').replace('\r\n', '\n')
    lines = [ln.strip() for ln in text.split('\n')]

    # Determine section type along the document by headings
    section_type_by_idx = {}
    current = None
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'disaster recovery projects' in low:
            current = 'disaster'
        elif 'capital improvement projects' in low:
            current = 'capital'
        section_type_by_idx[i] = current

    # Identify project title lines: if the next few lines contain 'Updates' or 'Project Schedule'
    candidate_indices = []
    for i, ln in enumerate(lines):
        if not ln or ':' in ln:
            continue
        la = '\n'.join(lines[i+1:i+8]).lower()
        if ('updates' in la) or ('project schedule' in la) or ('estimated schedule' in la) or ('project description' in la):
            candidate_indices.append(i)

    # Build project blocks
    for t_i, start_idx in enumerate(candidate_indices):
        end_idx = candidate_indices[t_i+1] if t_i+1 < len(candidate_indices) else len(lines)
        block_lines = lines[start_idx:end_idx]
        title = block_lines[0]
        block_text = '\n'.join(block_lines)
        sec = section_type_by_idx.get(start_idx)
        p_type = 'disaster' if (sec == 'disaster' or re.search('FEMA|CalOES|CalJPIA|Woolsey|fire', block_text, re.IGNORECASE)) else 'capital'
        # Extract begin construction dates
        begin_dates = []
        for m in re.finditer('Begin\\s+Construction\\s*:\\s*([^\n]+)', block_text, re.IGNORECASE):
            begin_dates.append(m.group(1).strip())
        for m in re.finditer('Begin\\s+construction\\s*:\\s*([^\n]+)', block_text):
            begin_dates.append(m.group(1).strip())
        projects.append({'name': title, 'type': p_type, 'begin_dates': begin_dates, 'doc_filename': doc.get('filename')})

# Determine eligible base names for disaster projects started in 2022
eligible_base_names = set()
for p in projects:
    if p['type'] != 'disaster':
        continue
    if any(('2022' in (bd or '')) for bd in p['begin_dates']):
        eligible_base_names.add(base_name(p['name']))

# Sum funding for disaster entries with matching base names
total = 0
included = []
for row in funding_rows:
    pname = row.get('Project_Name', '')
    amt_str = row.get('Amount')
    try:
        amt = int(amt_str)
    except Exception:
        try:
            amt = int(re.sub('[^0-9]', '', str(amt_str)))
        except Exception:
            continue
    if not is_disaster_name(pname):
        continue
    if base_name(pname) in eligible_base_names:
        total += amt
        included.append({'Project_Name': pname, 'Amount': amt})

result = {
    'eligible_project_basenames': sorted(list(eligible_base_names)),
    'funding_records_included': included,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json'}

exec(code, env_args)
