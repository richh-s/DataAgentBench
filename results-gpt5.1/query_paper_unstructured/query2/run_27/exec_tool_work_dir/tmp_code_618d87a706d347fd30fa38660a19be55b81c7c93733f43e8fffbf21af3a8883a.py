code = """import json

path = var_call_1FUKgxJcgDHNyFnVgFM0FkzJ
with open(path, 'r') as f:
    citations = json.load(f)

path2 = var_call_SpyIo8Gpgnjf9DkYQjfa9poq
with open(path2, 'r') as f:
    papers = json.load(f)

source_by_title = {}
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    source = None
    for line in text.split('\n')[:80]:
        if 'Copyright' in line and 'ACM' in line:
            source = 'ACM'
            break
    if source:
        source_by_title[title] = source

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
if avg is not None:
    avg = round(avg, 2)

print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_call_1FUKgxJcgDHNyFnVgFM0FkzJ': 'file_storage/call_1FUKgxJcgDHNyFnVgFM0FkzJ.json', 'var_call_SpyIo8Gpgnjf9DkYQjfa9poq': 'file_storage/call_SpyIo8Gpgnjf9DkYQjfa9poq.json'}

exec(code, env_args)
