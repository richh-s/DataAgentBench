code = """import json, re
with open(var_call_BM51I30oAu2S3Iytx6gDIzK1, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
for doc in docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for i, line in enumerate(lines):
        if re.search(r'(?i)Spring(?:/Summer)?\s*2022|Spring of 2022|March\s*2022|April\s*2022|May\s*2022', line):
            # look upward for project title within 10 lines
            found = None
            for k in range(1, 12):
                idx = i - k
                if idx < 0:
                    break
                cand = lines[idx].strip()
                if not cand:
                    continue
                # skip known section headers or short markers
                if re.search(r'(?i)^(updates:|project schedule:|project description:|agenda item|page \d+|item|cid:|approved by:|to:|prepared by:|date prepared:|meeting date:)', cand):
                    continue
                # skip lines ending with ':'
                if cand.endswith(':'):
                    continue
                # skip lines that are all uppercase words like 'PUBLIC WORKS COMMISSION'
                if re.fullmatch(r'[A-Z0-9\W\s]+', cand) and len(cand.split())>1:
                    continue
                # skip lines that are like '(cid:131)'
                if re.search(r'\(cid:', cand):
                    continue
                # Candidate should be reasonably short
                if 3 <= len(cand) <= 120:
                    found = cand
                    break
            if found:
                candidates.append(found)

# deduplicate preserving order
seen = set()
projects = []
for p in candidates:
    if p not in seen:
        seen.add(p)
        projects.append(p)

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_call_BM51I30oAu2S3Iytx6gDIzK1': 'file_storage/call_BM51I30oAu2S3Iytx6gDIzK1.json', 'var_call_T3E2Gtr9Skk7kPywXXcfXGbG': []}

exec(code, env_args)
