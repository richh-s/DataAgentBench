code = """import json, re
path = var_call_BbHlkOS5ptYiDuPuA4GtohCC
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

matches = []
for doc in docs:
    text = doc.get('text','')
    # find all occurrences of 'spring' and '2022' within 120 chars
    for m in re.finditer(r'(Spring[,\s]*2022|2022[,\s]*Spring|Spring\s+\d{4})', text, re.IGNORECASE):
        start = m.start()
        # capture 1000 chars before match to find project header
        window_start = max(0, start-1000)
        snippet = text[window_start:start+200]
        matches.append({'filename': doc.get('filename'), 'match_text': m.group(0), 'snippet': snippet})

# Also search for explicit month-year like 'March 2022', 'Apr 2022', 'May 2022'
for doc in docs:
    text = doc.get('text','')
    for m in re.finditer(r'\b(March|Mar\.|April|Apr\.|May|May\.)[,\s]*2022\b|2022[- ](?:03|04|05)\b', text, re.IGNORECASE):
        start = m.start()
        window_start = max(0, start-1000)
        snippet = text[window_start:start+200]
        matches.append({'filename': doc.get('filename'), 'match_text': m.group(0), 'snippet': snippet})

# Deduplicate by snippet content
seen = set()
unique = []
for m in matches:
    key = (m['filename'], m['match_text'], m['snippet'][:200])
    if key not in seen:
        seen.add(key)
        unique.append(m)

# Print count and snippets
out = {'count': len(unique), 'examples': unique[:20]}
import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BbHlkOS5ptYiDuPuA4GtohCC': 'file_storage/call_BbHlkOS5ptYiDuPuA4GtohCC.json', 'var_call_wzdYOCoVDSdfZqe0nUNWVPJq': []}

exec(code, env_args)
