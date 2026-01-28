code = """import json, re, os

# Load civic docs
civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding table
funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Patterns
suffix_pattern = re.compile(r'\s*\((?:FEMA(?:/[A-Za-z]+)?|CalOES|CalJPIA)(?:[^)]*)\)\s*$', re.IGNORECASE)

def base_name(name):
    n = suffix_pattern.sub('', name).strip()
    n = re.sub(r'\s+', ' ', n)
    return n

def is_disaster_name(name):
    return bool(re.search(r'(FEMA|CalOES|CalJPIA)', name, re.IGNORECASE))

projects = []

for doc in civic_docs:
    text = doc.get('text') or ''
    text = text.replace('\r\n', '\n')
    lines = [ln.strip() for ln in text.split('\n')]

    # Identify section lines
    section_indices = {}
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'disaster recovery projects' in low:
            section_indices[i] = 'disaster'
        elif 'capital improvement projects' in low:
            section_indices[i] = 'capital'

    current_section = None
    section_by_idx = {}
    for i in range(len(lines)):
        if i in section_indices:
            current_section = section_indices[i]
        section_by_idx[i] = current_section

    def is_title_line(ln):
        if not ln:
            return False
        if ':' in ln:
            return False
        if len(ln) < 4 or len(ln) > 140:
            return False
        excl = {'agenda', 'subject', 'discussion', 'updates', 'project updates', 'project schedule', 'recommended action', 'to', 'prepared by', 'approved by', 'meeting date', 'date prepared', 'item', 'commission meeting', 'report', 'city of', 'page', 'agenda item', 'project description'}
        if ln.strip().lower() in excl:
            return False
        if not re.search(r'[A-Za-z]', ln):
            return False
        words = ln.split()
        if len(words) < 2:
            return False
        capscore = sum(1 for w in words if re.match(r'^[A-Z0-9][A-Za-z0-9/()\'-]*$', w))
        if capscore / len(words) < 0.5:
            return False
        return True

    title_indices = []
    for i, ln in enumerate(lines):
        if is_title_line(ln):
            lookahead = '\n'.join(lines[i+1:i+12]).lower()
            if ('updates' in lookahead) or ('project schedule' in lookahead) or ('project description' in lookahead) or ('estimated schedule' in lookahead):
                title_indices.append(i)

    cleaned_indices = []
    last = -10
    for idx in sorted(set(title_indices)):
        if idx - last > 1:
            cleaned_indices.append(idx)
            last = idx
    title_indices = cleaned_indices

    for t_i, start_idx in enumerate(title_indices):
        end_idx = title_indices[t_i+1] if t_i+1 < len(title_indices) else len(lines)
        block_lines = lines[start_idx:end_idx]
        title = block_lines[0].strip()
        block_text = '\n'.join(block_lines)
        sec_type = section_by_idx.get(start_idx)
        p_type = 'disaster' if (sec_type == 'disaster' or is_disaster_name(title) or re.search(r'(FEMA|CalOES|CalJPIA|Woolsey|fire)', block_text, re.IGNORECASE)) else 'capital'
        begin_dates = []
        for m in re.finditer(r'Begin\s+Construction\s*:\s*([^\n]+)', block_text, re.IGNORECASE):
            begin_dates.append(m.group(1).strip())
        for m in re.finditer(r'Begin\s+construction\s*:\s*([^\n]+)', block_text):
            begin_dates.append(m.group(1).strip())
        projects.append({'name': title, 'type': p_type, 'begin_dates': begin_dates, 'doc_filename': doc.get('filename')})

eligible_base_names = set()
for p in projects:
    if p['type'] != 'disaster':
        continue
    if any(('2022' in (bd or '')) for bd in p['begin_dates']):
        eligible_base_names.add(base_name(p['name']))

total = 0
included_records = []
for row in funding_rows:
    fname = row['Project_Name']
    amt_str = row.get('Amount')
    try:
        amt = int(amt_str)
    except Exception:
        try:
            amt = int(re.sub(r'[^0-9]', '', str(amt_str)))
        except Exception:
            continue
    if not is_disaster_name(fname):
        continue
    if base_name(fname) in eligible_base_names:
        total += amt
        included_records.append({'Project_Name': fname, 'Amount': amt})

result = {
    'eligible_project_basenames': sorted(list(eligible_base_names)),
    'funding_records_included': included_records,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json'}

exec(code, env_args)
