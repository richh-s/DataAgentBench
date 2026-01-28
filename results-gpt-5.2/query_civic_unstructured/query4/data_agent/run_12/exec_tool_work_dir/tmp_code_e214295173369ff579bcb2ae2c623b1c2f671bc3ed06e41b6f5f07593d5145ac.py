code = """import json, re

# Load mongo docs (may be a file path)
raw = var_call_RU0Eeenz3jeZ4nl37lbeV0m4
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

# Regex to capture project blocks with schedule lines
# We look for a project name line followed by 'Updates' and 'Project Schedule' or 'Estimated Schedule'
block_re = re.compile(
    r"\n\s*([A-Z0-9][^\n]{2,120}?)\n\s*\n\s*\(cid:190\)\s*Updates:.*?(?:Project Schedule|Estimated Schedule).*?(?:\n\s*\(cid:131\)\s*(?:Begin Construction|Begin construction|Start Construction|Start):\s*([^\n]+))",
    re.IGNORECASE | re.DOTALL,
)

spring2022_projects = set()

for d in docs:
    text = d.get('text','')
    for m in block_re.finditer(text):
        name = m.group(1).strip()
        begin = m.group(2).strip()
        # normalize begin string
        b = begin.lower()
        if '2022' in b and 'spring' in b:
            spring2022_projects.add(name)

# Also catch formats like 'Begin Construction: May 2022' etc within March-May 2022
month_map = {'march':3,'april':4,'may':5}
month_re = re.compile(r"\b(begin construction|begin construction|begin|start)\s*:\s*([A-Za-z]+)\s+2022\b", re.IGNORECASE)
for d in docs:
    text = d.get('text','')
    # split by project headings (blank lines), crude: look for lines followed by '(cid:190) Updates'
    lines = text.splitlines()
    for i,line in enumerate(lines[:-1]):
        if line.strip() and i+2 < len(lines) and 'updates' in lines[i+2].lower():
            name = line.strip()
    for mm in month_re.finditer(text):
        mon = mm.group(2).lower()
        if mon in month_map:
            # nearest previous non-empty line could be project name; too fuzzy, skip
            pass

proj_list = sorted(spring2022_projects)
result = {"spring_2022_project_count": len(proj_list), "spring_2022_projects": proj_list}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WF7nOmUatVD8vw8PJCkI3sVH': ['Funding'], 'var_call_wRmXiS5fuWvTjHJBViejlb7C': ['civic_docs'], 'var_call_RU0Eeenz3jeZ4nl37lbeV0m4': 'file_storage/call_RU0Eeenz3jeZ4nl37lbeV0m4.json'}

exec(code, env_args)
