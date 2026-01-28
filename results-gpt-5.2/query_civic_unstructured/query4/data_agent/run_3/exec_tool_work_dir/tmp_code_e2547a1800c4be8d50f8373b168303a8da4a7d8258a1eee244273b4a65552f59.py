code = """import json, re
import pandas as pd
from pathlib import Path

# Load civic docs (may be file path)
docs_var = var_call_NJuQuU8dAwc68QljUo19BomL
if isinstance(docs_var, str) and docs_var.endswith('.json'):
    docs = json.loads(Path(docs_var).read_text())
else:
    docs = docs_var

text_all = "\n\n".join(d.get('text','') for d in docs)

# Extract candidate project names and schedules from patterns like:
# <Project Name> ... Project Schedule: ... Begin Construction: Spring 2022
lines = text_all.splitlines()
records = []
current_project = None

proj_name_pat = re.compile(r'^(?!\s)([A-Za-z0-9][A-Za-z0-9\-\&\,\./\(\)\'\u2019\s]{3,})$')
begin_pat = re.compile(r'Begin\s+Construction\s*:\s*([A-Za-z]+\s*\d{4}|\d{4}-[A-Za-z]+|\d{4}-Spring|\d{4}-Summer|\d{4}-Fall|\d{4}-Winter|Spring\s*\d{4}|Summer\s*\d{4}|Fall\s*\d{4}|Winter\s*\d{4})', re.IGNORECASE)
start_pat = re.compile(r'\b(Start|Begin)\b[^:\n]{0,40}:\s*([A-Za-z]+\s*\d{4}|\d{4}-[A-Za-z]+|\d{4}-Spring|\d{4}-Summer|\d{4}-Fall|\d{4}-Winter|Spring\s*\d{4}|Summer\s*\d{4}|Fall\s*\d{4}|Winter\s*\d{4})', re.IGNORECASE)

# Identify project blocks by headings used in agendas (project name line followed by bullets)
for i, ln in enumerate(lines):
    s = ln.strip()
    if not s:
        continue
    # heuristic: project name lines often have no colon and not too long
    if len(s) <= 120 and ':' not in s and 'Projects' not in s and 'Project Schedule' not in s and 'Updates' not in s and 'Project Description' not in s:
        # filter out generic section headers
        if s.lower() in {'capital improvement projects (design)','capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects','capital improvement projects','disaster recovery projects (design)','disaster recovery projects (construction)'}:
            continue
        # treat as potential project name
        current_project = s
    # look for begin/start date in nearby lines
    m = begin_pat.search(ln) or start_pat.search(ln)
    if m and current_project:
        date_str = m.group(1) if m.re.pattern==begin_pat.pattern else m.group(2)
        records.append({'Project_Name': current_project, 'Start': date_str})

# Normalize Start string to canonical like 'Spring 2022'
def norm_season(s):
    s = s.strip()
    s = s.replace(',', ' ')
    s = re.sub(r'\s+', ' ', s)
    # convert 2022-Spring -> Spring 2022
    m = re.match(r'(\d{4})-(Spring|Summer|Fall|Winter)', s, re.IGNORECASE)
    if m:
        return f"{m.group(2).title()} {m.group(1)}"
    m = re.match(r'(Spring|Summer|Fall|Winter)\s*(\d{4})', s, re.IGNORECASE)
    if m:
        return f"{m.group(1).title()} {m.group(2)}"
    # month year e.g. March 2022; map March-May to Spring
    m = re.match(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s*(\d{4})', s, re.IGNORECASE)
    if m:
        month = m.group(1).lower()
        year = m.group(2)
        season = None
        if month in ['march','april','may']:
            season = 'Spring'
        elif month in ['june','july','august']:
            season = 'Summer'
        elif month in ['september','october','november']:
            season = 'Fall'
        elif month in ['december','january','february']:
            season = 'Winter'
        if season:
            return f"{season} {year}"
    return s

for r in records:
    r['Start_Norm'] = norm_season(r['Start'])

# Deduplicate by project, take earliest mention (not necessary)
df = pd.DataFrame(records).dropna()
# filter spring 2022
spring2022 = df[df['Start_Norm'].str.lower().eq('spring 2022')]
projects = sorted(spring2022['Project_Name'].unique().tolist())

print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_3PvoLb4aWAWEKtJBVZCC1wcP': ['Funding'], 'var_call_NJuQuU8dAwc68QljUo19BomL': 'file_storage/call_NJuQuU8dAwc68QljUo19BomL.json'}

exec(code, env_args)
