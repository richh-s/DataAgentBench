code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_KYRK4xUSAtxEAJdgI1BrqhqV)
fund = load_json_maybe(var_call_5wBIUvFbVq6D7BGzPAvwAJbx)

# Build map of project_name -> total_amount (int)
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

# Parse civic docs for project blocks that include 'Project Schedule' and capture et and status
# Heuristic: a project header line is a non-empty line not starting with bullets and followed by an Updates section.

def extract_projects_from_text(text):
    lines = text.splitlines()
    projects = []
    i=0
    while i < len(lines):
        line = lines[i].strip()
        # candidate project name: title case-ish and not section headings
        if line and not line.startswith(('(', 'cid:', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Staff', 'Recommended')):
            # avoid obvious labels
            if re.search(r'Project( Schedule| Description| Updates)?\s*:', line):
                i += 1
                continue
            # look ahead for 'Updates' within next 5 lines
            look = "\n".join([lines[j] for j in range(i+1, min(i+8, len(lines)))])
            if re.search(r'Updates\s*:', look):
                name = line
                # gather block until blank line followed by another likely title or until 40 lines
                block_lines = []
                j = i
                while j < len(lines) and j < i+60:
                    bl = lines[j]
                    if j>i and lines[j].strip()=='' and j+1 < len(lines):
                        # potential end if next non-empty looks like new project or section
                        k=j+1
                        while k < len(lines) and lines[k].strip()=='' :
                            k+=1
                        if k>=len(lines):
                            j=k
                            break
                        nxt = lines[k].strip()
                        if nxt and re.search(r'(Projects \(|Disaster Recovery|Capital Improvement|Page \d|Agenda Item)', nxt):
                            j=k
                            break
                        # if next has Updates soon, treat as new project
                        look2 = "\n".join([lines[m] for m in range(k+1, min(k+8, len(lines)))])
                        if re.search(r'Updates\s*:', look2):
                            j=k
                            break
                    block_lines.append(bl)
                    j+=1
                block = "\n".join(block_lines)

                # status: look for 'Construction was completed' or 'completed' etc in block
                status = None
                if re.search(r'\bConstruction was completed\b', block, flags=re.I) or re.search(r'\bNotice of completion\b', block, flags=re.I):
                    status = 'completed'
                elif re.search(r'\bcomplete(d)?\b', block, flags=re.I) and re.search(r'\bComplete (Design|Construction)\b', block, flags=re.I):
                    # not definitive
                    pass

                # extract end time: first occurrence after 'Complete (Design|Construction):'
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
    if not txt:
        continue
    all_projects.extend(extract_projects_from_text(txt))

# Determine park-related: name or block contains 'park' or 'playground' or known park facilities
park_kw = re.compile(r'\b(park|playground|bluffs)\b', re.I)

def is_park_related(p):
    nm = p.get('Project_Name','')
    blk = p.get('block','')
    return bool(park_kw.search(nm) or park_kw.search(blk))

# Completed in 2022: status completed and et contains 2022 OR block contains 'completed ... 2022'

def completed_in_2022(p):
    blk = p.get('block','')
    et = p.get('et') or ''
    if re.search(r'completed\s+\w+\s+2022', blk, flags=re.I) or re.search(r'completed\s+in\s+\w+\s*2022', blk, flags=re.I):
        return True
    if et and '2022' in et:
        # but ensure it's completed status
        return (p.get('status')=='completed')
    # also accept completed status and mention 'November 2022' etc anywhere
    if p.get('status')=='completed' and re.search(r'\b2022\b', blk):
        return True
    return False

selected = []
for p in all_projects:
    if is_park_related(p) and completed_in_2022(p):
        name = p['Project_Name']
        amt = fund_map.get(name)
        selected.append({'Project_Name': name, 'funding': amt if amt is not None else 0})

# de-duplicate by name taking funding once
seen=set(); total=0
for r in selected:
    if r['Project_Name'] in seen:
        continue
    seen.add(r['Project_Name'])
    total += int(r['funding'] or 0)

print('__RESULT__:')
print(json.dumps({'total_funding_completed_park_projects_2022': total, 'projects': sorted(list(seen))}))"""

env_args = {'var_call_4PG5K1JFOxGDnVSmjHEy9scy': ['Funding'], 'var_call_LZiL1tp6SEIuXVpXZIGyQBMT': ['civic_docs'], 'var_call_KYRK4xUSAtxEAJdgI1BrqhqV': 'file_storage/call_KYRK4xUSAtxEAJdgI1BrqhqV.json', 'var_call_5wBIUvFbVq6D7BGzPAvwAJbx': 'file_storage/call_5wBIUvFbVq6D7BGzPAvwAJbx.json'}

exec(code, env_args)
