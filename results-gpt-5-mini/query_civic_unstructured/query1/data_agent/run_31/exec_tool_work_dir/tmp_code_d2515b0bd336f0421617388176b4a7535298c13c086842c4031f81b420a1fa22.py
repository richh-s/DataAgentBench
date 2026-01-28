code = """import json
from pathlib import Path
import re
import string

civic_path = Path('file_storage/call_x5yXZsAAfqzLymT3gHILyQpc.json')
funding_path = Path('file_storage/call_zuIL1ZirMabii4vC6dEGiW4a.json')

with civic_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with funding_path.open('r', encoding='utf-8') as f:
    funding = json.load(f)

# simple extraction by searching for project titles under the Design section
projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    marker = 'capital improvement projects (design)'
    if marker not in lower:
        continue
    start = lower.find(marker)
    # find end by looking for 'capital improvement projects (construction)' or '(not started)'
    end_candidates = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'capital improvement projects (construction)']
    end = None
    for cand in end_candidates:
        idx = lower.find(cand, start+1)
        if idx!=-1:
            end = idx
            break
    section = text[start:end] if end else text[start:]
    # now find lines that look like project names: lines before a line that starts with '(cid' or 'updates:'
    lines = [ln.strip() for ln in section.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        if low.startswith('(cid') or low.startswith('updates') or low.startswith('project'):
            continue
        # if next non-empty line contains 'updates' or '(cid', consider ln a project name
        next_nonempty = ''
        for j in range(i+1, min(i+6,len(lines))):
            if lines[j]:
                next_nonempty = lines[j].lower()
                break
        if 'update' in next_nonempty or next_nonempty.startswith('(cid'):
            projects.add(ln)
        else:
            # include known project keywords
            if any(k in low for k in ['park','road','drain','storm','civic center','skate','pch','malibu','trancas','clover','latigo','retaining','slope','water','traffic','walkway']):
                projects.add(ln)

# normalize helper
trans_table = str.maketrans('', '', string.punctuation)
def normalize(s):
    if not s:
        return ''
    s2 = s.lower()
    s2 = s2.replace('\n',' ').replace('\r',' ')
    s2 = ' '.join(s2.split())
    s2 = s2.translate(trans_table)
    return s2

norm_projects = {normalize(p): p for p in projects}

# find funding amounts > 50000 and match
matches = set()
for rec in funding:
    pname = rec.get('Project_Name')
    if not pname:
        continue
    try:
        amt = int(str(rec.get('Amount','0')))
    except:
        try:
            amt = int(float(str(rec.get('Amount','0'))))
        except:
            amt = 0
    if amt <= 50000:
        continue
    np = normalize(pname)
    if np in norm_projects:
        matches.add(norm_projects[np])
        continue
    for nd, orig in norm_projects.items():
        if nd and (nd in np or np in nd):
            matches.add(orig)
            break
    else:
        # token overlap
        tokens = set(np.split())
        for nd, orig in norm_projects.items():
            if len(tokens & set(nd.split())) >= 2:
                matches.add(orig)
                break

result = {'count': len(matches), 'projects': sorted(list(matches))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PvP9ggpoXdIFKvf81tjWJq4X': ['civic_docs'], 'var_call_ReFFgmHoistAkOtfwguJGOQC': ['Funding'], 'var_call_x5yXZsAAfqzLymT3gHILyQpc': 'file_storage/call_x5yXZsAAfqzLymT3gHILyQpc.json', 'var_call_zuIL1ZirMabii4vC6dEGiW4a': 'file_storage/call_zuIL1ZirMabii4vC6dEGiW4a.json', 'var_call_uBYiH7Y8tyNbgWxsT1VHvyxV': {'n': 500}, 'var_call_xWbJUzbF5vBlOKEJCIhcaZ0E': {'civic_path': 'file_storage/call_x5yXZsAAfqzLymT3gHILyQpc.json', 'funding_path': 'file_storage/call_zuIL1ZirMabii4vC6dEGiW4a.json'}}

exec(code, env_args)
