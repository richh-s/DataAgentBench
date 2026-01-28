code = """import json, re
path = var_call_V2Ly6OD6obg5ajtxJc9hBho4
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = set()
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    norm_lines = [ln.rstrip() for ln in lines]
    for i, ln in enumerate(norm_lines):
        if 'Updates' in ln or 'Updates:' in ln:
            title = None
            for j in range(1,6):
                idx = i-j
                if idx < 0:
                    break
                cand = norm_lines[idx].strip()
                if cand == '':
                    continue
                if cand.startswith('(') or cand.lower().startswith('page'):
                    continue
                title = cand
                break
            if not title:
                continue
            if 'park' in title.lower():
                tail = '\n'.join(norm_lines[i:i+12]).lower()
                if 'completed' in tail and '2022' in tail:
                    t = re.sub(r'^\s*[-\d\.\)]+\s*', '', title)
                    found.add(t)

# Additional pattern search
for doc in docs:
    orig = doc.get('text','')
    text = orig.lower()
    # find patterns like '\n<Title>\n(cid:190) Updates:' earlier may have caught
    # look for 'construction was completed' within 40 chars of a project title containing 'park'
    for m in re.finditer(r"([A-Za-z0-9 \-\'\,\(\)]+park[A-Za-z0-9 \-\'\,\(\)]{0,60})[\s\S]{0,120}completed[^\n]{0,60}2022", text):
        title = m.group(1).strip()
        start = orig.lower().find(title)
        if start != -1:
            orig_title = orig[start:start+len(title)].strip()
            found.add(orig_title)
        else:
            found.add(title)

result = sorted(found)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V4vF7nwAMnAbiopKMftn913k': ['civic_docs'], 'var_call_zhqmXNrCRCQ3GsnKQ7jhMenX': ['Funding'], 'var_call_V2Ly6OD6obg5ajtxJc9hBho4': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json'}

exec(code, env_args)
