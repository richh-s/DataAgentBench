code = """import json, re
from collections import defaultdict

# Load civic docs
import os
civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding table
funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Helper functions
suffix_pattern = re.compile(r"\s*\((?:FEMA(?:/[A-Za-z]+)?|CalOES|CalJPIA)(?:[^)]*)\)\s*$", re.IGNORECASE)

def base_name(name: str) -> str:
    # remove disaster suffix at end and normalize spaces
    n = suffix_pattern.sub("", name).strip()
    # also normalize multiple spaces and dashes around
    n = re.sub(r"\s+", " ", n)
    return n

def is_disaster_name(name: str) -> bool:
    return bool(re.search(r"FEMA|CalOES|CalJPIA", name, re.IGNORECASE))

# Parse civic docs to extract projects with section type and begin construction dates
projects = []  # list of dicts: {name, type, begin_dates}

for doc in civic_docs:
    text = doc.get('text') or ''
    # normalize
    text = text.replace('\r\n', '\n')
    lines = [ln.strip() for ln in text.split('\n')]
    current_type = None
    # We'll build blocks: find title lines and gather following lines until next title or section header.
    # Identify indices of title lines
    title_indices = []
    # Pre-process to mark section changes
    section_indices = {}
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'disaster recovery projects' in low:
            section_indices[i] = 'disaster'
        elif 'capital improvement projects' in low:
            section_indices[i] = 'capital'
    # Build a mapping of line idx to current section type so far
    current_section = None
    section_by_idx = {}
    for i in range(len(lines)):
        if i in section_indices:
            current_section = section_indices[i]
        section_by_idx[i] = current_section

    # Function to decide if a line is a project title
    def is_title_line(ln: str) -> bool:
        if not ln:
            return False
        if ':' in ln:
            return False
        if len(ln) < 4 or len(ln) > 140:
            return False
        # Exclude common headings
        excl = {'agenda', 'subject', 'discussion', 'updates', 'project updates', 'project schedule', 'recommended action', 'to', 'prepared by', 'approved by', 'meeting date', 'date prepared', 'item', 'commission meeting', 'report', 'city of', 'page', 'agenda item', 'project description'}
        if ln.strip().lower() in excl:
            return False
        # Must contain letters and spaces
        if not re.search(r"[A-Za-z]", ln):
            return False
        # Require at least two words and mostly title case or with words capitalized
        words = ln.split()
        if len(words) < 2:
            return False
        # Heuristic: many words start with uppercase or are acronyms
        capscore = sum(1 for w in words if re.match(r"^[A-Z0-9][A-Za-z0-9/()'\-]*$", w))
        if capscore/len(words) < 0.5:
            return False
        return True

    # Collect candidate title indices
    for i, ln in enumerate(lines):
        if is_title_line(ln):
            # Check that nearby lines indicate it's a project (lookahead for Updates or Project Schedule within next 10 lines)
            lookahead = '\n'.join(lines[i+1:i+12]).lower()
            if ('updates' in lookahead) or ('project schedule' in lookahead) or ('project description' in lookahead) or ('estimated schedule' in lookahead):
                title_indices.append(i)

    # Remove duplicates / very close indices
    cleaned_indices = []
    last = -10
    for idx in sorted(set(title_indices)):
        if idx - last > 1:
            cleaned_indices.append(idx)
            last = idx
    title_indices = cleaned_indices

    # Build blocks
    for t_idx_i, start_idx in enumerate(title_indices):
        end_idx = title_indices[t_idx_i+1] if t_idx_i+1 < len(title_indices) else len(lines)
        block_lines = lines[start_idx:end_idx]
        title = block_lines[0].strip()
        block_text = '\n'.join(block_lines)
        # Determine type: from section at the title line or presence of FEMA/CalOES/CalJPIA keywords
        sec_type = section_by_idx.get(start_idx)
        p_type = 'disaster' if (sec_type == 'disaster' or is_disaster_name(title) or re.search(r"FEMA|CalOES|CalJPIA|Woolsey|fire", block_text, re.IGNORECASE)) else 'capital'
        # Extract begin construction lines
        begin_dates = []
        for m in re.finditer(r"Begin\s+Construction\s*:\s*([^\n]+)", block_text, re.IGNORECASE):
            begin_dates.append(m.group(1).strip())
        # Also consider 'Begin construction' with lowercase c
        for m in re.finditer(r"Begin\s+construction\s*:\s*([^\n]+)", block_text):
            begin_dates.append(m.group(1).strip())
        # Also sometimes 'Begin const' variations? Keep simple.

        projects.append({
            'name': title,
            'type': p_type,
            'begin_dates': begin_dates,
            'doc_filename': doc.get('filename')
        })

# Filter projects: disaster and started in 2022
eligible_base_names = set()
for p in projects:
    if p['type'] != 'disaster':
        continue
    if any('2022' in (bd or '') for bd in p['begin_dates']):
        eligible_base_names.add(base_name(p['name']))

# Build funding sum: include only funding entries that are disaster (name has suffix keywords) and base name matches eligible
total = 0
included_records = []
for row in funding_rows:
    fname = row['Project_Name']
    amt_str = row.get('Amount')
    try:
        amt = int(amt_str)
    except Exception:
        # try to parse numeric
        try:
            amt = int(re.sub(r"[^0-9]", "", str(amt_str)))
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

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json'}

exec(code, env_args)
