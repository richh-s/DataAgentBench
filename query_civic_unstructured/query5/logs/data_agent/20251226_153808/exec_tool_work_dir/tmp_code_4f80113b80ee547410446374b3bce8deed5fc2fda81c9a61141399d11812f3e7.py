code = """import json

# Load civic docs
civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding rows
funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Helper functions without regex

def has_disaster_keyword(s):
    s = (s or '').lower()
    return ('fema' in s) or ('caloes' in s) or ('caljpia' in s)


def strip_disaster_suffix(name):
    # Remove trailing parenthetical disaster suffix if present at the end
    n = name or ''
    n = n.strip()
    if n.endswith(')'):
        idx = n.rfind('(')
        if idx != -1:
            inside = n[idx+1:-1].lower()
            if ('fema' in inside) or ('caloes' in inside) or ('caljpia' in inside):
                n = n[:idx].strip()
    return ' '.join(n.split())

# Extract eligible disaster project base names from civic docs
eligible_base_names = set()

for doc in civic_docs:
    text = (doc.get('text') or '').replace('\r\n', '\n')
    lines = [ln.strip() for ln in text.split('\n')]
    n = len(lines)

    # Map section type across lines
    section_by_idx = {}
    current = None
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'disaster recovery projects' in low:
            current = 'disaster'
        elif 'capital improvement projects' in low:
            current = 'capital'
        section_by_idx[i] = current

    # Scan for lines with Begin Construction indicating 2022
    for i, ln in enumerate(lines):
        low = ln.lower()
        if ('begin construction' in low):
            # extract after ':' if present
            after = ''
            if ':' in ln:
                after = ln.split(':', 1)[1].strip()
            else:
                after = ln
            if '2022' not in after:
                continue
            # Determine if disaster project
            sec = section_by_idx.get(i)
            is_disaster = (sec == 'disaster')
            if not is_disaster:
                # check nearby context for keywords
                start = max(0, i-10)
                end = min(n, i+10)
                ctx = '\n'.join(lines[start:end]).lower()
                if ('fema' in ctx) or ('caloes' in ctx) or ('caljpia' in ctx) or ('woolsey' in ctx) or ('fire' in ctx):
                    is_disaster = True
            if not is_disaster:
                continue
            # Find title above
            title = None
            for j in range(i-1, max(-1, i-20), -1):
                if j < 0:
                    break
                t = lines[j].strip()
                if not t:
                    continue
                if ':' in t:
                    continue
                tl = t.lower()
                if tl in {'updates', 'project updates', 'project schedule', 'estimated schedule', 'agenda', 'subject', 'discussion', 'report', 'page'}:
                    continue
                if len(t) >= 3:
                    title = t
                    break
            if title:
                eligible_base_names.add(strip_disaster_suffix(title))

# Sum funding for disaster-related entries with matching base names
total = 0
included_records = []

for row in funding_rows:
    pname = row.get('Project_Name', '')
    if not has_disaster_keyword(pname):
        continue
    if strip_disaster_suffix(pname) in eligible_base_names:
        amt_str = row.get('Amount')
        try:
            amt = int(amt_str)
        except Exception:
            try:
                amt = int(''.join(ch for ch in str(amt_str) if ch.isdigit()))
            except Exception:
                continue
        total += amt
        included_records.append({'Project_Name': pname, 'Amount': amt})

result = {
    'eligible_project_basenames': sorted(list(eligible_base_names)),
    'funding_records_included': included_records,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json'}

exec(code, env_args)
