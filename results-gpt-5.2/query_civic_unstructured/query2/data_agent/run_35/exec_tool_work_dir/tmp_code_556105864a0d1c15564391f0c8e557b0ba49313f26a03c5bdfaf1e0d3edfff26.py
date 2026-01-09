code = """import re, json
from pathlib import Path

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        return json.loads(Path(var).read_text())
    return var

recs = load(var_call_gsdNDPGLj7bdgeEHBqh2edcd)
text_all = "\n".join(r.get('text','') for r in recs)
lines = [ln.strip() for ln in text_all.splitlines()]

bullet_prefixes = ('(cid', '\uf0b7', '•', '-')
header_starts = ('Public', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital', 'Storm', 'Page')

def is_title(ln):
    if (not ln) or (len(ln) > 120):
        return False
    if ln.startswith(header_starts):
        return False
    if ln.startswith(bullet_prefixes):
        return False
    if ln.endswith(':') or (':' in ln):
        return False
    if ln.count(' ') > 12:
        return False
    return True

park_re = re.compile(r"\b(park|playground|bluffs|skate)\b", re.I)

current = None
completed_2022 = set()
for ln in lines:
    if is_title(ln):
        current = ln
    if current and park_re.search(current):
        if re.search(r"Construction was completed\s*(,)?\s*[A-Za-z]*\s*2022", ln, re.I) or re.search(r"Complete Construction:\s*.*2022", ln, re.I):
            completed_2022.add(current)

print('__RESULT__:')
print(json.dumps({'projects': sorted(completed_2022), 'count': len(completed_2022)}))"""

env_args = {'var_call_BS3mWapbppeBGys41aMraj6f': ['Funding'], 'var_call_3GqwVynV65vRLEHoYdkLXplO': ['civic_docs'], 'var_call_xaBtDyrvLf2HBp16vz21aGew': 'file_storage/call_xaBtDyrvLf2HBp16vz21aGew.json', 'var_call_FzqbhXr7HgF7ktDvO9gKCH1S': {'completed_park_projects': [], 'count': 0}, 'var_call_gsdNDPGLj7bdgeEHBqh2edcd': 'file_storage/call_gsdNDPGLj7bdgeEHBqh2edcd.json'}

exec(code, env_args)
