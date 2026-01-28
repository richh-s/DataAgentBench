code = """import json
from statistics import mean

# Load the stored results from previous tool calls
mongo_path = var_call_3rhr0PH8PI7k7kl8Ius4eUS8
citations_path = var_call_qRYquB40A3tsXCZIGqUmpFJB

with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_docs = json.load(f)

with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Extract titles from filenames in mongo results (strip .txt)
acm_titles = set()
for doc in mongo_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    acm_titles.add(title)

# Find citation records for titles that are in ACM set
matched_counts = []
matched_titles = []
for rec in citations:
    title = rec.get('title')
    count_raw = rec.get('citation_count')
    try:
        count = int(count_raw)
    except Exception:
        # skip if cannot parse
        continue
    if title in acm_titles:
        matched_counts.append(count)
        matched_titles.append(title)

if matched_counts:
    avg = mean(matched_counts)
    avg_rounded = round(avg, 2)
    result = {
        'average_citation_count': avg_rounded,
        'num_acm_papers_cited_in_2018': len(matched_counts)
    }
else:
    result = {
        'average_citation_count': None,
        'num_acm_papers_cited_in_2018': 0
    }

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_3rhr0PH8PI7k7kl8Ius4eUS8': 'file_storage/call_3rhr0PH8PI7k7kl8Ius4eUS8.json', 'var_call_qRYquB40A3tsXCZIGqUmpFJB': 'file_storage/call_qRYquB40A3tsXCZIGqUmpFJB.json'}

exec(code, env_args)
