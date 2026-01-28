code = """import json
path = var_call_VPIjJV0MwaTNmYb1IXbnb3Ip
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

project_names = []
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        low = line.lower()
        # consider lines that look like titles
        if any(word in low for word in ['project', 'repairs', 'repair', 'improvements', 'facility', 'phase', 'playground', 'walkway']):
            # get a block of following lines
            block = '\n'.join(lines[i:i+12]).lower()
            if 'fema' in block or 'emergency' in block or 'caloes' in block or 'disaster' in block or 'federal' in block:
                title = line.strip()
                # clean title
                if title == '':
                    continue
                # remove leading non-alphanumeric chars
                import re
                title = re.sub(r'^[^A-Za-z0-9]+', '', title)
                if title not in project_names:
                    project_names.append(title)

# If nothing found, fallback: search entire docs for lines containing FEMA or emergency and take nearby lines
if not project_names:
    import re
    for doc in docs:
        text = doc.get('text','')
        m = re.finditer(r'(.{0,200})(FEMA|emergency)(.{0,200})', text, re.IGNORECASE)
        for match in m:
            snippet = match.group(0)
            # try to find a line with 'Project' in snippet
            lines = snippet.splitlines()
            for line in lines:
                if 'project' in line.lower():
                    title = line.strip()
                    title = re.sub(r'^[^A-Za-z0-9]+', '', title)
                    if title and title not in project_names:
                        project_names.append(title)

print('__RESULT__:')
print(json.dumps(project_names))"""

env_args = {'var_call_VPIjJV0MwaTNmYb1IXbnb3Ip': 'file_storage/call_VPIjJV0MwaTNmYb1IXbnb3Ip.json'}

exec(code, env_args)
