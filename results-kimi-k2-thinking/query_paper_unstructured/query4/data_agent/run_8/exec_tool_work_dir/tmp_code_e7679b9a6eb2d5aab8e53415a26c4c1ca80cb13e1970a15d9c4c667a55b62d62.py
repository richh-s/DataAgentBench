code = """import json
import re

# Access the stored results
paper_docs = locals()['var_functions.query_db:14']
citations_data = locals()['var_functions.query_db:15']

# Load from file paths if needed
if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

print('Documents:', len(paper_docs))
print('Citations:', len(citations_data))

# Build a dictionary of total citations per title
citation_dict = {}
for cit in citations_data:
    title = cit.get('title')
    count = int(cit.get('total_citations', 0))
    if title in citation_dict:
        citation_dict[title] += count
    else:
        citation_dict[title] = count

print('Unique titles in citations:', len(citation_dict))

# Process papers
results = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Find year
    year = None
    year_search = re.search(r'20(1[0-9]|20)', text)
    if year_search:
        year = int(year_search.group())
    
    # Check for physical activity domain (case-insensitive)
    lower_text = text.lower()
    is_activity = any(kw in lower_text for kw in 
                     ['physical activity', 'fitness', 'exercise', 'steps'])
    
    if year == 2016 and is_activity:
        # Get citation count
        cit_count = citation_dict.get(title, 0)
        results.append({
            'title': title,
            'total_citation_count': cit_count
        })
        print('Found paper:', title[:50])

# Prepare output
print('Total papers found:', len(results))
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
