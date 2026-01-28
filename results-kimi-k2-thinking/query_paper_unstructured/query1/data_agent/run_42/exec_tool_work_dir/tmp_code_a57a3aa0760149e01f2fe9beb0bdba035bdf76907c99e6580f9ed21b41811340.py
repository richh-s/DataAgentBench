code = """import json
import re

# Access the stored file path from the variable
file_path = locals()['var_functions.query_db:4']

# Load the paper documents from the file
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

print(f'Total number of paper documents: {len(paper_docs)}')

# Function to extract paper information from text with broader food-related terms
def extract_paper_info_with_food(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename (remove .txt)
    title = re.sub(r'\.txt$', '', filename)
    
    # Try to extract domain information by searching for food-related terms in the text
    text_lower = text.lower()
    
    # Food-related terms to search for
    food_terms = [
        'food', 'eating', 'diet', 'nutrition', 'calorie', 'meal', 
        'restaurant', 'cooking', 'recipe', 'dietary', 'weight'
    ]
    
    found_food_terms = []
    for term in food_terms:
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(term) + r'\b'
        if re.search(pattern, text_lower):
            found_food_terms.append(term)
    
    return {
        'title': title,
        'food_terms': found_food_terms,
        'filename': filename
    }

# Process all papers to find those with food-related terms
food_related_papers = []
for doc in paper_docs:
    paper_info = extract_paper_info_with_food(doc)
    if paper_info['food_terms']:  # If any food terms found
        food_related_papers.append(paper_info)

print(f'Number of papers with food-related terms: {len(food_related_papers)}')

# Show all papers with their food terms
for paper in food_related_papers:
    print(f"Paper: {paper['title']}")
    print(f"  Food terms found: {paper['food_terms']}")
    print()

# Get the titles of food-related papers
food_paper_titles = [p['title'] for p in food_related_papers]

print(f'Total food-related papers: {len(food_paper_titles)}')

result = {'food_paper_titles': food_paper_titles, 'count': len(food_paper_titles)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'food_paper_titles': [], 'count': 0}}

exec(code, env_args)
