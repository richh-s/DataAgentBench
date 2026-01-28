code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

funding = load_records(var_call_rAHitqOuLrlh5WKubhvWvcqL)
docs = load_records(var_call_K9FlW7oxrDQ771DWPj4Fw2xM)

funding_names = set(r['Project_Name'] for r in funding)

# detect 'Capital Improvement Projects (Design)' sections and capture project names that follow
status_design_projects = set()

# patterns indicating section start
start_pat = re.compile(r'(?im)^\s*Capital Improvement Projects\s*\(\s*Design\s*\)\s*$')
# patterns indicating section end
end_pat = re.compile(r'(?im)^\s*Capital Improvement Projects\s*\(\s*(Construction|Not Started)\s*\)\s*$|^\s*Disaster Recovery Projects\b')

bullet = re.compile(r"^[ \t\u00a0\-\*\u2022\(\)cid:\d;\.]*")

for d in docs:
    text = d.get('text') or ''
    if not text:
        continue
    # find all design section blocks
    for m in start_pat.finditer(text):
        start = m.end()
        # find nearest end after start
        m_end = end_pat.search(text, start)
        end = m_end.start() if m_end else len(text)
        block = text[start:end]
        # scan lines; collect candidate project names by matching against funding names
        for line in block.splitlines():
            s = line.strip()
            if not s:
                continue
            # ignore obvious non-names
            if re.search(r'(?i)^(updates|project schedule|estimated schedule|project description|page \d+ of \d+|agenda item|recommended action|discussion)\b', s):
                continue
            s2 = bullet.sub('', s).strip()
            if not s2:
                continue
            # try exact match
            if s2 in funding_names:
                status_design_projects.add(s2)

# count those design projects that also have funding > 50k (already filtered in funding list)
answer_count = len(status_design_projects.intersection(funding_names))

print('__RESULT__:')
print(json.dumps({'count': answer_count, 'projects': sorted(status_design_projects.intersection(funding_names))}))"""

env_args = {'var_call_t9mkzZDLCH9CqlWmSSLi1Tgc': [{'cnt': '276'}], 'var_call_K9FlW7oxrDQ771DWPj4Fw2xM': 'file_storage/call_K9FlW7oxrDQ771DWPj4Fw2xM.json', 'var_call_rAHitqOuLrlh5WKubhvWvcqL': 'file_storage/call_rAHitqOuLrlh5WKubhvWvcqL.json'}

exec(code, env_args)
