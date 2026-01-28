code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_KYRK4xUSAtxEAJdgI1BrqhqV)
fund = load_json_maybe(var_call_5wBIUvFbVq6D7BGzPAvwAJbx)

fund_map = {}
for r in fund:
    pn = (r.get('Project_Name') or '').strip()
    if not pn:
        continue
    amt = r.get('total_amount')
    try:
        amt_i = int(amt)
    except Exception:
        try:
            amt_i = int(float(amt))
        except Exception:
            continue
    fund_map[pn] = fund_map.get(pn, 0) + amt_i

def extract_projects_from_text(text):
    lines = text.splitlines()
    projects = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and not line.startswith(('(', 'cid:', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Staff', 'Recommended')):
            if re.search(r'Project( Schedule| Description| Updates)?\s*:', line):
                i += 1
                continue
            look = "\\n".join(lines[i+1:min(i+8, len(lines))])
            if re.search(r'Updates\s*:', look):
                name = line
                block_lines = []
                j = i
                while j < len(lines) and j < i + 60:
                    if j > i and lines[j].strip() == '':
                        k = j + 1
                        while k < len(lines) and lines[k].strip() == '':
                            k += 1
                        if k >= len(lines):
                            j = k
                            break
                        nxt = lines[k].strip()
                        if nxt and re.search(r'(Projects \(|Disaster Recovery|Capital Improvement|Page \d|Agenda Item)', nxt):
                            j = k
                            break
                        look2 = "\\n".join(lines[k+1:min(k+8, len(lines))])
                        if re.search(r'Updates\s*:', look2):
                            j = k
                            break
                    block_lines.append(lines[j])
                    j += 1
                block = "\\n".join(block_lines)

                status = None
                if re.search(r'\bConstruction was completed\b', block, flags=re.I) or re.search(r'\bNotice of completion\b', block, flags=re.I):
                    status = 'completed'

                et = None
                m = re.search(r'Complete (?:Design|Construction)\s*:\s*([^\n\r]+)', block, flags=re.I)
                if m:
                    et = m.group(1).strip()

                projects.append({'Project_Name': name, 'status': status, 'et': et, 'block': block})
                i = j
                continue
        i += 1
    return projects

all_projects = []
for d in docs:
    txt = d.get('text') or ''
    if txt:
        all_projects.extend(extract_projects_from_text(txt))

park_kw = re.compile(r'\b(park|playground|bluffs)\b', re.I)

def is_park_related(p):
    return bool(park_kw.search(p.get('Project_Name','')) or park_kw.search(p.get('block','')))

def completed_in_2022(p):
    blk = p.get('block','')
    et = p.get('et') or ''
    if re.search(r'completed[^\n]*2022', blk, flags=re.I):
        return True
    if et and '2022' in et:
        return p.get('status') == 'completed'
    if p.get('status') == 'completed' and re.search(r'\b2022\b', blk):
        return True
    return False

matched = []
seen = set()
for p in all_projects:
    if is_park_related(p) and completed_in_2022(p):
        name = p['Project_Name']
        if name not in seen:
            seen.add(name)
            matched.append({'Project_Name': name, 'funding': int(fund_map.get(name, 0))})

total = sum(r['funding'] for r in matched)

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': matched}))"""

env_args = {'var_call_4PG5K1JFOxGDnVSmjHEy9scy': ['Funding'], 'var_call_LZiL1tp6SEIuXVpXZIGyQBMT': ['civic_docs'], 'var_call_KYRK4xUSAtxEAJdgI1BrqhqV': 'file_storage/call_KYRK4xUSAtxEAJdgI1BrqhqV.json', 'var_call_5wBIUvFbVq6D7BGzPAvwAJbx': 'file_storage/call_5wBIUvFbVq6D7BGzPAvwAJbx.json'}

exec(code, env_args)
