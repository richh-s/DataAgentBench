code = """import json
import re

# Check what variables are available in locals()
available_vars = list(locals().keys())
print('__DEBUG__ Available variables:', available_vars[:10])  # Print first 10 to avoid clutter

# Try to access the paper_docs data directly
paper_docs = locals().get('var_functions.query_db:2', [])
citations = locals().get('var_functions.query_db:6', [])

print('__DEBUG__ Paper docs type:', type(paper_docs))
print('__DEBUG__ Paper docs length:', len(paper_docs) if isinstance(paper_docs, list) else 'Not a list')
print('__DEBUG__ Citations type:', type(citations))
print('__DEBUG__ Citations length:', len(citations) if isinstance(citations, list) else 'Not a list')

# If they're not lists, they might be file paths
if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)
if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Process paper_docs to extract title and domain
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '').lower()  # Convert to lowercase for easier matching
    
    # Extract title from filename (remove .txt)
    title = re.sub(r'\.txt$', '', filename)
    
    # Check if paper is in 'food' domain
    food_keywords = ['food', 'eating', 'diet', 'nutrition', 'calorie', 'meal']
    is_food_domain = any(keyword in text for keyword in food_keywords)
    
    if is_food_domain:
        paper_info.append({'title': title})

# Create a set of food domain paper titles for fast lookup
food_titles = set(p['title'] for p in paper_info)

# Filter and sum citations for food domain papers
total_citations = 0
citation_records_found = 0

for citation in citations:
    cite_title = citation.get('title', '')
    if cite_title in food_titles:
        total_citations += int(citation.get('citation_count', 0))
        citation_records_found += 1

result = {
    'total_citation_count': total_citations,
    'food_papers_identified': len(food_titles),
    'citation_records_found': citation_records_found
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
