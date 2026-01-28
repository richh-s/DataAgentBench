code = """import json, re

# Load the large query result from MongoDB stored in the provided file path
path = var_call_dziWdH68wzWWoRRglXmdYLQx
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

keywords = ['fema', 'emergency']
found = []

for doc in docs:
    text = doc.get('text', '')
    # Split into blocks separated by 2+ newlines
    blocks = re.split(r"\n{2,}", text)
    # Clean blocks
    blocks_clean = [b.strip() for b in blocks]
    for idx, block in enumerate(blocks_clean):
        low = block.lower()
        if any(k in low for k in keywords):
            # Heuristic: find a preceding block that looks like a title (short, not system tokens)
            title = None
            for j in range(max(0, idx-3), idx)[::-1]:
                b = blocks_clean[j]
                if len(b) > 0 and len(b) < 200 and '(cid:' not in b.lower() and 'updates:' not in b.lower() and 'project description' not in b.lower():
                    # Use the first line of this block as title candidate
                    title = b.splitlines()[0].strip()
                    break
            if not title:
                # Fallback: use the first line of current block
                title = block.splitlines()[0].strip()
            found.append({'project_name': title, 'match_block': block[:500]})

# Deduplicate by project_name preserving order
seen = set()
unique = []
for item in found:
    name = item['project_name']
    if name and name not in seen:
        seen.add(name)
        unique.append(name)

result = unique

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jWONQnnlxfAddtKc97l9A619': ['civic_docs'], 'var_call_kS6pRvnaONEfsjsY5YLZIDQR': ['Funding'], 'var_call_dziWdH68wzWWoRRglXmdYLQx': 'file_storage/call_dziWdH68wzWWoRRglXmdYLQx.json'}

exec(code, env_args)
