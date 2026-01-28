code = """import re, json
from datetime import datetime

# Load full Mongo result from file
file_path = var_call_PJNSWbNI9folvHQHuUpB9Z94
with open(file_path, 'r') as f:
    mongo_records = json.load(f)

# Heuristic to extract year from text
year_pattern = re.compile(r'(19|20)\d{2}')

papers = {}
for doc in mongo_records:
    text = doc.get('text', '')
    # extract years, pick the most recent reasonable one <= 2025
    years = [int(y) for y in year_pattern.findall(text) if isinstance(y, str)]
    # year_pattern with group gives tuples; adjust
    years_fixed = []
    for m in year_pattern.finditer(text):
        years_fixed.append(int(m.group(0)))
    years = years_fixed
    year = max([y for y in years if 1900 <= y <= 2025], default=None)

    # crude contribution detection: look for 'empirical' and ensure it's about contribution
    if re.search(r'empirical', text, re.IGNORECASE):
        # store if year > 2016
        if year and year > 2016:
            title = doc.get('filename', '').replace('.txt', '').strip()
            papers[title] = {'title': title, 'year': year}

# Load citation aggregates
file_path2 = var_call_qQc1Gf48YtxpksJCKXwrM5G0
with open(file_path2, 'r') as f:
    citation_records = json.load(f)

citations_map = {rec['title'].strip(): int(rec['total_citations']) for rec in citation_records}

results = []
for title, info in papers.items():
    if title in citations_map:
        results.append({'title': title, 'total_citations': citations_map[title]})

# sort by title for stable output
results_sorted = sorted(results, key=lambda x: x['title'])

out = json.dumps(results_sorted, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PJNSWbNI9folvHQHuUpB9Z94': 'file_storage/call_PJNSWbNI9folvHQHuUpB9Z94.json', 'var_call_qQc1Gf48YtxpksJCKXwrM5G0': 'file_storage/call_qQc1Gf48YtxpksJCKXwrM5G0.json'}

exec(code, env_args)
