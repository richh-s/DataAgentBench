code = """import json
import re

# Load citations result (possibly from file)
path = var_call_1FUKgxJcgDHNyFnVgFM0FkzJ
with open(path, 'r') as f:
    citations = json.load(f)

# Load paper docs (possibly from file)
path2 = var_call_SpyIo8Gpgnjf9DkYQjfa9poq
with open(path2, 'r') as f:
    papers = json.load(f)

# Build map from title to source by parsing text for 'Copyright' line containing ACM
source_by_title = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # look for 'Copyright' lines
    source = None
    for line in text.split('\n')[:80]:  # only first 80 lines
        if 'Copyright' in line and 'ACM' in line:
            source = 'ACM'
            break
    if source:
        source_by_title[title] = source

# Filter citations for ACM-sourced papers
counts = []
for row in citations:
    title = row['title']
    if source_by_title.get(title) == 'ACM':
        try:
            c = int(row['citation_count'])
        except Exception:
            continue
        counts.append(c)

avg = sum(counts)/len(counts) if counts else None

import math
if avg is not None:
    avg = round(avg, 2)

result = avg

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1FUKgxJcgDHNyFnVgFM0FkzJ': 'file_storage/call_1FUKgxJcgDHNyFnVgFM0FkzJ.json', 'var_call_SpyIo8Gpgnjf9DkYQjfa9poq': 'file_storage/call_SpyIo8Gpgnjf9DkYQjfa9poq.json'}

exec(code, env_args)
