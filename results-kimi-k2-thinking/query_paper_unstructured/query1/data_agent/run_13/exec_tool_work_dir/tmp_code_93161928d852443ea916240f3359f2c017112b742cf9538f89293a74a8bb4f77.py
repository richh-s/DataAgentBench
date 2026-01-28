code = """import json
import re

# Load the datasets
citations_path = locals()['var_functions.query_db:6']
paper_docs_path = locals()['var_functions.query_db:8']

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_path, 'r') as f:
    paper_docs_data = json.load(f)

# Extract domains from papers
food_papers = []
all_domains = []

for paper in paper_docs_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    text_lower = text.lower()
    title_lower = title.lower()
    
    domains = []
    
    # Check for domain mentions
    if 'food' in text_lower:
        domains.append('food')
    if 'physical activity' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower:
        domains.append('finances')
    
    all_domains.extend(domains)
    
    if 'food' in domains:
        food_papers.append(title)

# Get total citations for food papers
food_citations_total = 0
food_citations_by_paper = {}

for citation in citations_data:
    cit_title = citation.get('title', '')
    if cit_title in food_papers:
        count = int(citation.get('citation_count', 0))
        food_citations_total += count
        
        if cit_title not in food_citations_by_paper:
            food_citations_by_paper[cit_title] = 0
        food_citations_by_paper[cit_title] += count

# Debug info
result = {
    'total_papers': len(paper_docs_data),
    'food_papers_found': len(food_papers),
    'food_paper_titles': food_papers,
    'total_citations_for_food_papers': food_citations_total,
    'citations_by_food_paper': food_citations_by_paper
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_papers': 5, 'food_papers': 3, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_functions.execute_python:16': {'total_papers': 5, 'first_paper_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
