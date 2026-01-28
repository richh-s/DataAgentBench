code = """import json, re
# read the large civic docs query result from storage variable
path = var_call_V2Ly6OD6obg5ajtxJc9hBho4
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = set()
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # normalize lines by stripping
    norm_lines = [ln.rstrip() for ln in lines]
    for i, ln in enumerate(norm_lines):
        if 'Updates' in ln or 'Updates:' in ln:
            # look back up to 5 lines to find a title that is non-empty and not starting with '(' or 'Page'
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
                # choose this candidate as title
                title = cand
                break
            if not title:
                continue
            # check if title contains 'park'
            if 'park' in title.lower():
                # check next up to 12 lines for 'completed' AND '2022'
                tail = '\n'.join(norm_lines[i:i+12]).lower()
                if 'completed' in tail and '2022' in tail:
                    # clean title remove leading numbering or bullets
                    t = re.sub(r'^\s*[-\d\.\)]+\s*', '', title)
                    found.add(t)

# As backup, also search for lines that directly mention 'Construction was completed' and 'park' nearby
for doc in docs:
    text = doc.get('text','').lower()
    # find occurrences of 'construction was completed' with 2022
    for m in re.finditer(r"([\w \-\'\,\(\)]+park[\w \-\'\,\(\)]{0,60})[\s\S]{0,120}completed[^\n]{0,60}2022", text):
        title = m.group(1).strip()
        # capitalize appropriately by extracting original substring from original text
        orig = doc.get('text','')
        start = orig.lower().find(title)
        if start!=-1:
            orig_title = orig[start:start+len(title)].strip()
            found.add(orig_title)
        else:
            found.add(title)

result = sorted(found)
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V4vF7nwAMnAbiopKMftn913k': ['civic_docs'], 'var_call_zhqmXNrCRCQ3GsnKQ7jhMenX': ['Funding'], 'var_call_V2Ly6OD6obg5ajtxJc9hBho4': 'file_storage/call_V2Ly6OD6obg5ajtxJc9hBho4.json'}

exec(code, env_args)
