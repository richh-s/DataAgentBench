code = """import json, re
from pathlib import Path

docs_path = var_call_T7sf1DXAkweBowsJnBnlIKEa
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

spring_pattern = re.compile(r"Spring\b.*2022|2022.*Spring|\b(Spring)\b", re.IGNORECASE)
months_pattern = re.compile(r"\b(March|April|May)\b.*2022|2022.*\b(March|April|May)\b|2022[-_/ ]?(March|April|May)", re.IGNORECASE)

results = []

for doc in docs:
    lines = doc.get('text','').splitlines()
    for i,line in enumerate(lines):
        if spring_pattern.search(line) or months_pattern.search(line):
            # gather context
            start = max(0, i-6)
            context = '\n'.join(lines[start:i+3])
            # try to find a title: look backwards for a line that looks like a project name
            title = None
            for j in range(i-1, max(0,i-12)-1, -1):
                cand = lines[j].strip()
                if cand and len(cand) > 5 and not cand.lower().startswith(('page','agenda','item','to:', 'subject', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'recommend', 'discussion')):
                    # avoid lines that end with ':' or are 'Updates' etc
                    if cand.endswith(':'):
                        continue
                    title = cand
                    break
            results.append({'filename': doc.get('filename'), 'line_num': i+1, 'matched_line': line.strip(), 'title_guess': title, 'context': context})

# Deduplicate by title_guess
seen = set()
uniq = []
for r in results:
    t = r['title_guess'] or r['matched_line']
    if t not in seen:
        seen.add(t)
        uniq.append(r)

output = {'matches_count': len(uniq), 'matches': uniq[:200]}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_HW9ZkBmGMYzpwgAdnQj3jbbt': ['civic_docs'], 'var_call_tAowD8W9bhtcSi6T7DehBuLG': ['Funding'], 'var_call_T7sf1DXAkweBowsJnBnlIKEa': 'file_storage/call_T7sf1DXAkweBowsJnBnlIKEa.json', 'var_call_sk4Py445O2dS9gieZNkgmkxu': 'file_storage/call_sk4Py445O2dS9gieZNkgmkxu.json', 'var_call_Nb7i27L6OQRid4duyT4fxfav': {'count_projects': 0, 'total_funding': 0, 'projects': []}}

exec(code, env_args)
