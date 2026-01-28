code = """import json
import re
import os

# Access the stored file path from the variable
file_path = locals()['var_functions.query_db:4']

print(f'File path: {file_path}')
print(f'File exists: {os.path.exists(file_path)}')

# Load the paper documents from the file
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

print(f'Total number of paper documents: {len(paper_docs)}')

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
        pattern = r'\b' + re.escape(domain) + r'\b'
        if re.search(pattern, text_lower):
            found_domains.append(domain)
    
    return {
        'title': title,
        'domains': found_domains,
        'filename': filename
    }

# Process all papers to find those in 'food' domain
food_paper_titles = []
for doc in paper_docs:
    paper_info = extract_paper_info(doc)
    if 'food' in paper_info['domains']:
        food_paper_titles.append(paper_info['title'])

print(f'Number of papers in food domain: {len(food_paper_titles)}')
print(f'Sample food paper titles: {food_paper_titles[:10]}')

result = {'food_paper_titles': food_paper_titles, 'count': len(food_paper_titles)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
