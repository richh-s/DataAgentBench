code = """import json
import os

# Load the full citations data from the file
citations_path = locals()['var_functions.query_db:6']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load the full paper_docs data from the file
paper_docs_path = locals()['var_functions.query_db:8']
with open(paper_docs_path, 'r') as f:
    paper_docs_data = json.load(f)

# Preprocess papers to extract titles and domains
papers_info = []

for paper in paper_docs_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (without .txt extension)
    title = filename.replace('.txt', '')
    
    # Look for domain information in the text
    domains = []
    text_lower = text.lower()
    
    # Common domains to search for
    domain_keywords = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 
        'productivity', 'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health_behavior', 'weight'
    ]
    
    for keyword in domain_keywords:
        if keyword in text_lower:
            domains.append(keyword)
    
    papers_info.append({
        'title': title,
        'domains': domains,
        'text': text
    })

# Count how many papers have 'food' in their domains
food_papers = [p for p in papers_info if 'food' in p['domains']]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers_info),
    'food_papers': len(food_papers),
    'food_paper_titles': [p['title'] for p in food_papers[:10]]  # First 10 for preview
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
