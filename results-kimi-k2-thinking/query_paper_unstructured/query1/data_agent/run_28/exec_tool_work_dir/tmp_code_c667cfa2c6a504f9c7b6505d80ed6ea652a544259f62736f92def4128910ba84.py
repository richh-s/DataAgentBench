code = """import json
from difflib import get_close_matches

# Load data
cits = json.load(open(locals()['var_functions.query_db:2'])) if isinstance(locals()['var_functions.query_db:2'], str) else locals()['var_functions.query_db:2']
papers = json.load(open(locals()['var_functions.query_db:22'])) if isinstance(locals()['var_functions.query_db:22'], str) else locals()['var_functions.query_db:22']

print('Total papers:', len(papers))
print('Total citations:', len(cits))

# Find food papers
food_papers = []
for doc in papers:
    text = doc.get('text', '').lower()
    if 'food' in text or 'eating' in text or 'diet' in text:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        food_papers.append(title)

print('Food papers found:', len(food_papers))
if food_papers:
    print('Sample food papers:', food_papers[:5])

# Check citation titles
citation_titles = [c.get('title', '') for c in cits]
print('\nCitation titles sample:', citation_titles[:5])

# Try fuzzy matching
from collections import defaultdict
citation_dict = defaultdict(int)
for c in cits:
    title = c.get('title', '')
    count = int(c.get('citation_count', 0))
    citation_dict[title] += count

total_citations = 0
matches_found = 0

for food_title in food_papers:
    matches = get_close_matches(food_title, list(citation_dict.keys()), n=1, cutoff=0.6)
    if matches:
        total_citations += citation_dict[matches[0]]
        matches_found += 1
        print(f'MATCHED: {food_title[:50]} -> {matches[0][:50]} = {citation_dict[matches[0]]}')

print('\nFinal results:')
print('Matches found:', matches_found)
print('Total citations:', total_citations)

result = {'total_citation_count': total_citations, 'matched_papers': matches_found}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}, 'var_functions.execute_python:38': {'total_citation_count': 0}}

exec(code, env_args)
