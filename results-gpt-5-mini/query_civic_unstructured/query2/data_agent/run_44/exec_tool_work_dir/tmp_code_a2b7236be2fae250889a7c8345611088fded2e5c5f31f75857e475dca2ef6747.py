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
            # look ahead for 'completed' and '2022'
            look = '\n'.join(lines[i:i+13]).lower()
            if 'completed' in look and '2022' in look:
                title = line.strip()
                # clean simple bullets/numbers
                if title and (title[0]=='-' or title[0].isdigit()):
                    # remove leading non-alpha chars
                    import re
                    title = re.sub(r'^\W+','',title)
                if title not in found:
                    found.append(title)

# also search entire text for patterns 'Construction was completed' and find nearest preceding title line
for doc in docs:
    text = doc.get('text','')
    low = text.lower()
    if 'construction was completed' in low and '2022' in low:
        idx = low.find('construction was completed')
        # look backwards up to 300 chars to find a newline and extract a line with 'park'
        start = max(0, idx-300)
        snippet = text[start:idx]
        lines = snippet.splitlines()
        # scan reverse for a line containing 'park'
        for line in reversed(lines):
            if 'park' in line.lower():
                title = line.strip()
                if title and (title[0]=='-' or title[0].isdigit()):
                    import re
                    title = re.sub(r'^\W+','',title)
                if title not in found:
                    found.append(title)
                break

# final unique list
found = sorted(found)
print('__RESULT__:')
import json
print(json.dumps(found))"""

env_args = {'var_call_V4vF7nwAMnAbiopKMftn913k': ['civic_docs'], 'var_call_zhqmXNrCRCQ3GsnKQ7jhMenX': ['Funding'], 'var_call_V2Ly6OD6obg5ajtxJc9hBho4': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json', 'var_call_hpPReWfvyf7lehCWFK0cGfHh': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json'}

exec(code, env_args)
