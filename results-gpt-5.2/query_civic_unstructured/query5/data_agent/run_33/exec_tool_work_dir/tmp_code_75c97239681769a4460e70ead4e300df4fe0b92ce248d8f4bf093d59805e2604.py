code = """import json, re
from pathlib import Path

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str) and maybe_path_or_records.endswith('.json'):
        return json.loads(Path(maybe_path_or_records).read_text())
    return maybe_path_or_records

civic_recs = load_records(var_call_ZYtrRg6YQuqLcxt7slVcKrb9)

def extract_disaster_projects_started_2022(text):
    # Find disaster recovery section and project blocks
    # Heuristic: capture lines between 'Disaster Recovery Projects' and next major header
    lines = text.splitlines()
    # normalize
    idx = None
    for i,l in enumerate(lines):
        if re.search(r'Disaster Recovery Projects', l, re.I):
            idx = i
            break
    if idx is None:
        return []
    # take a window after header
    window = lines[idx:]
    # stop if another agenda item end? keep reasonable size
    window = window[:800]
    # Identify project names as standalone lines (not bullets) followed by 'Updates' and 'Project Schedule'
    projects = []
    for i,l in enumerate(window):
        l_str = l.strip()
        if not l_str or len(l_str) > 120:
            continue
        # likely project name line: Title Case words and contains keywords, and not starting with '(' or 'Page'
        if l_str.startswith(('(cid', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement')):
            continue
        # exclude common labels
        if re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)\b', l_str, re.I):
            continue
        # Consider as project if next few lines contain 'Project Schedule'
        next_chunk = '\n'.join([w.strip() for w in window[i:i+30]])
        if re.search(r'Project Schedule', next_chunk, re.I) and re.search(r'Begin (Construction|Design|Construction:)', next_chunk, re.I):
            # get begin line
            m = re.search(r'Begin (?:Construction|Design)\s*:\s*([^\n\r]+)', next_chunk, re.I)
            begin = m.group(1).strip() if m else None
            projects.append((l_str, begin))
    # filter begins containing 2022
    out = []
    for name, begin in projects:
        if begin and '2022' in begin:
            out.append(name)
    # de-dup
    seen=set(); uniq=[]
    for n in out:
        if n not in seen:
            seen.add(n); uniq.append(n)
    return uniq

projects_2022=set()
for rec in civic_recs:
    for p in extract_disaster_projects_started_2022(rec.get('text','')):
        projects_2022.add(p)

result = {'projects_started_2022_disaster': sorted(projects_2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_mfWaEFrfiY7eOT37QkwDcsbv': ['Funding'], 'var_call_2XFv5yYihjWlW1Gp9BKjtyGo': [{'total_funding': '1410000'}], 'var_call_mWWzHlltBpzVXGUApq0UA9q2': ['civic_docs'], 'var_call_ZYtrRg6YQuqLcxt7slVcKrb9': 'file_storage/call_ZYtrRg6YQuqLcxt7slVcKrb9.json'}

exec(code, env_args)
