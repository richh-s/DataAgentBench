code = """import json
import re
from collections import defaultdict

# Load all paper documents
paper_docs_path = locals()['var_functions.query_db:8']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Load all citations
citations_path = locals()['var_functions.query_db:6']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create mapping of title to total citations
citation_map = defaultdict(int)
for cit in citations:
    title = cit.get('title', '')
    total_cit = int(cit.get('total_citations', 0))
    citation_map[title] = total_cit

results = []

# Process each paper document
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    # Skip if no text
    if not text:
        continue
    
    # Extract year - look for year patterns
    year = None
    # Look for patterns like 2017, 2018, 2019, etc.
    year_match = re.search(r'20[1-9][0-9]', text)
    if year_match:
        year = int(year_match.group())
    
    # Check if paper has 'empirical' contribution
    has_empirical = 'empirical' in text.lower()
    
    # Get total citations
    total_citations = citation_map.get(title, 0)
    
    # Apply filters: empirical and published after 2016
    if has_empirical and year and year > 2016:
        results.append({
            'title': title,
            'total_citations': total_citations
        })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'paper_docs_count': 5, 'citations_count': 259}, 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'contribution': 'empirical', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': 'empirical', 'total_citations': 266}], 'var_functions.execute_python:18': []}

exec(code, env_args)
