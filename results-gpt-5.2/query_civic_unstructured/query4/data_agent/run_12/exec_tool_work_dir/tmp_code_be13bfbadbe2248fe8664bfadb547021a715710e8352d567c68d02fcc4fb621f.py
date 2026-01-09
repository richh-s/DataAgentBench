code = """import json, re

raw = var_call_RU0Eeenz3jeZ4nl37lbeV0m4
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

# Capture: Project name line, then later a line with Begin Construction: <value>
block_re = re.compile(
    r"\n\s*([A-Z0-9][^\n]{2,120}?)\n(?:.*?)(?:Project Schedule|Estimated Schedule)(?:.*?)(?:Begin Construction|Begin construction)\s*:\s*([^\n]+)",
    re.IGNORECASE | re.DOTALL,
)

spring2022_projects = set()

for d in docs:
    text = d.get('text','')
    for m in block_re.finditer(text):
        name = m.group(1).strip()
        begin = m.group(2).strip().lower()
        if '2022' in begin and 'spring' in begin:
            spring2022_projects.add(name)

proj_list = sorted(spring2022_projects)
result = {"spring_2022_project_count": len(proj_list), "spring_2022_projects": proj_list}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WF7nOmUatVD8vw8PJCkI3sVH': ['Funding'], 'var_call_wRmXiS5fuWvTjHJBViejlb7C': ['civic_docs'], 'var_call_RU0Eeenz3jeZ4nl37lbeV0m4': 'file_storage/call_RU0Eeenz3jeZ4nl37lbeV0m4.json'}

exec(code, env_args)
