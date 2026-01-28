code = """import json
import pandas as pd
# load the citations data from previous stored file
with open(var_call_BMQZZ8eg5m7Zh9DJLBFwpd6N, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# convert citation_count to int
for r in citations:
    r['citation_count'] = int(r['citation_count'])

# load paper docs list
with open(var_call_xMBGKOdyMHo3TtpYfIyNOc2Q, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build a mapping from filename to text for quick lookup
paper_text_by_filename = {p['filename']: p['text'] for p in papers}

# We need to identify papers published by ACM. The hint: source field may appear in text like 'ACM' or 'Copyright 2015 © ACM' etc.
# Also need papers published in 2018. We will extract year and source by searching the text for patterns.

import re

def extract_year(text):
    # search for 4-digit year between 1900 and 2025
    m = re.search(r"(19|20)\d{2}", text)
    if m:
        return int(m.group(0))
    return None

def has_acm(text):
    # look for 'ACM' near copyright or DOI or 'ACM' word
    return bool(re.search(r"\bACM\b", text))

# For each citation record, map to filename and check paper info
results = []
for rec in citations:
    title = rec['title']
    filename = title + '.txt'
    citation_count = rec['citation_count']
    paper_text = paper_text_by_filename.get(filename)
    if paper_text:
        year = extract_year(paper_text)
        source_is_acm = has_acm(paper_text)
    else:
        year = None
        source_is_acm = False
    results.append({'title': title, 'filename': filename, 'citation_count': citation_count, 'year': year, 'is_acm': source_is_acm})

# Filter papers published in 2018 and source ACM
filtered = [r for r in results if r['year'] == 2018 and r['is_acm']]

# compute average citation_count
if filtered:
    avg = sum(r['citation_count'] for r in filtered)/len(filtered)
else:
    avg = None

out = {'num_2018_acm_papers': len(filtered), 'average_citation_count': avg, 'papers': filtered}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BMQZZ8eg5m7Zh9DJLBFwpd6N': 'file_storage/call_BMQZZ8eg5m7Zh9DJLBFwpd6N.json', 'var_call_xMBGKOdyMHo3TtpYfIyNOc2Q': 'file_storage/call_xMBGKOdyMHo3TtpYfIyNOc2Q.json'}

exec(code, env_args)
