code = """import json
import pandas as pd
# load data files from storage
with open(var_call_BMQZZ8eg5m7Zh9DJLBFwpd6N, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_xMBGKOdyMHo3TtpYfIyNOc2Q, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# build filename->text mapping
paper_text_by_filename = {p['filename']: p.get('text','') for p in papers}

import re

def has_acm(text):
    return bool(re.search(r"\bACM\b", text))

# For each citation record (these are citations in 2018), check if the paper's text contains ACM
filtered = []
missing = 0
for rec in citations:
    title = rec.get('title')
    citation_count = int(rec.get('citation_count',0))
    filename = title + '.txt'
    text = paper_text_by_filename.get(filename)
    if text is None:
        missing += 1
        continue
    if has_acm(text):
        filtered.append({'title': title, 'citation_count': citation_count, 'filename': filename})

if filtered:
    avg = sum(r['citation_count'] for r in filtered)/len(filtered)
else:
    avg = None

out = {'num_acm_papers_in_2018_citations': len(filtered), 'average_citation_count': avg, 'missing_paper_docs': missing}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BMQZZ8eg5m7Zh9DJLBFwpd6N': 'file_storage/call_BMQZZ8eg5m7Zh9DJLBFwpd6N.json', 'var_call_xMBGKOdyMHo3TtpYfIyNOc2Q': 'file_storage/call_xMBGKOdyMHo3TtpYfIyNOc2Q.json', 'var_call_mWN53iPzeAUcaOHrz5iGHCC1': {'num_2018_acm_papers': 0, 'average_citation_count': None, 'papers': []}}

exec(code, env_args)
