code = """import json
import re

# Load the paper documents from the file path stored in var_functions.query_db:4
with open('var_functions.query_db:4', 'r') as f:
    paper_docs = json.load(f)

print(f"Total number of paper documents: {len(paper_docs)}")

# Function to extract paper information from text
def extract_paper_info(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename (remove .txt)
    title = re.sub(r'\.txt$', '', filename)
    
    # Try to extract domain information by searching for common domains in the text
    text_lower = text.lower()
    
    # Common domains to search for
    domains = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 
        'productivity', 'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health_behavior', 'weight'
    ]
    
    found_domains = []
    for domain in domains:
        # Use word boundaries to avoid partial matches
        if re.search(r'\b' + re.escape(domain) + r'\b', text_lower):
            found_domains.append(domain)
    
    return {
        'title': title,
        'domains': found_domains,
        'filename': filename
    }

# Process all papers
papers_with_domains = []
for doc in paper_docs:
    paper_info = extract_paper_info(doc)
    papers_with_domains.append(paper_info)

# Filter papers in 'food' domain
food_papers = [p for p in papers_with_domains if 'food' in p['domains']]

print(f"Number of papers in 'food' domain: {len(food_papers)}")
for paper in food_papers[:10]:  # Show first 10
    print(f"  - {paper['title']}")

# Save food paper titles for joining with citations
food_paper_titles = [p['title'] for p in food_papers]

print('\n__RESULT__:')
print(json.dumps(food_paper_titles))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
