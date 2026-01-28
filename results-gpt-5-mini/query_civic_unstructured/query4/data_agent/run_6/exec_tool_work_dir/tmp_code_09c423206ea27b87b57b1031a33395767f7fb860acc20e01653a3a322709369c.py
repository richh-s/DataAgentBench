code = """import json, re
# Load the civic docs query result saved to a file path
path = var_call_WQOnz4h2kKRYxFLRC3s88Esu
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = set()
for doc in docs:
    text = doc.get('text','')
    # find occurrences of lines with 'Project'
    for m in re.finditer(r'(?P<name>.{0,120}?Project[^\n\r]*)', text, flags=re.I):
        name = m.group('name').strip()
        start = m.start()
        snippet = text[start:start+400]
        if re.search(r'spring', snippet, flags=re.I) and re.search(r'2022', snippet):
            projects.add(name)
            continue
        # check for months March/April/May 2022
        if re.search(r'(march|april|may)\s*,?\s*2022', snippet, flags=re.I) or re.search(r'2022.*(march|april|may)', snippet, flags=re.I):
            projects.add(name)

# As a fallback, also search for 'Begin Construction' or 'Advertise' followed by 'Spring' and '2022' and try to grab a preceding project title line
for doc in docs:
    text = doc.get('text','')
    for m in re.finditer(r'(?P<action>(Begin Construction|Advertise|Project Schedule|Estimated Schedule).{0,80}?(Spring).{0,30}?(2022))', text, flags=re.I):
        start = m.start()
        # look backwards for a nearby line that looks like a project title (short line)
        before = text[max(0, start-200):start]
        lines = before.strip().splitlines()
        if lines:
            candidate = lines[-1].strip()
            # choose candidate if it contains keywords or is reasonably short
            if 3 < len(candidate) < 120 and any(k in candidate.lower() for k in ['project','repair','improvements','improvement','study','plan','park','water','road','drain','playground']):
                projects.add(candidate)

projects_list = sorted(projects)
# Output JSON string with list of project names
out = json.dumps({"projects": projects_list})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_hSIn0HXpIysBJLncOq2LulYt': ['civic_docs'], 'var_call_6f74mMKpIuCBNIwpLg5yIUV5': ['Funding'], 'var_call_WQOnz4h2kKRYxFLRC3s88Esu': 'file_storage/call_WQOnz4h2kKRYxFLRC3s88Esu.json'}

exec(code, env_args)
