code = """import json
import re

# Load full MongoDB data
mongo_file = var_functions.query_db:34
with open(mongo_file, 'r') as f:
    mongo_data = json.load(f)

print('Total papers from MongoDB: ' + str(len(mongo_data)))

# Extract year from text
def extract_year(text):
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        return 2000 + int(match.group(1))
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        return int(match.group(1))
    return None

# Check if paper is empirical
def is_empirical_paper(text):
    return 'empirical' in text.lower() or 'empirically' in text.lower()

# Process all papers
papers_2017_plus = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    year = extract_year(text)
    if year and year > 2016 and is_empirical_paper(text):
        papers_2017_plus.append(title.lower())

print('Empirical papers after 2016: ' + str(len(papers_2017_plus)))

# Load citations
 citation_file = var_functions.query_db:35
 with open(citation_file, 'r') as f:
    citations = json.load(f)

citation_titles = set()
for cit in citations:
    citation_titles.add(cit['title'].lower())

print('Total citation titles: ' + str(len(citation_titles)))

# Find intersections
matching_titles = []
for title in papers_2017_plus:
    if title in citation_titles:
        matching_titles.append(title)

print('Matching titles: ' + str(len(matching_titles)))

# Build final results
final_results = []
citation_map = {cit['title'].lower(): int(cit['total_citations']) for cit in citations}
mongo_title_map = {filename.replace('.txt', '').lower(): filename.replace('.txt', '') for doc in mongo_data for filename in [doc.get('filename', '')] if filename}

for title_key in matching_titles:
    if title_key in mongo_title_map:
        final_results.append({
            'title': mongo_title_map[title_key],
            'total_citations': citation_map[title_key]
        })

# Sort by citations descending
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print('Final results: ' + str(len(final_results)))
for i, paper in enumerate(final_results[:10]):
    print(str(i+1) + '. ' + paper['title'] + ' - ' + str(paper['total_citations']))

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}}

exec(code, env_args)
