code = """import json, re
# var_call_wImwkSyb52z6GhaPMqPSk2rh is available from previous tool call and contains the file path
p = var_call_wImwkSyb52z6GhaPMqPSk2rh
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)
texts = [d.get('text','') for d in docs]
found = set()
for text in texts:
    for m in re.finditer(r'(?i)park', text):
        idx = m.start()
        start = max(0, idx-300)
        end = min(len(text), idx+400)
        window = text[start:end]
        # check if 'completed' and '2022' appear after the occurrence within window
        after = text[idx:end]
        if re.search(r'completed', after, re.I) and re.search(r'2022', after):
            # try to extract a project name around the 'park' occurrence
            # capture capitalized phrase including 'Park' up to line breaks
            # search backwards to the previous double newline or line start
            pre_segment = text[max(0, idx-200):idx+200]
            # regex to capture a phrase containing 'park'
            m2 = re.search(r'([A-Z][A-Za-z0-9 &,\-\'"()]{0,120}?park[A-Za-z0-9 &,\-\'"()]{0,120}?)', pre_segment, re.I)
            if m2:
                name = m2.group(1).strip()
                # clean up whitespace and trailing punctuation
                name = re.sub(r'\s+', ' ', name)
                name = name.strip(' -:\n\r')
                found.add(name)
# convert to sorted list
result = sorted(found)
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wImwkSyb52z6GhaPMqPSk2rh': 'file_storage/call_wImwkSyb52z6GhaPMqPSk2rh.json'}

exec(code, env_args)
