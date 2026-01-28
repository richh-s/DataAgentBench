code = """import json
path = var_call_V2Ly6OD6obg5ajtxJc9hBho4
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = set()
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # scan each line for a probable title containing 'park'
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'park' in low and len(line.strip())>0 and len(line.strip())<200:
            # skip lines that are clearly section headers
            if line.strip().lower().startswith('page'):
                continue
            # look ahead up to 12 lines for 'completed' and '2022'
            look = '\n'.join(lines[idx:idx+13]).lower()
            if 'completed' in look and '2022' in look:
                title = line.strip()
                # clean common bullets
                if title.startswith('-') or title[0].isdigit():
                    # remove leading bullets/numbers
                    import re
                    title = re.sub(r'^\s*[-\d\.\)]+\s*', '', title)
                found.add(title)

result = sorted(found)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V4vF7nwAMnAbiopKMftn913k': ['civic_docs'], 'var_call_zhqmXNrCRCQ3GsnKQ7jhMenX': ['Funding'], 'var_call_V2Ly6OD6obg5ajtxJc9hBho4': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json'}

exec(code, env_args)
