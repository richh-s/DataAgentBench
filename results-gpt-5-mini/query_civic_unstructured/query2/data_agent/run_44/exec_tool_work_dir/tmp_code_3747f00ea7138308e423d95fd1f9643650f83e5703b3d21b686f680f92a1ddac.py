code = """import json
path = var_call_hpPReWfvyf7lehCWFK0cGfHh
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = []
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if 'park' in low and line.strip():
            look_lines = lines[i:i+13]
            look_text = " ".join([l.lower() for l in look_lines])
            if 'completed' in look_text and '2022' in look_text:
                title = line.strip()
                if title and (not title[0].isalnum()):
                    j=0
                    while j < len(title) and not title[j].isalnum():
                        j+=1
                    title = title[j:]
                if title not in found:
                    found.append(title)

for doc in docs:
    text = doc.get('text','')
    low = text.lower()
    if 'construction was completed' in low and '2022' in low:
        idx = low.find('construction was completed')
        start = idx-300 if idx>300 else 0
        snippet = text[start:idx]
        lines = snippet.splitlines()
        for line in reversed(lines):
            if 'park' in line.lower():
                title = line.strip()
                if title and (not title[0].isalnum()):
                    j=0
                    while j < len(title) and not title[j].isalnum():
                        j+=1
                    title = title[j:]
                if title not in found:
                    found.append(title)
                break

found = sorted(found)
print('__RESULT__:')
print(json.dumps(found))"""

env_args = {'var_call_V4vF7nwAMnAbiopKMftn913k': ['civic_docs'], 'var_call_zhqmXNrCRCQ3GsnKQ7jhMenX': ['Funding'], 'var_call_V2Ly6OD6obg5ajtxJc9hBho4': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json', 'var_call_hpPReWfvyf7lehCWFK0cGfHh': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json'}

exec(code, env_args)
