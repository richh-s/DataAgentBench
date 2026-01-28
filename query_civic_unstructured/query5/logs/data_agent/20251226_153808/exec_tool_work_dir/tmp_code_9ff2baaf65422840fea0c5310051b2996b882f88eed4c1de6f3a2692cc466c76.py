code = """import json

civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)


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

eligible = set()

for doc in civic_docs:
    text = (doc.get('text') or '')
    lines = [ln.strip() for ln in text.splitlines()]
    n = len(lines)

    section_by_idx = {}
    current = None
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'disaster recovery projects' in low:
            current = 'disaster'
        elif 'capital improvement projects' in low:
            current = 'capital'
        section_by_idx[i] = current

    for i, ln in enumerate(lines):
        low = ln.lower()
        if ('begin construction' in low) and ('2022' in ln):
            sec = section_by_idx.get(i)
            is_dis = (sec == 'disaster')
            if not is_dis:
                start = max(0, i-12)
                end = min(n, i+12)
                ctx = ' '.join(lines[start:end]).lower()
                if has_disaster_keyword(ctx):
                    is_dis = True
            if not is_dis:
                continue
            title = None
            j = i - 1
            skip = {'updates', 'project updates', 'project schedule', 'estimated schedule', 'agenda', 'subject', 'discussion', 'report', 'page', 'item'}
            while j >= 0 and j >= i - 20:
                t = lines[j].strip()
                if t == '' or (':' in t):
                    j -= 1
                    continue
                if t.lower() in skip:
                    j -= 1
                    continue
                title = t
                break
            if title:
                eligible.add(strip_disaster_suffix(title))

Total = 0
included = []
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
        included.append({'Project_Name': pname, 'Amount': amt})

result = {'eligible_project_basenames': sorted(list(eligible)), 'funding_records_included': included, 'total_funding': Total}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json', 'var_call_kaXnF2m8GPl1J9oXIje1pDwq': 'ok', 'var_call_ElDAewPKYFmoArgOqYdtWrUA': {'docs': 19, 'funding_rows': 500}}

exec(code, env_args)
