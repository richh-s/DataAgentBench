code = """import json
import re

# Get stored data - handle both direct data and file paths
papers_input = locals()['var_functions.query_db:30']
citations_input = locals()['var_functions.query_db:28']

# Load actual data
if isinstance(papers_input, str) and papers_input.endswith('.json'):
    with open(papers_input, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_input

if isinstance(citations_input, str) and citations_input.endswith('.json'):
    with open(citations_input, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_input

# Debug first few items to understand structure
print('Paper data sample:', papers_data[0] if papers_data else 'Empty')
print('Citation data sample:', citations_data[0] if citations_data else 'Empty')

# Create citation lookup
citation_map = {}
for cit in citations_data:
    if isinstance(cit, dict):
        citation_map[cit.get('title', '')] = int(cit.get('total_citations', 0))

# Process papers
results = []
for doc in papers_data:
    if isinstance(doc, dict):
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        title = filename.replace('.txt', '') if filename else ''
        
        year_match = re.search(r'(20\d{2})', text)
        year = int(year_match.group(1)) if year_match else None
        
        has_empirical = 'empirical' in text.lower()
        
        if has_empirical and year and year > 2016 and title in citation_map:
            results.append({'title': title, 'total_citations': citation_map[title]})

# Sort
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Format
output = []
for item in results_sorted:
    output.append(item['title'] + ': ' + str(item['total_citations']) + ' citations')

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations']}

exec(code, env_args)
