code = """import json

def has_disaster_keyword(s):
    s = (s or '').lower()
    return ('fema' in s) or ('caloes' in s) or ('caljpia' in s) or ('woolsey' in s) or ('fire' in s)


def strip_disaster_suffix(name):
    n = (name or '').strip()
    if n.endswith(')'):
        idx = n.rfind('(')
        if idx != -1:
            inside = n[idx+1:-1].lower()
            if ('fema' in inside) or ('caloes' in inside) or ('caljpia' in inside):
                n = n[:idx].strip()
    return ' '.join(n.split())

# Load civic docs
civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding rows
funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

eligible = set()

for doc in civic_docs:
    text = (doc.get('text') or '').replace('\r\n', '\n')
    lines = [ln.strip() for ln in text.split('\n')]
    n = len(lines)

    # Map section by index
    section_by_idx = {}
    current = None
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'disaster recovery projects' in low:
            current = 'disaster'
        elif 'capital improvement projects' in low:
            current = 'capital'
        section_by_idx[i] = current

    # Identify candidate project titles
    candidate_indices = []
    headers_excl = {
        'agenda', 'subject', 'discussion', 'updates', 'project updates', 'project schedule', 'estimated schedule',
        'recommended action', 'to', 'prepared by', 'approved by', 'meeting date', 'date prepared', 'item',
        'commission meeting', 'report', 'city of', 'page', 'agenda item', 'project description'
    }
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if ':' in ln:
            continue
        low = ln.lower()
        if low in headers_excl:
            continue
        if not any(ch.isalpha() for ch in ln):
            continue
        words = [w for w in ln.split() if any(c.isalpha() for c in w)]
        if len(words) < 2:
            continue
        capscore = sum(1 for w in words if w[0].isupper() or w.isupper())
        if capscore < (len(words) * 0.5):
            continue
        # lookahead for typical project sections
        lookahead = ' '.join(lines[i+1:i+12]).lower()
        if ('updates' in lookahead) or ('project schedule' in lookahead) or ('estimated schedule' in lookahead) or ('project description' in lookahead):
            candidate_indices.append(i)

    # Build blocks and extract begin construction dates
    for idx_i, start_idx in enumerate(candidate_indices):
        end_idx = candidate_indices[idx_i+1] if idx_i+1 < len(candidate_indices) else n
        block_lines = lines[start_idx:end_idx]
        title = block_lines[0].strip()
        block_text = ' '.join(block_lines)
        # Determine type
        sec = section_by_idx.get(start_idx)
        is_dis = (sec == 'disaster') or has_disaster_keyword(title) or has_disaster_keyword(block_text)
        if not is_dis:
            continue
        # Find begin construction dates in block
        begin_dates = []
        for bl in block_lines:
            bl_low = bl.lower()
            if 'begin construction' in bl_low and ':' in bl:
                begin_dates.append(bl.split(':', 1)[1].strip())
        if any('2022' in bd for bd in begin_dates):
            eligible.add(strip_disaster_suffix(title))

# Sum matching funding rows
Total = 0
for row in funding_rows:
    pname = row.get('Project_Name', '')
    if not has_disaster_keyword(pname):
        continue
    if strip_disaster_suffix(pname) in eligible:
        amt_str = row.get('Amount')
        try:
            amt = int(amt_str)
        except Exception:
            digits = ''.join(ch for ch in str(amt_str) if ch.isdigit())
            amt = int(digits) if digits else 0
        Total += amt

print('__RESULT__:')
print(json.dumps({'eligible_project_basenames': sorted(list(eligible)), 'total_funding': Total}))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json', 'var_call_kaXnF2m8GPl1J9oXIje1pDwq': 'ok', 'var_call_ElDAewPKYFmoArgOqYdtWrUA': {'docs': 19, 'funding_rows': 500}, 'var_call_ZdIBJHOcMNOL48rOZtlFzTH7': {'eligible_project_basenames': ['Agenda Item # 4.A.', 'Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Slope Stabilization Project', 'Westward Beach Road.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'beginning in April 2022.', 'beginning in Fall 2022.', 'beginning in Spring 2022.', 'bid with bids due November 17.', 'coming weeks.', 'completing the final design.', 'damaged by the Woolsey Fire.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'final design and preparing the project for public bidding.', 'guardrails within the project limits.', 'is finalizing the bid documents.', 'of 2022.', 'started and is anticipated to be completed by the Spring of 2022.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'funding_records_included': [{'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': 92000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': 43000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': 32000}], 'total_funding': 211000}}

exec(code, env_args)
