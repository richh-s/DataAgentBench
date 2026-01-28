code = """import json
import re

# Load paper_docs data
with open('var_functions.query_db:2', 'r') as f:
    paper_docs = json.load(f)

# Load citations data
with open('var_functions.query_db:6', 'r') as f:
    citations = json.load(f)

# Process paper_docs to extract title and domain
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = re.sub(r'\.txt$', '', filename)
    
    # Check if paper is in 'food' domain
    # Look for food-related keywords in the text
    # Common patterns: food, eating, diet, nutrition, calorie, meal
    food_keywords = ['food', 'eating', 'diet', 'nutrition', 'calorie', 'meal', 'dietary']
    is_food_domain = False
    
    for keyword in food_keywords:
        if re.search(r'\b' + keyword + r'\b', text, re.IGNORECASE):
            is_food_domain = True
            break
    
    if is_food_domain:
        paper_info.append({
            'title': title,
            'domain': 'food'
        })

# Create a set of food domain paper titles for fast lookup
food_titles = set(p['title'] for p in paper_info)

# Filter and sum citations for food domain papers
total_citations = 0
citation_count = 0

for citation in citations:
    cite_title = citation.get('title', '')
    if cite_title in food_titles:
        total_citations += int(citation.get('citation_count', 0))
        citation_count += 1

result = {
    'total_citation_count': total_citations,
    'food_papers_with_citations': len(food_titles),
    'citation_records_found': citation_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
